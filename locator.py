import os
import subprocess
import logging
import sys

class Locator:
    def __init__(self):
        self.cmd = 'locate' if self.__check_has_locate() else None
        self.limit = 5

    def set_limit(self, limit):
        print('set limit to '+str(limit))
        self.limit = limit

    def __check_has_locate(self):
        try:
            subprocess.check_call(['which', 'locate'])
            return True
        except:
            return False

    def run(self, pattern):
        if self.cmd == None:
            raise RuntimeError('command locate not found or options config error')
        else:
            cmd = [self.cmd, '-l', str(self.limit)]
            args = pattern.split(' ')
            if args[0] == 'r':
                cmd.extend(args[1:])
            else:
                cmd.extend(['-iA', pattern])
            print('----->'+str(cmd))
            output = subprocess.check_output(cmd)
            return output.splitlines()
