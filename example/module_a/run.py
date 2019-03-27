import os

import simtools

root = os.path.dirname(__file__)
sim = simtools.Simulation()
sim.add_source_files(os.path.join(root, "tst", "*.sv"))
sim.run()
