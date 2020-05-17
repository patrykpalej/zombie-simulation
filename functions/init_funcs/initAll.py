from datetime import datetime

from functions.init_funcs.initMap import init_map
from functions.init_funcs.initCharacters import init_characters


def init_all(time_tracker):
    """
    Initializes characters (humans, zombies) and the 2D map
    """
    humans, zombies = init_characters()

    map_name = "map.png"
    map_2d = init_map(map_name)

    time_tracker["after_init"] = datetime.now()
    return humans, zombies, map_2d, time_tracker
