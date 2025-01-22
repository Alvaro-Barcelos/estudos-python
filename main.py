
salario = float(input("Informe o seu salario: "))
confirma = (salario >= 1)

if(confirma):
    if(salario <= 1000):
        print("Estagio")
    elif(salario >= 1001 and salario < 2000):
        print("Junior")
    else:
        print("Senior/Pleno")
else:
    print("cliente não trabalha")



for x in ["python", 2, True, {"name": "guilherme"}]:
    print(x)
