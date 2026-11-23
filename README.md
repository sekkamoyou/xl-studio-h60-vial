# XL Studio H60 Vial firmware

An unofficial Vial port for the XL Studio H60 PCB with USB ID `CD60:FE01`, an STM32F103, and the factory Plum UF2 bootloader. Check the PCB and USB ID before flashing. The Hiney H60 is a different target.

The port supports ANSI and ISO Enter, split Backspace, split left and right Shift, and 6.25u, 6u, 7u, or three-piece spacebars. It has four keymap layers and RGB underglow. On the public default keymap, Fn+Esc toggles the underglow and Fn+/ selects the next effect. At startup, the firmware clears all 35 RGB LEDs when underglow is set to All Off.

## Install

1. Download `xl_studio_h60_vial.uf2` from [Releases](https://github.com/sekkamoyou/xl-studio-h60-vial/releases) and compare its SHA-256 hash with `SHA256SUMS`.
2. Save your Vial configuration on your own machine.
3. With USB connected, press the PCB reset button twice in quick succession. Wait for the `STM32F1Plum` drive to appear.
4. Copy the UF2 to that drive and wait for the keyboard to restart. Reconnect in Vial and check your layout and bindings. Reload your saved configuration if needed.

The image updates the application region. The EEPROM compatibility ID matches the previous H60 boot-LED fix. Firmware with a different EEPROM ID may initialize Vial keymaps, macros and layout options when first booted.

## Build from the release source archive

Download `h60-vial-public-source.tar.gz` from the same release as the UF2. It includes Vial-QMK, this port, and the exact ChibiOS, ChibiOS-Contrib, LUFA and printf source revisions used to build the UF2. Use QMK's Python requirements, the `qmk` CLI, GNU Make, and an Arm embedded toolchain. The release used Python 3.12 and xPack GNU Arm Embedded GCC 13.2.1.

From the extracted `vial-qmk` directory, run:

```sh
python3 h60-release/generate_layout.py
make SKIP_GIT=yes SKIP_VERSION=yes xl_studio/h60:vial
python3 h60-release/make_uf2.py xl_studio_h60_vial.bin xl_studio_h60_vial.uf2
```

## Build from this repository

From this repository's root, prepare the pinned upstream checkout and apply the H60 changes:

```sh
port_root=$PWD
git clone https://github.com/vial-kb/vial-qmk.git vial-qmk
git -C vial-qmk checkout --detach dd43959ae5c08d8a28d38a1acf7b04e86b14a344
git -C vial-qmk submodule update --init lib/chibios lib/chibios-contrib lib/lufa lib/printf
git -C vial-qmk apply "$port_root/patches/vial-eeprom-compatibility.patch"
python3 tools/generate_layout.py
mkdir -p vial-qmk/keyboards/xl_studio
cp -R keyboards/xl_studio/h60 vial-qmk/keyboards/xl_studio/
cd vial-qmk
make SKIP_GIT=yes SKIP_VERSION=yes xl_studio/h60:vial
python3 "$port_root/tools/make_uf2.py" xl_studio_h60_vial.bin xl_studio_h60_vial.uf2
```

## Verification

- All 64 combinations of layout options passed the Vial layout parser checks.
- A clean build from the release source archive reproduced the UF2 byte for byte.
- The release UF2 was installed on a matching H60. Vial Web displayed the new layout with the existing layout options. The final settings matched the pre-install snapshot after the original lighting preferences were restored.
- After disconnecting and reconnecting USB with underglow set to All Off, the upper-right green LED stayed off and normal typing was confirmed.

See [license and source notices](LICENSES.md). The firmware is distributed without warranty.
