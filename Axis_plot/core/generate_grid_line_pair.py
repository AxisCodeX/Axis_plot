import numpy as np

def generate_grid_line_pair_horizontal(y_coordinate,graph):

    x = np.full(y_coordinate.shape,graph.x)
    grid_start = np.column_stack((x , y_coordinate))
    w =graph.x +  np.full(y_coordinate.shape,graph.width)
    grid_end = np.column_stack((w,y_coordinate))
    line = np.column_stack((grid_start,grid_end))
    line = line.reshape((line.shape[0] * 2,2))
    return line





def generate_grid_line_pair_vertical(x_coordinate,graph):

    y = np.full(x_coordinate.shape,graph.y)

    grid_start = np.column_stack((x_coordinate,y))

    h =graph.y +  np.full(x_coordinate.shape,graph.height)
    grid_end = np.column_stack((x_coordinate,h))
    line = np.column_stack((grid_start,grid_end))
    line = line.reshape(line.shape[0] * 2 , 2)
    return line




