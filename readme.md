# RFID Check In System

## Purpose
- Made to help check in system in a small scale organization or club
- Hosted on a Raspberry Pi (developed on Pi 4) on Ubuntu

## Set up
- On fresh install of Ubuntu LTS (server)
    1. sudo apt update
    2. sudo apt upgrade
    3. sudo apt install
    4. sudo apt install python3
    5. sudo apt install python3-dev python3-pip python3-venv
    6. Install items for RFID reader
        - sudo apt install python3-lgpio
        - lsmod | grep spi 
            - search for spi_bcm2835
    7. Install items for OLED I2C 
        - sudo apt install -y python3-smbus i2c-tools
        - sudo apt install -y python3-pil
        - i2cdetect -y 1
            - check for the oled display

    8. sudo apt install php libapache2-mod-php
- installing git
    1. sudo apt install git-all
    2. git --version
- Install SQL
    1. sudo apt install mysql-server
    
sudo apt-get install python3-dev python3-rpi.gpio

### Initialization
#### Python
1. python3 -m venv env
2. source env/bin/activate  || (windows) source env/Scripts/activate
3. Install items for RFID reader
    - python3 -m pip install spidev
    - python3 -m pip install mfrc522
4. install items for OLED
    - pip install oled-text
    - [docs for oled-text](https://pypi.org/project/oled-text/) 

#### Install SQL




## Resources
- [RFID set up](https://www.instructables.com/RFID-RC522-Raspberry-Pi/)
- [Integrate RFID](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
- [LGPIO for ubuntu](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#3-basic-gpio-example)
- [Installing PHP on Ubuntu](https://ubuntu.com/server/docs/programming-php)
- [Python MFRC522 Doc](https://pypi.org/project/mfrc522-python/#using-simplemfrc522-class-1)
- [OLED Setup](https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/#google_vignette)
- https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root

## Hardware
- RFID reader --> rc522
- Raspberry PI

## Assumptions
- Apache server is installed