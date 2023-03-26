#
# Template for Python program
# Name: James Bond
# Date : 2023/03/27
#

import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
print(raw_data.info())

# 2. Process
total = raw_data["Price"].sum()
var   = raw_data["Price"].var()
std   = raw_data["Price"].std()

# 3. Output
print(f"VAR: {var}")
print(f"STD: {std}")
