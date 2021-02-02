from math import fabs
print('\033[32m-=\033[m'*20)
print(f'\033[34m{"ANALISADOR DE TRIÂNGULOS":^40}\033[m')
print('\033[32m-=\033[m'*20)
l1 = float(input('Primeiro Segmento: '))
l2 = float(input('Segundo Segmento: '))
l3 = float(input('Terceiro Segmento: '))
if fabs(l2-l3) < l1 < l2+l3 and fabs(l1-l3) < l2 < l1+l3 and fabs(l1-l2) < l3 < l1+l2 :
    print('Os segmentos acima podem formar um Triângulo',end=' ')
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('Escaleno')
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Equilátero')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não podem formar um Triângulo!!')
