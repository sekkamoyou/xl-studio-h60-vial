# SPDX-License-Identifier: GPL-2.0-or-later
import struct
import sys
from pathlib import Path


def make_uf2(firmware):
    assert 8 <= len(firmware) <= 0x17000
    stack, reset = struct.unpack_from('<II', firmware)
    assert 0x20000000 < stack <= 0x20004c00
    assert reset & 1 and 0x08007000 <= reset < 0x08007000+len(firmware)
    program = firmware + bytes((-len(firmware)) % 256)
    packets = []
    for offset in range(0, len(program), 256):
        data = program[offset:offset+256]
        if offset % 1024 == 0:
            assert data != bytes([255])*256
            # Plum skips erasing if a page's first payload already matches.
            packets.append((0x08007000+offset, bytes([255])*256))
        packets.append((0x08007000+offset, data))
    return b''.join(struct.pack('<8I', 0x0a324655, 0x9e5d5157, 0x2000, address, 256,
                                index, len(packets), 0xabcdf103)
                    + data + bytes(220) + struct.pack('<I', 0x0ab16f30)
                    for index, (address, data) in enumerate(packets))


if __name__ == '__main__':
    assert len(sys.argv) == 3, 'Usage: python3 make_uf2.py firmware.bin firmware.uf2'
    source, target = map(Path, sys.argv[1:])
    assert source.resolve() != target.resolve()
    target.write_bytes(make_uf2(source.read_bytes()))
