from operations.bfs import get_neighbors

def kahn_sort(graph_obj, rep_type):
    
    in_degree = {i: 0 for i in range(1, graph_obj.nodes + 1)}
    
    for u in range(1, graph_obj.nodes + 1):
        neighbors = get_neighbors(graph_obj, u, rep_type)
        for v in neighbors:
            in_degree[v] += 1
            

    S = [node for node, degree in in_degree.items() if degree == 0]
    L = []
    
    while S:
        n = S.pop(0)  
        L.append(n) 
   
        neighbors = get_neighbors(graph_obj, n, rep_type)
        for m in neighbors:
            in_degree[m] -= 1
            if in_degree[m] == 0:
                S.append(m)
 
    if len(L) != graph_obj.nodes:
        raise ValueError("Graf zawiera co najmniej jeden cykl (Algorytm Kahna).")
        
    return L

def tarjan_sort(graph_obj, rep_type):
    
    marks = {i: 0 for i in range(1, graph_obj.nodes + 1)}
    L = []
    
    def visit(n):
        if marks[n] == 2:  # permanent
            return
        if marks[n] == 1:  # temporary
            raise ValueError("Graf zawiera co najmniej jeden cykl (Algorytm Tarjana).")
            
        marks[n] = 1 
        
        neighbors = get_neighbors(graph_obj, n, rep_type)
        for m in neighbors:
            visit(m)
            
        marks[n] = 2 
        L.insert(0, n) 
        
    for n in range(1, graph_obj.nodes + 1):
        if marks[n] == 0:
            visit(n)
            
    return L