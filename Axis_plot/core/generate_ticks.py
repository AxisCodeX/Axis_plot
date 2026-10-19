import numpy as np



def generate_ticks(limit, interval):
    k_min = np.ceil(limit[0] / interval)
    k_max =  np.floor(limit[1] / interval )
    
    ticks = np.arange(k_min,k_max+ 1)  * interval
    
    return ticks