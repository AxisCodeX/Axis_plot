import numpy as np

def interval(limit,dimension,grid_spacing):
    rng = limit[1] - limit[0]

    no_of_ticks = dimension/grid_spacing

    raw_interval = rng/no_of_ticks


    exponent = np.floor(np.log10(raw_interval))

    fraction  = raw_interval / (10** exponent)

    if fraction < 1.5:
                m = 1
    elif fraction <3:
                m = 2
    elif fraction < 7:
                m = 5
    else : 
                m = 10
    
    interval = m * (10**exponent)

    return interval
