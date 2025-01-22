## Retira a duplicação de valores porém não mantém a ordem.
nums = {1,2,4,3,2}

print(nums)

numero = set([1,2,3,5,4,3,2,3,1])

print(numero)

numero = list(numero)

print(numero[1])

comidas = {"Goiaba", "maracuja", "noses", "ameixa"}

print(comidas)

comida_a = {"Goiaba", "noses", }
comida_b = {"maracuja", "noses", "ameixa"}

print(comida_b.union(comida_a, comida_b))