# hamming distance

def hamming_distance(x, y):
  return bin(x ^ y).count('1')
a = int(input())
b = int(input())
print("Hamming distance between",a,"and",b,"is",hamming_distance(a, b))
