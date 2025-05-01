def es_palindromo(cadena):
    cadena = cadena.lower()
    return cadena == cadena[::-1]
texto = input("Ingrese una palabra o frase: ")
print("¿Es palíndromo?", es_palindromo(texto)) 