# Pede a palavra ao usuário
palavra = input("Digite uma palavra para contar as vogais: ")

# Cria uma lista/string com as vogais que queremos buscar (em minúsculas)
vogais = "aeiou"

# Inicializa o contador de vogais
total_vogais = 0

# O loop 'for' vai passar por cada letra da palavra, uma por uma
for letra in palavra:
    # Convertemos a letra para minúscula com .lower() para garantir que pegue 'A' ou 'a'
    if letra.lower() in vogais:
        total_vogais += 1

print("-" * 30)
print(f"A palavra '{palavra}' contém {total_vogais} vogais.")