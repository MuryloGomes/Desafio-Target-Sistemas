def inverter(string):
    opc = 0
    string_invertida = []
    while opc < len(string):
        string_invertida.append(string[-(opc + 1)])
        opc +=1 
    return ''.join(string_invertida) 

string = input('Digite alguma palavra: ')

nova_string = inverter(string)
print(f'Nova string: {nova_string}.')