#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Ricardos.geral@gmail.com


from machine import Pin  #control GPIOs of micro controler
redPin = 34    # GPIO34
greenPin = 35  # GPIO35
bluePin = 32   # GPIO32


def blink(pin):
    led = Pin(pin, Pin.OUT)
    led.value(1)

def turnOff(pin):
    led = Pin(pin, Pin.OUT)
    led.value(0)

def redOn():
    blink(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)