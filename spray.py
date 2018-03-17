import machine
import time

class Motor:
	def __init__(self):
		self.speedPin = machine.Pin(5,machine.Pin.OUT)
		self.directionPin = machine.Pin(0,machine.Pin.OUT)

	def spin(self, duration, direction):
		from time import sleep
		self.directionPin.value(direction)
		self.speedPin.on()
		sleep(duration)
		self.speedPin.off()

	def spinForward(self, duration):
		self.spin(duration=duration, direction=1)

	def spinBackward(self, duration):
		self.spin(duration=duration, direction=0)



def spray():
	motor = Motor()

	motor.spinForward(duration=0.5)
	motor.spinBackward(duration=0.25)
