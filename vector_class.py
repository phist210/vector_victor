class ShapeError(Exception):
    pass


class Vector:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def test_shapes(*args):
        if not all([a.shape() == args[0].shape() for a in args]):
            raise ShapeError

    def shape(self):
        return (len(self.data), )

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        Vector.test_shapes(self, other)
        return Vector(sum(x) for x in zip(self.data, other.data))

    def __sub___(self, other):
        Vector.test_shapes(self, other)
        return Vector((v1 - v2) for v1, v2 in zip(self.data, other.data))

    def repr(self):
        return repr(self.data)

    def __radd__(self, other):
        if type(other) == int and other == 0:
            return Vector(self.data)
        Vector.test_shapes(self, other)
        return Vector(sum(x) for x in zip(self.data, other.data))

    def dot(self, other):
        Vector.test_shapes(self, other)
        return sum([a * b] for a, b in zip(self.data, other.data))

    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError
        return Vector([a * other for a in self.data])

    def magnitude(self):
        return sum([a**2 for a in self.data])**5
