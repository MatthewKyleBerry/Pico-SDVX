# Pico-SDVX

A Project for turning the inexpensive Raspberry PI pico into a cotroller for USC, SDVX and other rhythm games using CircuitPython.


### Current Features:
- Plug and play
- Button mapping for momentary switches through all GPIO pins
- Custom keycodes for buttons
- Double press rejection (Default 10 cycles)
- Dial mapping for Rotary encoders through all GPIO pins
- Custom keycodes for dials
- Debounce for Rotary encoders

### Upcoming Features:
- coming soon

### Default settings
Name | Key| GPIO
|:--|:--:|:--:|
Start | ([1]) | ([GP9])
BTa,BTb,BTc,BTd | ([D][F][J][K]) | ([GP15][GP14][GP13][GP12])
FXr,FXl | ([C][M]) | ([GP11][GP10])
Dail-R | ([O][P]) | ([GP16][GP17])
Dial-L | ([W][E]) | ([GP18][GP19])



### Installation

1. Plug in Pico while holding down BOOTSEL
2. Unzip Pico-SDVX
3. Drag and drop code.py, libraries, and adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2 into the Pico
4. Once the Pico reboots it should be ready to plug in GPIO 

### Required libraries:
- [circuitpython uf2](https://circuitpython.org/board/raspberry_pi_pico/)
- [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- [ticks - from adafruit lib](https://circuitpython.org/libraries)
- [asyncio - from adafruit lib](https://circuitpython.org/libraries)
- [rotaryio - from adafruit lib](https://circuitpython.org/libraries)

### Parts List
- [Raspberry Pi Pico](https://www.adafruit.com/product/5525)
- 2x 100 ohm resistors
- 7x 1k ohm resitors
- 7x 3.3V Diodes (I used LEDs)
- [BT Buttons](https://www.aliexpress.us/item/2251832857137258.html?spm=a2g0o.detail.1000014.24.5f14720aRXPfRW&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.281175.0&scm_id=1007.40050.281175.0&scm-url=1007.40050.281175.0&pvid=e1246435-960d-4233-9040-633a6960782b&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40050.281175.0,pvid:e1246435-960d-4233-9040-633a6960782b,tpp_buckets:668%232846%238115%232000&pdp_ext_f=%7B%22sku_id%22%3A%2267375362097%22%2C%22sceneId%22%3A%2230050%22%7D&pdp_npi=2%40dis%21USD%2117.99%2117.99%21%21%21%21%21%40210323a116673347964976311ec7e6%2167375362097%21rec)
- [FX and Start Buttons](https://www.aliexpress.com/item/2251832467827163.html?spm=2114.30010308.3.2.MPUfbB&ws_ab_test=searchweb201556_8%2Csearchweb201602_2_10017_405_404_301_407_406_10040%2Csearchweb201603_2&btsid=49678139-a03d-4cc6-b940-93b38f89f956&gatewayAdapt=4itemAdapt)
- [Vol Rotary Encoders](https://www.amazon.com/dp/B07MWZ4CLT/?coliid=I183GLNDLFTQF5&colid=1BNLKE657MKDX&psc=1&ref_=lv_ov_lig_dp_it)

