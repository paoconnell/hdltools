from vunit.verilog import VUnit
import os


class Simulation(object):

    def __init__(self):
        self.ui = VUnit.from_argv()
        self.lib = self.ui.add_library("lib")

    def add_source_files(self, source_files):
        self.lib.add_source_files(source_files)

    def run(self, coverage=False):
        self.ui.main()
