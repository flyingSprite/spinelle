
import pexpect
import sys

"""

Pexpect Docs: http://pexpect.readthedocs.io/en/stable/
"""


class SimulationOnSsh(object):

    @staticmethod
    def is_win32():
        return sys.platform == 'win32'

    def login(self):
        if not self.is_win32():
            ssh = pexpect.spawn('ssh admin@192.168.105.82')
            res = ssh.expect(['Are you sure you want to continue connecting (yes/no)?', 'password:'])
            print(res)


sim = SimulationOnSsh()
sim.login()
