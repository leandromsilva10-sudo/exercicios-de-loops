# Pede o número para o usuário e converte para inteiro
numero = int(input("Digite o número que você deseja estudar a tabuada: "))

print(f"\n✨ Tabuada do {numero} ✨")
print("-" * 20)

# O range(1, 11) vai gerar os números de 1 até 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado}")

print("-" * 20)