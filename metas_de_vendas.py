venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']

meta = 50

# Inicializa o índice em 0
i = 0

# O loop vai rodar enquanto o índice for menor que o tamanho da lista de vendedores
while i < len(vendedores):
    # Verifica se a venda do vendedor atual é maior ou igual à meta
    if venda[i] >= meta:
        print(vendedores[i])
    
    # Incrementa o índice para passar para o próximo vendedor
    i += 1