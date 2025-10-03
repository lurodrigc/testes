materias = ["Matemática", "Biologia", "Geografia"]

materias.append("Inglês")
print(materias)

materias.insert(2, "Espanhol")
print(materias)

materias.remove("Biologia")
print(materias)

materia_remov = materias.pop(0)
print(materias)
print(materia_remov)

materias.sort()
print(materias)

materias.reverse()
print(materias)

print("O número de vezes que matemática apareceu foram:", materias.count("Matemática"))

print("O primeiro índice de Espanhol foi:", materias.index("Espanhol"))

print("O comprimento disso é:", len(materias))

pessoa = {"Nome": "João","Idade": "25", "Cidade": "Madrid"}
print(pessoa["Idade"])
print(pessoa["Nome"])
print(pessoa["Cidade"])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.update({"Profissão": "Engenheiro"})
print(pessoa)