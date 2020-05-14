import matplotlib.pyplot as plt


def show_humans_stats(humans, if_block, t, fig, fig_label, attribs, titles,
                      map_dims):
    """
    Displays real time plots with humans parameters' distributions
    """

    plt.figure(fig_label)
    plt.clf()

    attribs_dict = dict((att, []) for att in attribs)
    [attribs_dict[attr].append(getattr(h, attr))
     for h in humans for attr in attribs]

    axes = []
    for ax in range(len(attribs_dict)):
        axes.append(fig.add_subplot(4, 2, ax+1))
        axes[-1].scatter(range(len(humans)), attribs_dict[attribs[ax]])
        axes[-1].set_title(titles[ax])
        plt.tick_params(axis='x', which='both', bottom=False, top=False,
                        labelbottom=False)

    axes[0].set_ylim([0, map_dims[1]])
    axes[1].set_ylim([0, map_dims[0]])
    plt.subplots_adjust(left=0.05, bottom=0.01, right=0.95, top=0.92,
                        wspace=0.2, hspace=0.3)
    plt.suptitle("Humans  (" + str(len(humans)) + ")", fontsize=15,
                 y=0.99)

    plt.show(block=if_block)


def show_zombies_stats(zombies, if_block, t, fig, fig_label, attribs, titles,
                       map_dims):
    """
    Displays real time plots with zombiesparameters' distributions
    """

    plt.figure(fig_label)
    plt.clf()

    attribs_dict = dict((att, []) for att in attribs)
    [attribs_dict[attr].append(getattr(z, attr))
     for z in zombies for attr in attribs]

    axes = []
    for ax in range(len(attribs_dict)):
        axes.append(fig.add_subplot(3, 2, ax + 1))
        axes[-1].scatter(range(len(zombies)), attribs_dict[attribs[ax]], c='r')
        axes[-1].set_title(titles[ax])
        plt.tick_params(axis='x', which='both', bottom=False, top=False,
                        labelbottom=False)

    axes[0].set_ylim([0, map_dims[1]])
    axes[1].set_ylim([0, map_dims[0]])
    plt.subplots_adjust(left=0.05, bottom=0.01, right=0.95, top=0.92,
                        wspace=0.2, hspace=0.3)
    plt.suptitle("Zombies  (" + str(len(zombies)) + ")", fontsize=15,
                 y=0.99)

    plt.show(block=if_block)
