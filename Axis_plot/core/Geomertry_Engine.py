import numpy as np

class Geometry_Engine:
    def __init__(self):
        pass


    def convert_to_screen_coordinate(self,coordinates,limit,dimension,d_range):
        d_min,d_max = d_range
        rng = limit[1] - limit[0]
        screen_coordinates =d_min + ((coordinates - limit[0])/rng) * (dimension)
        return screen_coordinates


    def nice_num(self,limit,dimension,grid_spacing):
        rng = limit[1] - limit[0]
        no_of_ticks = dimension//grid_spacing
        raw_interval = rng / no_of_ticks

        exponent = np.floor(np.log10(raw_interval))
        fraction = raw_interval / (10 ** exponent)
        if fraction < 1.5:
            m = 1
        elif fraction <3:
            m = 2
        elif fraction < 7:
            m = 5
        else : 
            m = 10
        interval = m * (10 ** exponent)

        ticks = np.arange(limit[0]*10**np.abs(exponent),(limit[1]*10**np.abs(exponent) +1) , interval*10**np.abs(exponent))/10**np.abs(exponent) 

        return ticks

    def orientation(self,no_of_graphs,width,height,grid_spacing,orientation,r_c = 0 , c_c = 0):
        coors = []
        if orientation == "ROW":
            width = width // no_of_graphs
            height = height

            for n in range(no_of_graphs):
                xmin = (n*width) + grid_spacing
                xmax = xmin + width - (1.5 * grid_spacing) 

                ymin = grid_spacing
                ymax = height - grid_spacing
                coors.append([xmin,xmax,ymin,ymax])
        if orientation == "COLUMN":
            width = width 
            height = height // no_of_graphs

            for n in range(no_of_graphs):
                xmin = grid_spacing
                xmax = width - grid_spacing

                ymin = (n * height) + grid_spacing
                ymax = ymin + height -(1.5 *  grid_spacing)
                coors.append([xmin,xmax,ymin,ymax])

            
        
        return coors



geometry_engine = Geometry_Engine()
