import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import warnings

# warnings.filterwarnings('ignore')   # nie pokazuj ostrzeżeń

# Konfiguracja wyglądu wykresów
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')
plt.rcParams['figure.figsize'] = (12, 8)

print("=== PROGRAM DO ANALIZY STATYCZNEJ ===")

print("1. Wczytywanie danych")
try:
    data = pd.read_csv('heart.csv')
except FileNotFoundError:
    print('Nie znaleziono pliku - generuję przykładowe dane')
    np.random.seed(42)
    n = 200 # liczba obserwacji
    # dane numeryczne: wiek, zarobki, wydatki, wzrost, waga - rozkład normalny
    data = pd.DataFrame({
        'wiek': np.random.normal(45, 15, n).astype(int),
        'zarobki': np.random.normal(5000, 1500, n),
        'wydatki': np.random.normal(3000, 800, n),
        'wzrost': np.random.normal(175, 10, n),
        'waga': np.random.normal(75, 15, n)
    })
    #dane kategoryczne
    data['plec'] = np.random.choice(['K', 'M'], n)
    data['wyksztalcenie'] = np.random.choice(['podstawowe', 'średnie', 'wyższe'], n, p=[0.2, 0.5, 0.3])
    data['region'] = np.random.choice(['Północ', 'Południe', 'Wschód', 'Zachód'], n)

    # Dodanie BMI na podstawie wzrostu i wagi
    data['bmi'] = data['waga'] / ((data['wzrost'] / 100) ** 2)

print(f'Rozmiar danych; {data.shape}')
print('\nPierwsze 5 wierszy danych:')
print(data.head().to_string())

print("\n2. Statystyka opisowa...")
print("\nPodstawowe miary statystyczne:")
print(data.describe())

print("\nMacierz korelacji:")
corr_matrix = data.select_dtypes(include=[np.number]).corr()
print(corr_matrix)

# Wizualizacja macierzy korelacji
plt.figure()
sns.heatmap(corr_matrix)
plt.title('Macierz korelacji')
plt.tight_layout()
plt.savefig('macierz_korelacji.png')
plt.close()