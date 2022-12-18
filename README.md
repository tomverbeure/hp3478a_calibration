
# HP 3478A Calibration Data Read/Write

Simple PyVISA scripts to dump the calibration data of an HP 3478A multimeter.

This repo goes along with my 
[HP 3478A Multimeter Calibration Data Backup and Battery Replacement](https://tomverbeure.github.io/2022/12/02/HP3478A-Multimeter-Calibration-Data-Backup-and-Battery-Replacement.html) blog post.

## Raw pyvisa scripts

To use, first install the linux-gpib kernel drivers, and install pyvisa and
pyvisa-py as follows:

```sh
pip3 isntall pyvisa pyvisa-py
```

Then edit the `hp3478a_read_calibration.py` script to point to the correct VISA interface. The default
script points to `GPIB::7`.

On my machine, running the script results in the following:

```
Fetching calibration data...

Contents of calibration RAM:
0000: 40 40 40 40 43 40 48 42 4f 44 44 40 4d 4b 40 40  @@@@C@HBODD@MK@@
0010: 40 40 43 43 42 4f 45 43 40 4e 40 40 40 40 40 40  @@CCBOEC@N@@@@@@
0020: 43 42 4f 44 40 40 4e 47 49 49 49 49 49 47 42 40  CBOD@@NGIIIIIGB@
0030: 4f 43 4c 4a 4b 49 49 49 49 49 49 42 40 4e 4f 4e  OCLJKIIIIIIB@NON
0040: 49 4c 40 40 40 40 40 40 40 40 40 40 40 4f 4f 49  IL@@@@@@@@@@@OOI
0050: 49 48 46 40 49 42 4e 4e 40 4c 4a 4c 49 49 49 49  IHF@IBNN@LJLIIII
0060: 49 45 41 4c 40 45 4e 4a 4d 49 49 49 49 49 48 41  IEAL@ENJMIIIIIHA
0070: 4c 41 4f 41 4a 4c 40 40 40 40 40 40 41 4c 4f 43  LAOAJL@@@@@@ALOC
0080: 40 4e 40 49 49 49 49 49 49 41 4c 4d 42 4e 49 4f  @N@IIIIIIALMBNIO
0090: 49 49 49 49 49 49 41 4c 4d 44 42 4a 49 49 49 49  IIIIIIALMDBJIIII
00a0: 49 49 49 41 4c 4e 4c 4d 49 45 49 49 49 49 49 49  IIIALNLMIEIIIIII
00b0: 41 4c 42 41 4f 4a 4a 40 40 40 40 44 42 43 40 40  ALBAOJJ@@@@DBC@@
00c0: 43 4c 4e 47 40 40 40 40 40 44 43 40 41 4c 43 4e  CLNG@@@@@DC@ALCN
00d0: 48 40 40 40 40 40 40 40 40 40 40 40 4f 4f 49 49  H@@@@@@@@@@@OOII
00e0: 48 46 40 49 43 4e 43 41 41 4c 40 40 40 40 40 40  HF@ICNCAAL@@@@@@
00f0: 40 40 40 40 40 40 4f 4f 40 40 40 40 40 40 40 40  @@@@@@OO@@@@@@@@

Checksum for all calibration values:
Checksum  0: 0xff  PASS
Checksum  1: 0xff  PASS
Checksum  2: 0xff  PASS
Checksum  3: 0xff  PASS
Checksum  4: 0xff  PASS
Checksum  5: 0xff  PASS (unused, FAIL is OK)
Checksum  6: 0xff  PASS
Checksum  7: 0xff  PASS
Checksum  8: 0xff  PASS
Checksum  9: 0xff  PASS
Checksum 10: 0xff  PASS
Checksum 11: 0xff  PASS
Checksum 12: 0xff  PASS
Checksum 13: 0xff  PASS
Checksum 14: 0xff  PASS
Checksum 15: 0xff  PASS
Checksum 16: 0xff  PASS (unused, FAIL is OK)
Checksum 17: 0xff  PASS
Checksum 18: 0xff  PASS (unused, FAIL is OK)

Writing calibration data to 'hp3478a_cal_data.bin'.
```

On your HP 3478A, the calibration data will obviously be different...

Note that in the printout above, each calibration value has an offset of 64. The
actual RAM values go from 0 to 15, not from 64 to 79.

## pymeasure Example

I added calibration data read/write functionality to [pymeasure](https://github.com/pymeasure/pymeasure).

The [pymeasure_calibration_read_write.py](./pymeasure_calibration_read_write.py) script
show how to use it.

In addition to installing `pyvisa` and `pyvisa-py`, you also need to install `pymeasure` to
run the script:

```sh
pip3 isntall pymeasure
```



