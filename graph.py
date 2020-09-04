#!/usr/bin/env python3
"""A simple directed graph class."""

class Node:
    def __init__(self, name):
        self.name = name
        self.indegree = 0
        self.outdegree = 0
        self.edges = []
    
    def __str__(self):
        outstr = "node: %s; edges: " % self.name
        for i, edge in enumerate(self.edges):
            if i < (len(self.edges) - 1):
                outstr += "%s, " % edge.name
            else:
                outstr += edge.name
        return outstr
        
    def add_neighbour(self, other):
        self.edges.append(other)
    
    def num_edges(self):
        return len(self.edges)
    
    def has_edges(self):
        return len(self.edges) > 0
    
    def get_edge(self):
        return self.edges[0]

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.nodes = 0
    
    def __str__(self):
        out_string = ""
        for i, node in enumerate(self.adj_list.values()):
            if i < (self.nodes - 1):
                out_string += "%s -> " % node.name
            else:
                out_string += node.name
            n_edges = node.num_edges()
            for j, connected in enumerate(node.edges):
                if j < (n_edges - 1):
                    out_string += "%s, " % connected.name
                else:
                    out_string += "%s\n" % connected.name
        return out_string
    
    def __iter__(self):
        return iter(self.adj_list.values())
    
    def add_edge(self, source_name, target_name):
        if source_name not in self.adj_list:
            # print("adding %s" % source_name)
            source_node = Node(source_name)
            self.adj_list[source_name] = source_node
            self.nodes += 1
        if target_name not in self.adj_list:
            # print("adding %s" % target_name)
            target_node = Node(target_name)
            self.adj_list[target_name] = target_node
            self.nodes += 1
        self.adj_list[source_name].add_neighbour(self.adj_list[target_name])
        self.adj_list[source_name].outdegree += 1
        self.adj_list[target_name].indegree += 1
