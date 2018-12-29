# http://www.highbright.com.tw
# PC-24V60W-4-R

from basectrl import *

class HibrCtrl(BaseCtrl):

    DEFAULT_BRIGHT = 80
    ALL_CHANNELS = 'A'
    OFF_BRIGHT = 0

    def _save_all_bright(self, bright):
        for i in range(self.channels):
            self.bright[i] = bright

    def _init(self):
        self.bright = [0] * self.channels
        self._save_all_bright(self.DEFAULT_BRIGHT)

    def command(self, cmd):
        self.log.info("Command: %s", cmd)
        self.write(cmd + "\r\n")

    def set(self, channel, bright):
        self.log.info("Command: set channel {} to {}".format(channel, bright))
        cmd = "{},{}\r\n".format(channel, bright)
        self.write(cmd)
        if bright <= self.OFF_BRIGHT:
            return
        if channel == self.ALL_CHANNELS:
            self._save_all_bright(bright)
        else:
            self.bright[channel - 1] = bright

    def on(self, channel=0):
        if channel == 0:
            channel=self.ALL_CHANNELS
            bright = self.bright[0]
        else:
            bright = self.bright[channel - 1]
        self.set(channel, bright)

    def off(self, channel=0):
        if channel == 0:
            channel=self.ALL_CHANNELS
        self.set(channel, self.OFF_BRIGHT)

