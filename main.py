import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from mfrc522 import MFRC522
from time import sleep


# reader2 = SimpleMFRC522()
print("="*15 + "\nREADER LIVE\n")

# try:
#     while (True): 
#         id = reader2.read_id()
#         print("ID:", id)
#         # print("Text:",text)
#         values = reader
# finally:
#     GPIO.cleanup()


reader = MFRC522()
status = None
try: 
    while True:
        (status,TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)
        if status != reader.MI_OK:
            sleep(0.1)
            continue
        status, backData = reader.MFRC522_Anticoll()
        print(backData)
        # print(reader.MFRC522_Read())
        blocks = [0,1,2,3]
        data = []
        for block_num in blocks:
            block_data = reader.MFRC522_Read(block_num)
            if block_data:
                data += block_data
        if data:
            print(''.join(chr(i) for i in data))
finally:
    GPIO.cleanup()