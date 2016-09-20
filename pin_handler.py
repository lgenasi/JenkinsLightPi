#!/usr/bin/python 
import wiringpi2
import time

def setUpPin(name, pin):
	print ("Using GPIO pin:"  + str(pin) + " as '" + name + "'.")
	wiringpi2.pinMode(pin, 1)

def setUpAllPins(pinConfig):
	wiringpi2.wiringPiSetupGpio()

	print ("Loading GPIO pins...")
	for name, pin in pinConfig.items():
		setUpPin(name, pin);

def setLEDs(pinConfig, outputDict):
	for key, value in outputDict.items():
		wiringpi2.digitalWrite(pinConfig[key], value)

def illuminatePassing(passing, pinConfig):
	if passing:
		setLEDs(pinConfig, {"success": 1, "failure": 0})
	elif not passing:
		setLEDs(pinConfig, {"success": 0, "failure": 1})
	else:
		setLEDs(pinConfig, {"success": 0, "failure": 0})

def illuminateBuilding(building, pinConfig, pollingFrequency):
	while building and pollingFrequency > 0:
		setLEDs(pinConfig, {"success": 0, "failure": 0})
		time.sleep(1)
		setLEDs(pinConfig, {"success": 1, "failure": 1})
		time.sleep(3)
		pollingFrequency = pollingFrequency - 4
