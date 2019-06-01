import RPi.GPIO as GPIO
import time
import datetime

a1 = 13
a2 = 16
open = 1
iopen = 0

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(a1, GPIO.OUT, initial=open)
GPIO.setup(a2, GPIO.OUT, initial=iopen)

try:  
    while True:

        GPIO.output(a1, open)
        GPIO.output(a2, iopen)
        time.sleep(0.01)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("{} GPIO {}={}, {}={}".format(st, a1, GPIO.input(a1), a2,GPIO.input(a2)))

        time.sleep(5.0)                 # wait half a second  
        if(open==1):
            open = 0
            iopen = 1
        else:
            open = 1
            iopen = 0
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program 