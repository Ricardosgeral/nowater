import time
from machine import Pin  #control GPIOs of micro controler
import python.RGBled as RGBled

def main():
    buz = Pin(4, Pin.OUT)                           # buzzer
    water_detector = Pin(27,Pin.IN,Pin.PULL_UP)     # output from non-contact water sensor
    pull_up = Pin(12,Pin.IN)                        # to detect if the non-contact water sensor is working

    #turn off all leds and buzzer
    buz.value(0)
    RGBled.redOff()
    RGBled.greenOff()
    RGBled.blueOff()

    # initial run
    for i in range(5):
        RGBled.magentaOn()
        time.sleep(0.3)
        RGBled.magentaOff()
        time.sleep(0.3)

    while True:
        if pull_up.value()==1:                  #the water sensor is not connected or is broken! Yellow alert
            while pull_up.value()==1:
                RGBled.greenOff()
                RGBled.yellowOn()
                time.sleep(0.5)
                RGBled.yellowOff()
                time.sleep(0.5)
                buz.value(0)

        if water_detector.value()==1:           # no water  - RED alert
            while water_detector.value()==1:
                RGBled.greenOff()
                buz.value(1)
                RGBled.redOn()
                time.sleep(0.5)
                buz.value(0)
                RGBled.redOff()
                time.sleep(0.5)
        else:                                   # water is detected   - GREEN light
            buz.value(0)
            RGBled.greenOn()

        time.sleep(0.2)                         # small interval

if __name__ == '__main__':
    main()