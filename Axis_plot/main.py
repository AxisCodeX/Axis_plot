from Frame import Frame


frame = Frame(800,800)

graph_page = frame.create_graph_page()
graph_page.plot_points([1,2,3,4],[1,2,3,4])
frame.run()





