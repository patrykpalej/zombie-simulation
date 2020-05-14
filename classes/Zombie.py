import numpy as np


class Zombie:
    def __init__(self, zombies_params):
        self.x = zombies_params["x"]
        self.y = zombies_params["y"]

        self.color = zombies_params["color"]
        self.velocity = zombies_params["velocity"]
        self.r = zombies_params["r"]

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
                cw_potential = 1
                ccw_potential = 2
                if cw_potential < ccw_potential:
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
