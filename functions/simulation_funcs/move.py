def move(humans, zombies):
    """
    For each character calls a 'decide' method and based on its results
    changes position (and only position) of the character.
    """

    for human in humans:
        human.change_position(humans, zombies)

    for zombie in zombies:
        zombie.change_position(humans)
