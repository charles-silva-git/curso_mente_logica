# Variáveis
idade = 32
nome = "Charles Silva"
altura = 1.75

# Tipos de dados
# int, float, textos: Strings, bool : true ou false
cidade = 'São Paulo'

esta_logado = True

print(nome)
print(type(nome))

nome = 2

print(nome)

# Verificar dados
print(type(nome)) # str = string / int
print(type(cidade)) # str = string
print(type(esta_logado)) # bool = boolean
print(type(altura)) # Float

# Operadores
print(5 + 1.5)
print(5 * 1.5)
print(5 / 1.5)
print(5 - 1.5)
print(5 % 1.5) #resto da divisão
print(5 ** 1.5) # Potência

# Concatenação -> União dos dois textos
# Unir com o símobolo de "+"
nomeUsuario = "João"
frase = " Olá " + nomeUsuario +", tudo bem?"

print(frase) # Olá João, tudo bem?

# Comparações
maior = 10 > 5
maior2 = 5 > 10

print(maior) #true
print(maior2) #false
print(5 == 5) # igual
print(5 != 6) # diderente