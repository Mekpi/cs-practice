import numpy as np
def reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    arr = np.asarray(values)
    return arr.reshape(-1, width).tolist()

def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype = float)
    res = arr[np.ix_(rows, columns)]
    return res.tolist()

def column_means(matrix):
    if matrix == []:
        return []
    arr = np.asarray(matrix)
    res = arr.mean(axis=0)
    return res.tolist()

def column_range(matrix, column):
    if matrix == []:
        return []
    arr = np.asarray(matrix)
    col = arr[:, column]
    res = np.max(col) - np.min(col)
    return res

print(reshape_rows([], 3))
print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0], [1]))
print(column_means([[1.5, 2.5]]))
#print(column_range([], 1) )
