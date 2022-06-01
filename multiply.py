# to multiply all the numbers in given sequence togheter.

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
l = [2,4,5,6,7,8]
print(multiply(l))
