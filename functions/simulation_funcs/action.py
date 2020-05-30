import numpy as np

from classes.Zombie import Zombie


def action(humans, zombies, t, total_n_killed, total_n_inf):
    """
    For each character performs an action such as a battle with an opponent.
    Returns the state of characters after all fights.
    """

    # 1. Get all pairs which are about to clash
    clash_pairs = []
    for h, human in enumerate(humans):
        for z, zombie in enumerate(zombies):
            if np.sqrt((human.x - zombie.x)**2 + (human.y - zombie.y)**2) < \
                    human.r + zombie.r:
                clash_pairs.append((h, z))

    # 2. Calculate how many rivals has each character
    rivals_number = {"humans": [0 for _ in humans],
                     "zombies": [0 for _ in zombies]}

    for pair in clash_pairs:
        rivals_number["humans"][pair[0]] += 1
        rivals_number["zombies"][pair[1]] += 1

    # 3. Carry out all clashes considering number of rivals and remember the
    # results
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

    # 4. Implement results of the fight - death, infection etc.

    # Increase n_killed and n_infected
    for human, human_result in zip(humans, victories["humans"]):
        human.n_killed += human_result

    for zombie, zombie_result in zip(zombies, victories["zombies"]):
        zombie.n_infected += zombie_result

    # Remove killed zombies and turn infected humans into zombies
    killed_zombies = loosers["zombies"].copy()
    killed_zombies = list(set(killed_zombies))
    killed_zombies.sort()
    killed_zombies.reverse()

    for zombie_index in killed_zombies:
        del zombies[zombie_index]

    # ---
    infected_humans = loosers["humans"]
    infected_humans = list(set(infected_humans))
    infected_humans.sort()
    infected_humans.reverse()

    for human_index in infected_humans:
        h = humans[human_index]
        zombie_params = {"x": h.x, "y": h.y, "color": 0.85,
                         "velocity": h.velocity, "r": h.r,
                         "nose": h.eye, "poison": h.strength}

        del humans[human_index]
        zombies.append(Zombie(zombie_params))

    return total_n_killed, total_n_inf
