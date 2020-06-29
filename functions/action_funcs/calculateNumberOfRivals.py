def calc_n_of_rivals(humans, zombies, clash_pairs):
    """
    Calculates number of rivals for all characters
    """

    rivals_number = {"humans": [0 for _ in humans],
                     "zombies": [0 for _ in zombies]}

    for pair in clash_pairs:
        rivals_number["humans"][pair[0]] += 1
        rivals_number["zombies"][pair[1]] += 1

    return rivals_number
