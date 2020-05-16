import numpy as np


def action(humans, zombies):
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
    rivals_number = {"humans": [0 for i in humans],
                     "zombies": [0 for i in zombies]}

    for pair in clash_pairs:
        rivals_number["humans"][pair[0]] += 1
        rivals_number["zombies"][pair[1]] += 1

    # 3. Carry out all clashes considering number of rivals and remember the
    # results
    victories = {"humans": [0 for i in humans],
                 "zombies": [0 for i in zombies]}
    loosers = {"humans": [], "zombies": []}
    for pair in clash_pairs:
        h = pair[0]
        z = pair[1]
        result \
            = np.sign(humans[h].battle_points/rivals_number["humans"][h]
                      - zombies[z].battle_points/rivals_number["zombies"][z])

        if result == 1:
            victories["humans"][h] += 1
            loosers["zombies"].append(z)
        else:
            victories["zombies"][z] += 1
            loosers["humans"].append(h)

    # 4. Implement results of the fight - death, infection,
    # n_killed/n_infected increase etc.
    # first add points for all victories, later consider loosers

    return humans, zombies
