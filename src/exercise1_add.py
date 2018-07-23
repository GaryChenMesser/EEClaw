import RPi.GPIO as GPIO
import time

# 這個練習沒有規定程式終止的條件，所以程式不會自己停下來

def my_callback(channel):
  if GPIO.input(channel):
    print("我被按了")
  else:
    print("我被放開了")

def main():
  channel = 12
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(channel, GPIO.IN)

  GPIO.add_event_detect(channel, GPIO.BOTH, callback=my_callback)

  while True:
    # time.sleep(1)
    pass

if __name__ == "__main__":
  main()
