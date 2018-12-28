#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Updated: 12/27/2018
# Created: 8/4/2018
# Author: loblab

import time
import RPi.GPIO as GPIO
from baseapp import *
from hibr import *
from lots import *

class LightApp(BaseApp):

    PIN_SIG = 14

    DEFAULT_DEVICE = "ttyUSB0"
    DEFAULT_BAUDRATE = 9600
    DEFAULT_VERIFY = -1
    DEFAULT_INTERVAL = 0.01

    def init_args(self):
        self.argps.add_argument('-d', '--device', dest='device', type=str, default=self.DEFAULT_DEVICE,
                help="Light control device port. default: '%s'" % self.DEFAULT_DEVICE)
        self.argps.add_argument('-b', '--baudrate', dest='baudrate', type=int,
                default=self.DEFAULT_BAUDRATE,
                help="Baudrate. default: %d" % self.DEFAULT_BAUDRATE)
        self.argps.add_argument('-v', '--verify', dest='verify', type=float,
                default=self.DEFAULT_VERIFY,
                help="Verify flag & delay (in second). <0: no verify; >=0: wait the time & verify. default: %f" % self.DEFAULT_VERIFY)
        self.argps.add_argument('-w', '--wait', dest='wait', type=float, default=self.DEFAULT_INTERVAL,
                help="Interval of 2 commands. default: %f" % self.DEFAULT_INTERVAL)

    def init_lots_ctrl(self, devpath):
        self.ctrl = LotsCtrl(app, devpath, self.args.baudrate)
        self.ctrl.set(1, 19)
        self.ctrl.set(2, 19)
        for i in range(3):
            self.ctrl.on(0)
            time.sleep(0.1)
            self.ctrl.off(0)
            time.sleep(0.1)

    def startup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_SIG, GPIO.OUT)
        devpath = "/dev/%s" % self.args.device
        self.init_lots_ctrl(devpath)

    def cleanup(self):
        self.ctrl.off(0)
        self.log.info("Cleanup GPIO")
        GPIO.cleanup()

    def init_wait(self):
        self.c = 0
        self.t1 = time.time()

    def wait(self):
        self.c += 1
        wait = self.t1 + self.args.wait * self.c
        wait -= time.time()
        if wait > 0:
            time.sleep(wait)

    def case1(self):
        while not self.quit_flag:
            self.wait()
            self.ctrl.on(2)
            GPIO.output(self.PIN_SIG, GPIO.HIGH)
            self.wait()
            self.ctrl.off(2)
            GPIO.output(self.PIN_SIG, GPIO.LOW)

    def run(self):
        self.init_wait()
        self.case1()
        return 0

if __name__ == "__main__":
    app = LightApp("Light control test program", "0.1")
    app.main()

