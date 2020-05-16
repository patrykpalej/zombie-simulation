def prepare(humans, zombies):
    """
    Calculate battle points for each character
    """

    for h in humans:
        h.battle_points = h.strength * (1 + h.n_killed / 10) * (h.stamina / 5)

    for z in zombies:
        z.battle_points = z.poison * (1 + z.n_infected / 10)

    return humans, zombies
