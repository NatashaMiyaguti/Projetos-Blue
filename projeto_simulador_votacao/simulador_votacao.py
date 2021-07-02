# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação

from datetime import datetime #importa a data atual
from operator import itemgetter   #para ordenar o dicionario#
from collections import defaultdict   #agrupa dados do dicionario#
from random import randint
from time import sleep
from rich import print   #importa as cores e emotion, somente pode ser usados nos prints#
from tqdm import tqdm   #importa a barra de carregamento#



print(""" 

[blue]
   _____________________
  /                 `   \\
  |  .-----------.  |   |-----.
  |  |           |  |   |-----|
  |  | "votação" |  |   |-----|
  |  |           |  |   |-----|
  |  |           |  |   |-----|
  |  `-----------'  |   |-----'/\\
   \________________/___'     /  \\
      /                      / / /
     / //               //  / / /
    /                      / / /
   / _/_/_/_/_/_/_/_/_/_/ /   /
  / _/_/_/_/_/_/_/_/_/_/ /   /
 / _/_/_/_______/_/_/_/ / __/
/______________________/ /    
\______________________\/

[blue]
""")

candidatos = { 'Joao': 0 , 'Pedro': 0 , 'Ana': 0 , 'Voto Nulo': 0 , 'Voto em Branco': 0 }

def autoriza_voto(ano):
    idade = datetime.now().year - ano #para colocar o ano atual
    if idade < 16:
        autorizacao = 'NEGADO'
    elif 18 <= idade < 70:
        autorizacao = 'OBRIGATORIO'  
    else:
        autorizacao = 'OPCIONAL'
    return autorizacao

def votacao(autorizacao, voto):
    if voto not in range (1,6):
        print('Opção inválida')
    elif autorizacao == 'OPCIONAL' or autorizacao == 'OBRIGATORIO': 
        print('\n[blue]Voto computado.[blue]\n  Obrigada.\n')
        if voto == 1:
            candidatos['Joao'] += 1
        elif voto == 2:
            candidatos['Pedro'] += 1
        elif voto == 3:
            candidatos['Ana'] += 1
        elif voto == 4:
            candidatos['Voto Nulo'] += 1
        elif voto == 5:
            candidatos['Voto em Branco'] += 1
    else:
        print('Você não pode votar')
        

while True:
    ano = randint(1970, 2020)#int(input('Digite o ano de nascimento: '))#randint(1970, 2020)
    sleep(1)

    print('\n Escolha seu voto:')
    sleep (1)
    print(f'''
    1 - João 
    2 - Pedro 
    3 - Ana    
    4 - Voto Nulo
    5 - Voto em Branco
    ''')
    sleep(1)
    voto_escolhido = randint(1,5)#int(input('Digite o numero do seu voto: '))#randint(1,5)
    votacao(autoriza_voto(ano), voto_escolhido )
    
    continuar = str(input('Deseja continuar[S/N]: \n')). strip().upper()[0]
    if continuar == 'N':
        break

ranking_final = sorted(candidatos.items(), key = itemgetter(1), reverse = True) #ranking_final foram ordenadas do maior para o menor, para o ranking ficar na ordem de quem teve mais votos#
total_votos =  sum(candidatos.values()) # faz a soma de votos para cada candidato
if total_votos > 0: # valida se houve votos
    print('\n'+'_'*93) #fiz os prints assim para conseguir montar uma tabela
    print(f'|[magenta]{"Candidatos".center(30)}|{"Votos".center(30)}|{"Porcentagem".center(30)}|[magenta]')
    print('-'*93)
    for key, val in ranking_final:
        porcentagem = round((val / total_votos) * 100, 0) #transformei a quantidade de votos em %
        print(f'[blue]|{key.center(30)}|{str(val).center(30)}|{(str(porcentagem) + " %").center(30)}|[blue]')
    print('-'*93)

    somente_candidatos = candidatos.copy()
    [somente_candidatos.pop(key) for key in ['Voto Nulo', 'Voto em Branco']] # eu tiro do dicionario as keys 'voto nulo' e 'voto em branco', para poder saber quem ganhou e eles não serem listados como ganhadores
    candidatos_agrupados = defaultdict(list) #criei uma variavel que recebe uma  lista. "defauldict" faz um agrupamento dos candidatos por numero de votos, para saber quem tem valores iguais#
    for key, val in sorted(somente_candidatos.items(), key = itemgetter(1), reverse = True): #ordena do maior para o menor, para o ranking ficar na ordem de quem teve mais votos#
        candidatos_agrupados[val].append(key) #coloca no dicionario#

    total_votos =  sum(somente_candidatos.values())
    if total_votos > 0: #valida os votos validos
        for key, val in sorted(dict(candidatos_agrupados).items(),reverse = True): #os candidatos_agrupadas foram ordenados do maior para o menor#
            porcentagem = round((key / total_votos) * 100, 0)
            print(f'Com {porcentagem} % de votos') 
            for candidato in val:
                print(f'\n[blue] {candidato.center(50)}[blue]')

        vencedor_dict = sorted(dict(candidatos_agrupados).items(),reverse = True)[0]  #candidatos_agrupados agrupa os candidatos pelo numero de votos, pois poderia ter mais de um com a mesma quantidade de votos#
        vitoria = vencedor_dict[1]
        print()
        for i in tqdm(range (150)): #cria um indicador de carregamento#
                sleep(0.0001)
        print()
        if len(vitoria) > 1:  #caso tenho mais de um candidato na posicao 1#
            print(f'[yellow]Houve empate! Aguardem data para nova votação, entre os candidatos:[yellow]')
            for i in vitoria: 
                print(f'[yellow]{i}[yellow]'.center(50))
        else:
            print(f':trophy: [green]O(A) vencedor(a) das eleições é:\n[green]')
            sleep(1)
            print(f'[green]{vitoria[0].center(50)}[green]') #mostra qnd ha um unico vencedor#
    else:
        print('[red]\nNão houve votos válidos.[red]')
else:
    print('[red]\nSem votos computados.[red]')

