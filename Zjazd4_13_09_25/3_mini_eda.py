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


