from uteis import *
from termcolor import colored #pip install termcolor no terminal para vizualizar cores do código.
from prettytable import PrettyTable #pip3 install prettytable no terminal.

def main():
    print(colored("=====================================", 'cyan'))
    print(colored("||                                 ||", 'cyan'))
    print(colored("||    Sistema Climático em Python  ||", 'cyan'))
    print(colored("||                                 ||", 'cyan'))
    print(colored("=====================================", 'cyan'))
    dados = le_arquivo("dados.csv")
    while True:
        print(colored("\n\nSelecione uma das opções abaixo:", 'blue'))
        print(colored("1 - Visualização dos dados de precipitação", 'green'))
        print(colored("2 - Visualização dos dados de temperatura máxima", 'yellow'))
        print(colored("0 - Sair", 'red'))
        opcao = int(input(colored("Opção selecionada: ", 'magenta')))
        if opcao == 1:
            while True:
                mes = int(input("Digite o mês (1 a 12): "))
                ano = int(input("Digite o ano (1961 a 2016): "))  
                if validar_mes(mes) and validar_ano(ano):
                    print(colored("Mes/ano valido", 'green'))
                    dados_precipitacao = visualizacao_precipitacao_mes(dados, mes, ano)
                    for dado in dados_precipitacao:
                        print(dado)
                    break
                else:
                    print(colored("Mês ou ano inválido. Tente novamente.", 'red'))
                    break
        elif opcao == 2:
            while True:
                ano = int(input("Digite o ano (1962 a 2019): "))
                if validar_ano(ano):
                    dados_temperatura = temperatura_maxima(dados, ano)
                    print(dados_temperatura)
                    break
                else:
                    print(colored("Ano inválido. Tente novamente.", 'red'))    
        if opcao == 0:
            print(colored("=====================================", 'cyan'))
            print(colored("||                                 ||", 'cyan'))
            print(colored("||        Programa encerrado       ||", 'cyan'))
            print(colored("||                                 ||", 'cyan'))
            print(colored("=====================================", 'cyan'))
            break 
main()