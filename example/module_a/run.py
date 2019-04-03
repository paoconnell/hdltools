import os

import hdltools

def generate_input(params):
    def func(output_path):
        print("Generating Input value: {:d}".format(params['value']))
        return True
    return func

root = os.path.dirname(__file__)
sim = hdltools.Simulation()
sim.add_include_dir(os.path.join(root, "..", "include"))
sim.add_source_files(os.path.join(root, "tst", "*.sv"))

params = {
'value': 0,
}
for value in [10, 20]:
    params = params.copy()
    params['value'] = value
    sim.add_config("module_a_tb", "name1", params=params, pre_config=generate_input(params))
    sim.add_config("module_a_tb", "name2", params=params, test_case="advanced", pre_config=generate_input(params))
    sim.add_config("module_a_tb", "name3", params=params, test_case="basic")

sim.run()
