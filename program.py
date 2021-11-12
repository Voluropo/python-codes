'''python is a high level programming language'''
name = input('please enter your name:')
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))
choice = input('pick an operation you would like to perform(+,-,*,/):')
if choice == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif choice == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif choice == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif choice == '/':
    print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('invalid option')
print('end of program you did a good job')
