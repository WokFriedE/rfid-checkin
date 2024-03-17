import time 

#RFID Reader
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#OLED
from board import SCL, SDA
import busio
from oled_text import OledText

import sqlite3


def main():

    i2c = busio.I2C(SCL, SDA)
    oled = OledText(i2c,128,32)
    oled.text("Hello", 1)
    oled.text("world!",2)

    reader2 = SimpleMFRC522()
    print("="*15 + "\nREADER LIVE\n")

    try:
        while (True): 
            id = reader2.read_id()
            t = time.localtime()
            curr_time = time.strftime("%H:%M:%S", t) 
            print("ID", curr_time+":", id)
            oled.clear()
            set_text(oled, id,"")
            if(id == 296001312055):
                oled.text("bye",2)
                break

            time.sleep(1)
    finally:
        GPIO.cleanup()
        oled.clear()
        

def set_text(oled: OledText, row1, row2):
    oled.clear()
    oled.text(row1,1)
    oled.text(row2,2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass