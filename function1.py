def square_input(x):
    return x*x


# Call function
square_me = square_input
print(square_me(45))


# Nested functions
def sum_squares(x):
    def square_in(x):
        return x*x
    return sum([square_in(x1) for x1 in x])


sq = sum_squares
print(sq([3, 4]))
