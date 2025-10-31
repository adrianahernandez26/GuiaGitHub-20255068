palabra=(input())
letra= (input())[-1]
palabra_termina = palabra.lower().endswith(letra.lower())
print (palabra_termina)