
# Um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais



idade = int(input("DIGITE SUA IDADE: "))

if idade <= 12:
    print("Você é uma Criança")

elif idade <= 17:
    print("Você é um Adolescente")

elif idade <= 59:
    print("Você é um Adulto")

elif idade >= 60:
    print("Você é um Idoso")    
