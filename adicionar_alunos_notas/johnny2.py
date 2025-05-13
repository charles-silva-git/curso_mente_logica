import os  # Importa o módulo os para interagir com o sistema operacional
from time import sleep  # Importa a função sleep para pausar a execução por um tempo

def LimparTela():  # Função para limpar a tela do terminal
    # Executa o comando 'cls' no Windows para limpar a tela
    # Para outros sistemas operacionais, seria necessário usar outro comando
    os.system('cls')

def menu():  # Função que exibe o menu principal e retorna a opção escolhida
    cabecalho('MENU')  # Chama a função para exibir o cabeçalho do menu
    print("""
[1] Adicionar alunos e notas
[2] Exibir alunos e notas
[3] Sair
""")  # Exibe as opções do menu
    return lerDados('Digite uma das opções: ', int)  # Lê a opção do usuário, convertendo para inteiro

def cabecalho(msg):  # Função para exibir um cabeçalho estilizado
    tamanho = len(msg) + 30  # Define o tamanho da borda com base no comprimento da mensagem
    borda = '=' * tamanho  # Cria uma linha de '=' com o tamanho definido
    # Exibe a borda, a mensagem centralizada com traços e a borda novamente
    print(f'{borda}\n{msg.center(tamanho, "-")}\n{borda}')

def converterFloat(dados):  # Função para converter uma string em float, substituindo vírgula por ponto
    return float(dados.replace(',', '.'))

def lerDados(msg, conversor):  # Função genérica para ler e converter dados de entrada
    while True:  # Loop infinito até obter entrada válida
        try:
            return conversor(input(msg))  # Tenta ler a entrada e converter usando a função fornecida
        except ValueError:  # Caso a conversão falhe
            print('\033[31mERRO!! Valor invalido\033[m')  # Exibe mensagem de erro em vermelho

def validadorDeNome(msg):  # Função para validar nomes (apenas letras)
    while True:
        nome = input(msg)  # Lê o nome do usuário
        if nome.isalpha():  # Verifica se o nome contém apenas letras
            return nome  # Retorna o nome válido
        else:
            print('\033[31mERRO!! Valor invalido\033[m')  # Mensagem de erro se inválido

def cadastroAluno(cadastros):  # Função para cadastrar um novo aluno
    while True:  # Loop para permitir cadastro de múltiplos alunos
        LimparTela()  # Limpa a tela
        cabecalho('CADASTRO DE ALUNOS')  # Exibe o cabeçalho de cadastro
        notas = []  # Lista para armazenar as notas do aluno
        # Solicita o nome do aluno, validando e capitalizando (primeira letra maiúscula)
        nome = validadorDeNome('Digite o nome do aluno: ').capitalize()
        # Pede a quantidade de provas/atividades feitas pelo aluno
        qtd_provas = lerDados(f'Quantas atividades/provas {nome} fez: ', int)
        # Loop para coletar cada nota
        for num in range(1, qtd_provas + 1):  # De 1 até a quantidade de provas
            # Solicita a nota, convertendo para float
            notas.append(lerDados(f'Digite a {num}ª nota: ', float))
        # Armazena as notas do aluno como uma tupla no dicionário de cadastros
        cadastros[nome] = tuple(notas)

        # Loop para perguntar se deseja continuar adicionando alunos
        while True:
            try:
                opc = input('Continuar adicionando alunos? [S/N] ').upper().strip()[0]
                # Pega a primeira letra da resposta, em maiúsculo, e verifica se é S ou N
                if opc in 'SN':
                    break  # Sai do loop se a resposta for válida
                print('\033[31mERRO!! Valor invalido\033[m')  # Mensagem de erro para resposta inválida
            except IndexError:
                # Caso o usuário insira uma resposta vazia, evita erro
                print('\033[31mERRO!! Valor invalido\033[m')
        if opc == 'N':  # Se a resposta for 'N', sai do cadastro de alunos
            LimparTela()
            break

def exibirAlunos(cadastros):  # Função para exibir a lista de alunos e suas notas
    LimparTela()  # Limpa a tela
    cabecalho('BOLETIM')  # Exibe o cabeçalho do boletim
    if len(cadastros) > 0:  # Se houver alunos cadastrados
        for nome, notas in cadastros.items():  # Para cada aluno e suas notas
            print(f'O aluno {nome} teve as seguintes notas: ')  # Exibe o nome do aluno
            for i, nota in enumerate(notas, start=1):  # Para cada nota com índice começando em 1
                print(f'\t{i}ª nota: {nota:.1f}')  # Exibe a nota formatada com uma casa decimal
                sleep(0.5)  # Pausa por 0.5 segundos para efeito visual
            # Exibe a média final do aluno
            print(f'Média final do aluno {nome} é {media(notas):.1f}')
            print("==" * 20)  # Separador visual
    else:
        print('Nenhum aluno foi cadastrado ainda')  # Caso não haja alunos cadastrados

    # Loop para sair da visualização
    while True:
        if lerDados('Digite 999 para sair: ', int) == 999:  # Aguarda o usuário digitar 999
            LimparTela()  # Limpa a tela
            break  # Sai do loop
        print('\033[31mERRO!! Valor invalido\033[m')  # Mensagem de erro se entrada inválida

def media(notas):  # Função para calcular a média das notas
    return sum(notas) / len(notas)  # Soma todas as notas e divide pela quantidade

# Dicionário inicial com alguns alunos pré-cadastrados
alunos = {'Rodrigo': (0, 3.5, 2, 1), 'Natan': (0, 8, 9, 10)}

# Loop principal do programa
while True:
    opc = menu()  # Chama o menu e obtém a opção do usuário
    if opc == 1:  # Se a opção for 1
        cadastroAluno(alunos)  # Chama a função para cadastrar alunos
    elif opc == 2:  # Se a opção for 2
        exibirAlunos(alunos)  # Exibe os alunos cadastrados
    elif opc == 3:  # Se a opção for 3
        print('==' * 20)  # Exibe uma linha separadora
        print('Obrigado volte sempre!')  # Mensagem de despedida
        break  # Encerra o programa
    else:  # Caso a opção seja inválida
        LimparTela()  # Limpa a tela
        print('\033[31mDigite uma opção válida.\033[m')  # Mensagem de erro em vermelho