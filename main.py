import time
from machine import Pin  #control GPIOs of micro controler

def main():
    led_buz = Pin(2, Pin.OUT)
    water_detector = Pin(27,Pin.IN,Pin.PULL_UP)
    led_buz.value(0)

    while True:
        if water_detector.value()==1:
            while water_detector.value()==1:
                led_buz.value(1)
                time.sleep(0.3)
                led_buz.value(0)
                time.sleep(0.3)
        else:
            led_buz.value(0)
        time.sleep(0.3)

if __name__ == '__main__':
    main()