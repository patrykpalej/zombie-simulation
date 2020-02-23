import json
import pandas as pd
import matplotlib.pyplot as plt

from functions.simulation_funcs.move import move
from functions.simulation_funcs.action import action
from functions.simulation_funcs.updateLog import update_log
from functions.simulation_funcs.showSimulation import show_simulation
from functions.simulation_funcs.showStats import show_humans_stats, \
    show_zombies_stats


def run_simulation(humans, zombies, map_2d):
    """
    Performs the simulation. Takes lists of humans and zombies objects and a
    map. Returns a log which contains information about the simulation run.
    """

    # 1. Plots configuration
    with open("plots_config.json") as handle:
        plots_config = json.load(handle)

    labels = list(plots_config.keys())
    figures = []
    plt.ion()
    for label, geom in plots_config.items():
        fig = plt.figure(label)
        figures.append(fig)
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(geom[0], geom[1], geom[2], geom[3])

    # 2. Simulation
    t = 1
    end_sim = 0
    simulation_log = pd.DataFrame()  # for now it's a df

    while not end_sim:
        move(humans, zombies)
        action(humans, zombies)

        show_simulation(map_2d, humans, zombies, False, t)
        show_humans_stats(humans, False, t, figures[1], labels[1])
        show_zombies_stats(zombies, False, t, figures[2], labels[2])

        simulation_log = update_log(simulation_log, humans, zombies)

        if t >= 15 or len(humans) < 1 or len(zombies) < 1:
            end_sim = 1
            show_simulation(map_2d, humans, zombies, True, t)
        t += 1
        plt.pause(0.01)

    return simulation_log
