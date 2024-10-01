lista = [0, 1]
opc = 0
x = int(input('Digite um número inteiro: '))

while True:
    elemento_novo = lista[opc] + lista[opc + 1]
    opc += 1
    lista.append(elemento_novo)

    if elemento_novo >= x:
        break

print(f'Sequência de fibonacci: {lista}')

if lista[-1] == x:
    print(f'o numero {x} pertence a sequência.')

else:
    print(f'O numero {x} não pertence a sequência.')