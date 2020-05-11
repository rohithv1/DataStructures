# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:24:13 2020

@author: Rohith_Vemulapally
"""

# Base class for Graphs

import abc


class Graph(abc.ABC):
    
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass
    
    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self, v):
        pass
    
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass
                        
    