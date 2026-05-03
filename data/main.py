import sys
from graph import Graph
from operations.printer import print_graph
from operations.find import find_edge
from operations.bfs import run_bfs , get_neighbors
from operations.dfs import run_dfs

def mode_generate(rep_type):
    try:
        nodes = int(input("nodes> "))
        if nodes <= 0:
            raise ValueError("Liczba wierzchołków musi być dodatnia.")
            
        saturation = float(input("saturation> "))
        if not (0.0 <= saturation <= 100.0):
            raise ValueError("Nasycenie musi być z przedziału [0, 100].")
            
        return Graph.generate_dag(nodes, saturation, rep_type)
        
    except ValueError as e:
        print(f"Błąd: {e}")
        sys.exit(1)
    except EOFError:
        sys.exit(1)

def mode_user_provided(rep_type):
    try:
        nodes = int(input("nodes> "))
        if nodes <= 0:
            raise ValueError("Liczba wierzchołków musi być dodatnia.")
            
        input_data = {i: [] for i in range(1, nodes + 1)}
        
        for i in range(1, nodes + 1):
            line = input(f"{i}> ").strip()
            if line:
                neighbors = [int(x) for x in line.replace(',', ' ').split() if x]
                input_data[i] = neighbors
                
        return Graph.from_user_input(nodes, input_data, rep_type)
        
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane.")
        sys.exit(1)
    except EOFError:
        return Graph.from_user_input(nodes, input_data, rep_type)

def main():
    if len(sys.argv) < 2:
        print("Użycie: python main.py [--generate | --user-provided]")
        sys.exit(1)

    mode = sys.argv[1]

    try:
        rep_type = input("type> ").strip().lower()
        if rep_type not in ['matrix', 'list', 'table']:
            print("Błąd: Nieznana reprezentacja. Dostępne: matrix, list, table.")
            sys.exit(1)
    except EOFError:
        sys.exit(1)

    if mode == "--generate":
        graph = mode_generate(rep_type)
    elif mode == "--user-provided":
        graph = mode_user_provided(rep_type)
    else:
        print("Błąd: Nieznany tryb.")
        sys.exit(1)

    while True:
        try:
            action = input("action> ").strip().lower()
            
            if action == "print":
                print_graph(graph, rep_type)
                
            elif action == "find":
                u = int(input("from> "))
                v = int(input("to> "))
                print(f"Szukanie krawędzi ({u}, {v})...")
                
                if find_edge(graph, u, v):
                    print(f"Edge ({u}, {v}) exists.")
                else:
                    print(f"Edge ({u}, {v}) does not exist.")

            elif action in ["bfs", "breadth-first-search", "breadth first search"]:

                wynik = run_bfs(graph, start_node=1, rep_type=rep_type)
                wynik_str = " ".join(str(node) for node in wynik)
                print(f"Inline: {wynik_str}")

            elif action in ["dfs", "depth-first-search", "depth first search"]:
               
                def neighbouor_accessor(node):
                    return get_neighbors(graph, node, rep_type)
                
                wynik = run_dfs(1,neighbouor_accessor)
                wynik_str = " ".join(str(node) for node in wynik)
            
                print(f"Inline: {wynik_str}")
                
            elif action in ["exit", "quit", ""]:
                break
                
            else:
                print("Nieznana akcja.")
                
        except EOFError:
            break
        except ValueError:
            print("Błąd: Nieprawidłowa wartość.")

if __name__ == "__main__":
    main()