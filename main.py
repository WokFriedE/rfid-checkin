import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from mfrc522 import MFRC522


# reader = SimpleMFRC522()
print("="*15 + "\nREADER LIVE\n")

# try:
#     while (True): 
#         # id, text= reader.read()
#         print("ID:", id)
#         print("Text:",text)
#         print
# finally:
#     GPIO.cleanup()


reader = MFRC522()
status = None
while true:
    (status,TagType) = reader.Request(reader.PICC_REQIDL)
    if status != reader.MI_OK:
        sleep(0.1)
        continue
    status, backData = reader.MFRC522_Anticoll()
    print(backData)