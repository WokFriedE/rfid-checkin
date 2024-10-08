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
    5. sudo apt install python3-lgpio
    6. sudo apt install python3-dev python3-pip python3-venv
    7. lsmod | grep spi 
        - search for spi_bcm2835
    8. sudo apt install php libapache2-mod-php
- installing git
    1. sudo apt install git-all
    2. git --version

### Initialization
#### Python
1. python3 -m venv env
2. source env/bin/activate  || (windows) source env/Scripts/activate
3. python3 -m pip install spidev
4. python3 -m pip install mfrc522



## Resources
- [RFID set up](https://www.instructables.com/RFID-RC522-Raspberry-Pi/)
- [Integrate RFID](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
- [LGPIO for ubuntu](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#3-basic-gpio-example)
- [Installing PHP on Ubuntu](https://ubuntu.com/server/docs/programming-php)
- https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root

## Hardware
- RFID reader --> rc522
- Raspberry PI

## Assumptions
- Apache server is installed