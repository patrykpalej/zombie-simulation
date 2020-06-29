import random
import numpy as np


class Human:
    def __init__(self, human_params):
        self.x = human_params["x"]
        self.y = human_params["y"]

        self.color = 0.3
        self.velocity = human_params["velocity"]
        self.r = human_params["r"]

        self.battle_points = 0
        self.a = 0
        self.a1 = 0
        self.a2 = 0
        self.w_proportion = 0
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
        z_point_advantage = np.array([])
        z_relative_x = np.array([])
        z_relative_y = np.array([])
        z_dist = np.array([])

        for zombie in zombies:
            z_point_advantage \
                = np.append(z_point_advantage, h_bp - zombie.battle_points)
            z_relative_x = np.append(z_relative_x, zombie.x - x)
            z_relative_y = np.append(z_relative_y, zombie.y - y)
            z_dist = np.append(z_dist, np.sqrt(z_relative_x[-1]**2 +
                                               z_relative_y[-1]**2))

        # 3. Save information about other humans distribution and parameters
        h_point_advantage = np.array([])
        h_relative_x = np.array([])
        h_relative_y = np.array([])
        h_dist = np.array([])
        for human in humans:
            if human is not self:
                h_point_advantage = np.append(h_point_advantage,
                                              h_bp - human.battle_points)
                h_relative_x = np.append(h_relative_x, human.x - self.x)
                h_relative_y = np.append(h_relative_y, human.y - self.y)
                h_dist = np.append(h_dist, np.sqrt(h_relative_x[-1]**2 +
                                                   h_relative_y[-1]**2))

        # 4. Calculate subsequent priorities and accelearation coefficient
        w1_x = sum(z_point_advantage*z_relative_x
                   / (z_relative_x**2 + z_relative_y**2)**(eye+1))
        w1_y = sum(z_point_advantage*z_relative_y
                   / (z_relative_x**2 + z_relative_y**2)**(eye+1))
        w1 = p1*np.array([w1_x, w1_y])

        w2_x = -sum(h_point_advantage*h_relative_x
                    / (h_relative_x**2 + h_relative_y**2)**(eye+1))
        w2_y = -sum(h_point_advantage * h_relative_y
                    / (h_relative_x**2 + h_relative_y**2)**(eye+1))
        w2 = (1-p1)*np.array([w2_x, w2_y])

        w = w1 + w2

        module = np.linalg.norm
        betha = module(w)/(module(w1) + module(w2))
        a1 = betha - p2*(betha - 0.5)**2 + p2/4
        a2 = 1/(stam**p3 + 1)
        a = 2*max(a1 - a2, 0)

        self.a1 = a1
        self.a2 = a2
        self.a = a
        self.w_proportion = betha
        self.true_velo = v*a

        # 5. Calculate velocity coordinates
        v_vec = self.true_velo * w/module(w)

        # 6. Recalculate output coefficients - new coordinates and new stamina
        new_stamina = stam - p3/100*(a-1)

        # 7. Implement displacement and changing direction in case the...
        # ... water is nearby
        if map_2d[int(round(y + v_vec[1])), int(round(x + v_vec[0]))] == 1:
            new_x = x + v_vec[0]
            new_y = y + v_vec[1]
        else:
            new_x = x
            new_y = y
            # calc. new velo. vec. assuming clock-wise and c. clock-wise flip
            unit_flip = np.pi / 8
            for i in range(1, int(np.pi / unit_flip + 1)):

                # velocities (clock wise and counter clock wise)
                vx_new_cw = np.cos(unit_flip * i) * v_vec[0] \
                            + np.sin(unit_flip * i) * v_vec[1]
                vy_new_cw = -np.sin(unit_flip * i) * v_vec[0] \
                            + np.cos(unit_flip * i) * v_vec[1]

                vx_new_ccw = np.cos(unit_flip * i) * v_vec[0] \
                             - np.sin(unit_flip * i) * v_vec[1]
                vy_new_ccw = np.sin(unit_flip * i) * v_vec[0] \
                             + np.cos(unit_flip * i) * v_vec[1]

                # positions
                x_new_cw = x + vx_new_cw
                y_new_cw = y + vy_new_cw
                x_new_ccw = x + vx_new_ccw
                y_new_ccw = y + vy_new_ccw

                # check which direction is better (lower pseudograv. potential)
                def multimodule(arr1, arr2):
                    result = []
                    for ar1, ar2 in zip(arr1, arr2):
                        result.append(module([ar1, ar2]))
                    return np.array(result)

                cw_dist_diff = module(np.array([x+v_vec[0] - x_new_cw,
                                                y+v_vec[1] - y_new_cw]))
                ccw_dist_diff = module(np.array([x + v_vec[0] - x_new_ccw,
                                                y + v_vec[1] - y_new_ccw]))

                if cw_dist_diff > ccw_dist_diff:
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

        # print(w1, w2)

        return [new_x, new_y, new_stamina]
