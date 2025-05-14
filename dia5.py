# Estrutura de repetição

# Repetir N vezes
# Onde n, a gente pode definir
# Ou n é uma condição

frutas = ["maçã", "banana", "laranja"]
# for + variável temporária + in + lista: a representação de lisa é através de [colchetes]
# bloco repetido N vezes

for fruta in frutas:
    print("Fruta: ", fruta)

for i in range(5): # O "i" é uma variável temporária para o uso do for, o range é para indicar uma contagem até a quantidade de vezes que você estipular
    print("Num: ", i)    

print(frutas[0]) # Quando faço isso eu acesso a numeração da lista em que cada fruta está alocada
print(frutas[2]) 
# frutas = ["maçã", "banana", "laranja"], sendo: maçã 0, banana 1, laranja 2

# while

contador = 0

while contador < 5:
    print("Num while: ", contador)
    contador += 1 # Aqui eu to pedindo mpara o computador acrescentar sempre +1 ao resultado até chegar em 5, senão fica um loop infinito sem sair do zero
# Um loop com uma condição mal definida = loop infinito = bug

for i in range(10):
    if i == 5:
        break # Aqui quer dizer que quando o "i" for igual a "5" o programa para "break"
    print("Num for", i)    

# break => para o loop
# continue => pula uma execução

for i in range(10):
    if i == 2:
        continue
    print("Num for", i)



# Calcular multiplicação de 1 a N
N = int(input("Digite um número: "))
multiplicacao = 0

for i in range(1, N + 1):
    resultado = N * i
    print(resultado)   

# Identificar números pares e ímpares até 20
pares = 0
impares = 0

for i in range(1, 10):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares: ", pares)
print("Impares: ", impares)            
