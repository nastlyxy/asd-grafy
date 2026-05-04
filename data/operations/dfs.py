def run_dfs(start_node,get_neighbors):

    visited = set()            
    result = []
    
    def dfs_recursive(node):

        visited.add(node)
        result.append(node)

        neighbours = get_neighbors(node)

        for neighbour in neighbours:
            if neighbour not in visited:
                dfs_recursive(neighbour)

    dfs_recursive(start_node)

    return result



