from machine import Pin
import utime

def stop_and_go():
    button = Pin(14,Pin.IN,Pin.PULL_DOWN)
    green_led = Pin(13,Pin.OUT)
    yellow_led = Pin(12,Pin.OUT)
    red_led = Pin(11,Pin.OUT)
    pico_led = Pin(25,Pin.OUT)
    while True:
        pico_led.value(0) #This function checks if the pico_led is off.
        if button.value() == 0:#if button is off
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
        elif button.value() == 1: #If button is on
            print("The button has been Pressed! Call for help!!!!!!!!!!")
            pico_led.toggle()
        else:
            print("There is a error!")
stop_and_go()
