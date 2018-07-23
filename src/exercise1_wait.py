import RPi.GPIO as GPIO
import time

channel = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
  GPIO.wait_for_edge(channel, GPIO.BOTH)

  if GPIO.input(channel):
    print("我被按了")
  else:
    print("我被放開了")
