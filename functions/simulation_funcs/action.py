from functions.action_funcs.getAllPairsToClash import get_all_pairs_to_clash
from functions.action_funcs.calculateNumberOfRivals import calc_n_of_rivals
from functions.action_funcs.carryOutClashes import carry_out_clashes
from functions.action_funcs.implementResults import implement_results


def action(humans, zombies, t, total_n_killed, total_n_inf):
    """
    For each character performs an action such as a battle with an opponent.
    Returns the state of characters after all fights.
    """

    # 1. Get all pairs which are about to clash
    clash_pairs = get_all_pairs_to_clash(humans, zombies)

    # 2. Calculate how many rivals has each character
    rivals_number = calc_n_of_rivals(humans, zombies, clash_pairs)

    # 3. Carry out all clashes considering number of rivals and remember the
    victories, loosers, total_n_killed, total_n_inf \
        = carry_out_clashes(humans, zombies, clash_pairs, rivals_number,
                            total_n_killed, total_n_inf, t)

    # 4. Implement results of the fight - death, infection etc.
    implement_results(humans, zombies, victories, loosers)

    return total_n_killed, total_n_inf
