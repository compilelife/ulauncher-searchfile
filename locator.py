import os
import subprocess
import logging
import sys

class Locator:
    def __init__(self):
        self.cmd = 'locate' if self.__check_has_locate() else None
        self.limit = 5
        self.opt = ''

    def set_limit(self, limit):
        print('set limit to '+str(limit))
        self.limit = limit

    def set_locate_opt(self, opt):
        print('set locate opt to '+opt)
        self.opt = opt

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
                cmd.append(self.opt)
                cmd.extend(args)
            print('----->'+str(cmd))
            output = subprocess.check_output(cmd)
            return output.splitlines()
