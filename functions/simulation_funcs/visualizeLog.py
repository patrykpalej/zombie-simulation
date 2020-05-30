import matplotlib.pyplot as plt


def visualize_log(simulation_log):
    """
    Analyze and visualize simulation log
    """
    # 1. Number of characters throughout iterations
    fig, ax1 = plt.subplots(figsize=(14, 9))
    ax2 = ax1.twinx()

    n_humans = simulation_log["N_H"][:]
    n_zombies = simulation_log["N_Z"][:]
    ax1.plot(n_humans, color="#1f77b4")
    ax2.plot(n_zombies, color="red")

    ax1.set_ylim([0, 1.1*max(max(n_humans), max(n_zombies))])
    ax2.set_ylim([0, 1.1*max(max(n_humans), max(n_zombies))])

    plt.title("Number of humans and zombies in subsequent iterations",
              fontsize=20)
    ax1.set_xlabel("Iterations", fontsize=20)
    ax1.set_ylabel("Humans", fontsize=16, color="#1f77b4")
    ax2.set_ylabel("Zombies", fontsize=16, color="red")

    ax1.tick_params(axis='both', labelsize=14)
    ax2.tick_params(axis='both', labelsize=14)

    plt.savefig(figure=fig, fname="results/output1.png")

    # 2. Average battle points throughout iterations
    fig, ax1 = plt.subplots(figsize=(14, 9))
    ax2 = ax1.twinx()

    bp_humans = simulation_log["mean_BP_H"][:]
    bp_zombies = simulation_log["mean_BP_Z"][:]
    ax1.plot(bp_humans, color="#1f77b4")
    ax2.plot(bp_zombies, color="red")

    ax1.set_ylim([0, 1.1*max(max(bp_humans), max(bp_zombies))])
    ax2.set_ylim([0, 1.1*max(max(bp_humans), max(bp_zombies))])

    plt.title("Average battle points of humans and zombies in subsequent "
              "iterations", fontsize=20)
    ax1.set_xlabel("Iterations", fontsize=20)
    ax1.set_ylabel("Humans", fontsize=16, color="#1f77b4")
    ax2.set_ylabel("Zombies", fontsize=16, color="red")

    ax1.tick_params(axis='both', labelsize=14)
    ax2.tick_params(axis='both', labelsize=14)

    # 3. Total n_killed and n_infected
    fig, ax1 = plt.subplots(figsize=(14, 9))
    ax2 = ax1.twinx()

    n_killed = simulation_log["total_n_killed"][:]
    n_infected = simulation_log["total_n_infected"][:]
    ax1.plot(n_killed, color="#1f77b4")
    ax2.plot(n_infected, color="red")

    ax1.set_ylim([0, 1.1 * max(max(n_killed), max(n_infected))])
    ax2.set_ylim([0, 1.1 * max(max(n_killed), max(n_infected))])

    plt.title("Average battle points of humans and zombies in subsequent "
              "iterations", fontsize=20)
    ax1.set_xlabel("Iterations", fontsize=20)
    ax1.set_ylabel("Humans", fontsize=16, color="#1f77b4")
    ax2.set_ylabel("Zombies", fontsize=16, color="red")

    ax1.tick_params(axis='both', labelsize=14)
    ax2.tick_params(axis='both', labelsize=14)

    plt.savefig(figure=fig, fname="results/output3.png")

    plt.close('all')
