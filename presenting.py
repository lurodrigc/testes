print("Olá")

nome = input('Me diga seu nome: ')
print("Olá,", nome, ". É um prazer.")

idade = int(input("Quantos anos você tem? "))
print("Então você tem", idade, "anos...")

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade...")

nota = float(input("Bom, vamos lá. Gostaria de saber: em sua última avaliação valendo nota (de 0 a 100), quanto você tirou? "))

if nota >= 90:
    print("Excelente!")
elif nota >= 75:
    print("Ótimo!")
else:
    print("Parabéns pelo esforço, mas você consegue melhorar...")

