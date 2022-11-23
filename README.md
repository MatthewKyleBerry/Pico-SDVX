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
- 1ms avg polling

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

##### 125hz Polling
1. Plug in Pico while holding down BOOTSEL
2. Unzip Pico-SDVX
3. Drag and drop adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2 into the Pico
4. let the Pico reboot
5. Drag and drop code.py, and libraries
6. ... and you are ready to disconnect and plug in gpio.

##### 1000hz Polling

###### Drag and drop
1. Plug in Pico while holding down BOOTSEL
2. Unzip Pico-SDVX
3. Drag and drop firmware.uf2 into the Pico
4. let the Pico reboot
5. Drag and drop code.py, and libraries
6. ... and you are ready to disconnect and plug in gpio.

###### Build Your Own
1. Install WSL, cmake, make, git, arm-none-eabi-gcc, pip3 and required from [link](https://learn.adafruit.com/building-circuitpython/build-circuitpython)
2. Download source and submodules for circuitpython.
3. Edit /shared-module/usb-hid/```__init__.c``` so that all binterval referances read 0x01 and not 0x08.
4. build circuitpython by ```cd /port/raspberrypi``` ```sudo make BOARD=raspberry_pi_pico_w``` or ```sudo make BOARD=raspberry_pi_pico``` 
5. Plug in Pico while holding down BOOTSEL
6. Unzip Pico-SDVX
7. Drag and drop firmware.uf2 into the Pico
8. let the Pico reboot
9. Drag and drop code.py, and libraries
10. ... and you are ready to disconnect and plug in gpio.

### Required Libraries:
- [Optional - circuitpython uf2](https://circuitpython.org/board/raspberry_pi_pico/)
- [adafruit_hid - from adafruit lib](https://circuitpython.org/libraries)
- [ticks - from adafruit lib](https://circuitpython.org/libraries)
- [asyncio - from adafruit lib](https://circuitpython.org/libraries)
- [rotaryio - from adafruit lib](https://circuitpython.org/libraries)

### Parts List
- [Raspberry Pi Pico](https://www.adafruit.com/product/5525)
- 2x 100 ohm resistors
- 7x 1k ohm resitors
- 7x 3.3V Diodes (I used LEDs)
- OBSA-LHS1F-LN 100g
- [BT Buttons](https://www.aliexpress.us/item/2251832857137258.html?spm=a2g0o.detail.1000014.24.5f14720aRXPfRW&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.281175.0&scm_id=1007.40050.281175.0&scm-url=1007.40050.281175.0&pvid=e1246435-960d-4233-9040-633a6960782b&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40050.281175.0,pvid:e1246435-960d-4233-9040-633a6960782b,tpp_buckets:668%232846%238115%232000&pdp_ext_f=%7B%22sku_id%22%3A%2267375362097%22%2C%22sceneId%22%3A%2230050%22%7D&pdp_npi=2%40dis%21USD%2117.99%2117.99%21%21%21%21%21%40210323a116673347964976311ec7e6%2167375362097%21rec)
- [FX and Start Buttons](https://www.aliexpress.com/item/2251832467827163.html?spm=2114.30010308.3.2.MPUfbB&ws_ab_test=searchweb201556_8%2Csearchweb201602_2_10017_405_404_301_407_406_10040%2Csearchweb201603_2&btsid=49678139-a03d-4cc6-b940-93b38f89f956&gatewayAdapt=4itemAdapt)
- [Vol Rotary Encoders](https://www.amazon.com/dp/B07MWZ4CLT/?coliid=I183GLNDLFTQF5&colid=1BNLKE657MKDX&psc=1&ref_=lv_ov_lig_dp_it)
- [Encoder Knobs](https://www.ebay.com/itm/302843963802?hash=item4682e8299a:g:6nYAAOSw6B5ZcaJb&amdata=enc%3AAQAHAAAA0JQjmexRLuCQW7Udd1uDE3D6t0%2FRUopIkf8074W%2ByjvfrORYECxAi2O0oxk7A4PcSkmFY7Cznpb59tHD4zUPIDbiLUBAIdCl5u9IuKnWuVDPAT0i%2B8FeBR1ZkV4zTXVtepIddEQa5IxoF5bo0EGyzg4f7KxPprE2rNw5HdPbqUaElxvT%2BaxjwyT3QtjAOZVObnIcT0UEBMnDGw%2FxnfYYZM%2F57BzJQLmdH%2Bj9mv2LFcs7bHvMLbpCp1Tk6ldRevwbwn7kCW0nTzfOwLtV%2F2BiU2c%3D%7Ctkp%3ABFBMssKdz4Zh)
