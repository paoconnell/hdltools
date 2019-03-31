import os

import simtools

root = os.path.dirname(__file__)
sim = simtools.Simulation()
sim.add_source_files(os.path.join(root, "tst", "*.sv"))

sim.add_config("module_a_tb", "name1")
sim.add_config("module_a_tb", "name2", test_case="advanced")

sim.run()
