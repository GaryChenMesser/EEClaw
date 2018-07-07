import RPi.GPIO as GPIO
import time

# global variable
# motor channel
X_MOTOR = 12
Y_MOTOR = 13
Z_MOTOR = 18
# button channel
RIGHT    = 2
LEFT     = 3
FORWARD  = 4
BACKWARD = 17
CLAW     = 27
RESET    = 10


GPIO.setmode(GPIO.BCM)
  
# configure for reset button
GPIO.setup(RESET, GPIO.IN)

while(1):
  print('wait')
  GPIO.wait_for_edge(RESET, GPIO.BOTH)
  print('another wait')
  timeout = GPIO.wait_for_edge(RESET, GPIO.BOTH, timeout=4500)
  if timeout is None:
    break
