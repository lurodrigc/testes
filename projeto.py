print("Olá! Vamos começar um quiz. Seja bem vindo!")
resposta = input("Deseja iniciar agora? Responda com 'S' para sim e 'N' para não: ")

if resposta != "S":
    print("Ok! Volte quando puder iniciar o quiz.")

pontos = 0


print("Ótimo! Vamos começar.")
print("Qual empresa desenvolveu o GTA? \n (A) Rockstar Games \n (B) Ubsoft \n (C) EA \n (D) Steam")
r1 = input("Resposta: ")

if r1 == "A":
    print("Correto!")
    pontos = pontos + 1
if r1 == "D":
    print("Errado! A Steam é só um app de compra de jogos, que o GTA está.")



print("Vamos continuar! Entre essas opções, qual deles era um dos 3 personagens principais do GTA V? \n (A) Arthur Morgan \n (B) Lamar Davis \n " \
"(C) Trevor Phillips \n (D) Chopp")
r2 = input("Resposta: ")

if r2 == "C":
    print("Correto!")
    pontos = pontos + 1
if r2 == "B":
    print("Errado... Lamar era amigo dos protagonistas, somente.")
if r2 == "D":
    print("Chopp era o animal de estimação de um dos protagonistas.")



print("Agora, a última pergunta. Qual era o nome da cidade do GTA V? \n (A) Vice CIty " \
"\n (B) Liberty City \n (C) San Andreas \n (D) Los Santos")
r3 = input("Resposta: ")

if r3 == "D":
    print("Certíssimo!")
    pontos = pontos + 1
else:
    print("Errado...")


print("Agora, vamos contabilizar seus pontos...")
print("Fazendo os cáluclos, sua pontuação foi:", pontos)
if pontos > 2:
    print("Excelente!")
else:
    print("Se quiser, pode tentar novamente!")
