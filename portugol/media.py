v1 = float(input("Vamos fazer a soma da sua média de teste e prova. DIgite a nota do seu teste: "))
v2 = float(input("\nOK! Agora, digite a nota da sua prova: "))

print("Ótimo! No teste, você tirou", v1,
      " e na prova", v2, ". Vamos calcular a média!")

somador = (v1 + v2) / 2
print("Sua média resultou em", somador, ".")

if somador > 6:
    print("Párabens! Você foi aprovado(a)")
else:
    print("Você está reprovado(a), sinto muito.")
