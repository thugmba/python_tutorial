#
# Calculator
#

sum = 0

# 1. Input
x1 = input("Enter x1: ")
x2 = input("Enter x2: ")
x3 = input("Enter x3: ")
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
#   Input: x1=5, x2=10, x3=11
#   Output: SD=xx.xxx
#
1. calculate mean
2. tmp1 = x1 - mean
3. tmp2 = x2 - mean
3. tmp3 = x3 - mean
4. (tmp1 + tmp2 + tmp3)**2
5. #4/n
5. sqrt(#5)

# 3. Output
print(f"Sum: {sum}")