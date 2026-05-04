import os

def export_visuals(graph_obj, filename="graph_visualization.tex"):
    
    
    
    data = graph_obj.get_list()
    edges = []
    nodes = set()
    
    
    if isinstance(data, dict):
        for u, neighbors in data.items():
            nodes.add(u)
            for v in neighbors:
                edges.append((u, v))
                nodes.add(v)
    else:
        for i, neighbors in enumerate(data):
            u = i + 1
            nodes.add(u)
            for v in neighbors:
                edges.append((u, v))
                nodes.add(v)

    total_nodes = max(graph_obj.nodes, len(nodes)) if nodes else graph_obj.nodes

    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n\n")
            
            f.write("\\begin{center}\n")
            f.write("\\begin{tikzpicture}[>=stealth, node distance=2cm, every node/.style={circle, draw=blue!80!black, fill=blue!15, thick, minimum size=8mm, font=\\bfseries}]\n")
            
            
            if total_nodes > 0:
                angle_step = 360 / total_nodes
                for i in range(1, total_nodes + 1):
                    angle = (i - 1) * angle_step
                    f.write(f"  \\node ({i}) at ({angle}:3cm) {{{i}}};\n")
                    
                f.write("\n")
                
                
                for u, v in edges:
                    f.write(f"  \\draw[->] ({u}) -- ({v});\n")
                    
            f.write("\\end{tikzpicture}\n")
            f.write("\\end{center}\n\n")
            
            f.write("\\end{document}\n")
            
        print(f"Sukces! Graf został zapisany do pliku: {os.path.abspath(filename)}.Aby wygenerować wizualizację, skompiluj ten plik .tex za pomocą LaTeX (np. Overleaf).")
        
    except IOError:
        print("Błąd: Nie udało się zapisać pliku.")