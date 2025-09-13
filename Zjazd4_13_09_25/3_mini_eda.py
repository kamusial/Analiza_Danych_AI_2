import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
n = 40

godziny_nauki = rng.normal(loc=3.5, scale=1, size=n).clip(0.5, 6.5)
# print(godziny_nauki)
# print(type(godziny_nauki))

wynik = 50 + 8 * godziny_nauki + rng.normal(loc=0, scale=6, size=n)
wynik = np.clip(wynik, 0, 100)
# print(wynik)

df = pd.DataFrame({"godziny": godziny_nauki, "wynik": wynik})

# --- Podsumowanie liczbowe ---
# print(df.describe())

summary = pd.DataFrame({
    "Średnia": df.mean(numeric_only=True),
    "Mediana": df.median(numeric_only=True),
    "SD": df.std(numeric_only=True, ddof=1),
    "Q1": df.quantile(0.25, numeric_only=True),
    "Q3": df.quantile(0.75, numeric_only=True)
})
print('Podsumowanie')
print(summary.round(2))

# Histogram czasu nauki
plt.figure(figsize=(6, 4))
plt.hist(df["godziny"], edgecolor='black')
plt.xlabel('godziny')
plt.ylabel('liczebność')
plt.tight_layout()
plt.show()

# histogram wyników
plt.figure(figsize=(6, 4))
plt.hist(df["wynik"], edgecolor='black')
plt.xlabel('wyniki [%]')
plt.ylabel('liczebność')
plt.tight_layout()
plt.show()

# Boxplot
plt.boxplot([df["godziny"], df["wynik"]], labels=['godziny', 'wynik'], showmeans=True)
plt.title('Boxplot: godziny vs wyniki')
plt.tight_layout()
plt.show()

x = df['godziny'].values
y = df['wynik'].values

a, b = np.polyfit(x, y, 1)
plt.figure(figsize=(6, 4))
plt.scatter(x, y, alpha=0.8)
plt.plot(np.sort(x), a* np.sort(x) + b)
plt.title(f'Rozrzut (trendL y={a:.2f}x+{b:.2f})')
plt.xlabel("godziny nauki")
plt.ylabel("wynik [%]")
plt.tight_layout()
plt.show()


