from __future__ import print_function
from datetime import date
import serial
import io


# Listen to serial communication from ADDR at BAUD rate
# stream should be "Temp,Humidity,Press,WindSpd,WindDir,Rain"

ADDR = '/dev/ttyACM0'
BAUD = 9600
PATH = './weather_data.csv'


def ToCSV(readings):
    with open(PATH, buffering=1, mode='a'):


def main(serial_obj):
    pass


if __name__ == '__main__':
    ser = serial.Serial(ADDR, BAUD, timeout=1)
    ser.flush()
    main(ser)