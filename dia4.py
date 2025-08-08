
#Condicionais
#Estruturas : if e else

idade = 15

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é MENOR de idade")
    
    #Meia entrada => menor de 18 anos ou esteja estudando em escola pública
    
estuda_em_escola_publica = True
idade  = 18

if idade < 18 or estuda_em_escola_publica:
    print("Você tem direito a meia-entrada")
else :
    print("Você não tem direito a meia-entrada")        
    
    #Nota: A, B, C
    # > 9 = A, > 8 = B, > 6 + C
    
nota = 10
    
if nota > 9:
    print("Você é classificação A")
elif nota > 8:
    print("Você é classificação B")
elif nota > 6:
    print("Você é classificação C")
else :
    print("Você precisa melhorar")                
    
    #Comissão de vendas
    # > 1000 = 5%
    # > 500 = 10%
    # = 20%
    
venda = 600

if venda > 1000:
    comissao1 = venda * 0.5
    print("Sua comissão é de: ", comissao1)
elif venda > 500:
    comissao = venda * 0.10
    print("Sua comissãao é de: ", comissao)
else:
    comissao = venda * 0.20
    print("Sua comissão é de: ", comissao)        
        
        
#Baseado na entrada do usuario se um numero é maior ou menor que zero

numero = int(input("digite um número: "))

if numero > 0:
    print("Esse número é maior que ZERO")
else :
    print("Esse número é menor que ZERO")            