#!/bin/bash

if [[ -e /dev/spidev0.0 ]]
then echo "SPI exists"
else echo "no SPI"
fi