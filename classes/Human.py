import numpy as np


class Human:
    def __init__(self, human_params):
        self.x = human_params["x"]
        self.y = human_params["y"]

        self.color = human_params["color"]

        self.velocity = human_params["velocity"]
        self.r = human_params["r"]

        self.smell = human_params["smell"]
        self.eye = human_params["eye"]
        self.resist = human_params["resist"]
        self.strength = human_params["strength"]
        self.stamina = human_params["stamina"]

    def choose_new_position(self, humans, zombies):
        """
        Chooses new (x, y) position of a single human basing on distribution
        of humans and zombies on the map. Returns the new position
        """

        new_x = self.x + np.random.normal(0, 10)
        new_y = self.y + np.random.normal(0, 10)

        return [new_x, new_y]
