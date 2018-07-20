import RPi.GPIO as GPIO
import time

# global variable
UP       = 6
DOWN     = 13

# look up table
# input channel : output channel
lookup = { UP       : 25,
           DOWN     : 12 }
  
def move_callback(button):
  print('button {} call back.'.format(button))
  if GPIO.input(button): # RISING EDGE -> MOTOR START
    GPIO.output(lookup[button], GPIO.HIGH)
  else: # FALLING EDGE -> MOTOR STOP
    GPIO.output(lookup[button], GPIO.LOW)
    
def main():
  # configure gpio
  GPIO.setmode(GPIO.BCM)
  
  # configure for control button
  for button in lookup:
    # set up for every channel
    GPIO.setup(button, GPIO.IN)
    GPIO.add_event_detect(button, GPIO.BOTH, callback=move_callback)

    GPIO.setup(lookup[button], GPIO.OUT)
    
  while True:
    time.sleep(1)
  
if __name__=='__main__':
  main()
