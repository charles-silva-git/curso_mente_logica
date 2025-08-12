
import random #Biblioteca de números aleatórios do Phyton

print("Bem-Vindo ao jogo do 'Advinhe o Número'")


while True: #Repetir um código até o usuário acertar
    
    numero_secreto = random.randint(1, 50) #Gerar um número aleatório entre (1 - 50)
    
    #print(numero_secreto)
    
    tentativas = 5
    
    print("PENSEI EM UM NÚMERO ENTRE 1 E 50")
    print("VOCÊ TEM 5 TENTATIVAS PARA ADVINHAR")
    
    while tentativas > 0: #Loop até as tentativas acabarem
        
        palpite = input("DIGITE SEU PALPITE: ")
        
        if not palpite.isdigit(): #Validação para checar se o usuário digitou um número
            print("ENTRADA INVÁLIDA, DIGITE UM NÚMERO ENTRE 1 E 50")
            continue
        
        palpite = int(palpite) #Converter palpite para inteiro
        
        if palpite <1 or palpite >50: # Garantir que o número seja no intervalo estipulado
            print("O NÚMERO DEVE SER ENTRE 1 E 50")
            continue
        
        
        tentativas -= 1 #Subtrair as tentativas
        
        if palpite == numero_secreto:
            print(f"PARABÉNS, VOCÊ ADVINHOU O NÚMERO! VOCÊ AINDA TINHA {tentativas} TENTATIVAS")
            break # Parar o loop se acertar o número
        elif palpite < numero_secreto:
            print("O NÚMERO É MAIOR QUE ESSE")
        else:
            print("O NÚMERO É MENOR QUE ESSE")        
        
        print(f"TENTATIVAS RESTANTES: {tentativas}")
    
    else: # Isso é um while else para quando as tentativas acabarem e o usuário não acertar o número
        print(f"VOCÊ PERDEU! O NÚMERO SECRETO ERA: {numero_secreto}") 
    
    #PERGUNTAR SE O JOGADOR QUER JOGAR NOVAMENTE
    jogar_novamente = input("VOCÊ DESEJA JOGAR NOVAMENTE? (S/N)").lower() #lower para dar certo se o usuário digitar a resposta em minúsculo tmb           
    
    if jogar_novamente != "S":
        print("OBRIGADO POR PARTICIPAR! ATÉ A PRÓXIMA...")
        break