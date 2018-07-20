import RPi.GPIO.as GPIO
import time

channel = 12
GPIO.setmode(channel, GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
  GPIO.wait_for_edge(channel, GPIO.BOTH)

  if GPIO.input(channel):
    print("Push down!")
  else:
    print("Pull up!")
