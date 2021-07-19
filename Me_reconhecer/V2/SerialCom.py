

import serial
import time

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(x.encode())
    time.sleep(0.01)
    data = arduino.readline()
    return data


while True:
    value = write_read("c100,050")
    print(value)
