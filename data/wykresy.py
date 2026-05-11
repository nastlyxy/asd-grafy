import csv
import matplotlib.pyplot as plt
import os

def wczytaj_dane(nazwa_pliku):
    """Wczytuje dane z pliku CSV wygenerowanego przez benchmark."""
    n_vals, matrix_vals, list_vals, table_vals = [], [], [], []
    try:
        with open(nazwa_pliku, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                n_vals.append(int(row['n']))
                matrix_vals.append(float(row['matrix']))
                list_vals.append(float(row['list']))
                table_vals.append(float(row['table']))
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {nazwa_pliku}. Upewnij się, że uruchomiłeś benchmark.py.")
        return None
    return n_vals, matrix_vals, list_vals, table_vals

def stworz_pojedynczy_wykres(dane, tytul, nazwa_pliku, folder="images"):
    """Generuje i zapisuje pojedynczy wykres t=f(n) dla trzech reprezentacji."""
    if dane is None:
        return

    n, matrix, adj_list, table = dane
    
    plt.figure(figsize=(8, 5))
    
    # Kolory i style linii dla przejrzystości
    plt.plot(n, matrix, label='Macierz (Matrix)', color='#d62728', marker='o', linestyle='-')
    plt.plot(n, adj_list, label='Lista (List)', color='#1f77b4', marker='s', linestyle='--')
    plt.plot(n, table, label='Tabela (Table)', color='#2ca02c', marker='^', linestyle=':')
    
    plt.title(tytul)
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas obliczeń (ms)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Tworzenie folderu, jeśli nie istnieje
    os.makedirs(folder, exist_ok=True)
    
    sciezka = os.path.join(folder, nazwa_pliku)
    plt.savefig(sciezka, dpi=300)
    plt.close() # Zamknięcie figury, by nie zużywać pamięci
    print(f"Zapisano: {sciezka}")

def generuj_wszystkie_wykresy():
    # Definicje zadań do wykonania zgodnie z wymaganiami 
    zadania = [
        ('wyniki_krawedzie.csv', 'Wyszukiwanie krawędzi: t=f(n)', 'wykres_krawedzie.png'),
        ('wyniki_kahn.csv', 'Algorytm Kahna: t=f(n)', 'wykres_kahn.png'),
        ('wyniki_tarjan.csv', 'Algorytm Tarjana: t=f(n)', 'wykres_tarjan.png')
    ]

    print("Generowanie osobnych wykresów...")
    for csv_file, tytul, output_name in zadania:
        dane = wczytaj_dane(csv_file)
        stworz_pojedynczy_wykres(dane, tytul, output_name)

if __name__ == "__main__":
    generuj_wszystkie_wykresy()