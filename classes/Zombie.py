class Zombie:
    def __init__(self, zombies_params):
        self.x = zombies_params["x"]
        self.y = zombies_params["y"]

        self.color = zombies_params["color"]

        self.velocity = zombies_params["velocity"]
        self.r = zombies_params["r"]

        self.nose = zombies_params["smell"]
        self.zombieness = zombies_params["eye"]
        self.poison = zombies_params["poison"]
