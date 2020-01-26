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
