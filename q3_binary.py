#program to find binary and check whether last digit of binary is 0 or 1

number=int(input('Enter Number:-'))
x=number

i=1
bin=0

while number!=0:
 
    rem = number % 2
    number //= 2
    bin += rem * i
    i *= 10

print('binary of',x,'is',bin)

if number%2==0:
    print('last digit of binary is- 0')

else:
      print('last digit of binary is- 1')
