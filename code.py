import time
import usb_hid
import board
import digitalio
import asyncio
import rotaryio
from rainbowio import colorwheel
import neopixel

from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#----------------Global-Variables----------------

buttonDelay = 10 #debounce iterations for buttons
DialDelay = 25 #how much the dial needs to rotate to receive an input out of 360
DialRatio = 120 #simulated detents

VolRR = 0
VolRL = 0
VolLR = 0
VolLL = 0

LedNum=int(24)

LeftLaser=(0,170,255)
RightLaser=(255,0,128)
VolLPixels = neopixel.NeoPixel(board.GP20, LedNum, brightness=.7, auto_write=False)
VolRPixels = neopixel.NeoPixel(board.GP21, LedNum, brightness=.7, auto_write=False)
#----------------Classes----------------

class Button:
    def __init__(self,GPIO):
        self.name = str(GPIO)
        self.port = digitalio.DigitalInOut(GPIO)
        self.port.pull = digitalio.Pull.DOWN
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
    pass
        
    
    
class Dial:
    def __init__(self,GPIO):
        self.port = digitalio.DigitalInOut(GPIO)
        self.port.direction = digitalio.Direction.INPUT
        self.port.pull = digitalio.Pull.DOWN

    @property
    def value(self):
        return self.port.value

#----------------Button-setup----------------

keb = Keyboard(usb_hid.devices)

VolR = rotaryio.IncrementalEncoder(board.GP16,board.GP17)
VolRLastPos = VolR.position
VolL = rotaryio.IncrementalEncoder(board.GP18,board.GP19)
VolLLastPos = VolL.position


BTa = Button(board.GP15)
BTb = Button(board.GP14)
BTc = Button(board.GP13)
BTd = Button(board.GP12)

FXr = Button(board.GP11)
FXl = Button(board.GP10)

Strt = Button(board.GP9)

mouse = Mouse(usb_hid.devices)
x=0

#----------------Functions----------------
async def main():
    sendBTa = asyncio.create_task(sendPress(BTa,Keycode.D))
    sendBTb = asyncio.create_task(sendPress(BTb,Keycode.F))
    sendBTc = asyncio.create_task(sendPress(BTc,Keycode.J))
    sendBTd = asyncio.create_task(sendPress(BTd,Keycode.K))
    
    sendFXr = asyncio.create_task(sendPress(FXr,Keycode.C))
    sendFXl =asyncio.create_task(sendPress(FXl,Keycode.M))
    
    sendStrt = asyncio.create_task(sendPress(Strt,Keycode.ONE))
    
    await asyncio.gather(sendBTa,sendBTb,sendBTc,sendBTd,sendFXr,sendFXl,sendStrt)
    
async def sendPress(BTN,Key):
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
        
def VolLed(group,pos,color,width):
    groupPos=int((pos)/360*LedNum)
    dimColor=(color[0]/2,color[1]/2,color[2]/2)
    dimmerColor=(color[0]/9,color[1]/6,color[2]/9)
    ledList=range(groupPos,groupPos+width)
    
    
    group.fill((0,0,0))
    for i in ledList:
        if i==groupPos+1 or i==groupPos+3:
            group[i%LedNum]=dimColor
            group[(i-int(LedNum/2))%LedNum]=dimColor
        elif i==groupPos+2:
            group[i%LedNum]=color
            group[(i-int(LedNum/2))%LedNum]=color
        else:
            group[i%LedNum]=dimmerColor
            group[(i-int(LedNum/2))%LedNum]=dimmerColor
            
    group.show()
    
    



#----------------Runtime----------------
while True:
    VolRPos = VolR.position
    VolLPos = VolL.position
    
    if (VolRPos != VolRLastPos):
        if VolRPos < VolRLastPos:
            VolRR += 1
            if VolRR > DialDelay:
                VolRL = 0
                keb.send(Keycode.P)
                VolRR = DialDelay - 360/DialRatio
                VolLed(VolRPixels,VolRPos%360,RightLaser,5)
                 
        elif VolRPos > VolRLastPos:
            VolRL += 1
            if VolRL > DialDelay:
                VolRR = 0
                keb.send(Keycode.O)
                VolRL = DialDelay - 360/DialRatio
                VolLed(VolRPixels,VolRPos%360,RightLaser,5)

    VolRLastPos = VolRPos
    
    if (VolLPos != VolLLastPos):
        if VolLPos < VolLLastPos:
            VolLR += 1
            if VolLR > DialDelay:
                VolLL = 0
                keb.send(Keycode.E)
                VolLR = DialDelay - 360/DialRatio
                VolLed(VolLPixels,VolLPos%360,LeftLaser,5)

                 
        elif VolLPos > VolLLastPos:
            VolLL += 1
            if VolLL > DialDelay:
                VolLR = 0
                keb.send(Keycode.W)
                VolLL = DialDelay - 360/DialRatio
                VolLed(VolLPixels,VolLPos%360,LeftLaser,5)

    VolLLastPos = VolLPos
    
    
    
        
    
    asyncio.run(main())