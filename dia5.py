
#Estrutura de repetição

#Repetiir N vezes
#Onde N, a gente pode definir
#Ou N é uma condição

frutas = ["maçã", "banana", "laranja"]
legumes = ["cenoura", "batata", "chuchu"]

# for item_individual in lista:
# bloco repetido N vezes

for fruta in frutas:
    print("Fruta: ", fruta)
    
for legume in legumes:
    print("Legume: ", legume)    

for i in range(5):
    print("Num: ", i)    
    
print (frutas[0])    
print (frutas[1]) 
print (legumes[1]) 

contador = 0
while contador < 5:
    #contador += 1
    print("Num while:", contador)
    contador += 1
    #Se eu faço um loop com uma condiçao mal definida resulta em um loop infinito = bug
    
# Calcular a multiplicação de 1 a N

N = int(input("Digite um número: "))

for i in range(1, N + 1):
    resultado = N * i
    print(resultado)    
   
for i in range(10):
    if i == 5:
        break #Responsavel por parar a sequencia
    
    print ("Num for: ", i)
    
# Identificar numeros pares e impares ate 20

pares = 0
impares = 0

for i in range(1, 249):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares: ", pares)
print("Impares: ", impares)            
        
    