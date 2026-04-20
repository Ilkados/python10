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


    


# Simple example of the logic, not your specific exercise
def security_guard(check_function, action_function):
    def wrapper(person):
        if check_function(person): # The "Gate"
            return action_function(person) # Let them in
        return "Access Denied" # The "Fizzle"
    return wrapper