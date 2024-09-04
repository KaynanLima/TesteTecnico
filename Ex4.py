FATURAMENTO = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

TOTAL = sum(FATURAMENTO.values())

print("\nO percentual para cada Estado é o seguinte:")
for estado, valor in FATURAMENTO.items():
    PERCENTUAL = (valor / TOTAL) * 100
    print(f"{estado}: {PERCENTUAL:.1f}%")