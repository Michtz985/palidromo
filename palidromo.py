def palindromo(numero):
    numeroincial = numero
    alrevez = 0

    while numero > 0:
        digito = numero % 10  
        alrevez = alrevez * 10 + digito  
        numero //= 10  

    return numeroincial == alrevez


numero = 161
numero2= 138

if palindromo(numero):
    print(f"{numero} en efecto es un palidromo.")
else:

    print(f"{numero2}no es un palidromo")
