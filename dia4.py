# Condicionais -> estruturas if, else
idade = 16

# Estrutura do if -> if COMPARACAO:
# O bloco do if é executado quando a condição é verdadeira

if idade >= 18:
    print("Você é maior de idade!")

# else
# É executado quando a condição do if não executa

else:
    print("Você é menor de idade!")    

# Nota recruta, soldado, oficial
# > 9 = oficial, > 7 = soldado, > 5 = recruta


nota = int(input("Digite aqui sua nota: "))
 
# elif -> else + if
# Condição intermediária entre if e else

if nota > 9:
    print("Você é um Oficial")
elif nota > 7:
    print("Você é um Soldado")
elif nota > 5:
    print("Você é um Recruta")
else:
    print("Você precisa melhorar!")             


# Comissão de vendas
# > 1000 = 0.5%
# > 500 = 1%
# 2%

valor_do_produto_vendido = int(input("Digite o valor do produto vendido: "))

comissao = valor_do_produto_vendido * 0.005
comissao2 = valor_do_produto_vendido * 0.01
comissao3 = valor_do_produto_vendido * 0.02

if valor_do_produto_vendido > 1000:
    print("A comissão da venda foi: ", comissao)
elif valor_do_produto_vendido > 500:
    print("A comissão da venda foi: ", comissao2)
else :
    print("A comissão da venda foi: ", comissao3)        