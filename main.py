"""
Main script of the simulation
"""

from functions.init_funcs.initAll import init_all
from functions.runSimulation import run_simulation


humans, zombies, map_2d = init_all()

run_simulation(humans, zombies, map_2d)
