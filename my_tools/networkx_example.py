# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:53:59 2023

@author: User
"""

import networkx as nx
import matplotlib.pyplot as plt

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1,
    "width": 1,
}

G = nx.DiGraph([(0, 3), (1, 3), (2, 4), (3, 5), (3, 6), (4, 6), (5, 6)])

# group nodes by column
left_nodes = [0, 1, 2]
middle_nodes = [3, 4]
right_nodes = [5, 6]

# set the position according to column (x-coord)
pos = {n: (0, i) for i, n in enumerate(left_nodes)}
print(pos)
pos.update({n: (1, i + 0.5) for i, n in enumerate(middle_nodes)})
print(pos)
pos.update({n: (2, i + 0.5) for i, n in enumerate(right_nodes)})
print(pos)

#G.add_node("Singapore")
print('G->',G)
#nx.draw_networkx(G, pos, **options)
nx.draw(G, pos, with_labels = True, **options)

# =============================================================================
# # Set margins for the axes so that nodes aren't clipped
# ax = plt.gca()
# # ax = plt.axes(projection='3d')
# ax.margins(0.20)
# ax.set_title("Привет")
# 
# plt.grid(False)
# 
# plt.axis("off")
# plt.show()
# =============================================================================
