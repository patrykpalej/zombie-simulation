import numpy as np


def carry_out_clashes(humans, zombies, clash_pairs, rivals_number,
                      total_n_killed, total_n_inf, t):
    """
    Calculates number of humans' victories and zombies which lost a battle
    """

    victories = {"humans": [0 for _ in humans],
                 "zombies": [0 for _ in zombies]}
    loosers = {"humans": [], "zombies": []}
    single_iter_human_victories = 0
    single_iter_zombie_victories = 0
    for pair in clash_pairs:
        h = pair[0]
        z = pair[1]
        result \
            = np.sign(humans[h].battle_points/rivals_number["humans"][h]
                      - zombies[z].battle_points/rivals_number["zombies"][z])

        if result == 1:
            victories["humans"][h] += 1
            loosers["zombies"].append(z)
            print("human winner in {} iteration".format(t))
            single_iter_human_victories += 1
        else:
            victories["zombies"][z] += 1
            loosers["humans"].append(h)
            print("zombie winner in {} iteration".format(t))
            single_iter_zombie_victories += 1

    total_n_killed += single_iter_human_victories
    total_n_inf += single_iter_zombie_victories

    return victories, loosers, total_n_killed, total_n_inf
