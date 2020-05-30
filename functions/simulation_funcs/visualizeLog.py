import numpy as np
import matplotlib.pyplot as plt


def visualize_log(simulation_log):
    """
    Analyze and visualize simulation log
    """
    n_humans = simulation_log["N_H"][:]
    n_zombies = simulation_log["N_Z"][:]

    bp_humans = simulation_log["mean_BP_H"][:]
    bp_zombies = simulation_log["mean_BP_Z"][:]

    n_killed = simulation_log["total_n_killed"][:]
    n_infected = simulation_log["total_n_infected"][:]

    # 1. Number of characters throughout iterations
    # fig, ax1 = plt.subplots(figsize=(14, 9))
    # ax2 = ax1.twinx()

    # ax1.plot(n_humans, color="#1f77b4")
    # ax2.plot(n_zombies, color="red")
    #
    # ax1.set_ylim([0, 1.1*max(max(n_humans), max(n_zombies))])
    # ax2.set_ylim([0, 1.1*max(max(n_humans), max(n_zombies))])
    #
    # plt.title("Number of humans and zombies in subsequent iterations",
    #           fontsize=20)
    # ax1.set_xlabel("Iterations", fontsize=20)
    # ax1.set_ylabel("Humans", fontsize=16, color="#1f77b4")
    # ax2.set_ylabel("Zombies", fontsize=16, color="red")
    #
    # ax1.tick_params(axis='both', labelsize=14)
    # ax2.tick_params(axis='both', labelsize=14)
    #
    # plt.savefig(figure=fig, fname="results/output1.png")

    # 2. Average battle points throughout iterations
    # fig, ax1 = plt.subplots(figsize=(14, 9))
    # ax2 = ax1.twinx()

    # ax1.plot(bp_humans, color="#1f77b4")
    # ax2.plot(bp_zombies, color="red")
    #
    # ax1.set_ylim([0, 1.1*max(max(bp_humans), max(bp_zombies))])
    # ax2.set_ylim([0, 1.1*max(max(bp_humans), max(bp_zombies))])
    #
    # plt.title("Average battle points of humans and zombies in subsequent "
    #           "iterations", fontsize=20)
    # ax1.set_xlabel("Iterations", fontsize=20)
    # ax1.set_ylabel("Humans", fontsize=16, color="#1f77b4")
    # ax2.set_ylabel("Zombies", fontsize=16, color="red")
    #
    # ax1.tick_params(axis='both', labelsize=14)
    # ax2.tick_params(axis='both', labelsize=14)

    # 3. Total n_killed and n_infected
    # fig, ax1 = plt.subplots(figsize=(14, 9))
    # ax2 = ax1.twinx()

    # ax1.plot(n_killed, color="#1f77b4")
    # ax2.plot(n_infected, color="red")
    #
    # ax1.set_ylim([0, 1.1 * max(max(n_killed), max(n_infected))])
    # ax2.set_ylim([0, 1.1 * max(max(n_killed), max(n_infected))])
    #
    # plt.title("Average battle points of humans and zombies in subsequent "
    #           "iterations", fontsize=20)
    # ax1.set_xlabel("Iterations", fontsize=20)
    # ax1.set_ylabel("Humans", fontsize=16, color="#1f77b4")
    # ax2.set_ylabel("Zombies", fontsize=16, color="red")
    #
    # ax1.tick_params(axis='both', labelsize=14)
    # ax2.tick_params(axis='both', labelsize=14)
    #
    # plt.savefig(figure=fig, fname="results/output3.png")

    # 4. Number of, battle points and n_killed/infected on one plot
    def two_scales(_ax1, data1, data2, c1, c2, y_lim):
        _ax2 = _ax1.twinx()
        _ax1.plot(data1, color=c1)
        _ax2.plot(data2, color=c2)
        _ax1.tick_params(axis='both', labelsize=11)
        _ax2.tick_params(axis='both', labelsize=11)
        _ax1.set_ylabel("Humans", fontsize=14, color=c1)
        _ax2.set_ylabel("Zombies", fontsize=14, color=c2)
        _ax1.set_ylim([0, y_lim])
        _ax2.set_ylim([0, y_lim])

        return _ax1, _ax2

    # Create axes
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(11, 11))
    ylim = 1.1*max(max(n_humans), max(n_zombies))
    ax1, ax1a = two_scales(ax1, n_humans, n_zombies, '#1f77b4', 'red', ylim)
    ylim = 1.1 * max(max(bp_humans), max(bp_zombies))
    ax2, ax2a = two_scales(ax2, bp_humans, bp_zombies, '#1f77b4', 'red', ylim)
    ylim = 1.1 * max(max(n_killed), max(n_infected))
    ax3, ax3a = two_scales(ax3, n_killed, n_infected, '#1f77b4', 'red', ylim)

    # Add description
    ax3.set_xlabel("Iterations", fontsize=18)
    plt.subplots_adjust(top=0.99, bottom=0.05, hspace=0.2)
    fig.text(0.04, 0.85, "Number of", ha='center', va='center',
             rotation='vertical', fontsize=18)
    fig.text(0.04, 0.53, "Battle points", ha='center', va='center',
             rotation='vertical', fontsize=18)
    fig.text(0.04, 0.2, "N_killed / infected", ha='center', va='center',
             rotation='vertical', fontsize=18)

    plt.savefig(figure=fig, fname="results/output_plot.png")

    plt.close('all')
