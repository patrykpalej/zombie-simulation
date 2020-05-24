import numpy as np


class Zombie:
    def __init__(self, zombies_params):
        self.x = zombies_params["x"]
        self.y = zombies_params["y"]

        self.color = 0.85
        self.velocity = zombies_params["velocity"]
        self.r = zombies_params["r"]

        self.battle_points = 0
        self.n_infected = 0

        self.nose = zombies_params["nose"]
        self.poison = zombies_params["poison"]

    def choose_new_position(self, humans, map_2d):
        """
        Chooses new (x, y) position of a single zombie basing on distribution
        of humans on the map. Returns the new position
        """
        # 1. Put information about the zombie into variables
        x = self.x
        y = self.y
        v = self.velocity
        n = self.nose

        # 2. Save information about humans distribution and smell
        x_h = np.array([])
        y_h = np.array([])
        smell = np.array([])
        for human in humans:
            x_h = np.append(x_h, human.x)
            y_h = np.append(y_h, human.y)
            smell = np.append(smell, human.smell)

        # 3. Calculate velocity coordinates
        gamma_x = -n*sum(smell*(x-x_h)
                         / ((x-x_h)**2+(y-y_h)**2)**((n+2)/2))
        gamma_y = -n*sum(smell * (y-y_h)
                         / ((x-x_h)**2 + (y-y_h)**2)**((n+2)/2))

        module = np.linalg.norm
        gamma_module = module(np.array([gamma_x, gamma_y]))
        gamma_hat_x = gamma_x / gamma_module
        gamma_hat_y = gamma_y / gamma_module

        v_x = v*gamma_hat_x
        v_y = v*gamma_hat_y

        # 4. Implement displacement and changing direction in case the
        # water is nearby
        new_x = x
        new_y = y
        if map_2d[int(round(y + v_y)), int(round(x + v_x))] == 1:
            new_x = x + v_x
            new_y = y + v_y
        else:
            # calc. new velo. vec. assuming clock-wise and c. clock-wise flip
            unit_flip = np.pi/8
            for i in range(1, int(np.pi/unit_flip+1)):

                # velocities (clock wise and counter clock wise)
                vx_new_cw = np.cos(unit_flip * i) * v_x \
                    + np.sin(unit_flip * i) * v_y
                vy_new_cw = -np.sin(unit_flip * i) * v_x \
                    + np.cos(unit_flip * i) * v_y

                vx_new_ccw = np.cos(unit_flip * i) * v_x \
                    - np.sin(unit_flip * i) * v_y
                vy_new_ccw = np.sin(unit_flip * i) * v_x \
                    + np.cos(unit_flip * i) * v_y

                # positions
                x_new_cw = x + vx_new_cw
                y_new_cw = y + vy_new_cw
                x_new_ccw = x + vx_new_ccw
                y_new_ccw = y + vy_new_ccw

                # check which direction is better (lower pseudograv. potential)
                def multimodule(arr1, arr2):
                    result = []
                    for a1, a2 in zip(arr1, arr2):
                        result.append(module([a1, a2]))
                    return np.array(result)

                cw_potential \
                    = sum(smell/(multimodule(x_new_cw-x_h,
                                             y_new_cw-y_h))**n)
                ccw_potential \
                    = sum(smell/(multimodule(x_new_ccw-x_h,
                                             y_new_ccw-y_h))**n)
                if cw_potential > ccw_potential:
                    if map_2d[int(round(y_new_cw)),
                              int(round(x_new_cw))] == 1:
                        new_x = x_new_cw
                        new_y = y_new_cw
                        break
                else:
                    if map_2d[int(round(y_new_ccw)),
                              int(round(x_new_ccw))] == 1:
                        new_x = x_new_ccw
                        new_y = y_new_ccw
                        break

        return [new_x, new_y]
