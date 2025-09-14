import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, ttest_ind, f_oneway
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
    n = 200  # liczba obserwacji
    # dane numeryczne: wiek, zarobki, wydatki, wzrost, waga - rozkład normalny
    data = pd.DataFrame({
        'wiek': np.random.normal(45, 15, n).astype(int),
        'zarobki': np.random.normal(5000, 1500, n),
        'wydatki': np.random.normal(3000, 800, n),
        'wzrost': np.random.normal(175, 10, n),
        'waga': np.random.normal(75, 15, n)
    })
    # dane kategoryczne
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
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Macierz korelacji')
plt.tight_layout()
plt.savefig('macierz_korelacji.png')
plt.close()

print('\n3. Testy statystyczne...')
if 'plec' in data.columns:
    zarobki_k = data[data['plec'] == 'K']['zarobki']
    zarobki_m = data[data['plec'] == 'M']['zarobki']
    t_stat, p_value = ttest_ind(zarobki_k, zarobki_m)
    print(f'Test t-Studenta dla zarobków między K, a M')
    print(f'Statystyka t: {t_stat:.4f}, p-value: {p_value:.4f}')
    # intepretacja wyniku
    alpha = 0.05
    if p_value < alpha:
        print('Istnieje statystycznie znacząca różnica w zarobkach, między K, a M')
    else:
        print('Nie ma statystycznie znaczącej różnicy w zarobkach między płciami')

    # ANOVA - porównanie zarobków między różnymi poziomami wyksztacenia
if 'wyksztalcenie' in data.columns:
    groups = []
    for poziom in data['wyksztalcenie'].unique():  # 'podstawowe', 'średnie', 'wyższe'
        groups.append(data[data['wyksztalcenie'] == poziom]['zarobki'])
        f_stat, p_value = f_oneway(*groups)
