meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print("=== Vendedores que bateram a meta ===")

# Percorre a lista de vendas pegando o nome e o valor de cada vendedor
for vendedor, valor in vendas:
    # Verifica se as vendas do vendedor atingiram ou superaram a meta
    if valor >= meta:
        print(f"O(A) vendedor(a) {vendedor} bateu a meta! Valor vendido: R${valor:,.2f}")