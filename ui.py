import numpy
arry = []
a = int(input('array size-'))
for i in range(a):
  arry.append(int(input('element:')))
arry = numpy.array(arry)
print(arry)
