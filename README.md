# Light controllers

Support & test some RS232 based light controller devices.

Test command speed & delay.

- Platform: Linux (Raspberry Pi), Python 2.x/3.x
- Ver: 0.1
- Ref: [Testing method & report of some light controllers (Chinese)](https://www.jianshu.com/u/3c1a902a844b)
- Updated: 12/30/2018
- Created: 12/27/2018
- Author: loblab

![Test environment](https://raw.githubusercontent.com/loblab/lightctrl/master/test-env.jpg)

## Supported/tested devices

### [LOTS](http://www.lotsmv.com/)

- LTS-2DPC2460-2S

### [High bright](http://www.highbright.com.tw/)

- PC-24V60W-8-R-115200
- PC-24V120W-4-R-115200

## Usage

Run test.py -h to see help. And some command line examples:

```bash
./test.py -h
./test.py -t lots -b 9600 -w 0.012
./test.py -d ttyUSB1 -t hibr -b 115200 -w 0.1 -c 8
```

![script screenshot](https://raw.githubusercontent.com/loblab/lightctrl/master/screenshot.png)

