import serial
import time

class BaseCtrl:

    COMMAND_DELAY = 0.05

    def __init__(self, app, device='/dev/ttyUSB0', baudrate=9600, channels=8):
        self.verify_wait = -1
        self.channels = channels
        self.log = app.log
        self.log.info("Init %s(%s, baudrate: %d)", self.__class__.__name__, device, baudrate)
        self.port = serial.Serial(device,
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1)
        self.port.reset_input_buffer()
        self._init()

    def _init(self):
        pass

    def set_verify(self, wait):
        self.verify_wait= wait
        if wait >= 0:
            self.port.reset_input_buffer()

    def write(self, cmd):
        self.log.debug("Write: %s", cmd)
        data = cmd.encode()
        self.port.write(data)

    def read(self, size=0):
        if size > 0:
            data = self.port.read(size)
        else:
            data = self.port.readline()
        self.log.debug("Read: %s", data)
        return data

    def set(self, channel, bright):
        self.log.error("set({}, {}): to be implemented".format(channel, bright))

    def on(self, channel=0):
        self.log.error("on({}): to be implemented".format(channel))

    def off(self, channel=0):
        self.log.error("off({}): to be implemented".format(channel))

