import RPi.GPIO as GPIO
import time

# global variable
RIGHT    = 17
LEFT     = 27
FORWARD  = 22
BACKWARD = 5
UP       = 6
DOWN     = 13
RESET    = 19

# look up table
# input channel : output channel
lookup = { RIGHT    : 26,
           LEFT     : 18,
           FORWARD  : 23,
           BACKWARD : 24,
           UP       : 25,
           DOWN     : 12 }

def init():
  # configure gpio
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(RESET, GPIO.IN) 
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
