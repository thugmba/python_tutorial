#
# Calculator
#

sum = 0

# 1. Input
x1 = input("Enter x1: ")
x2 = input("Enter x2: ")

# 2. Process
for x in range(int(x1),int(x2)+1):
    sum += x

# 3. Output
print(f"Sum: {sum}")