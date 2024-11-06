# Math Interpreter

expression = input('Please insert an arithmetic expression: ')
x, y, z = expression.split(' ')

if y == '+':
    print(float(int(x)+int(z)))
elif y == '-':
    print(float(int(x)-int(z)))
elif y == '/':
    print(float(int(x)/int(z)))
elif y == '*':
    print(float(int(x)*int(z)))
