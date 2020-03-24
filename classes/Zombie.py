import numpy as np


class Zombie:
    def __init__(self, zombies_params):
        self.x = zombies_params["x"]
        self.y = zombies_params["y"]

        self.color = zombies_params["color"]

        self.velocity = zombies_params["velocity"]
        self.r = zombies_params["r"]

        self.nose = zombies_params["nose"]
        self.zombieness = zombies_params["zombieness"]
        self.poison = zombies_params["poison"]

    def choose_new_position(self, humans):
        """
        Chooses new (x, y) position of a single zombie basing on distribution
        of humans on the map. Returns the new position
        """
        # 1. Save information about humans distribution and smell
        x_h = []
        y_h = []
        smell = []
        for human in humans:
            x_h.append(human.x)
            y_h.append(human.y)
            smell.append(human.smell)

        xh_vec = np.array(x_h)
        yh_vec = np.array(y_h)
        s_vec = np.array(smell)

        # 2. Put information about the zombie into variables // !!! TO CONSIDER
        x = self.x
        y = self.y
        v = self.velocity
        n = self.nose

        # 3. Calculate velocity coordinates
        gamma_x = -(n+1) * sum(s_vec*(x-xh_vec) /
                               ((x-xh_vec)**2+(y-yh_vec)**2)**((n+3)/2))

        gamma_y = -(n + 1) * sum(s_vec * (y - yh_vec) /
                                 ((x-xh_vec)**2+(y-yh_vec)**2)**((n+3)/2))

        gamma_module = np.sqrt(gamma_x**2 + gamma_y**2)
        gamma_hat_x = gamma_x / gamma_module
        gamma_hat_y = gamma_y / gamma_module

        v_x = v*gamma_hat_x
        v_y = v*gamma_hat_y

        # 4. Implement displacement and changing direction in case the
        # water is nearby

        # code here

        # - - - - - - -
        # - - - - - - -
        new_x = self.x + v_x
        new_y = self.y + v_y

        return [new_x, new_y]
