import numpy as np

def convert_to_screen_coordinate(coordinate,limit,dimension):
    coordinate = np.array(coordinate)
    rng = limit[1] - limit[0]
    screen_coordinate = (coordinate - limit[0]) * (dimension / rng)
    return screen_coordinate



def convert_to_graph_coordinate(c,limit,dimension):
    graph_coordinate =  ((c/dimension) * (limit[1] - limit[0])) + limit[0]
    return graph_coordinate