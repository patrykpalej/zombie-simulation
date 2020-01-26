import json

from classes.Human import Human
from classes.Zombie import Zombie


def init_characters():
    """
    This function initializes list of objects (humans and zombies) and
    passes them to the init_all() function
    """

    # 1. Load parameters from json files
    with open("data/characters/initial_humans_params.json") as handle:
        humans_dict = json.load(handle)
    with open("data/characters/initial_zombies_params.json") as handle:
        zombies_dict = json.load(handle)

    # 2. Create characters objects using data from loaded json files
    humans = []
    for h in range(len(humans_dict["x"])):
        human_params = dict()

        human_params["x"] = humans_dict["x"][h]
        human_params["y"] = humans_dict["y"][h]
        human_params["color"] = humans_dict["color"][h]
        human_params["velocity"] = humans_dict["velocity"][h]
        human_params["r"] = humans_dict["r"][h]
        human_params["smell"] = humans_dict["smell"][h]
        human_params["eye"] = humans_dict["eye"][h]
        human_params["resist"] = humans_dict["resist"][h]
        human_params["strength"] = humans_dict["strength"][h]
        human_params["stamina"] = humans_dict["stamina"][h]

        humans.append(Human(human_params))

    zombies = []
    for z in range(len(zombies_dict["x"])):
        zombie_params = dict()

        zombie_params["x"] = zombies_dict["x"][z]
        zombie_params["y"] = zombies_dict["y"][z]
        zombie_params["color"] = zombies_dict["color"][z]
        zombie_params["velocity"] = zombies_dict["velocity"][z]
        zombie_params["r"] = zombies_dict["r"][z]
        zombie_params["nose"] = zombies_dict["nose"][z]
        zombie_params["zombieness"] = zombies_dict["zombieness"][z]
        zombie_params["poison"] = zombies_dict["poison"][z]

        zombies.append(Zombie(zombie_params))

    return humans, zombies
