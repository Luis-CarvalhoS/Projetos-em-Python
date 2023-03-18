import csv, datetime
from prettytable import PrettyTable ##pip3 install prettytable no terminal.


def le_arquivo(nome_arquivo):
    dados = [] # Aqui realizamos a criação da lista 'dados', observe que ela se apresenta vazia no momento atual.
    with open(nome_arquivo, "r") as arquivo: #Aqui vamos abrir o arquivo atribuído à variável 'nome_arquivo' e abri-lo em modo leitura ('r').
        linhas = arquivo.readlines()#Utilizei o bloco 'with' para garantir que nosso arquivo seja fechado automaticamente após o término da operação de leitura.
        i = 0#Utilizando o método 'readlines()', conseguimos ler todas as linhas do arquivo e atribuí-las como uma lista à variável 'linhas'.
        for linha in linhas:#Criamos uma variável de controle "i", que se inicia com o valor 0.
            if i > 0:#Vamos percorrer todas as linhas da lista 'linhas', que já foi alimentada com os dados do arquivo.
                dados.append(linha.split(";"))#Utilizamos a variável 'i' para ignorar a primeira linha do nosso banco de dados, já que ela contém informações que não são relevantes para a nossa interação.
            i +=1#Para apresentar os dados, utilizaremos a lista 'dados', que já foi alimentada. Cada linha dessa lista é dividida em ponto e vírgula (';'), formando várias strings.
    return dados#Aqui retornamos os dados


def validar_mes(mes):#Aqui faremos a verificação, se o mes informado corresponde com nossa base de dados.
    if mes < 1 or mes > 12:
        return False
    return True


def validar_ano(ano):#Vamos realizar a verificação de ano, para saber se esta dentro dos parametros do nosso banco de dados.
    if not 1961 <= ano <= 2016:
        return False
    return True


def visualizacao_precipitacao_mes(dados, mes_filtrar, ano_filtrar):#Recebemos uma lista de dados, mes e ano a ser considerado, estao validamos se estao de acordo com os valores informados.
    lista_filtrada = []#Caso valide, o dado é adicionado a lista filtrada.
    for dado in dados:
        dia, mes, ano = dado[0].split("/")#Realizamos a divisão, para melhor processamento e vizualização dos dados.
        if int(ano_filtrar) == int(ano) and int(mes_filtrar) == int(mes):
            lista_filtrada.append((dado[0], dado[1]))
    return lista_filtrada#Aqui retornamos, todos os dias do mes escolhido, do ano solicitado.

        

def temperatura_maxima(dados, ano_filtrar):
    meses = {#Aqui iremos relacionar o número ao nome do mes, com a criação de um dicionario.
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    temperaturas_maximas = {mes: (None, None) for mes in range(1, 13)}#Aqui iniciamos zerado a temperatura e dia maximo de cada mes.
    for dado in dados:
        dia, mes, ano = dado[0].split("/")
        if int(ano_filtrar) == int(ano) and int(dia) <= 7:#Percorremos a lista a fim de filtrar somente os primeiros 7 dias de cada mes, e ainda avaliar se é o mesmo mes informado.
            mes_int = int(mes)
            temperatura = float(dado[2])#Caso a expressão seja verdadeira, a temperatura é convertida para float e verificamos se é maior que a maior temperatura atual, se for:
            #A temperatura maxima e os dias sao atualizados em temperatura_maxima
            if temperaturas_maximas[mes_int][0] is None or temperatura > temperaturas_maximas[mes_int][0]:
                temperaturas_maximas[mes_int] = (temperatura, int(dia))
    table = PrettyTable()
    table.field_names = ["Mês", "Dia", "Temperatura máxima"]
    for mes, (temperatura, dia) in temperaturas_maximas.items():
        if temperatura is not None:
            table.add_row([meses[mes], dia, f"{temperatura:.1f}°C"])
    return str(table)



    
    









































