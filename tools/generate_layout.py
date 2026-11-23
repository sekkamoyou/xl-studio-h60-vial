# SPDX-License-Identifier: GPL-2.0-or-later
"""Generate the Vial definition from H60 switch positions and key sizes."""

import json
from pathlib import Path


def key(row, column, width=1, **shape):
    if width != 1:
        shape["w"] = width
    return shape, f"{row},{column}"


def row(keys, *, x=0, option=None):
    result = []
    for shape, position in keys:
        if x:
            shape = {"x": x, **shape}
            x = 0
        if shape:
            result.append(shape)
        if option is not None:
            group, choice = option
            position += f"\n\n\n{group},{choice}"
        result.append(position)
    return result


def bottom_row(keys, choice):
    return row([key(4, column, width, **shape) for column, width, shape in keys],
               option=(4, choice))


keymap = [
    row([key(0, col) for col in range(13)])
    + row([key(0, 13, 2)], option=(0, 0)),
    row([key(1, 0, 1.5)] + [key(1, col) for col in range(1, 13)])
    + row([key(1, 13, 1.5)], option=(1, 0)),
    row([key(2, 0, 1.75)] + [key(2, col) for col in range(1, 12)])
    + row([key(2, 12, 2.25)], option=(1, 0)),
    row([key(3, 0, 2.25)], option=(2, 0))
    + row([key(3, col) for col in range(2, 12)])
    + row([key(3, 12, 2.75)], option=(3, 0)),
    bottom_row([(0, 1.25, {}), (1, 1.25, {}), (2, 1.25, {}), (6, 6.25, {}),
                (10, 1.25, {}), (11, 1.25, {}), (12, 1.25, {}), (13, 1.25, {})], 0),
    # Vial aligns each alternate with its default group's upper-left corner.
    row([key(0, 13), key(2, 13)], x=13, option=(0, 1)),
    row([key(2, 12, 1.25, h=2, x2=-0.25, w2=1.5, h2=1)], x=13.75, option=(1, 1)),
    row([key(1, 13)], x=12.75, option=(1, 1)),
    row([key(3, 0, 1.25), key(3, 1)], option=(2, 1))
    + row([key(3, 12, 1.75), key(3, 13)], x=10, option=(3, 1)),
    bottom_row([(0, 1.5, {"d": True}), (1, 1, {}), (2, 1.5, {}), (6, 6, {}),
                (10, 1.5, {}), (11, 1, {})], 1),
    bottom_row([(0, 1.5, {}), (1, 1, {}), (2, 1.5, {}), (6, 7, {}),
                (11, 1.5, {}), (12, 1, {}), (13, 1.5, {})], 2),
    bottom_row([(0, 1.5, {}), (1, 1, {}), (2, 1.5, {}), (5, 3, {}), (6, 1, {}),
                (9, 3, {}), (11, 1.5, {}), (12, 1, {}), (13, 1.5, {})], 3),
]

definition = {
    "name": "XL Studio H60",
    "vendorId": "0xCD60",
    "productId": "0xFE01",
    "matrix": {"rows": 5, "cols": 14},
    "lighting": "qmk_rgblight",
    "layouts": {
        "labels": ["Split Backspace", "ISO Enter", "Split Left Shift", "Split Right Shift",
                   ["Bottom Row", "6.25u", "6u", "7u", "3u + 1u + 3u"]],
        "keymap": keymap,
    },
}

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    target = root / "keyboards/xl_studio/h60/keymaps/vial/vial.json"
    target.write_text(json.dumps(definition, indent=2) + "\n", encoding="utf-8")
