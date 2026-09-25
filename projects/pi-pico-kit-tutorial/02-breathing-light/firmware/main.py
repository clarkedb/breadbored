from machine import PWM, Pin
from utime import sleep

led = PWM(Pin(2))
led.freq(1000)
led_value = 0
led_speed = 5

while True:
    led_value += led_speed
    led.duty_u16(int(led_value * 500))
    sleep(0.1)
    if led_value >= 100:
        led_value = 100
        led_speed = -5
    elif led_value <= 0:
        led_value = 0
        led_speed = 5
