def make_adder(n):
    def add(x):
        return x + n 
    return add

add5 = make_adder(5)
print(add5(3))

class Counter:
    def __int__(self):
        self.count  = 0 
    
    def __call__(self):
        self.count+=1

class A:
    def call(self):
        print("i was called")

class WithoutCall:
    def show(self):
        print("show method")
a = WithoutCall()

a.show()


    
