// SPDX-License-Identifier: GPL-2.0-or-later
#pragma once
#include_next <mcuconf.h>
// Original application at 0x0800e892 sets PLLXTPRE and RCC_CFGR=0x001f6400.
#undef STM32_PLLXTPRE
#define STM32_PLLXTPRE STM32_PLLXTPRE_DIV2
