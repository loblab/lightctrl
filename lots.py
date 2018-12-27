# http://www.lotsmv.com/
# LTS-2DPC2460-4S

from basectrl import *
import time
from functools import reduce

class LotsCtrl(BaseCtrl):

    CMD_FMT = "$%d%d%03X"
    CH_ON = 1
    CH_OFF = 2
    CH_SET = 3
    CH_GET = 4
    ALL_ON = 5
    ALL_OFF = 6
    RET_OK = b'$'
    RET_NG = b'&'

    @staticmethod
    def append_checksum(txt):
        num = [ord(c) for c in txt]
        xor = reduce(lambda a, b: a ^ b, num, 0)
        ret = "%s%02X" % (txt, xor)
        return ret

    def verify(self):
        ret = self.read(1)
        if ret != self.RET_OK:
            self.log.warning("Readback error: %s (%s)", ret, cmd)

    def command(self, cmd, verify_wait=-1):
        self.log.info("Command: %s", cmd)
        self.write(LotsCtrl.append_checksum(cmd))
        if verify_wait < 0:
            return
        if verify_wait > 0:
            time.sleep(verify_wait)
        self.verify()

    def set(self, channel, bright):
        self.command(self.CMD_FMT % (self.CH_SET, channel, bright), self.verify_wait)

    def on(self, channel=0):
        cmd = self.CH_ON if channel > 0 else self.ALL_ON
        self.command(self.CMD_FMT % (cmd, channel, 0), self.verify_wait)

    def off(self, channel=0):
        cmd = self.CH_OFF if channel > 0 else self.ALL_OFF
        self.command(self.CMD_FMT % (cmd, channel, 0), self.verify_wait)

