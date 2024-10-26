# 4. Cálculo de Percentual de Faturamento por Estado

faturamentoEstados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

totalFaturamento = sum(faturamentoEstados.values())
percentuais = {estado: (valor / totalFaturamento) * 100 for estado, valor in faturamentoEstados.items()}

for estado, percentual in percentuais.items():
    print(f"Percentual de {estado}: {percentual:.2f}%")