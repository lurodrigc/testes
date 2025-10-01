hip = float(input("Vamos ver se um triângulo é retângulo? Preciso que você me informe o maior lado, a hipotenusa: "))

v1 = float(input("Agora, me diga um dos dois lados: "))
v2 = float(input("Agora, me diga o outro lado: "))

soma = v1**2 + v2**2
trian = hip**2

if soma == trian:
    print("Seu triângulo é retângulo!")

else:
    print("Seu triângulo não é retangulo.")
