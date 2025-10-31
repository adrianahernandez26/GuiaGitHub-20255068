DUI= input()
largo_es_diez_caracteres= len(DUI)==10
el_noveno_caracter_es_guion= DUI[8]=="-"
es_valido= largo_es_diez_caracteres and el_noveno_caracter_es_guion
print(es_valido)