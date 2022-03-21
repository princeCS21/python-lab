#Program to reverse number

print('Enter the number:-')
number=int(input())
rev=0
while number>0:
    rem=number%10
    rev=rev*10+rem
    number=number//10

print('Number after reversed is ',rev)
