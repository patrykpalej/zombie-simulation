def update_log(simulation_log, humans, zombies, total_n_killed,
               total_n_infected):
    """
    Updates the simulation log after each time iteration and returns it
    """
    # 1. Number of
    n_h = len(humans)
    n_z = len(zombies)
    # 2. Battle points
    mean_bp_h = sum([h.battle_points for h in humans])/len(humans) \
        if humans else 0
    mean_bp_z = sum([z.battle_points for z in zombies])/len(zombies) \
        if zombies else 0
    # 3. Cummulated number of killed/infected
    # function args
    # 4. ...

    new_row = [n_h, n_z,
               mean_bp_h, mean_bp_z,
               total_n_killed, total_n_infected]

    simulation_log.loc[len(simulation_log)] = new_row

    return simulation_log
