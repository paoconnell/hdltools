from vunit.verilog import VUnit
import os


class Simulation(object):

    def __init__(self):
        self.ui = VUnit.from_argv()
        self.lib = self.ui.add_library("lib")

    def add_source_files(self, source_files):
        self.lib.add_source_files(source_files)

    def add_config(self, testbench, name, test_case=None, params=None, pre_config=None):
        tbs = self.lib.get_test_benches("*"+testbench)
        if len(tbs) > 1:
            raise ValueError("Testbench {:s} found multiple times!".format(testbench))
        if tbs[0].name != testbench:
            raise ValueError("Testbench {:s} not found!".format(testbench))
        tb = tbs[0]
        if test_case is not None:
            tb = tb.test(test_case)
        if params is not None:
            name = name + "-" + "_".join(str(key)+"="+str(val) for key, val in params.items())
        tb.add_config(name, pre_config=pre_config)

    def run(self, coverage=False):
        self.ui.main()
