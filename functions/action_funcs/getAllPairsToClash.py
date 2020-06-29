import numpy as np


def get_all_pairs_to_clash(humans, zombies):
    """
    Lists (by index) all pairs H-Z which are about to clash
    """
    clash_pairs = []
    for h, human in enumerate(humans):
        for z, zombie in enumerate(zombies):
            if np.sqrt((human.x - zombie.x)**2 + (human.y - zombie.y)**2) < \
                    human.r + zombie.r:
                clash_pairs.append((h, z))

    return clash_pairs
