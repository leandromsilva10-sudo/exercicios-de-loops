numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Variável acumuladora para guardar a soma de todos os números
soma_total = 0

print("=== Mostrando os números individuais ===")

# Primeiro loop: percorre cada uma das sublistas
for lista in numeros:
    
    # Segundo loop: percorre cada número dentro da lista atual
    for numero in lista:
        print(f"Número encontrado: {numero}")
        
        # Soma o número atual ao total acumulado
        soma_total += numero

print("-" * 40)
print(f"A soma total de todos os números é: {soma_total}")
