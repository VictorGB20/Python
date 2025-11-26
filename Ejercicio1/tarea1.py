import math

cateto1 = float(input('Introduce el primer cateto: '))
cateto2 = float(input('Introduce el segundo cateto: '))

hipotenusa = math.pow(cateto1,2)+math.pow(cateto2,2)
print(hipotenusa)