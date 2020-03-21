def move(humans, zombies):
    """
    For each character calls a 'choose_new_position' method and - later -
    based on its results changes position (and only position) of the characters
    """

    # 1. All characters choose a new position
    new_human_positions = []
    new_zombie_positions = []

    for human in humans:
        new_human_positions.append(human.choose_new_position(humans, zombies))

    for zombie in zombies:
        new_zombie_positions.append(zombie.choose_new_position(humans))

    # 2. All characters move
    for human, new_position in zip(humans, new_human_positions):
        human.x = new_position[0]
        human.y = new_position[1]

    for zombie, new_position in zip(zombies, new_zombie_positions):
        zombie.x = new_position[0]
        zombie.y = new_position[1]
