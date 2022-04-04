from machine import Pin
import utime
import _thread

button = Pin(14,Pin.IN,Pin.PULL_DOWN)
green_led = Pin(13,Pin.OUT)
yellow_led = Pin(12,Pin.OUT)
red_led = Pin(11,Pin.OUT)
pico_led = Pin(25,Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread(): # This allows me to hit the button
                            # while the process of the led system
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())

def stop_and_go():
    while True:
        #The green_led turns on and off after 15secs
        green_led.value(1)
        utime.sleep(15)
        green_led.value(0)
        #The yellow_led turns on and off after 4.3secs
        yellow_led.value(1)
        utime.sleep(4.3)
        yellow_led.value(0)
        #The red_led turns on and off after 10secs
        red_led.value(1)
        utime.sleep(10)
        red_led.value(0)
        if button_pressed == True: #If button is on
            print("The button has been Pressed! Call for help!!!!!!!!!!")
            for x in range(10)
                pico_led.toggle()
                utime.sleep(1)
                pico_led.toggle()
            global button_pressed
            button_pressed = False
        else:
            print("There is a error!")

stop_and_go()
