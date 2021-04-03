from collections import namedtuple

vector = namedtuple("Dimensions", 'x y z')
vector_1 = vector(4, 3, 2)
vector_2 = vector(1, 0, 1)

manhattan_distance = abs(vector_1.x - vector_2.x) +\
    abs(vector_1.y - vector_2.y) +\
    abs(vector_1.z - vector_2.z)

print(manhattan_distance)
