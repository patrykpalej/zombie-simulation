class Human:
    def __init__(self, humans_params):
        self.x = humans_params["x"]
        self.y = humans_params["y"]

        self.color = humans_params["color"]

        self.velocity = humans_params["velocity"]
        self.r = humans_params["r"]

        self.smell = humans_params["smell"]
        self.eye = humans_params["eye"]
        self.resist = humans_params["resist"]
        self.strength = humans_params["strength"]
        self.stamina = humans_params["stamina"]
