def romano_a_entero(input):
    
    input = input.upper();

    numeros = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1};
    suma = 0;

    for i in range(len(input)):
        try:
            valor = numeros[input[i]];
            if i+1 < len(input) and numeros[input[i+1]] > valor:
                suma -= valor
            else: 
                suma += valor
    return suma;

print(suma(input("Dime un número romano:   ")));
