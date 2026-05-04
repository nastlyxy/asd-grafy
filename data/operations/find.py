from operations.bfs import get_neighbors

def find_edge(graph_obj, u, v, rep_type):
    try:
        neighbors = get_neighbors(graph_obj, u, rep_type)
        
        if v in neighbors:
            return True
    except Exception:
        pass
        
    return False