
#Operadores aritméticos

a = 5
b = 2

print(a + b)
print(a * b)
print(a / b)
print(a // b) #Divisão inteira
print(a ** b)  #exponenciação
print(a % b) #Resto  da divisão

#nota >= 7 e frequencia >= 80%

nota = 8
frequencia = 90
passouDeAno = nota >= 7 and frequencia >= 80

print (passouDeAno) 

#senhas iguais
#criando um registro de usuario

senha = "teste1234"
confirmacao_de_senha = " teste12345"

aviso_senha_errada = senha != confirmacao_de_senha

print ("A senha não combina ? ", aviso_senha_errada)

#conta do bar
#valor 123.85
#Quanto cada pessoa vai pagar

pessoas = 3
conta_a_pagar = 123.85

quanto_pra_cada = conta_a_pagar // pessoas

print("Cada um deve pagar: ", quanto_pra_cada)
