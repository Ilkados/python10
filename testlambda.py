#build in function ->Reduced

from functools import reduce


def sumAll(num1,num2):
   return  num1 + num2

numbers = [1,2,3,4]

result = reduce(sumAll,numbers)
print(result)