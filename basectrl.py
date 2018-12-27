import serial
import time

class BaseCtrl:

    COMMAND_DELAY = 0.05

    def __init__(self, app, device='/dev/ttyUSB0', baudrate=9600):
        self.verify_wait = -1
        self.log = app.log
        self.log.info("Light control device: %s, baudrate: %d", device, baudrate)
        self.port = serial.Serial(device,
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1)
        self.port.reset_input_buffer()

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

    def execute(self, cmd):
        self.log.info("Command: %s", cmd)
        print("Command: {}".format(cmd))
        #self.port.reset_input_buffer()
        data = cmd.encode()
        self.port.write(data)
        #time.sleep(BaseCtrl.COMMAND_DELAY)
        #line = self.port.readline()
        #print("Respone: {}".format(line))

    def request(self, cmd, size):
        self.port.reset_input_buffer()
        data = bytes(cmd)
        self.port.write(data)
        time.sleep(BaseCtrl.COMMAND_DELAY)
        data = self.port.read(size)
        if not data:
            print("%s: got empty data", cmd)
        print('Response: %s' % data)
        self.port.reset_input_buffer()
        return data


