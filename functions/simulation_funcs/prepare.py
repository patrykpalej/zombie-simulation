def prepare(humans, zombies):
    """
    Calculate battle points and color for each character
    """

    # 1. Humans
    bp_list = []
    for h in humans:
        h.battle_points \
            = h.strength * (1 + h.n_killed / 10)  # * (h.stamina / 4)
        bp_list.append(h.battle_points)

    for h in humans:
        h.color = 0.4 - 0.2*(h.battle_points - min(bp_list)) / \
                  (max(bp_list) - min(bp_list) + 0.01)

    # 2. Zombies
    bp_list = []
    for z in zombies:
        z.battle_points = z.poison * (1 + z.n_infected / 10)
        bp_list.append(z.battle_points)

    for z in zombies:
        z.color = 0.95 - 0.13 * (z.battle_points - min(bp_list)) / \
                  (max(bp_list) - min(bp_list) + 0.01)

    return humans, zombies
