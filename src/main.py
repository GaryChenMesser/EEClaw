import threading as thread
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
# PWM parameter
FREQUENCY  = 50
DEGREE_0   = 2.5
DEGREE_90  = 7.5
DEGREE_180 = 12.5

# look up table: button_channel -> [motor_channel, direction, pwm]
lookup = { RIGHT    : [X_MOTOR, DEGREE_180, 0],
           LEFT     : [X_MOTOR,   DEGREE_0, 0],
           FORWARD  : [Y_MOTOR, DEGREE_180, 0],
           BACKWARD : [Y_MOTOR,   DEGREE_0, 0],
           CLAW     : [Z_MOTOR,          0, 0]}

def init():
  # configure gpio
  GPIO.setmode(GPIO.BCM)
  
  # configure for reset button
  GPIO.setup(RESET, GPIO.IN)
  
  # configure for control button
  for button in lookup:
    # set up for every channel
    GPIO.setup(button, GPIO.IN)
    GPIO.setup(lookup[button][0], GPIO.OUT)
    
    # register callback for button
    GPIO.add_event_detect(button, GPIO.BOTH, callback=button_callback)
    
    # start pwm for motor
    lookup[button][2] = GPIO.PWM(lookup[button][0], FREQUENCY)
    lookup[button][2].start(DEGREE_90)
  
def exit():
  for button, pwm in lookup_table.items():
    pwm.stop()
  GPIO.cleanup()

def reset():
  lookup[Z_MOTOR][2].ChangeDutyCycle(DEGREE_180)
  time.sleep(1.5)
  lookup[X_MOTOR][2].ChangeDutyCycle(DEGREE_90)
  time.sleep(1.5)
  lookup[Y_MOTOR][2].ChangeDutyCycle(DEGREE_90)
  time.sleep(1.5)

def button_callback(button):
  if GPIO.input(button): # RISING EDGE -> MOTOR START
    if button != 27:
      lookup[button][2].ChangeDutyCycle(lookup[button][1])
    else:
      lookup[button][2].ChangeDutyCycle(DEGREE_0)
      time.sleep(1.5)
      lookup[button][2].ChangeDutyCycle(DEGREE_180)
      time.sleep(1.5)
    
  else: # FALLING EDGE -> MOTOR STOP
    if button != 27:
      lookup[button][2].ChangeDutyCycle(0)

def main():
  init()
  
  while(1):
    GPIO.wait_for_edge(RESET, GPIO.RISING)
    timeout = GPIO.wait_for_edge(RESET, GPIO.FALLING, timeout=4500)
    if timeout is None:
      break
    reset()
  
if __name__=='__main__':
  main()
