import RPi.GPIO as GPIO
import time

# 這個練習沒有規定程式終止的條件，所以程式不會自己停下來
# 用來檢查事件的while可以每檢查一次就休息0.01秒，因為觸發按鈕的最短時間大概是1/10秒的數量級

channel = 12
GPIO.setmode(channel, GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
  while GPIO.input(channel) == GPIO.LOW:
    pass
  print("我被按了")
  while GPIO.input(channel) == GPIO.HIGH:
    pass
  print("我被放開了")
