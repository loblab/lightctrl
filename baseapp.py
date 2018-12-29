import os
import sys
import time
import signal
import logging
import argparse

class BaseApp:

    def __init__(self, desc, ver_num):
        signal.signal(signal.SIGINT, self.sig_handler)
        signal.signal(signal.SIGTERM, self.sig_handler)
        self.quit_flag = False
        sfile = sys.argv[0]
        ver = ("Ver %s, " % ver_num) + time.strftime("%Y/%m/%d %H:%M %Z, loblab",
            time.localtime(os.path.getmtime(sfile)))
        self.argps = argparse.ArgumentParser(description=desc)
        self.argps.add_argument('-V', '--version', action='version', version=ver)
        self.argps.add_argument('-D', '--debug', action='store_true',
                help="output more logs (debug level)")
        self.init_args()
        self.args = self.argps.parse_args()
        self.init_logger()
        self.log.info(desc)
        self.log.info(ver)
        if self.args.debug:
            self.log.debug("Debug: on")

    def sig_handler(self, signum, frame):
        self.log.info("Got signal %d" % signum)
        self.quit_flag = True

    def init_args(self):
        pass

    def init_logger(self):
        FORMAT = '%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s'
        DATEFMT = '%m/%d %H:%M:%S'
        logging.basicConfig(format=FORMAT, datefmt=DATEFMT)
        self.log = logging.getLogger()
        if self.args.debug:
            self.log.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.INFO)

    def startup(self):
        pass

    def cleanup(self):
        pass

    def run(self):
        return 0

    def main(self):
        try:
            self.startup()
            rc = self.run()
        except Exception as e:
            self.log.exception(str(e))
            rc = -1
        finally:
            self.cleanup()
        return rc

