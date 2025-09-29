idade = int(input("Olá! preciso que diga sua idade, para classificarmos qual filme você poderá ver. Digite quantos anos você tem: "))

if idade < 10:
    print("A sua classificação indicativa para filmes é: Livre. Bom filme!")

if idade >= 10 and idade < 14:
    print("A sua classificação indicativa para filmes é: 10 anos. Bom filme!")

if idade >= 14 and idade < 16:
    print("A sua classificação indicativa para filmes é: 14 anos. Bom filme!")

if idade >= 16 and idade < 18:
    print("A sua classificação indicativa para filmes é: 16 anos. Bom filme!")

if (idade >= 18):
    print("A sua classificação indicativa para filmes é: 18 anos. Bom filme!")
