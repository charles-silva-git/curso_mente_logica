
#Listas(arrays) e tuplas
#Interligados com os Loops = estrutura de repetição

carros = ["BMW", "Fiat", "Ford"]

#Os itens começam a contar de zero
print(carros[0])
print(carros[2])

carros.append("Hyundai") #Adicionando um item a lista
print(carros[3])

carros [0] = "BMW elétrica" #Atualizando um item da lista
print(carros[0])

carros.remove("Fiat") #Removendo um item da lista
print(carros)

print(len(carros)) #Verifica quantos itens tem na lista

if "BMW elétrica" in carros:
    print("Achei!")       
    
# TUPLAS
# cria ( 1, 2, 3)
# Não pode modificar

cores = ("vermellho", "verde", "laranja", "roxo")

print(cores)

for cor in cores:
    print("COR: ", cor)
    
print(len(cores))    
                                                                              