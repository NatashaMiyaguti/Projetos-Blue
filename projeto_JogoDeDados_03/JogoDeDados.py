# Projeto 03 - Jogo de Dados:
# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4
# jogadores joguem um dado e tenham resultados aleatórios. O programa tem que:
# • Perguntar quantas rodadas você quer fazer; • Guardar os resultados dos
# dados em um dicionário.
# • Ordenar este dicionário, sabendo que o vencedor tirou o maior número no
# dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.

from math import nan
from random import randint
from time import sleep
from rich import print   #importa as cores e emotion, somente pode ser usados nos prints#
from operator import itemgetter   #para ordenar o dicionario#
from collections import defaultdict   #agrupa dados do dicionario#
from names import get_first_name   #caso queira preenchimento automatico nos nomes dos jogadores#
from tqdm import tqdm   #importa a barra de carregamento#

def linha():                    #cria uma funcao para fazer uma linha com '-'
    print(f'\n'+'-'*100+'\n')

    
jogadores = dict()    #cria dicionario par registrar as jogadas#
jogadores_vitoria = dict()  #cria dicionario para registrar as vitorias

while True:   #nesse bloco com while True o jogo só para qnd o usuario decide#
    print("""

    [blue1]
                (( _______
     _______     /\O    O\\
    /O     /\   /  \      \\
   /   O  /O \ / O  \O____O\ ))
((/_____O/    \\     /O     /
  \O    O\    / \  /   O  /
   \O    O\ O/   \/_____O/
    \O____O\/ ))          ))
  ((
      [/blue1]
    """)
    jogo = str(input('\nVamos jogar Dados? [S/N]: ')).strip().upper()[0]
    if jogo == 'N':
        print ('[blue]Até a próxima![blue]')
        break
    if jogo != 'S' and jogo != 'N':
        print ('[yellow]Resposta inválida[yellow]:confounded_face:')
        break

    jogadores_vitoria.clear()   # clear() limpa os dicionarios para comecar uma nova partida#
    jogadores.clear()    
    rodadas = int(input('\nDigite quantas rodadas iremos jogar: '))
    quantidade_jogadores = int(input('\nDigite a quantidade de jogadores: '))
    for j in range (quantidade_jogadores):
        nome_jogadores = str(input('Digite o nome do jogador: ')).title().strip()
        # nome_jogadores = get_first_name()  #caso nao queira escrever os nomes#
        
        jogadores[nome_jogadores] = 0          # criei no dicionario o nome_jogadores com valor '0' para depois receber o numero do dado#
        jogadores_vitoria[nome_jogadores] = 0  #criei no dicionario para somar o numero de vitorias da rodada#
    
    for n in range(rodadas):     #roda o numero de rodadas que foi pedido no input 'rodadas' #
        print('\n[blue]Vamos começar a rodada![blue]\n')
        print('[magenta]:game_die: Rolando os dados...[magenta]\n')
        sleep(1)
        for k, v in jogadores.items():   #  ele joga o dado de 1 a 6 para cada jogador#
            jogadores[k] = randint(1,6)
        sleep(1)
        
        jogadas_agrupadas = defaultdict(list) #criei uma variavel que recebe uma  lista. "defauldict" faz um agrupamento de jogadores por numero do dado, para saber quem tirou numeros iguais#
        for key, val in jogadores.items(): 
            jogadas_agrupadas[val].append(key) #coloca no dicionario#

        posicao = 0    #criando a posicao do ranking da rodada)        
        for key, val in sorted(dict(jogadas_agrupadas).items(),reverse = True): #as jogadas_agrupadas foram ordenadas do maior para o menor#
            posicao +=1   #para colocar a posicao a partir de 1#
            print(f'Em {posicao}° lugar, com o numero {key} no dado')
            for jogador in val:
                if posicao == 1:   #se o jogador ficar em 1°, no caso igual posicao 1  ele soma 1 ponto. Em seguida da o print de vencedor#
                    jogadores_vitoria[jogador] +=1
                print(f'[blue] Jogador {jogador}[blue]')
            sleep(1)
    sleep(1)
    print(f'\n[magenta]Computando as vitórias...[magenta]\n')
    sleep(1)
    for i in tqdm(range (150)): #cria um indicador de carregamento#
        sleep(0.0001)
    linha()       #funcao para linha#
    ranking_final = sorted(jogadores_vitoria.items(), key = itemgetter(1), reverse = True)   #jogadores_vitoria foram ordenadas do maior para o menor, para o ranking ficar na orde m de quem teve mais pontos#
    for key, val in ranking_final:
        print(f'[yellow]Jogador {key} teve {val} vitórias[yellow]')

    vitorias_agrupadas = defaultdict(list)
    for key, val in ranking_final:
        vitorias_agrupadas[val].append(key)
    sleep(2)
    vitoria_dict = sorted(dict(vitorias_agrupadas).items(),reverse = True)[0]  #vitorias_agrupadas agrupa os jogadores pelo numero de vitorias, pois poderia ter mais de um jogador com o mesmo numero de pontos#
    campeoes = vitoria_dict[1]
    linha()
    if len(campeoes) > 1:  #caso tenho mais de um jogador na posicao 1#
        print(f'[green]Os(As) grandes campeões(ãs) são:[green]')
        for i in campeoes: 
            print(f':trophy: [green]{i}[green]'.center(50))
    else:
        print(f':trophy: [green]O(A) grande campeão(ã) é:\n {campeoes[0].center(50)}[green]') #mostra qnd ha um unico campeão#



