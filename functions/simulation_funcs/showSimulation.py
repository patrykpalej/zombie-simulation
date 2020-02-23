import numpy as np
import matplotlib.pyplot as plt


def show_simulation(map_2d, humans, zombies, if_block, t):
    """
    Displays the map with characters on it in a given time step
    """

    showmap = map_2d.copy()

    for h in humans:
        radius = round(h.r)
        for x in range(-radius, radius+1):
            for y in range(-radius, radius+1):
                if round(np.sqrt(x**2 + y**2)) <= h.r:
                    showmap[round(h.y+y), round(h.x+x)] = h.color

    for z in zombies:
        radius = round(z.r)
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                if round(np.sqrt(x**2 + y**2)) <= z.r:
                    showmap[round(z.y+y), round(z.x+x)] = z.color

    plt.figure("Simulation")
    plt.imshow(showmap, cmap='nipy_spectral')
    plt.title(str(t))

    plt.show(block=if_block)
