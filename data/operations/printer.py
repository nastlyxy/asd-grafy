#There wiil be logic to print our graf in three ways(list , table and matrix).

#The matrx represantation
def print_matrix(graf_data,nodes):
    header_nums = " ".join(str(i) for i in range(1, nodes + 1))
    header = f"  | {header_nums}"
    print(header)
    
    separator = "--+" + "-" * (len(header) - 3) 
    print(separator)

    for i in range(nodes):
        row_number = i + 1
        row_values = " ".join(str(val) for val in graf_data[i])
        print(f"{row_number} | {row_values}")

#The list represantation
def print_list(graf_data,nodes):
    print("  Lista sąsiedztwa:")
    print("  " + "-" * 20)

    for i in range(1, nodes + 1):
        try:
            if isinstance(graf_data,dict):
                neighbors = graf_data.get(i, [])
            else:
                neighbors = graf_data[i - 1]


            if neighbors:
                neighbour_str = ", ".join(str(neighbor) for neighbor in neighbors)
                print(f"  {i} -> {neighbour_str}")
            else:
                 print(f"  {i} -> Brak sąsiadów")
        except (IndexError,KeyError):
            print(f" {i} -> Bład danych dla wierzchołka {i}")


#The table represantation
def print_table(graf_data):
    print("  Tabela krawędzi:")
    print("   u | v ")
    print("  ---+---")

    if not graf_data:
        print("  Brak krawędzi w grafie.")
        return
    try:
        for u,v in graf_data:
            print(f"  {u:>2} | {v:>2}")
    except (ValueError,TypeError):
        print("  Błąd danych krawędzi.")

#Main fun to print graf in required option 
def print_graph(graph_obj,rep_type):
    if rep_type == "matrix":
        graph_data = graph_obj.get_matrix()
        print_matrix(graph_data,graph_obj.nodes)
    elif rep_type == "list":
        graph_data = graph_obj.get_list()
        print_list(graph_data,nodes=graph_obj.nodes)
    elif rep_type == "table":
        graph_data = graph_obj.get_table()
        print_table(graph_data)
    else:
        print("Nieznany typ reprezentacji grafu.")
    print()

