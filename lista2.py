frutas = ["maça", "goiaba", "banana", "melão"]
print(frutas)
frutas.extend(["limão", "maracuja"])
print(frutas)
print(frutas.index("goiaba"))
frutas.append(["avelã", "amora"])
print(frutas)

frutas.pop()
print(frutas)
frutas.pop()
print(frutas)

frutas.sort()
print(frutas)
for fruta in frutas:
    print(fruta)

for indice, fruta in enumerate(frutas):
    print(f"{indice} - {fruta}")

numeros = [1,54,6,9,7]
pares = [numero for numero in numeros if numero % 2 == 0]
quadrado = [numero ** 2 for numero in numeros]

duplicado = numeros.copy()

print(duplicado, "Mostrando o copy")

print(id(numeros), id(duplicado))



print(pares)
print(quadrado)
"""
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
"""