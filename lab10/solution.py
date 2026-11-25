import numpy as np

def make_table(rows, columns):
    arr = np.arange(rows*columns)
    return arr.reshape(rows, columns).tolist()

m = make_table(5, 5)
print(m)

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    matrix = np.asarray(matrix).astype(np.float32)
    return matrix[row_start:row_stop, column_start:column_stop].tolist()

print(rectangle(m, 2, 4, 1, 3))

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    cp = np.asarray(matrix).copy()
    cp = cp.astype(np.float32)
    cp[row_start:row_stop, column_start:column_stop] = value
    return cp.tolist()

print(replace_rectangle(m, 2, 4, 1, 3, 10))

def matrix_vector_product(matrix, vector):
    matrix = np.asarray(matrix).astype(np.float32)
    vector = np.asarray(vector).astype(np.float32)
    return (matrix @ vector).tolist()

print(matrix_vector_product(m, [1, 2, 5, 7, 1]))

def matrix_multiply(left, right):
    left = np.asarray(left).astype(np.float32)
    right = np.asarray(right).astype(np.float32)
    return (left @ right).tolist()

def transpose_matrix(matrix):
    matrix = np.asarray(matrix).astype(np.float32)
    return matrix.T.tolist()

print(transpose_matrix(m))

def solve_system(matrix, vector):
    matrix = np.asarray(matrix).astype(np.float32)
    vector = np.asarray(vector).astype(np.float32)
    return np.linalg.solve(matrix, vector).tolist()

def tensor_channel_mean(tensor):
    tensor = np.asarray(tensor).astype(np.float32)
    return tensor.mean(axis=-1).tolist()

print(tensor_channel_mean(m))

def point_distance(first, second):
    first = np.asarray(first).astype(np.float32)
    second = np.asarray(second).astype(np.float32)
    return np.linalg.norm(first - second)
