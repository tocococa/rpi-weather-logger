from serial import Serial
import sys

if sys.platform.startswith('win'):
    PORT = "com3"
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    PORT = "/dev/ttyACM0"
else:
    raise EnvironmentError('Unsupported platform')

ser = Serial(
    port=PORT,
    baudrate=9600,
    timeout=0.05
)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        if len(ser_bytes) > 1:
            decoded_bytes = ser_bytes.decode("utf8")
            print(decoded_bytes)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        break
