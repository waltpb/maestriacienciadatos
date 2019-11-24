# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:56:17 2019
@author: wpinedob
"""

import networkx as nx
import matplotlib.pyplot as plt

# Instancia del gráfico direccional
G = nx.DiGraph()

# Instancia edges pro disolucion
edgesPro = [('User1','Influencer1'),('User2','Influencer1'),('User1','Influencer2')]
# Instancia edges anti disolucion
edgesAnti = [('User1','Influencer3'),('User3','Influencer3'),('User1','Influencer4')]

# Se listan los grupos por categoría
grupoPro = ['Influencer1', 'Influencer2']
grupoAnti = ['Influencer3','Influencer4']

# Se añaden los al gráfico ambos grupos
G.add_edges_from(edges, label='Pro', weight=1, color=2)
G.add_edges_from(edges2, label='Anti', weight=1, color=2)

# Se define la posicion, en este caso se usara el layout circular
position = nx.circular_layout(G)

# Se grafican ambas partes. 
nx.draw(G, pos=position, nodelist = grupoAnti, edgelist = edgesAnti,
                 with_labels = True, alpha= 0.5, linewidths = 1,
                 node_color = 'r', width = 1, font_size = 8,
                 node_size = 500, node_shape = 's' )

nx.draw(G, pos=position, nodelist = grupoPro, edgelist = edgesPro,
                 with_labels = True, alpha= 0.5, linewidths = 2,
                 node_color = 'b', width = 1, font_size = 8,
                 node_size = 500, node_shape = 's')
plt.show()

# Se define una nueva posicion, en este caso se usara el layout spring
position = nx.spring_layout(G)

nx.draw(G, pos=position, nodelist = grupoAnti, edgelist = edgesAnti,
                 with_labels = True, alpha= 0.5, linewidths = 2,
                 node_color = 'r', width = 1, font_size = 8,
                 node_size = 500, node_shape = 's' )

nx.draw(G, pos=position, nodelist = grupoPro, edgelist = edgesPro,
                 with_labels = True, alpha= 0.5, linewidths = 2,
                 node_color = 'b', width = 1, font_size = 8,
                 node_size = 500, node_shape = 's')
plt.show()
