#! /usr/bin/env python3

from pymeasure.instruments.hp import HP3478A

inst = HP3478A("GPIB0::7::INST")
inst.display_text = "cal data rd"
cal_data = inst.calibration_data
print(cal_data)
print(inst.verify_calibration_data(cal_data))

# !!!
# Deliberately corrupt calibration data!
# !!!
cal_data[1] = 1
print(cal_data)
print(inst.verify_calibration_data(cal_data))
inst.display_text = "cal data wr"
inst.calibration_data = cal_data
inst.display_reset()

