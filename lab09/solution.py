import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    values = np.asarray(values).astype(np.float32)
    return {
        "third": values[2],
        "last": values[-1],
        "middle": values[2:6].tolist(),
        "every_second": values[::2].tolist(),
        "reversed": values[::-1].tolist(),
    }

def change_vector(values):
    values_copy = np.asarray(values)
    values_copy[2:5] = 99
    values_copy[::2] = -1
    return values_copy.tolist()

def cap_above(values, limit):
    values_copy = np.asarray(values.copy())
    mask = values_copy > limit
    values_copy[mask] = limit
    return values_copy.tolist()

def celsius_to_fahrenheit(values):
    values = np.asarray(values)
    values = values * 9 / 5 + 32
    return values.tolist()


hours = make_hours()
print(hours)
print(vector_report(hours))
print(change_vector(hours))
print(cap_above(hours, 10))
print(celsius_to_fahrenheit(hours))
