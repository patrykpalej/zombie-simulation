import random
import numpy as np


class Human:
    def __init__(self, human_params):
        self.x = human_params["x"]
        self.y = human_params["y"]

        self.color = human_params["color"]
        self.velocity = human_params["velocity"]
        self.r = human_params["r"]

        self.battle_points = 0
        self.a1 = 0
        self.a2 = 0
        self.true_velo = 0
        self.n_killed = 0

        self.smell = human_params["smell"]
        self.eye = human_params["eye"]
        self.strength = human_params["strength"]
        self.stamina = human_params["stamina"]
        self.strategy = human_params["strategy"]

    def choose_new_position(self, humans, zombies):
        """
        Chooses new (x, y) position of a single human basing on distribution
        of humans and zombies on the map. Returns the new position
        """
        # 1. Put information about the human into variables
        x = self.x
        y = self.y
        v = self.velocity
        stam = self.stamina
        # h_bp = fight(...)  # battle points (to be calculated)
        strategy = self.strategy

        # 2. Save information about zombies distribution and parameters
        x_z = []
        y_z = []
        z_bp = []  # battle points
        z_point_advantage = []
        zombie_position_x = []  # position vector x-coord
        zombie_position_y = []  # position vector y-coord
        dist = []  # distances to subsequent zombies

        for zombie in zombies:
            x_z.append(zombie.x)
            y_z.append(zombie.y)
            # z_bp.append(fight(...))  # battle points (to be calculated)
            # z_point_advantage.append(h_bp - z_bp[-1])
            zombie_position_x.append(x_z[-1] - x)
            zombie_position_y.append(y_z[-1] - y)
            dist.append(np.sqrt(zombie_position_x[-1]**2 +
                                zombie_position_y[-1]**2))

        # 3. Save information about other humans distribution and parameters
        h_point_advantage = []
        human_position_x = []
        human_position_y = []
        dist_h = []
        for human in humans:
            # if human is not self:  # <-- this may disturb order of humans

            # human_bp = fight(...)  # battle points, to be calculated later
            # h_point_advantage.append(human_bp-h_bp)

            human_position_x.append(human.x - self.x)
            human_position_y.append(human.y - self.y)
            dist_h.append(np.sqrt(human_position_x[-1]**2 +
                                  human_position_y[-1]**2))

        # 4. Calculate subsequent priorities

        # 5. Calculate velocity coordinates

        # 6. Implement displacement and changing direction in case the...
        # ... water is nearby

        # 7. Recalculate output coefficients such as new stamina
        new_stamina = self.stamina

        # --------------------------------------
        # --------------------------------------

        # np.random.RandomState(0)
        # new_x = self.x + np.random.normal(0, 10)
        # np.random.RandomState(0)
        # new_y = self.y + np.random.normal(0, 10)
        # random.seed(0)
        new_x = self.x + random.normalvariate(0, 10)
        new_y = self.y + random.normalvariate(0, 10)

        return [new_x, new_y, new_stamina]
