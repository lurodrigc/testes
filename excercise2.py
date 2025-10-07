# fourth excercise from practicepython.com

num = int(input("Vamos ver quais são os divisores de um número que você deseja? Escreva o número: "))

divisors = []

for elem in range(1, num + 1):
    if num % elem == 0:
        divisors.append(elem)

print("Os divisores são: ", divisors)
