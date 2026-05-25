# 1. Identificar a quantidade de pessoas no quarto
while True:
    qtd_pessoas = int(input("Quantas pessoas ficarão no quarto (1 a 4)? "))
    if 1 <= qtd_pessoas <= 4:
        break
    print("Capacidade inválida! O hotel possui apenas quartos para 1, 2, 3 ou 4 pessoas.")

# Lista que vai armazenar os dados do quarto
quarto = []

# 2. Loop para perguntar o nome e o CPF de cada pessoa
for i in range(qtd_pessoas):
    print(f"\n--- Cadastro da {i + 1}ª pessoa ---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF (apenas números): ")
    
    # Cria a sublista da pessoa e adiciona à lista do quarto
    hospede = [nome, f"cpf:{cpf}"]
    quarto.append(hospede)

# 3. Exibir o resultado final da lista
print("\n=== Cadastro Concluído ===")
print("quarto =", quarto)