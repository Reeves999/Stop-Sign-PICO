from machine import Pin
import utime

led_light = Pin(15,Pin.OUT)
pico_led = Pin(25,Pin.OUT)

while True:
    pico_led.toggle()
    led_light.toggle()
    utime.sleep(5)