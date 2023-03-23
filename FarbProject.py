#Anwendungsplan:
#-----------------------------------------------------------------------------------
# 1. 2D Skulptur erschaffen 
# 2. 2D Skulptur in Graph umwandeln und als Adjazenzliste abspeichern
#    --> Vertices = Skulpturflächen, Edges = Behrührungskanten zu anderen Flächen
#    --> evtl. Graph bereinigen
#-----------------------------------------------------------------------------------
# Y3. Graph per Dateienpfad einlesen 
# 4. Farbalgorithm(en) schreiben und Graphvertices in Farbgruppen unterteilen.
# 5. Finale Farbcodes auswählen und den Farbgruppen zuweisen
#-----------------------------------------------------------------------------------
# 6. Graph als Datei abspeichern, sodass er als 2D zeichnung dargestellt werden kann.

import networkx as nx
import matplotlib.pyplot as plt

#Graph besteht aus nodes(mit Eigenschaft), edges(mit Eigenschaft)
G = nx.petersen_graph() 
#zum einlesen später
#nx.read_adjlist(path[, comments, delimiter, ...])
#G.add_node(4, day = 'Donnerstag')
print(G.nodes.data())
for node in G.nodes():
    



'''#nur zum Graph zeichnen#2. Skulptur einlesen
#for every Fläche eine Node
#G.add_node(1,{"colour": "P0"}) #mit Farbeigenschaft
    #for every angrenzende Fläche eine Edge
    #G.add_edge(1,2) #ohne Eigenschaft
subax = plt.subplot(111)
nx.draw_shell(G, nlist=[range(5,10), range(5)], with_labels=True, font_weight='bold')
plt.show()
'''

'''
graph = {
    "v1" : {"v2","v3"},
    "v2" : {"v1"},
    "v3" :  {"v1"}

}

def getVertcs(graph: dict) -> set:
    return set(graph.keys())

def getEdges(graph: dict) -> set:
    edges = set()
    for vertice in graph:
        for neighbour in graph[vertice]:
            edges.add({vertice, neighbour})
    return edges
'''



