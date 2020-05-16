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
        self.a = 0
        self.a1 = 0
        self.a2 = 0
        self.true_velo = 0
        self.n_killed = 0

        self.smell = human_params["smell"]
        self.eye = human_params["eye"]
        self.strength = human_params["strength"]
        self.stamina = human_params["stamina"]
        self.strategy = human_params["strategy"]

    def choose_new_position(self, humans, zombies, map_2d):
        """
        Chooses new (x, y) position of a single human basing on distribution
        of humans and zombies on the map. Returns the new position
        """
        # 1. Put information about the human into variables
        x = self.x
        y = self.y
        v = self.velocity
        stam = self.stamina
        eye = self.eye
        h_bp = self.battle_points
        p1 = self.strategy[0]
        p2 = self.strategy[1]
        p3 = self.strategy[2]

        # 2. Save information about zombies distribution and parameters
        # x_z = []
        # y_z = []
        z_point_advantage = []
        zombie_relative_x = []
        zombie_relative_y = []
        z_dist = []

        for zombie in zombies:
            # x_z.append(zombie.x)
            # y_z.append(zombie.y)
            z_point_advantage.append(h_bp - zombie.battle_points)
            zombie_relative_x.append(zombie.x - x)
            zombie_relative_y.append(zombie.y - y)
            z_dist.append(np.sqrt(zombie_relative_x[-1]**2 +
                                  zombie_relative_y[-1]**2))

        # 3. Save information about other humans distribution and parameters
        h_point_advantage = []
        human_relative_x = []
        human_relative_y = []
        h_dist = []
        for human in humans:
            if human is not self:
                h_point_advantage.append(h_bp - human.battle_points)
                human_relative_x.append(human.x - self.x)
                human_relative_y.append(human.y - self.y)
                h_dist.append(np.sqrt(human_relative_x[-1]**2 +
                                      human_relative_y[-1]**2))

        # 4. Calculate subsequent priorities and accelearation coefficient
        w1 = [1, 2]
        w1 = p1*np.array(w1)

        w2 = [-1, -3]
        w2 = (1-p1)*np.array(w2)

        w = w1 + w2

        module = np.linalg.norm
        betha = module(w)/(module(w1) + module(w2))
        a1 = betha - p2*(betha - 0.5)**2 + p2/4
        a2 = 1/(stam**p3 + 1)
        a = 2*max(a1 - a2, 0)

        self.a1 = a1
        self.a2 = a2
        self.a = a
        self.true_velo = v*a

        # 5. Calculate velocity coordinates
        v_vec = v * a * w/module(w)

        # 6. Implement displacement and changing direction in case the...
        # ... water is nearby

        # 7. Recalculate output coefficients - new coordinates and new stamina
        new_stamina = stam - p3/10*(a-1)
        new_x = self.x + v_vec[0]
        new_y = self.y + v_vec[1]

        return [new_x, new_y, new_stamina]
