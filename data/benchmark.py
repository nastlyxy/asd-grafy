import time
import csv
import random

from graph import Graph
from operations.find import find_edge
from operations.sorts import kahn_sort, tarjan_sort

def zapisz_do_csv(nazwa_pliku, dane):
    with open(nazwa_pliku, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['n', 'matrix', 'list', 'table'])
        writer.writeheader()
        writer.writerows(dane)

def uruchom_benchmark():
    
    rozmiary_n = [10, 50, 100, 200, 300, 500]
    nasycenie = 50.0 

    wyniki_krawedzie = []
    wyniki_kahn = []
    wyniki_tarjan = []

    print("Starting benchmark...")

    for n in rozmiary_n:
        print(f"Testowanie dla n={n}...")
    
        graph_obj = Graph.generate_dag(n, nasycenie, "matrix") 
        
        u = random.randint(1, n)
        v = random.randint(1, n)

        
        czasy_krawedzie = {'n': n}
        czasy_kahn = {'n': n}
        czasy_tarjan = {'n': n}

        for rep in ['matrix', 'list', 'table']:

            #krawedzie
            start = time.perf_counter()
            find_edge(graph_obj, u, v, rep)
            czasy_krawedzie[rep] = (time.perf_counter() - start) * 1000

            #sortowanie kahna
            start = time.perf_counter()
            kahn_sort(graph_obj, rep)
            czasy_kahn[rep] = (time.perf_counter() - start) * 1000  # ms

            #sortowanie tarjana
            start = time.perf_counter()
            tarjan_sort(graph_obj, rep)
            czasy_tarjan[rep] = (time.perf_counter() - start) * 1000  # ms

        wyniki_krawedzie.append(czasy_krawedzie)
        wyniki_kahn.append(czasy_kahn)
        wyniki_tarjan.append(czasy_tarjan)

    # Zapis danych
    zapisz_do_csv('wyniki_krawedzie.csv', wyniki_krawedzie)
    zapisz_do_csv('wyniki_kahn.csv', wyniki_kahn)
    zapisz_do_csv('wyniki_tarjan.csv', wyniki_tarjan)
    
    print("Wygenerowano pliki .csv (wyniki_krawedzie.csv, wyniki_kahn.csv, wyniki_tarjan.csv)!")

if __name__ == "__main__":
    uruchom_benchmark()