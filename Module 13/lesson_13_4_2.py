class Fibonacci:

    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number
    
    def __iter__(self):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration()
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
        return self.cur_val


fib_iterator = Fibonacci(100)
for i_value in fib_iterator:
    print(i_value)
print(8 in fib_iterator)



# def fibonacci(number):
#     result = []
#     cur_val = 0
