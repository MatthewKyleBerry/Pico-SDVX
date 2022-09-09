# Pico-SDV

A Project for turning the inexpensive Raspberry PI pico into a cotroller for USC, SDVX and other rhythm games.


### Current Features:
- Plug and play
- Button mapping for momentary switches through all GPIO pins
- Custom keycodes for buttons

### Upcoming Features:
- Dial mapping for Rotary encoders through all GPIO pins
- Custom keycodes for dials
- Debounce for Rotary encoders


### Default settings


Start                 ([1])           ([GP9])
BTa,BTb,BTc,BTd   ([D][F][J][K])      ([GP15][GP14][GP13][GP12])
FXr,FXl              ([C][M])         ([GP11][GP10])
Dail-R               ([W][E])         ([GP8][GP7])
Dial-L               ([O][P])         ([GP6][GP5])

Double press rejection (5 cycles)

### Installation

1. Plug in Pico while holding down BOOTSEL
2. Unzip Pico-SDVX
3. Drag and drop code.py, adafruit-circuitpython-hid-8.x-mpy-5.3.2, and adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2 into the Pico
4. Once the Pico reboots it should be ready to plug in GPIO 


