# 3. Cálculo de Faturamento
import json

faturamentoJson = '''{
    "faturamento": {
        "1": 1500.00,
        "2": 1800.00,
        "3": 0.00,
        "4": 2000.00,
        "5": 0.00,
        "6": 2200.00,
        "7": 3000.00,
        "8": 2500.00,
        "9": 0.00,
        "10": 3500.00,
        "11": 4000.00,
        "12": 5000.00
    }
}'''

dados = json.loads(faturamentoJson)
faturamentoDiario = list(dados["faturamento"].values())

menorFaturamento = min(faturamentoDiario)
maiorFaturamento = max(faturamentoDiario)

diasFaturamento = [valor for valor in faturamentoDiario if valor > 0]
media = sum(diasFaturamento) / len(diasFaturamento)

diasMedia = sum(1 for valor in diasFaturamento if valor > media)

print(f"Menor Faturamento: R${menorFaturamento:.2f}")
print(f"Maior Faturamento: R${maiorFaturamento:.2f}")
print(f"Número de dias acima da média mensal: {diasMedia}")