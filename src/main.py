import threading as thread
import RPi.GPIO as GPIO

# global variable
MOTOR_SPEED = 0.
ZERO_OFFSET = [0., 0., 0.]
POSITIVE_RANGE = [0., 0., 0.]
NEGATIVE_RANGE = [0., 0., 0.]


def init():
  # configure gpio
  
def exit():
  
def button_callback(channel):
  if GPIO.input(channel): # RISING EDGE -> MOTOR START
    
  else: # FALLING EDGE -> MOTOR STOP
def motor():
  
def main():
  
if __name__=='__main__':
  main()
