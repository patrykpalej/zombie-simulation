import numpy as np
from PIL import Image


def init_map(map_name):
    """
    Takes name of the file with map and returns an array where:
    0 - sea
    1 - land
    ...
    """

    img = Image.open("data/img/{}".format(map_name)).convert("RGB")
    arr3d = np.array(img, dtype='float32')
    arr2d = arr3d[:, :, 0]

    arr2d[arr2d == 255] = 1

    return arr2d
