#Program to find BMI

mass=float(input('Enter your weight in Kg: '))

height=float(input('Enter your height in meter: '))

BMI=mass/height**2

print(f'Body Mass Index is ={BMI:.2f}')
