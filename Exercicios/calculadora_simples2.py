
# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza o cálculo correspondente.

# Primeiro: o usuário digita a operação que deseja executar, sendo elas: +, -, /, //, *, ** e %.
# Segundo: aparece a mensagem na tela da operação que você escolheu
# Terceiro: O programa pede para digitar o primeiro número 
# Quarto: O programa pede para digitar o segundo número
# Quinto : O programa finaliza e aparece na tela o resultado da operação
# OBS: caso escoha aluma operação inválida o programa vai exibir na tela "ESSA NÃO É UMA OPERAÇÃO VÁLIDA"
# OBS2: na divisão caso o segundo numero digitado seja "0", vai aparecer uma msg de erro "  ERRO, DIVISÃO POR ZERO"

operacao = input("Digite a operação que deseja: ")

if operacao == '+':
    print("Você escolheu ADIÇÃO")
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: ")) 
    resultado = numer1 + numer2
    print("RESULTADO: ", resultado)


elif operacao == '-':
    print("Você escolheu a SUBTRAÇÃO!")
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: ")) 
    resultado2 = numer1 - numer2
    print("RESULTADO: ", resultado2)


elif operacao == '*':
    print("Você escolheu a MULTIPLICAÇÃO!")
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: ")) 
    resultado3 = numer1 * numer2
    print("RESULTADO: ", resultado3)


elif operacao == '/':
    print("Você escolheu a DIVISÃO!")
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: ")) 
    if numer2 != 0:
     resultado4 = numer1 / numer2
     print("RESULTADO: ", resultado4)
    else:
        print("ERRO, DIVISÃO POR ZERO") 


elif operacao == '**':
    print("Você escolheu a POTENCIAÇÃO!")
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: ")) 
    resultado5 = numer1 ** numer2
    print("RESULTADO: ", resultado5)


elif operacao == '%':
    print("Você escolheu o RESTO DA DIVISÃO!") 
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: ")) 
    resultado6 = numer1 % numer2
    print("RESULTADO: ", resultado6)


elif operacao == '//':
    print("Você escolheu o RESULTADO DA DIVISÃO INTEIRO!") 
    numer1 = int(input("DIGITE O PRIMEIRO NÚMERO A SER CALCULADO: "))
    numer2 = int(input("DIGITE O SEGUNDO NÚMERO A SER CALCULADO: "))
    if numer2 != 0: 
     resultado7 = numer1 // numer2
     print("RESULTADO: ", resultado7)
    else:
       print("ERRO, DIVISÃO POR ZERO") 


else:
    print("ESSA NÃO É UMA OPERAÇÃO VÁLIDA")        



