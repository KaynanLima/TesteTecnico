import json

with open('Ex3Faturamento.json', 'r') as file:
    DADOS = json.load(file)

FATURAMENTOS = [data['valor'] for data in DADOS['faturamento'] if data['valor'] > 0]

MENOR = min(FATURAMENTOS)
MAIOR = max(FATURAMENTOS)

MEDIA = sum(FATURAMENTOS) / len(FATURAMENTOS)
DIAS = sum(1 for valor in FATURAMENTOS if valor > MEDIA)

print(f"\nO maior faturamento do mês foi: R$ {MAIOR:.2f}")
print(f"O menor faturamento do mês foi: R$ {MENOR:.2f}")
print(f"O número de dias acima da média foi: {DIAS}")