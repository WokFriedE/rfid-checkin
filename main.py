import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time 


print("="*15 + "\nREADER LIVE\n")

reader2 = SimpleMFRC522()
try:
    while (True): 
        id = reader2.read_id()
        t = time.localtime()
        curr_time = time.strftime("%H:%M:%S", t) 
        print("ID", curr_time+":", id)
finally:
    GPIO.cleanup()

