import RPi.GPIO as GPIO
import time

def my_callback(channel):
  if GPIO.input(channel):
    print("Push down!")
  else:
    print("Pull up!")

def main():
  channel = 12
  GPIO.setmode(channel, GPIO.BCM)
  GPIO.setup(channel, GPIO.IN)

  GPIO.add_event_detect(channel, )

  while True:
    time.sleep(1)

if __name__ == "__main__":
  main()
