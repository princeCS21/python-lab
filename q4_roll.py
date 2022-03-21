#Program to find last three digit of university roll number.

print('Roll NUmber:-')
roll=int(input())

sum=0
for i in range(3):
    last_d=roll%10
    roll=roll//10
    sum=sum+last_d
print(sum)
