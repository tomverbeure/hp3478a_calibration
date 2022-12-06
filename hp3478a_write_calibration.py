#! /usr/bin/env python3

import pyvisa

def write_cal_data(hp3478a, cal_data):
    for addr in range(0, 256):
        # To write one nibble: 'X<address><byte>', where address and byte are raw 8-bit numbers.
        cmd = bytes([ord('X'), addr, cal_data[addr] ])
        hp3478a.write_raw(cmd)

def read_binary_file(filename):
    with open(filename, "rb") as f:
        cal_data = f.read()
    return cal_data

print("Writing calibration data...")
rm = pyvisa.ResourceManager()
hp3478a = rm.open_resource('GPIB0::7::INSTR')

cal_data = read_binary_file("hp3478a_cal_data.bin")
write_cal_data(hp3478a, cal_data)

