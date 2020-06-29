def get_ylims(humans, zombies):
    """
    Returns ylims for showing characters statistics
    """
    # 1. Calculate max values for the y_lims
    max_stamina = max([h.stamina for h in humans] + [0])
    max_battle_points = 1.1*max([h.battle_points for h in humans]
                                + [z.battle_points for z in zombies])
    max_truevelo = max([h.true_velo for h in humans] + [0])
    max_smell = 1.1*max([h.smell for h in humans] + [0])
    max_eyenose = 1.1*max([h.eye for h in humans] + [z.nose for z in zombies])

    # 2. Create lists of max ylims
    human_ylims = [[0, 2], [0, max(8, max_stamina)], [0, max_battle_points],
                   [0, 1], [0, 1], [0, max_truevelo],
                   [0, 1], [0, max_smell], [0, max_eyenose]]

    zombie_ylims = [[1, max_battle_points], [0, max_truevelo],
                    [0, max_eyenose]]

    return human_ylims, zombie_ylims
