from collections import deque

#this is help function to help collect data depend on type of graf
def get_neighbors(graph_obj, node,rep_type):
    
    neigbours = []

    if rep_type == "matrix":
        data =  graph_obj.get_matrix()
        if 1 <= node <= graph_obj.nodes:
            row = data[node - 1]
            #Look for 1 in matrix row to find neighbors
            for i, val in enumerate(row):
                if val == 1:
                    neigbours.append(i + 1)

    elif rep_type == "list":
        data = graph_obj.get_list()
        if isinstance(data, dict):
            neigbours = data.get(node, [])
        else:
            if 1 <= node <= graph_obj.nodes:
                neigbours = data[node - 1]

    elif rep_type == "table":
        data = graph_obj.get_table()
        for u, v in data:
            if u == node:
                neigbours.append(v)
    
    return sorted(neigbours)

#Main function to perform BFS
def run_bfs(graph_obj, start_node, rep_type):

    visited = set()            
    queue = deque([start_node]) 
    visited.add(start_node)
    
    result = [] 

    while queue:
        
        current = queue.popleft()
        result.append(current)
        neighbors = get_neighbors(graph_obj, current, rep_type)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) 
                
    return result
