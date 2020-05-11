# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:30:14 2020

@author: Rohith_Vemulapally
"""

# Graph implementation using Adjacency Matrix

import numpy as np
from basegraph import Graph

class AdjacencyMatrixGraph(Graph):
    
    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        
        self.matrix = np.zeros((num_vertices, num_vertices))
        
    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))
        
        if weight < 1:
            raise ValueError("An Edge cannot have weight < 1")
        
        self.matrix[v1][v2] = weight
        
        if not self.directed:
            self.matrix[v2][v1] = weight
            
    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Cannot access vertex {}, it is out of bound".format(v))
            
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)
            
        return adjacent_vertices
    
    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Cannot access vertex {}, it is out of bound".format(v))
            
        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1
                
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]
    
    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print("{} --> {}".format(i, v))
                

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(4, directed=True)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(2,3)


    for i in range(4):
        print("Adjacent to:", i, g.get_adjacent_vertices(i))
    
    for i in range(4):
        print("Indegree :", i, g.get_indegree(i))
    
    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge weights: ", i, j, g.get_edge_weight(i, j))
    
    g.display()