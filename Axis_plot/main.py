import numpy as np
from Frame import Frame


frame = Frame(1200,800)

collection = frame.collection(2)
for graph in collection:
    z = np.random.randint(-10,10)
    x = np.linspace(-z,z,1000)
    y = x**2
    graph.VertexPlot(x,y,1,True,True)




frame.run()
