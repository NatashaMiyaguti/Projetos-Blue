from random import randint
from time import sleep


while True:
    cont_computador = cont_jogagor = empate = 0

    jogo = str(input('\nVamos jogar Jokenpo? [S/N]: ')).strip().upper()[0]
    if jogo == 'N':
        print ('Até a próxima!')
        break
    if jogo != 'S' and jogo != 'N':
        print ('Resposta inválida')
        break

    rodadas = int(input('\nDigite quantas rodadas iremos jogar: '))

    for n in range(rodadas): 
        sleep(1)
        print('\nVamos começar a rodada!')
        computador = randint(1,3)
        sleep(2)
        print('\n[1] Pedra')
        sleep(1)
        print('[2] Papel')
        sleep(1)
        print('[3] Tesoura')
        sleep(1)
        escolha = int(input('\nQual opção você escolhe:'))
        sleep(1)
        
        if escolha == 1 and computador == 1:
            empate += 1
            print(f'\nVocê escolheu [{escolha}] Pedra, e o computador escolheu [1] Pedra.')
            sleep(2)
            print('Deu empate!!!'.center(50))
        elif escolha == 1 and computador == 2:
            cont_computador += 1
            print(f'\nVocê escolheu [{escolha}] Pedra, e o computador escolheu [2] Papel.')
            sleep(2)
            print ('Você perdeu!!!'.center(50))
        elif escolha == 1 and computador == 3:
            cont_jogagor += 1
            print(f'\nVocê escolheu [{escolha}] Pedra e o computador escolheu [3] Tesoura.')
            sleep(2)
            print('Você ganhou!!!'.center(50))
        
        elif escolha == 2 and computador == 2:
            empate += 1
            print(f'\nVocê escolheu [{escolha}] Papel, e o computador escolheu [2] Papel.')
            sleep(2)
            print('Deu empate!!!'.center(50))
        elif escolha == 2 and computador == 3:
            cont_computador +=1
            print(f'\nVocê escolheu [{escolha}] Papel, e o computador escolheu [3] Tesoura.')
            sleep(2)
            print ('Você perdeu!!!'.center(50))
        elif escolha == 2 and computador == 1:
            cont_jogagor +=1
            print(f'\nVocê escolheu [{escolha}] Papel e o computador escolheu [1] Pedra.')
            sleep(2)
            print('Você ganhou!!!'.center(50))
        elif escolha == 3 and computador == 3:
            empate +=1
            print(f'\nVocê escolheu [{escolha}] Tesoura, e o computador escolheu [3] Tesoura.')
            sleep(2)
            print('Deu empate!!!.center(50)')
        
        elif escolha == 3 and computador == 1:
            cont_computador +=1
            print(f'\nVocê escolheu [{escolha}] Tesoura, e o computador escolheu [1] Pedra.')
            sleep(2)
            print ('Você perdeu!!!'.center(50))
        elif escolha == 3 and computador == 2:
            cont_jogagor +=1
            print(f'\nVocê escolheu [{escolha}] Tesoura e o computador escolheu [1] Papel.')
            sleep(2)
            print('Você ganhou!!!'.center(50))
        else:
            (f'\n Você digitou [{escolha}]. Opção inválida!')

    print(f'''
   { '-'*60}
    ''')

    print(f'\nEm {rodadas} rodada(s)...')
    sleep(2)
    print(f'''\nVocê venceu {cont_jogagor} rodada(s).
Você perdeu {cont_computador} rodada(s).
Você empatou {empate} rodada(s).
    ''')
    sleep(1)
    if cont_jogagor > cont_computador:
        print('Você Ganhou!!!'.center(50))
    elif cont_computador> cont_jogagor:
        print('Você Perde!!!'.center(50))
    else:
        print('Deu Empate!!!'.center(50))

                        
