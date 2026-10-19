import numpy as np

def generate_grid_line_pair_x(x_coordinate,height):
    z = np.zeros(x_coordinate.shape)
    h = np.full(x_coordinate.shape,height)
    part1 = np.column_stack((x_coordinate,z))
    part2 = np.column_stack((x_coordinate,h))
    line = np.column_stack((part1,part2))
    line = line.reshape(line.shape[0]*2,2)
    return line

def generate_grid_line_pair_y(y_coordinate,width):
    z = np.zeros(y_coordinate.shape)
    w = np.full(y_coordinate.shape,width)

    part1 = np.column_stack((z,y_coordinate))
    part2 = np.column_stack((w,y_coordinate))

    line = np.column_stack((part1,part2))
    line = line.reshape(line.shape[0] * 2 , 2)
    return line