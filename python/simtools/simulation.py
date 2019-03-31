from vunit.verilog import VUnit
import os


class Simulation(object):

    def __init__(self):
        self.ui = VUnit.from_argv()
        self.lib = self.ui.add_library("lib")

    def add_source_files(self, source_files):
        self.lib.add_source_files(source_files)

    def add_config(self, testbench, name):
        tbs = self.lib.get_test_benches("*"+testbench)
        if len(tbs) > 1:
            raise ValueError("Testbench {:s} found multiple times!".format(testbench))
        if tbs[0].name != testbench:
            raise ValueError("Testbench {:s} not found!".format(testbench))
        tb = tbs[0]
        tb.add_config(name)

    def run(self, coverage=False):
        self.ui.main()
