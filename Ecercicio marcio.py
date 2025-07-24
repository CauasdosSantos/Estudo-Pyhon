import numpy as np

# 1
print(np.__version__)

# 2
arr = np.arange(10)
print(arr)

# 3
bool_arr = np.full((3, 3), True, dtype=bool)
print(bool_arr)

# 4
odd_numbers = arr[arr % 2 == 1]
print(odd_numbers)

# 5
arr[arr % 2 == 1] = -1
print(arr)

# 6
new_arr = np.where(arr % 2 == 1, -1, arr.copy())
print(new_arr)

# 7
new_arr_2d = arr.reshape(2, -1)
print(new_arr_2d)

# 8
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
stacked_vertically = np.vstack((a, b))
print(stacked_vertically)

# 9
stacked_horizontally = np.hstack((a, b))
print(stacked_horizontally)

# 10
a = np.array([1, 2, 3])
repeated_a = np.repeat(a, 3)
output = np.tile(repeated_a, 3)
print(output)

# 11
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
peaks = np.where((a > np.roll(a, 1)) & (a > np.roll(a, -1)))[0]
print(peaks)

# 12
A = np.array([[1, 2, 1],
              [1, 1, 1]])
B = np.array([[1, 5],
              [7, 1],
              [1, 9]])
C = np.dot(A, B)
print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Matriz C (A*B):\n", C)

# 13
def calculate_stats(matrix):
    row_means = np.mean(matrix, axis=1)
    row_stddevs = np.std(matrix, axis=1)
    col_means = np.mean(matrix, axis=0)
    col_stddevs = np.std(matrix, axis=0)
    return row_means, row_stddevs, col_means, col_stddevs

row_means, row_stddevs, col_means, col_stddevs = calculate_stats(C)
print("Média das linhas de C:", row_means)
print("Desvio padrão das linhas de C:", row_stddevs)
print("Média das colunas de C:", col_means)
print("Desvio padrão das colunas de C:", col_stddevs)

# 14
D = A[:, -2:]
mean_D = np.mean(D)
print("Matriz D:\n", D)
print("Média dos valores em D:", mean_D)

