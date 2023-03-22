#
# Calculator
#

import math
import statistics
import numpy

sum = 0
average = 0
sd = 0
step1 = 0
step2 = 0
step3 =0
step4 = 0
method2 = 0

# 1. Input
x1 = input("Enter x1: ")
x2 = input("Enter x2: ")
x3 = input("Enter x3: ")
op = input("Enter operator: ")
dataset = []

# 2. Process
if op == "+":
    sum = int(x1) + int(x2)
elif op == "-":
    sum = int(x1) - int(x2)
elif op == "/":
    sum = int(x1) / int(x2)
elif op == "*":
    sum = int(x1) * int(x2)
elif op == "AVG":
    average = (int(x1) + int(x2))/3
elif op =="SD":
    average = (int(x1) + int(x2) + int(x3))/3
    step1 = int(x1) - average
    step2 = int(x2) - average
    step3 = int(x3) - average
    step4 = (step1**2) + (step2**2) + (step3**2)
    sd = math.sqrt(step4/3)


    dataset = [int(x1),int(x2),int(x3)]
    method2 = statistics.stdev(dataset)
    method3 = statistics.pstdev(dataset)
    method4 = numpy.std(dataset)

# 3. Output
if op == "+":
    print(f"Sum : {sum}")
elif op == "-":
    print(f"Sum:{sum}")
elif op == "*":
    print(f"Sum:{sum}")
elif op == "/":
    print(f"Sum:{sum}")
elif op == "AVG":
    print(f"Average:{average}")
elif op == "SD":
    print(f"SD:{sd}")
    print(f"Method 2 - Statistics.stdev : {method2}")
    print(f"Method 3 - Statistics.pstdev : {method3}")
    print(f"Method 4 - numpy.std : {method4}")
