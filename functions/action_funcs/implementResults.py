from classes.Zombie import Zombie


def implement_results(humans, zombies, victories, loosers):
    """
    For each character performs an action such as a battle with an opponent.
    Returns the state of characters after all fights.
    """

    # Increase n_killed and n_infected
    for human, human_result in zip(humans, victories["humans"]):
        human.n_killed += human_result

    for zombie, zombie_result in zip(zombies, victories["zombies"]):
        zombie.n_infected += zombie_result

    # Remove killed zombies and turn infected humans into zombies
    killed_zombies = loosers["zombies"].copy()
    killed_zombies = list(set(killed_zombies))
    killed_zombies.sort()
    killed_zombies.reverse()

    for zombie_index in killed_zombies:
        del zombies[zombie_index]

    # ---
    infected_humans = loosers["humans"]
    infected_humans = list(set(infected_humans))
    infected_humans.sort()
    infected_humans.reverse()

    for human_index in infected_humans:
        h = humans[human_index]
        zombie_params = {"x": h.x, "y": h.y, "color": 0.85,
                         "velocity": h.velocity, "r": h.r,
                         "nose": h.eye, "poison": h.strength}

        del humans[human_index]
        zombies.append(Zombie(zombie_params))
