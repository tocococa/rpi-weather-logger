from datetime import datetime
from serial.serialutil import SerialException
from updater import updater
from serial import Serial

import sys
# Listen to serial communication from ADDR at BAUD rate
# stream should be "Temp,Humidity,Press,WindSpd,WindDir,Rain"


if sys.platform.startswith('win'):
    PORT = "com3"
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    PORT = "/dev/ttyACM0"
else:
    raise EnvironmentError('Unsupported platform')
BAUD = 9600
PATH = './server/logs.csv'
HTML = './server/darkhttpd/public_index/index.html'


def toCSV(line):
    line = datetime.today().strftime("%H:%M:%S %d/%m") + ',' + line + '\n'
    with open(PATH, buffering=1, mode='a') as file:
        file.write(line)


def main(ser):
    try:
        skip = 0
        while True:
            ser_bytes = ser.readline()
            if len(ser_bytes) > 1:
                decoded_bytes = ser_bytes.decode("utf8").strip()
                if decoded_bytes == "REBOOT":
                    print(decoded_bytes)
                    skip = 2
                elif skip > 0:
                    print(decoded_bytes)
                    skip -= 1
                else:
                    if len(decoded_bytes.split(',')) == 6:
                        print(decoded_bytes)
                        toCSV(decoded_bytes)
                        updater(PATH, HTML)
    except SerialException as err:
        print(f"Error {err}, possible disconnect")


if __name__ == '__main__':
    ser = Serial(
        port=PORT,
        baudrate=BAUD,
        timeout=0.05
    )
    ser.flushInput()
    main(ser)
