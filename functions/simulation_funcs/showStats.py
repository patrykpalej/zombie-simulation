import matplotlib.pyplot as plt


def show_humans_stats(humans, if_block, t, fig, fig_label):
    """
    Displays real time plots with humans parameters' distributions
    """

    plt.figure(fig_label)
    plt.clf()

    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot([0, 1], [0, t])
    ax2.plot([0, 1], [0, t])

    plt.suptitle(str(t))

    plt.show(block=if_block)


def show_zombies_stats(zombies, if_block, t, fig, fig_label):
    """
    Displays real time plots with zombiesparameters' distributions
    """

    plt.figure(fig_label)
    plt.clf()

    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot([0, 1], [0, t])
    ax2.plot([0, 1], [0, t])

    plt.suptitle(str(t))

    plt.show(block=if_block)
