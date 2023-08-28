# Author  = M.Mohammed Nowful Khan  
# Title   = Lazy Pad
# Insta   = mr_white_hat._ 
# GitHub  = Hacker Nowful
# Youtube = Hacker Nowful

import board
from analogio import AnalogIn
import usb_hid
from adafruit_hid.mouse import Mouse
import time
import digitalio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)

btn1_pin = board.GP20
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP1
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3_pin = board.GP0
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4_pin = board.GP21
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5_pin = board.GP2
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6_pin = board.GP3
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7_pin = board.GP22
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8_pin = board.GP5
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9_pin = board.GP4
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10_pin = board.GP14
btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11_pin = board.GP16
btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN



mouse = Mouse(usb_hid.devices)
xAxis = AnalogIn(board.A1)
yAxis = AnalogIn(board.A0)

in_min,in_max,out_min,out_max = (0, 65000, -5, 5)
filter_joystick_deadzone = lambda x: int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min) if abs(x - 32768) > 500 else 0

while True:
    
    x_offset = filter_joystick_deadzone(xAxis.value) * -1 
    y_offset = filter_joystick_deadzone(yAxis.value)
    mouse.move(x_offset, y_offset, 0)

    if btn1.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT) 
        time.sleep(0.1)

    if btn2.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)   
        time.sleep(0.1)
        
    if btn3.value:
        cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
        
        time.sleep(0.1)

    if btn4.value:
       cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)     
       time.sleep(0.1)

    if btn5.value:
       cc.send(ConsumerControlCode.PLAY_PAUSE)
       time.sleep(0.1)
       
    if btn6.value:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK) 
        time.sleep(0.1)

    if btn7.value:
        keyboard.send(Keycode.UP_ARROW)
        time.sleep(0.1)
        
    if btn8.value:
        keyboard.send(Keycode.UP_ARROW)
        time.sleep(0.1)

    if btn9.value:
        keyboard.send(Keycode.DOWN_ARROW)

    if btn11.value:
        mouse.click(Mouse.LEFT_BUTTON) 
        time.sleep(0.1)

    if btn10.value:
       mouse.click(Mouse.RIGHT_BUTTON)
       time.sleep(0.1)
   



