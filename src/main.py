import RPi.GPIO as GPIO
import time

# global variable
CRASH    = [False for i in range(4)]
RIGHT    = 5
LEFT     = 6
FORWARD  = 13
BACKWARD = 26
UP       = 23
DOWN     = 1
RESET    = 7
ENABLE   = 25

# look up table: button_channel -> [motor_channel, direction, pwm]
lookup = { RIGHT    : [4,  12],
           LEFT     : [17, 16],
           FORWARD  : [27, 20],
           BACKWARD : [22, 21],
           UP       : [8],
           DOWN     : [24],
           RESET    : [ENABLE] }

def init():
  # configure gpio
  GPIO.setmode(GPIO.BCM)
  
  # configure for control button
  for button in lookup:
    # set up for every channel
    GPIO.setup(button, GPIO.IN)
    if button != RESET:
      GPIO.add_event_detect(button, GPIO.BOTH, callback=move_callback)
    
    for i, channel in enumerate(lookup[button]):
      if i != 0:
        GPIO.setup(channel, GPIO.IN)
        GPIO.add_event_detect(channel, GPIO.BOTH, callback=stop_callback)
      
      else:
        GPIO.setup(channel, GPIO.OUT)
  
  # enable l293n
  GPIO.output(lookup[RESET][0], GPIO.HIGH)

def exit():
  GPIO.cleanup()

def reset():
  print('reset!')
  for function in lookup:
    GPIO.output(lookup[function][0], GPIO.LOW)
  

def move_callback(button):
  print('button {} call back.'.format(button))
  if GPIO.input(button): # RISING EDGE -> MOTOR START
    if not GPIO.input(lookup[button][1]):
      GPIO.output(lookup[button][0], GPIO.HIGH)
  else: # FALLING EDGE -> MOTOR STOP
    GPIO.output(lookup[button][0], GPIO.LOW)

def stop_callback(button):
  print('corner {} detected.'.format(button))
  if GPIO.input(button): # corner
    for key in lookup:
      if lookup[key][1] == button:
        GPIO.output(lookup[key][0], GPIO.LOW)
    
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
