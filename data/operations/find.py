def find_edge(graph_obj, u, v):

    graf_data = graph_obj.get_list()

    try:
        if isinstance(graf_data, dict):
            neighbors = graf_data.get(u, [])
        else:
            if 1 <= u <= graph_obj.nodes:
                neighbors = graf_data[u - 1]
            else:
                neighbours = []


        if v in neighbors:
            return True
        
    except (IndexError, KeyError):
        pass
    return False