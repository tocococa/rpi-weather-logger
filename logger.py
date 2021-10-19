from __future__ import print_function
from datetime import datetime
from updater import updater
import serial
# Listen to serial communication from ADDR at BAUD rate
# stream should be "Temp,Humidity,Press,WindSpd,WindDir,Rain"


ADDR = 'com3'
BAUD = 9600
PATH = './weather_data.csv'
HTML = './index.html'


def toCSV(line):
    line.insert(0, datetime.today().strftime("%H:%M:%S %d/%m"))
    with open(PATH, buffering=1, mode='a') as file:
        file.write(line)


def main(serial_obj):
    while True:
        if serial_obj.in_waiting > 0:
            line = serial_obj.readline().decode('utf-8').rstrip()
            print(line)
            toCSV(line)
            updater(PATH, HTML)


if __name__ == '__main__':
    ser = serial.Serial(
        port=ADDR,
        baudrate=BAUD,
        bytesize=8,
        parity="E",
        stopbits=1,
        timeout=0.05
    )
    ser.flush()
    main(ser)
