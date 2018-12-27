import logging
import argparse

class BaseApp:

    def __init__(self, description, version):
        self.argps = argparse.ArgumentParser(description=description)
        self.argps.add_argument('-V', '--version', action='version', version=version)
        self.argps.add_argument('-D', '--debug', action='store_true', help="show debug messages")
        self.init_args()
        self.args = self.argps.parse_args()
        self.init_logger()
        self.log.info(description)
        self.log.info(version)
        if self.args.debug:
            self.log.debug("Debug: on")

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

