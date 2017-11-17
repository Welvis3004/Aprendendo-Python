numero = float(input('Digite um numero: '))
print('A tabuada de {} é'.format(numero))
contador = 0
while contador < 10:
    print('{} x {} = {}'.format(contador, numero, contador*numero))
    contador = contador + 1