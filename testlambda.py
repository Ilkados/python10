def counter(start):
    def inc(step = 1):
        nonlocal start
        start += step
        print(start)
    return inc

my_inc = counter(5)
print(my_inc())
my_inc = counter(100)
print(my_inc())
         