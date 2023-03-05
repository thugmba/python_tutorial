#
# Template for Python program
#
import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
#print(raw_data.info())

# 2. Process
total = raw_data["Price"].sum()

# 3. Output
print(f"Total: {total}")

print(len(raw_data.index))
raw_data.loc[len(raw_data.index)] = ["Total",total]

raw_data.to_csv("Menu_total.csv")