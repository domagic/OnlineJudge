operator = {'+': '+', '-': '+', '*': '*', '/': '/'}
a = input()
character = input()
b = input()
if int(b) == 0 and character == '/':
    print('divided by zero')
else:
    print('{:.2f}'.format(eval(a + operator[character] + b)))
