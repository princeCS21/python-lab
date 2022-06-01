# fibonaaci series

def fib(number_of_terms):
   count = 0

   first = 0
   second = 1
   temp = 0
 
   while count <= number_of_terms:
      print(first)
      temp = first + second
      first = second
      second = temp
      count = count + 1

n = int(input())
fib(n)
