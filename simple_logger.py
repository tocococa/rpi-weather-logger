from serial import Serial
ser = Serial(
    port="com3",
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
