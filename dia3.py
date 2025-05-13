# Operadores aritméticos
a = 5
b = 2

print(a + b)
print(a * b)
print(a / b)
print(a ** b) # Exponenciação
print(a // b) # Resultado da divisão inteira
print(a % b) # Resto da divisão

# Operadores de comparação
x = 10
y = 5

print(x > y) # Maior que
print(x < y) # Menor que
print(x != y) # Diferente de
print(x >= y) # Maior ou igual
print(x <= y) # Menor ou igual

# Operadores Lógicos : AND, OR e NOT

# Unir comparações

# O AND só é verdadeiro quando ambas operações resultam em "true"
# O OR é verdadeiro quando pelo menos uma das operações resulta em "true"
# O NOT inverte um booleano

# AND
idade = int(input("Digite sua idade: ")) # int para transformar a entrada de dados em um número inteiro
possui_carteira = input("Digite se possui carteira (sim/não): ").lower() # .lower() para garantir que a resposta seja comparada independentemente de maiúsculas ou minúsculas.

pode_dirigir = (idade >= 18) and (possui_carteira == "sim") # Toda string tem que ser entre "aspas"

print("pode didrigir?", pode_dirigir)

# OR
eh_estudante = input("Você é estudante? ")
idade = int(input("Qual a sua idade? "))
meia_entrada = (eh_estudante == "sim" or idade >= 60)

print("Acesso a meia-entrada: ", meia_entrada)

# NOT
chovendo = True
nao_chovendo = not chovendo

print("chovendo", chovendo)
print("Não chovendso", nao_chovendo)

# Revisão
# Passou de ano : Nota > 7 e frequência > 80%

nota = float(input("Qual a sua nota? "))
frequencia = int(input("Qual a porcentagem de sua frequência? "))

if (nota >= 7.0) and (frequencia >= 80): {
    print("Parabéns você passou de ano!")
}
else: {
    print("Você é burro, não passou de ano!")
    }

# Senhas iguais
# Criando um registro de usuário

senha1 = int(input("Digite sua senha: "))
senha2 = int(input("Digite sua senha novamente: "))

if (senha1 == senha2):{
    print("Acesso Liberado!")
}
else:{
    print("Senha 2 diferente da senha 1, Acesso negado!")
}    

