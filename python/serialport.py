# 1 

import serial

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE
)

#2

print(ser.read(size=8))

#3

from datetime import datetime 

#while ser.isOpen():
    #datastring = ser.read(size=8)
    #print(datetime.utcnow().isoformat(), datastring)

#4

import io


sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding = 'ascii', newline= '\r')
sio._CHUNK_SIZE = 1

with open('temps.tsv', 'a') as f:
    while ser.isOpen():
        datastring = sio.readline()
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush()
        print(datetime.utcnow().isoformat(), datastring)

ser.close()



