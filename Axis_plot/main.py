from Frame import Frame
frame = Frame(1200,800)


graph = frame.graph_page(grids=True)
graph.scatter_plot([0,5,-5,10],[5,5,-5,10])
frame.run() 