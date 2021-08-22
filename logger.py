from __future__ import print_function
from datetime import date
import serial
import io


# Listen to serial communication from ADDR at BAUD rate
# stream should be "Temp,Humidity,Press,WindSpd,WindDir,Rain"

ADDR = '/dev/ttyACM0'
BAUD = 9600
PATH = './weather_data.csv'


def ToCSV(line):
    with open(PATH, buffering=1, mode='a') as file:
        file.write(line)


def main(serial_obj):
    while True:
        if serial_obj.in_waiting > 0:
            line = serial_obj.readline().decode('utf-8').rstrip()
            print(line)
            ToCSV(line)


if __name__ == '__main__':
    ser = serial.Serial(ADDR, BAUD, timeout=1)
    ser.flush()
    main(ser)
