# http://www.highbright.com.tw
# PC-24V60W-4-R

from basectrl import *

class HibrCtrl(BaseCtrl):

    def command(self, cmd):
        self.log.info("Command: %s", cmd)
        self.write(cmd + "\r\n")

    def set(self, channel, value):
        cmd = "%d,%d\r\n" % (channel, value)
        self.write(cmd)

