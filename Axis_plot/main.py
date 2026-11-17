import numpy as np
from Frame import Frame


frame = Frame(1200,800)

graph = frame.graph_page()

graph.Histogram(np.arange(101))







