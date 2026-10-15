from Frame import Frame


frame = Frame(1200,1000)

graph_pages = frame.create_graph_pages(2)
print(graph_pages)
for graph in graph_pages:
    graph.plot_points([1,2,3,4],[1,2,3,4])
frame.run()




