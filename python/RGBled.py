#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Ricardos.geral@gmail.com


from machine import Pin  #control GPIOs of micro controler
redPin = 5    # GPIO34
greenPin = 18  # GPIO35
bluePin = 19   # GPIO32


def blink(pin):
    on = Pin(pin, Pin.OUT)
    on.value(1)

def turnOff(pin):
    off = Pin(pin, Pin.OUT)
    off.value(0)

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