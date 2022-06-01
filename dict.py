#WAP to create a dictionary of radius of a circle and its circumferance.
D={}
n=int(input())
for i in range(n):
    radius=int(input())
    a=2*3.14*radius
    D[radius]=a
print(D)
