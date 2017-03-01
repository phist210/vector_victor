import math


class ShapeError(Exception):
    pass


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]


def are_equal(x, y, tolerance=0.001):
    """ Helper function to compare floats, which are often not quite equal. """
    return abs(x - y) <= tolerance


def shape_vectors(vector):
    return (len(vector),)


def vector_add(v1, v2):
    if shape_vectors(v1) == shape_vectors(v2):
        return [sum(x) for x in zip(v1, v2)]
    else:
        raise ShapeError
    #  or simply return vector_sum(v1, v2)


def vector_sub(v1, v2):
    #  or >>> return vector_sum(v1, vector_multiply(v2, -1)) <<< which adds the
    #  negative to the left side
    if shape_vectors(v1) == shape_vectors(v2):
        return [v1_item - v2_item for v1_item, v2_item in zip(v1, v2)]
    else:
        raise ShapeError


def vector_sum(*args):
    new_vector = [len(arg) == len(args[0]) for arg in args]
    if all(new_vector):
        return [sum(x) for x in zip(*args)]
    raise ShapeError


def dot(*args):
    new_vector = [len(arg) == len(args[0]) for arg in args]
    if all(new_vector):
        return sum([(a * b) for (a, b) in zip(*args)])
    raise ShapeError


def vector_multiply(vector, multiplier):
    return [x * multiplier for x in vector]


def vector_mean(*args):
    new_vector = [len(arg) == len(args[0]) for arg in args]
    if all(new_vector):
        return ([sum(item)/len(item) for item in zip(*args)])
    raise ShapeError


def magnitude(vector):
    return math.sqrt(sum(x**2 for x in vector))


print(shape_vectors(m))
print(vector_add(v, w))
print(vector_sub(v, w))
print(vector_sum(v, y, u, w, z))
print(dot(w, y))
print(vector_multiply(v, 0.5))
print(vector_mean(v, w))
print(magnitude(m))
