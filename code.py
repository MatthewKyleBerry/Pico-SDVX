import time
import usb_hid
import board
import digitalio
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#----------------Global-Variables----------------

buttonDelay = 10

#----------------Classes----------------

class Button:
    def __init__(self,GPIO):
        self.name = str(GPIO)
        self.port = digitalio.DigitalInOut(GPIO)
        self.port.direction = digitalio.Direction.INPUT
        self.state = self.port.value
        self.time = 0
    @property
    def value(self):
        return self.port.value
    @property
    def pin(self):
        return self.name

    def zero_Time(self):
        self.time = 0

    def inc_Time(self):
        self.time = self.time + 1

    def get_Time(self):
        return self.time
        
    
    
class Dial:
    def __init__(self,GPIO1,GPIO2):
        self.port1 = digitalio.DigitalInOut(GPIO1)
        self.port2 = digitalio.DigitalInOut(GPIO1)
        self.port1.direction = digitalio.Direction.INPUT
        self.port2.direction = digitalio.Direction.INPUT
        self.state1 = self.port1.value
        self.state2 = self.port2.value
    @property
    def value1(self):
        return self.port1.value
    @property
    def value2(self):
        return self.port2.value
    
#----------------Functions----------------
    
def sendPress(BTN,Key):
    if BTN.state != BTN.value:
        BTN.state = BTN.value
        
        print(BTN.pin + " = " + str(BTN.state))
        if (BTN.state == True) and (BTN.get_Time() > buttonDelay):
            keb.press(Key)
            #time.sleep(0.05)
        else:
            keb.release(Key)
            BTN.zero_Time()
    if (BTN.get_Time() <= buttonDelay):
        BTN.inc_Time()
            
            
def sendDial(DAIL,KeyR,KeyL):
    if (DAIL.state1 != DIAL.value1) or (DIAL.state2 != DIAL.value2):
        DAIL.state1 = DAIL.value1
        DAIL.state2 = DAIL.value2
        if (DAIL.state1 == True) and (DAIL.state2 == False):
            keb.send(KeyL)
        if (DAIL.state1 == False) and (DAIL.state1 == True):
            keb.send(KeyL)

#----------------Button-setup----------------

keb = Keyboard(usb_hid.devices)

BTa = Button(board.GP15)
print(BTa.state)

BTb = Button(board.GP14)
print(BTb.state)

BTc = Button(board.GP13)
print(BTc.state)

BTd = Button(board.GP12)
print(BTd.state)


FXr = Button(board.GP11)
print(FXr.state)

FXl = Button(board.GP10)
print(FXl.state)


Strt = Button(board.GP9)
print(Strt.state)


mouse = Mouse(usb_hid.devices)
x=0


#----------------Runtime----------------

while True:
    sendPress(BTa,Keycode.D)
    sendPress(BTb,Keycode.F)
    sendPress(BTc,Keycode.J)
    sendPress(BTd,Keycode.K)
    
    sendPress(FXr,Keycode.C)
    sendPress(FXl,Keycode.M)
    
    sendPress(Strt,Keycode.ONE)
        
        #if BTa.value == True:
        #    keb.press(Keycode.D)
        #elif BTa.value == False:
        #	 keb.release(Keycode.D)
