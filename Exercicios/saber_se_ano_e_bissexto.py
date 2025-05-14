

# Um programa que verifica se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Mas não é bissexto se for divisível por 100, exceto se for divisível por 400.

# Digita o ano
# Se o ano digitado dividido por 4 o resto for 0 e se o ano digitado dividido por 100 
# o resto é diferente de 0 ou se o ano digitado dividido por 400 que o resto dê 0, esse ano será BISSEXTO

ano = int(input("Digite aqui o ano, para saber se ele é bissexto ou não: "))

if ( ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print(ano, "Esse ano é BISSEXTO")
else:
    print(ano, "Esse ano não é BISSEXTO")    
