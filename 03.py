from faturamentos import dados_faturamento

valores_faturado = []

for i in dados_faturamento:
    faturamento = i['valor']
    if faturamento > 0:
        valores_faturado.append(faturamento)

menor_valor = min(valores_faturado) 
maior_valor = max(valores_faturado) 
media_valores = sum(valores_faturado) / len(valores_faturado) 

dias_acima_da_media = 0
for i in valores_faturado:
    if i > media_valores:
        dias_acima_da_media += 1

print(f'O menor valor faturado foi R${menor_valor:.2f}.')
print(f'O maior valor faturado foi R${maior_valor:.2f}.')
print(f'O número de dias que o faturamento diário foi maior que a média mensal foi {dias_acima_da_media}.')