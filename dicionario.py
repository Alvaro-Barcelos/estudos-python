pessoa = {
    "nome": "Testando Objeto",
    "idade": 2,
    "endereco": {
        "rua": "rua a",
        "numero": 2
    }
}
print(pessoa.get("endereco", {}))
pessoa["telefone"] = "32932-3445"
print(pessoa)
print(pessoa.keys())
pessoa.pop("telefone")
print(pessoa)
print(pessoa.values())

del pessoa["endereco"]["rua"]
print(pessoa)


pessoa2 = dict(nome="Testando formato", idade=3)

print(pessoa2)
copia = pessoa2.copy()
pessoa2.clear()
print(pessoa2)
print("Mostrando a copia do dicionario. ",copia)

