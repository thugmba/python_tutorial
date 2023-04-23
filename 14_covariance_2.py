#
# Template for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    print(f'Input x: {input_x}, Input y: {input_y}')
    length = len(input_x)
    sum = 0
    mean_x = statistics.mean(input_x)
    mean_y = statistics.mean(input_y)

    print(f'Mean x : {mean_x}, Mean y : {mean_y}')
    for x, y in zip(input_x, input_y):
        # print(x,y)
        sum += (int(x) - mean_x)*(int(y) - mean_y)
    cov = sum / length
    # print(f'Sum : {sum} N : {length} Cov:{cov}')
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')
