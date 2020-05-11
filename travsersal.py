# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:33:35 2020

@author: Rohith_Vemulapally
"""

# For traversing through Graphs
# Breadth first and depth first traversals

from queue import Queue
import numpy as np

from adjacency_matrix_graph import AdjacencyMatrixGraph


def breadth_first(graph, start=0):    
    queue = Queue()
    queue.put(start)
    visited = np.zeros(graph.num_vertices)
    
    while not queue.empty():
        vertex = queue.get()
        
        if visited[vertex] == 1:
            continue
        
        print("Breadth first Visited:", vertex)
        visited[vertex] = 1
        for v in graph.get_adjacent_vertices(vertex):
            queue.put(v)
            
def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return
    
    visited[current] = 1
    print("Depth first Visited:", current)
    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)
    
            

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(9)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,7)
    g.add_edge(1,5)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,6)
    g.add_edge(5,6)
    g.add_edge(6,8)
    
    breadth_first(g)
    
    visited = np.zeros(g.num_vertices)
    depth_first(g, visited)