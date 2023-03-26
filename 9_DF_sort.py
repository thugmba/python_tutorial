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
sorted = raw_data["Price"].sort_values()

# 3. Output
print(sorted)