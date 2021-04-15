a = [10, 20, 30, 40, 50, 60, 70]


def do_list(a_lst, func):
    total = 0
    for element in a_lst:
                total += func(element)
                print(element, ' ', total)

    return total


print(do_list(a, lambda x: x**3))

iter = filter(lambda y: y > 30, a)
for x in iter:
    print(x)
