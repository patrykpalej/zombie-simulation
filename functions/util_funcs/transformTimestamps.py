def transform_timestamps(time_tracker):
    """
    This function transforms timestamps of subsequent simulation stages into
    a dictionary of durations of them
    """
    def calculate_timediff(t1, t2):
        return (t2 - t1).seconds + (t2 - t1).microseconds/1000000

    durations = dict()

    durations["Initialization"] \
        = round(calculate_timediff(time_tracker["time_start"],
                                   time_tracker["after_init"]), 3)

    durations["Configuration"] \
        = round(calculate_timediff(time_tracker["after_init"],
                                   time_tracker["after_config"]), 3)

    iter_list = []
    for i, iteration in enumerate(time_tracker["iterations"]):
        if i == 0:
            iter_list\
                .append(round(calculate_timediff(time_tracker["after_config"],
                                                 iteration), 3))
        else:
            iter_list\
                .append(round(calculate_timediff(
                    time_tracker["iterations"][i-1], iteration), 3))
    durations["Iterations"] = iter_list

    durations["Finalization"] \
        = round(calculate_timediff(time_tracker["iterations"][-1],
                                   time_tracker["finish"]), 3)
    durations["Total"] \
        = round(durations["Initialization"] + durations["Configuration"]
                + sum(durations["Iterations"]) + durations["Finalization"], 3)

    return durations
