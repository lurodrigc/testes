valor = int(input("Digite um valor inteiro, e vamos confirmar se ele é primo: "))

contador = 0

for x in range(1, valor + 1):
    resto = valor % x
    if resto == 0:
        contador = contador + 1

if contador == 2:
    print(valor, " é primo!")
else:
    print(valor, " não é primo.")
