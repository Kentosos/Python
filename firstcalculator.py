print('This is a C.A.L.C.U.L.A.T.O.R.')
print('Computational Algorithm for Logical Calculations, Universal Linear Approximations, Tensor Operations & Results')
print('|-----------------|')

num1 = float(input('Enter first number: '))
op = input('Enter operator: ')
num2 = float(input('Enter second number: '))

print('|-----------------|')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('Invalid operator. You can use +, -, *, /.')