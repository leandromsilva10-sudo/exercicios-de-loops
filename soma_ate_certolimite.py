soma = 0
numero = 1

while soma <= 20:
    soma += numero
    print(f"Somando {numero}... Soma atual: {soma}")
    numero += 1

print("-" * 30)
print(f"A soma final que ultrapassou 20 foi: {soma}")