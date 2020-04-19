def move(humans, zombies, map_2d):
    """
    For each character calls a 'choose_new_position' method and - later -
    based on its results changes position (and only position) of the characters
    """

    # 1. All characters choose a new position
    new_human_positions = []
    new_human_stamina = []

    new_zombie_positions = []

    for human in humans:
        choose_new_position = human.choose_new_position(humans, zombies)

        new_human_positions.append(choose_new_position[:2])
        new_human_stamina.append(choose_new_position[2])

    for zombie in zombies:
        new_zombie_positions.append(zombie.choose_new_position(humans, map_2d))

    # 2. All characters move
    for human, new_position, new_stamina \
            in zip(humans, new_human_positions, new_human_stamina):
        human.x = new_position[0]
        human.y = new_position[1]
        human.stamina = new_stamina

    for zombie, new_position in zip(zombies, new_zombie_positions):
        zombie.x = new_position[0]
        zombie.y = new_position[1]
