# Licenses and source revisions

The combined H60 firmware is distributed under GNU GPL version 3. Individual files retain their original copyright notices and license terms. New H60 code uses `GPL-2.0-or-later`, including the Vial layout generator, generic keymap, and UF2 converter. See the license texts in [`licenses/`](licenses/).

| Component | Revision | Terms |
|---|---|---|
| [Vial-QMK](https://github.com/vial-kb/vial-qmk) | `dd43959ae5c08d8a28d38a1acf7b04e86b14a344` | GPL terms as marked in the source, including GPL-2.0-or-later for the Vial firmware code. See the upstream `LICENSE` and per-file notices. |
| [ChibiOS](https://github.com/qmk/ChibiOS) | `8bd61b804303f1614d574546c2dd735eeabb09f5` | GPLv3 for the RT kernel. Apache-2.0 for the HAL and the original `STM32F103xB.ld`. The derived `h60_plum.ld` keeps that copyright and license notice. |
| [ChibiOS-Contrib](https://github.com/qmk/ChibiOS-Contrib) | `3ac181e4ca5cafddaf8b472baa1d09c2b24c77b6` | See per-file notices. |
| [LUFA](https://github.com/qmk/lufa) | `549b97320d515bfca2f95c145a67bd13be968faa` | Dean Camera's permissive license, reproduced in `licenses/LUFA.txt`. |
| [printf](https://github.com/qmk/printf) | `c2e3b4e10d281e7f0f694d3ecbd9f320977288cc` | MIT, reproduced in `licenses/printf-MIT.txt`. |
| CMSIS and STM32F1 headers | Included in ChibiOS above | Arm CMSIS uses Apache-2.0. See `licenses/STMicroelectronics-BSD-3-Clause.txt` for the ST STM32F1 device notice. |

The source archive attached to each release contains the H60 port, the pinned Vial-QMK source and dependencies, and the build and UF2 conversion instructions. The H60 board files and the EEPROM compatibility override in [`patches/vial-eeprom-compatibility.patch`](patches/vial-eeprom-compatibility.patch) are the changes against the pinned Vial-QMK tree. The archive preserves the original license notices for all included source files.
