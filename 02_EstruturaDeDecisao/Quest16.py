'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa 
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
'''

print('Digite os valores de A, B, C: ')
a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if a != 0:
    if delta < 0:
        print('A equação não possui raízes reais!')
        print('Programada encerrado!')
    elif delta == 0:
        print('A equação possui apenas uma raíz real!')
        print('Programada encerrado!')
    else:
        print('A equação possui duas raizes reais!')
        print('Programada encerrado!')
else:
    print('A equação não é do segundo grau!')