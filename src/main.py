import RPi.GPIO as GPIO
import time

# global variable
RIGHT    = 5
LEFT     = 6
FORWARD  = 13
BACKWARD = 26
UP       = 23
DOWN     = 1
RESET    = 7

# look up table
# input channel : output channel
lookup = { RIGHT    : 4,
           LEFT     : 17,
           FORWARD  : 27,
           BACKWARD : 22,
           UP       : 8,
           DOWN     : 24 }

def init():
  # configure gpio
  GPIO.setmode(GPIO.BCM)
  
  # configure for control button
  for button in lookup:
    # set up for every channel
    GPIO.setup(button, GPIO.IN)
    
    if button != RESET:
      GPIO.add_event_detect(button, GPIO.BOTH, callback=move_callback)

    GPIO.setup(lookup[button], GPIO.OUT)

def exit():
  GPIO.cleanup()

def reset():
  print('reset!')
  for button in lookup:
    GPIO.output(lookup[button], GPIO.LOW)
  

def move_callback(button):
  print('button {} call back.'.format(button))
  if GPIO.input(button): # RISING EDGE -> MOTOR START
    GPIO.output(lookup[button], GPIO.HIGH)
  else: # FALLING EDGE -> MOTOR STOP
    GPIO.output(lookup[button], GPIO.LOW)
    
def main():
  init()
  while(1):
    print('wait')
    GPIO.wait_for_edge(RESET, GPIO.RISING)
    timeout = GPIO.wait_for_edge(RESET, GPIO.FALLING, timeout=2500)
    if timeout is None:
      break
    reset()
  
if __name__=='__main__':
  main()
