numeros = [1,2,3]
strings = []

strings.append("Olá")
strings.append("Mundo")


numeros[0] = 5

print(strings)

print(numeros[0])
print(numeros[1])
print(numeros[2])

#lista_de_notas = []
#for x in range(10):
#    pergunta = int(input("Insira a nota do aluno: "))
 #   lista_de_notas.append(pergunta)

#print(lista_de_notas)    


notas = []

for x in range(3):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)


print(min(notas))
"""
contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    contador += 1

print("Quantidade de notas: ", len(notas))
"""
"""

for i in notas:
    codigo_aluno = i[0]
    nota = i[1]
    print("Aluno ", codigo_aluno, " tirou a nota ", nota," nota!")
"""

player = {
    "nome": "Guilherme",
    "level": 1,
    "hp": 100,
    "exp": 300,
    "dano": 5
}

print(player)

npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome": "Monstro", "dano": 5, "hp":100, "exp": 10},
    {"nome": "Monstrão", "dano": 10, "hp":150, "exp": 15},
    {"nome": "Chefe", "dano": 25, "hp":200, "exp": 20}
]
print(npcs)