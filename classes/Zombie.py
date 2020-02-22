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

    def change_position(self, humans):
        """
        Changes (x, y) position of a zombie basing on distribution of humans
        on the map
        """
        # 1. Save information about humans distribution and smell
        x_h = []
        y_h = []
        smell = []
        for human in humans:
            x_h.append(human.x)
            y_h.append(human.y)
            smell.append(human.smell)

        # 2. Put information about the zombie into variables // !!! TO CONSIDER
        x = self.x
        y = self.y
        v = self.velocity
        n = self.nose

        # 3. Calculate velocity coordinates
        # ... some calculations ...
        # v_x = v*gamma_hat_x
        # v_y = v*gamma_hat_y

        # 4. Implement displacement and changing direction in case the
        # water is nearby

        # code here

        # - - - - - - -
        # - - - - - - -
        self.x += 1
        self.y += 1
