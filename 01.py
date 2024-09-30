soma = 0
k = 0  # opc "variavel de controle"
indice = 13 

while k < indice:
    k += 1
    if k == indice:
        break  
    soma += k
    print(soma)

print(f'O valor da variável soma é {soma}.')