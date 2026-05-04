import random

class Graph:
    def __init__(self, nodes, rep_type):
        self.nodes = nodes
        self.rep_type = rep_type
        self.adj_list = {i: [] for i in range(1, nodes + 1)}

    @classmethod
    def generate_dag(cls, nodes, saturation, rep_type):
        
        graph = cls(nodes, rep_type)
        max_edges = (nodes * (nodes - 1)) // 2
        target_edges = int(max_edges * (saturation / 100.0))
        
        current_edges = 0
        
        for i in range(1, nodes):
            graph.adj_list[i].append(i + 1)
            current_edges += 1
            
        while current_edges < target_edges:
            i = random.randint(1, nodes - 1)
            j = random.randint(i + 1, nodes)
            
            if j not in graph.adj_list[i]:
                graph.adj_list[i].append(j)
                current_edges += 1
                
        for i in graph.adj_list:
            graph.adj_list[i].sort()
            
        return graph

    @classmethod
    def from_user_input(cls, nodes, input_data, rep_type):
        graph = cls(nodes, rep_type)
        for u, neighbors in input_data.items():
            graph.adj_list[u] = neighbors
        return graph

    def get_matrix(self):
        matrix = [[0] * self.nodes for _ in range(self.nodes)]
        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                matrix[u - 1][v - 1] = 1 
        return matrix

    def get_list(self):
        return self.adj_list

    def get_table(self):
        edges = []
        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                edges.append((u, v))
        return edges