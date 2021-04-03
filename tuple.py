a_tuple = (1, 2, 'a')
b_tuple = 1, 2, 'c'

print(b_tuple[-1])
c_tuple = (5, 10, [100, 200, 300])
c_tuple[2][0] = 500
print(c_tuple)
# concatenate tuples
print(a_tuple + b_tuple)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[1:8:3])
print(a[:-1])
if 1 in a:
    print('Found 1')
else:
    print('No 1')
