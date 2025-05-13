eh_estudante = input("Você é estudante? ")
idade = int(input("Qual a sua idade? "))
meia_entrada = (eh_estudante == "sim" or idade >= 60)

print("Acesso a meia-entrada: ", meia_entrada)