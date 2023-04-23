#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    print(f'Input x : {input_x} Input y : {input_y}')
    sum = 0
    length = len(input_x)
    mean1 = statistics.mean(input_x)
    mean2 = statistics.mean(input_y)
    print(f'Mean x : {mean1} , Mean y : {mean2}')
    for i in range(len(input_x)):
        sum += (input_x[i]-mean1)*(input_y[i]-mean2)
    cov = sum/length
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')