print (' Seja bem vindo!!!\n')

import sys

jogo = str(input('Vamos jogar um jogo? [S/N]: ')).strip().upper()[0]
if jogo == 'N':
   print ('Até a próxima!')
   sys.exit()
if jogo != 'S' and jogo != 'N':
  print ('Resposta inválida')
  sys.exit()


import time

print (f'\n Começando em:\n3')
time.sleep (1)

print (f' Começando em:\n2')
time.sleep (1)

print (f' Começando em:\n1\n')
time.sleep (1)

print ('Boa sorte!\n\nJogo do Detetive\n')

time.sleep(2)

pergunta1 = str(input('Você telefonou para a vítima? [S/N]: ')).strip().upper()[0]
if pergunta1 != 'S' and pergunta1 != 'N':
  print ('Resposta inválida')
  sys.exit()

pergunta2 = str(input('Você esteve no local do crime? [S/N]:')).strip().upper()[0]
if pergunta1 != 'S' and pergunta1 != 'N':
  print ('Resposta inválida')
  sys.exit()

pergunta3 = str(input('Você mora perto da vítima? [S/N]:')).strip().upper()[0]
if pergunta1 != 'S' and pergunta1 != 'N':
  print ('Resposta inválida')
  sys.exit()

pergunta4 = str(input('Você devia para a vítima? [S/N]:')).strip().upper()[0]
if pergunta1 != 'S' and pergunta1 != 'N':
  print ('Resposta inválida')
  sys.exit()

pergunta5 = str(input('Você já trabalhou com a vítima? [S/N]: ')).strip().upper()[0]
if pergunta1 != 'S' and pergunta1 != 'N':
  print ('Resposta inválida')
  sys.exit()

print ()
contador = 0

if pergunta1 == 'S' :
  contador = contador + 1

if pergunta2 == 'S' :
  contador = contador + 1

if pergunta3 == 'S' :
  contador = contador + 1

if pergunta4 == 'S' :
  contador = contador + 1

if pergunta5 == 'S' :
  contador = contador + 1


time.sleep(2)

print ('Com base na nossa investigacão...\n')

time.sleep (2)

if contador == 2:
  print ('"Você é Suspeito"')

elif contador == 3 or contador == 4:
  print ('"Você é Cúmplice"')

elif contador == 5:
  print ('"Você é o Assassino"')

else:
  print ('"Você é inocente"')

print ('\n Fim de jogo!!!')