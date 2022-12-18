#! /usr/bin/env python3

from pymeasure.instruments.hp import HP3478A

inst = HP3478A("GPIB::7")

# Read calibration data
print("Reading calibration data...")
inst.display_text = "cal data rd"
cal_data = inst.calibration_data

print("Calibration data: ", cal_data)
print("Calibration data verification check: ", inst.verify_calibration_data(cal_data))

# Write calibration data
print("Writing calibration data...")
inst.display_text = "cal data wr"

try:
    inst.calibration_data = cal_data
except Exception as e:
    print(f"Failed to write calibration data: {str(e)}")

inst.display_reset()

