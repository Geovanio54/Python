import math
a = int(input('Digite o valor de A: '))  
b = int(input('Digite o valor de B: '))  
c = int(input('Digite o valor de C: ')) 
delt = b**2 - 4*a*c 
x1 = (-b + math.sqrt(delt)) / 2*a
x2 = (-b - math.sqrt(delt)) / 2*a
print('x1 = {:.1f} \nx2 = {:.1f}'.format(x1, x2))