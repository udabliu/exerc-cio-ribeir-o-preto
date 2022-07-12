from operator import contains


x = int(input('digite um número para saber se pertence a sequencia de fibonacci'))
num1 = 0
num2 = 1
contador = 3

while contador <=  x:
    num3 = num2 + num1
    num1 = num2
    num2 = num3 
    contador = contador + 1

    print(num1,num2)