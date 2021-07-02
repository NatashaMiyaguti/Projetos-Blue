# Esse projeto tem a finalidade de fixar os conhecimentos de Variáveis, Print, Input 
# e Condicionais, para isso crie um programa que faça 5 perguntas para uma 
# pessoa sobre um crime. As perguntas são:
# • "Você telefonou para a vítima?"
# • " Você esteve no local do crime?"
# • " Você mora perto da vítima?"
# • " Você devia para a vítima?"
# • " Você já trabalhou com a vítima?" 
# O programa deve, no final, emitir uma classificação sobre a participação da 
# pessoa no crime.
# Se a pessoa responder positivamente a:
# • 2 questões ela deve ser classificada como "Suspeita",
# • Entre 3 e 4 como "Cúmplice"
# • 5 como "Assassino". 
# • Caso contrário, ele será classificado como "Inocente".


from random import randint
from time import sleep
from rich import print #importa as cores e emotion, somente pode ser usados nos prints

while True:
    cont_computador = cont_jogagor = empate = 0  #variáveis criadas para fazer as contagens de vitórias/derrotas/empates

    jogo = str(input('\nVamos jogar Jokenpo? [S/N]: ')).strip().upper()[0]
    if jogo == 'N':
        print ('[blue]Até a próxima![blue]')
        break
    if jogo != 'S' and jogo != 'N':
        print ('[yellow]Resposta inválida[yellow]:confounded_face:')
        break

    rodadas = int(input('\nDigite quantas rodadas iremos jogar: '))

    for n in range(rodadas): 
        sleep(1)
        print('\n[blue]Vamos começar a rodada![blue]')
        computador = randint(1,3)
        sleep(2)
        print('\n[yellow][1] Pedra[yellow] :raised_fist:')
        sleep(1)
        print('[yellow][2] Papel[yellow] :raised_hand:')
        sleep(1)
        print('[yellow][3] Tesoura[yellow] :victory_hand:')
        sleep(1)
        escolha = int(input('\nQual opção você escolhe:'))
        sleep(1)
        
        if escolha == computador:
            empate += 1
            print(f'\nVocê escolheu [{escolha}] Pedra:raised_fist:, e o computador escolheu [1] Pedra:raised_fist:.')
            sleep(2)
            print('[yellow]Deu empate!!![yellow]'.center(50))
        elif escolha == 1 and computador == 2:
            cont_computador += 1
            print(f'\nVocê escolheu [{escolha}] Pedra:raised_fist:, e o computador escolheu [2] Papel:raised_hand:.')
            sleep(2)
            print ('[red]Você perdeu!!![red]'.center(50))
        elif escolha == 1 and computador == 3:
            cont_jogagor += 1
            print(f'\nVocê escolheu [{escolha}] Pedra:raised_fist: e o computador escolheu [3] Tesoura:victory_hand:.')
            sleep(2)
            print('[green]Você ganhou!!![green]'.center(50))
        
        elif escolha == 2 and computador == 3:
            cont_computador +=1
            print(f'\nVocê escolheu [{escolha}] Papel:raised_hand:, e o computador escolheu [3] Tesoura:victory_hand:.')
            sleep(2)
            print ('[red]Você perdeu!!![red]'.center(50))
        elif escolha == 2 and computador == 1:
            cont_jogagor +=1
            print(f'\nVocê escolheu [{escolha}] Papel:raised_hand: e o computador escolheu [1] Pedra:raised_fist:.')
            sleep(2)
            print('[green]Você ganhou!!![green]'.center(50))
        elif escolha == 3 and computador == 1:
            cont_computador +=1
            print(f'\nVocê escolheu [{escolha}] Tesoura:victory_hand:, e o computador escolheu [1] Pedra:raised_fist:.')
            sleep(2)
            print ('[red]Você perdeu!!![red]'.center(50))
        elif escolha == 3 and computador == 2:
            cont_jogagor +=1
            print(f'\nVocê escolheu [{escolha}] Tesoura:victory_hand: e o computador escolheu [1] Papel:raised_hand:.')
            sleep(2)
            print('[green]Você ganhou!!![green]'.center(50))
        else:
            print(f'\n Você digitou [{escolha}]. Opção inválida!:confounded_face:')

    print(f'''
   { '-'*60}
    ''')

    print(f'\n[blue]Em {rodadas} rodada(s)...[blue]')
    sleep(2)
    print(f'''\n[blue]Você venceu {cont_jogagor} rodada(s).
Você perdeu {cont_computador} rodada(s).
Você empatou {empate} rodada(s).[blue]
    ''')
    sleep(1)
    if cont_jogagor > cont_computador:
        print('[green]Você Ganhou!!![green]'.center(50))
    elif cont_computador> cont_jogagor:
        print('[red]Você Perde!!![red]'.center(50))
    else:
        print('[yellow]Deu Empate!!![yellow]'.center(50))

                        
