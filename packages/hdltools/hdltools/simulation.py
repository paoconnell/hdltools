from vunit.verilog import VUnit
import os


class Simulation(object):

    def __init__(self):
        self.ui = VUnit.from_argv()
        self.lib = self.ui.add_library("lib")
        self.include_dirs = []
        self.modelsim_flags = []

    def add_include_dir(self, dir):
        self.include_dirs.append(dir)

    def use_unisim_libraries(self):
        self.lib.add_source_file(os.path.join(os.environ["VUNIT_VIVADO_PATH"], "..", "data", "verilog", "src", "glbl.v"))
        self.ui.add_external_library("unisims_ver", os.path.join(os.environ["VUNIT_XILINX_LIBRARIES_PATH"], "unisims_ver"))
        self.modelsim_flags.extend(["lib.glbl"])

    def add_source_files(self, source_files):
        self.lib.add_source_files(source_files, include_dirs=self.include_dirs)

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
        self.ui.set_sim_option("modelsim.vsim_flags", self.modelsim_flags)
        self.ui.main()
