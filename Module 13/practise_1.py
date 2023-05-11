class SquaresIterator:
    def __init__(self, n):
        self.current = 1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            square = self.current ** 2
            self.current += 1
            return square


squares = SquaresIterator(5)
for square in squares:
    print(square)


print('-------------------------------------------------------------------')


def squares_generator(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


squares = squares_generator(5)
for square in squares:
    print(square)
print('-------------------------------------------------------------------')

n = 5
squares = (i ** 2 for i in range(1, n + 1))

for square in squares:
    print(square)