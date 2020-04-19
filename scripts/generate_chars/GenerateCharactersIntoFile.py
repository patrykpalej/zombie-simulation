"""
This script generates characters parameters based on config files with
distribution parameters of characters features
"""

import json
import random
import numpy as np


# 1. Read config data
with open("humans_config_data.json") as handle:
    humans_config = json.load(handle)

with open("zombies_config_data.json") as handle:
    zombies_config = json.load(handle)


# 2. Create dictionaries of humans and zombies
human_features = ["x", "y", "color", "velocity", "r", "smell", "eye",
                  "resist", "strength", "stamina", "strategy"]
humans_params = dict(zip(human_features, [[] for i in human_features]))

for h in range(humans_config["numberOf"]):
    i = random.randint(0, len(humans_config["x"]) - 1)
    for feature in human_features:
        if feature == "x" or feature == "y":
            value = np.random.normal(humans_config[feature][i][0],
                                     humans_config[feature][i][1], 1)[0]
            humans_params[feature].append(value)
        elif feature == "color" or feature == "strategy":
            humans_params[feature].append(humans_config[feature])
        else:
            value = np.random.normal(humans_config[feature][0],
                                     humans_config[feature][1], 1)[0]
            humans_params[feature].append(value)


zombie_features = ["x", "y", "color", "velocity", "r", "nose", "zombieness",
                   "poison"]
zombies_params = dict(zip(zombie_features, [[] for i in zombie_features]))

for z in range(zombies_config["numberOf"]):
    i = random.randint(0, len(zombies_config["x"]) - 1)
    for feature in zombie_features:
        if feature == "x" or feature == "y":
            value = np.random.normal(zombies_config[feature][i][0],
                                     zombies_config[feature][i][1], 1)[0]
            zombies_params[feature].append(value)
        elif feature == "color":
            zombies_params[feature].append(zombies_config[feature])
        else:
            value = np.random.normal(zombies_config[feature][0],
                                     zombies_config[feature][1], 1)[0]
            zombies_params[feature].append(value)


# 3. Dump dictionaries to json files
with open("../../data/characters/initial_humans_params.json", 'w') as handle:
    json.dump(humans_params, handle)

with open("../../data/characters/initial_zombies_params.json", 'w') as handle:
    json.dump(zombies_params, handle)
