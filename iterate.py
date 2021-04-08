class MyCounter(object):
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        'Returns itself as iterator object'
        return self

    def next(self):
        'Returns next value till current is lower than end'
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Using generator


c = MyCounter(1, 20)
print(c.next())

SimpleCounter = (x**2 for x in range(1, 10))

tot = 0
for val in SimpleCounter:
    print(val)
    tot += val

print(tot)

# Using yield


def my_gen(low, high):
    for x in range(1, 10):
        yield x**2


total = 0
for value in my_gen(1, 10):
    total += value

print(total)
