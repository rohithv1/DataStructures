# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:55:38 2020

@author: Rohith_Vemulapally
"""

from queue import Queue

from adjacency_matrix_graph import AdjacencyMatrixGraph


def topological_sort(graph):
    
    queue = Queue()
    indegree_map = {}
    
    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree(i)
        
        if indegree_map[i] == 0:
            queue.put(i)
    
    sorted_list = []
    #print(indegree_map)
    
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)
        
        #print(vertex)
        
        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] = indegree_map[v] - 1
            
            if indegree_map[v] == 0:
                queue.put(v)
                
    if len(sorted_list) != graph.num_vertices:
        raise ValueError("Graph has a cycle")
        
    print(sorted_list)
    

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(9, directed=True)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,7)
    g.add_edge(1,5)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    g.add_edge(3,6)
    g.add_edge(5,6)
    g.add_edge(6,8)
    
    topological_sort(g)
    
    