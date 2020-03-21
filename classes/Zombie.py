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
        new_x = self.x + 1
        new_y = self.y + 1

        return [new_x, new_y]
