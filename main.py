"""
Main script of the simulation
"""
from datetime import datetime

from functions.init_funcs.initAll import init_all
from functions.runSimulation import run_simulation
from functions.util_funcs.transformTimestamps import transform_timestamps


time_tracker = dict()
time_tracker["time_start"] = datetime.now()

humans, zombies, map_2d, time_tracker \
    = init_all(time_tracker)

simulation_log, time_tracker \
    = run_simulation(humans, zombies, map_2d, time_tracker)

time_tracker["finish"] = datetime.now()
durations = transform_timestamps(time_tracker)

print(durations)
