import networkx
import matplotlib.pyplot as plt

Graf = networkx.Graph()
Graf.add_nodes_from(['A','B','C','D','E','F']) #Tworzenie wierzchołków

krawedzie = [('A','B'), ('B','C'), ('C','D'), ('D','F'), ('E','F'),('C','E')] #tworzenie krawedzi

Graf.add_edges_from(krawedzie)

rozmieszczenie = networkx.spring_layout(Graf)

networkx.draw(Graf,rozmieszczenie, with_labels=True)

opis = {('A','B') :'krawędz nr.1',
('B','D'): 'krawędz nr.2',
('C','D'):'krawędz nr.3',
('D','F') :'krawędz nr.4',
('E','F'):'krawędz nr.5',
('C','E'):'krawędz nr.6 '
}

#podpunkt c
networkx.draw_networkx_edge_labels(Graf,rozmieszczenie,edge_labels=opis)

plt.title('graf nieskierowany')
plt.show()