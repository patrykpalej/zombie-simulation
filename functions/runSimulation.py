import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

from functions.simulation_funcs.move import move
from functions.simulation_funcs.action import action
from functions.simulation_funcs.prepare import prepare
from functions.simulation_funcs.updateLog import update_log
from functions.simulation_funcs.getYlims import get_ylims
from functions.simulation_funcs.showSimulation import show_simulation
from functions.simulation_funcs.showStats import show_humans_stats, \
    show_zombies_stats


def run_simulation(humans, zombies, map_2d, time_tracker):
    """
    Performs the simulation. Takes lists of humans and zombies objects and a
    map. Returns a log which contains information about the simulation run.
    """

    # 1. Configuration
    # a) figures configuration
    with open("data/plots_config.json") as handle:
        plots_config = json.load(handle)

    labels = list(plots_config.keys())[:3]
    figures = []
    plt.ion()
    for label in labels:
        fig = plt.figure(label)
        geom = plots_config[label]
        figures.append(fig)
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(geom[0], geom[1], geom[2], geom[3])

    # b) plots metadata configuration
    human_attribs = plots_config["human_attribs"]
    human_titles = plots_config["human_titles"]
    zombie_attribs = plots_config["zombie_attribs"]
    zombie_titles = plots_config["zombie_titles"]

    time_tracker["after_config"] = datetime.now()

    # 2. Simulation
    t = 1
    end_sim = 0
    simulation_log = pd.DataFrame()
    time_tracker["iterations"] = []
    while not end_sim:
        prepare(humans, zombies)
        move(humans, zombies, map_2d)
        action(humans, zombies)

        human_ylims, zombie_ylims = get_ylims(humans, zombies)
        show_simulation(map_2d, humans, zombies, False, t)
        show_humans_stats(humans, False, t, figures[1], labels[1],
                          human_attribs, human_titles, human_ylims)
        show_zombies_stats(zombies, False, t, figures[2], labels[2],
                           zombie_attribs, zombie_titles, zombie_ylims)

        simulation_log = update_log(simulation_log, humans, zombies)
        time_tracker["iterations"].append(datetime.now())

        if t >= 10 or len(humans) < 1 or len(zombies) < 1:
            time_tracker["stop_decision"] = datetime.now()
            end_sim = 1
            show_simulation(map_2d, humans, zombies, True, t)
            plt.close('all')

        t += 1
        plt.pause(0.01)

    return simulation_log, time_tracker
