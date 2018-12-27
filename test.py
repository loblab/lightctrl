#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Updated: 12/27/2018
# Created: 8/4/2018
# Author: loblab

import time
from baseapp import *
from hibr import *
from lots import *

class LightApp(BaseApp):

    DEFAULT_DEVICE = "ttyUSB0"
    DEFAULT_BAUDRATE = 9600
    DEFAULT_VERIFY = -1

    def init_args(self):
        self.argps.add_argument('-d', '--device', dest='device', type=str, default=self.DEFAULT_DEVICE,
                help="Light control device port. default: '%s'" % self.DEFAULT_DEVICE)
        self.argps.add_argument('-b', '--baudrate', dest='baudrate', type=int,
                default=self.DEFAULT_BAUDRATE,
                help="Baudrate. default: %d" % self.DEFAULT_BAUDRATE)
        self.argps.add_argument('-v', '--verify', dest='verify', type=float,
                default=self.DEFAULT_VERIFY,
                help="Verify flag & delay (in second). <0: no verify; >=0: wait the time & verify. default: %f" % self.DEFAULT_VERIFY)
        self.argps.add_argument('-w', '--wait', dest='wait', type=float, default=0,
                help="Wait in second between 2 commands. default: 0")

    def startup(self):
        device = "/dev/%s" % self.args.device
        self.ctrl = LotsCtrl(app, device, self.args.baudrate)

    def run(self):
        self.ctrl.set(1, 19)
        self.ctrl.set(2, 19)
        for i in range(3):
            self.ctrl.on(0)
            time.sleep(0.1)
            self.ctrl.off(0)
            time.sleep(0.1)
        for i in range(30000):
            self.ctrl.on(1)
            time.sleep(self.args.wait)
            self.ctrl.off(1)
            time.sleep(self.args.wait)
        return 0

if __name__ == "__main__":
    app = LightApp("Light control test program", "ver 0.1, loblab, 12/27/2018")
    app.main()

