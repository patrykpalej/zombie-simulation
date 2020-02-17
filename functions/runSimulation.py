import pandas as pd

from functions.simulation_funcs.move import move
from functions.simulation_funcs.action import action
from functions.simulation_funcs.showAll import show_all
from functions.simulation_funcs.updateLog import update_log


def run_simulation(humans, zombies, map_2d):
    """
    Performs the simulation. Takes lists of humans and zombies objects and a
    map. Returns a log which contains information about the simulation run.
    """

    t = 1
    end_sim = 0
    simulation_log = pd.DataFrame()  # for now it's a df

    while not end_sim:
        move(humans, zombies)
        action(humans, zombies)
        show_all(map_2d, humans, zombies, False)

        simulation_log = update_log(simulation_log, humans, zombies)

        if t >= 15 or len(humans) < 1 or len(zombies) < 1:
            end_sim = 1
            show_all(map_2d, humans, zombies, True)
        t += 1

    return simulation_log
