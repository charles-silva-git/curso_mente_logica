
numero = int(input("Digite aqui o número, pra saber se ele é par ou ímpar: ")) # Primeira maneira

if numero % 2 == 0:
    print("Esse número é par!", numero)
else:
    print("Esse número é ímpar!", numero)    

    

# Solicitar número
numero = int(input("Digite um número inteiro: "))            # Segunda maneira
# Verificar se é par ou ímpar
eh_par = (numero % 2) == 0
print("O número é par?", eh_par)