// SPDX-License-Identifier: GPL-2.0-or-later
#include "quantum.h"
#include "hal.h"

void keyboard_post_init_kb(void) {
#ifdef RGBLIGHT_ENABLE
    // Clear the LEDs when RGBLight skips sending a frame at startup.
    if (!rgblight_is_enabled()) {
        rgblight_set();
    }
#endif
    keyboard_post_init_user();
}

void bootloader_jump(void) {
    // Match the Plum marker recovered from the original firmware at 0x080072c4.
    *(volatile uint32_t *)0x20004C00 = 0xC220B134;
    NVIC_SystemReset();
}

void mcu_reset(void) {
    NVIC_SystemReset();
}

