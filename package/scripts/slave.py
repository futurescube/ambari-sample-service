import sys, os
from resource_management import *
from resource_management.core.exceptions import ComponentIsNotRunning
from resource_management.core.environment import Environment
from resource_management.core.logger import Logger

class Slave(Script):
    def install(self, env):
        print "Install My Slave"

    def configure(self, env):
        print "Configure My Slave"

    def start(self, env):
        print "Start My Slave"

    def stop(self, env):
        print "Stop My Slave"
    def status(self, env):
        print "Status..."

if __name__ == "__main__":
    Slave().execute()