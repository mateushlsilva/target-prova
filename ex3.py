diario = [100, 0, 230, 500, 0, 150, 80, 300, 0, 600]

faturamento = [fat for fat in diario if fat > 0]

media_anual = sum(faturamento) / len(faturamento)

diasAcima = sum(1 for f in faturamento if f > media_anual)

print(f"Menor faturamento: {min(faturamento)}")
print(f"Maior faturamento: {max(faturamento)}")
print(f"Número de dias com faturamento superior à média: {diasAcima}")