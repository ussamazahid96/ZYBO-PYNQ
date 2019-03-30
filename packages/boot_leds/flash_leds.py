#!/bin/env python3.6

from time import sleep
from pynq import overlay

base = overlay.Overlay("base.bit")

leds = [base.axi_gpio_led[i] for i in range(4)]

# Toggle board LEDs leaving small LEDs lit
for i in range(8):
    [l.off() for l in leds]
    sleep(.2)
    [l.on() for l in leds]
    sleep(.2)
