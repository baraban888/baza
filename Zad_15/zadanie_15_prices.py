import pandas as pd
import matplotlib.pyplot as plt

# Данні з завдання
prices = [
    (1, 2.12), (2, 2.56), (3, 3.10), (4, 3.16),
    (5, 3.38), (6, 5.12), (7, 6.55), (8, 4.12),
    (9, 4.12), (10, 3.65), (11, 4.65), (12, 4.25)
]

# Створюємо DataFrame
df = pd.DataFrame(prices, columns=["month", "price_pln"])
df = df.set_index("month")

# Нова колонка: ціна у доларах (4 злотих = 1 USD)
df["price_usd"] = df["price_pln"] / 4

# Малюємо графік
plt.plot(df.index, df["price_usd"], "r--")  # r-- = червона пунктирна лінія
plt.title("Price of goods (USD)")
plt.xlabel("Month")
plt.ylabel("USD")
plt.grid(True)

# Показуємо графік
plt.show()
