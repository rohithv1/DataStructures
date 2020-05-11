# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:27:35 2020

@author: Rohith_Vemulapally
"""

from basegraph import Graph

class Node:
    
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()
        
    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError("The vertex {} cannot be adjacent to itself".format(v))
        self.adjacency_set.add(v)
        
    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)
    

class AdjacencySetGraph(Graph):
    
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        
        self.vertex_list = []
        
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))
        
    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))
        
        if weight != 1:
            raise ValueError("An Edge cannot have weight < 1")
            
        self.vertex_list[v1].add_edge(v2)
        
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)
            
    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Cannot access vertex {}, it is out of bound".format(v))
        
        return self.vertex_list[v].get_adjacent_vertices()
    
    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Cannot access vertex {}, it is out of bound".format(v))
        
        indegree = 0
        for i in range(self.num_vertices):
            if v in self.vertex_list[i].get_adjacent_vertices():
                indegree += 1
        
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return 1
    
    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print("{} --> {}".format(i, v))
                
                

if __name__ == '__main__':
    g = AdjacencySetGraph(4, directed=True)
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
            
    