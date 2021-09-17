a = float(input())
func = str(input())
b = float(input())
if b == 0 and (func == '/' or func == 'div' or func == 'mod'):
    print('Деление на 0!')
elif func == '+':
    print(a + b)
elif func == '-':
    print(a - b)
elif func == '/':
    print(a / b)
elif func == '*':
    print(a * b)
elif func == 'mod':
    print(a % b)
elif func == 'pow':
    print(a ** b)
elif func == 'div':
    print(a // b)
