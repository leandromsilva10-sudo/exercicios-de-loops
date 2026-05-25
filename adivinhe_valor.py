import random

# O computador escolhe um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa o contador de tentativas
tentativas = 0

print("🤖 Bem-vindo ao Jogo da Adivinhação!")
print("Pensei em um número entre 1 e 100. Tente adivinhar!")
print("-" * 40)

# Começa o jogo
while True:
    # Recebe o palpite do jogador e converte para número inteiro (int)
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1  # Conta mais uma tentativa
    
    # Verifica o palpite
    if palpite == numero_secreto:
        print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
        break  # Interrompe o loop e encerra o jogo
    elif palpite < numero_secreto:
        print("💡 Hum... O número secreto é MAIOR. Tente novamente!")
    else:
        print("💡 Hum... O número secreto é MENOR. Tente novamente!")