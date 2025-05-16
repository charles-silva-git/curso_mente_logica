
# Listas e tuplas 
# Interligados com os loops - estrutura de repetição

carros = ["bmw", "fiat", "audi", "ford"]

# Os objetos da lista começam a contar de "0"
print(carros[0])
print(carros[3])

carros.append("hyundai")

print(carros[4])

carros[0] = "BMW elétrica"
print(carros[0])

print(carros)

carros.remove("ford")
print(carros)

# Saber quantos itens existe na minha lista "array"

print(len(carros))

# Verificar se existe aquele item na lista.

if "BMW elétrica" in carros:
    print("Achei o item que procura")    
    
# Tuplas
# Cria (1, 2, 3)
# E não pode ser mofificada

cores = ("vermelho", "verde", "laranja", "roxo")

print(cores)
print(cores[1])    

for cor in cores:
    print("Cor: ",cor )
    
print(len(cores))    
    
# Listas/array => você cria entre [colchetes] => pode ser modificada
# Tuplas = você cria entre (parenteses) => não pode ser modificada
    