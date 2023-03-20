#
# Calculator
#

sum = 0

# 1. Input
x1 = input("Enter x1: ")
x2 = input("Enter x2: ")
op = input("Enter operator: ")

# 2. Process
if op == "+":
    sum = int(x1) + int(x2)
elif op == "-":
    sum = int(x1) - int(x2)
elif op == "*":
    sum = int(x1) * int(x2)
elif op == "/":
    sum = int(x1) / int(x2)
elif op == "avg":
    sum = (int(x1) + int(x2))/2
elif op == "sd":
#
#   Homework 3
#     
1. calculate mean
2. tmp1 = mean - x1
3. tmp2 = mean - x2
4. (tmp1+ tmp2)**2
5. #4/n
5. sqrt(#5)

# 3. Output
print(f"Sum: {sum}")