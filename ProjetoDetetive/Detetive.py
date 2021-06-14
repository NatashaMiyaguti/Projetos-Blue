print (' Seja bem vindo!!!\n')

from sys import exit

jogo = str(input('Vamos jogar um jogo? [S/N]: ')).strip().upper()[0]
if jogo == 'N':
   print ('Até a próxima!')
   exit()
if jogo != 'S' and jogo != 'N':
  print ('Resposta inválida')
  exit()


from time import sleep

print (f'\n Começando em:\n3')
sleep (1)

print (f' Começando em:\n2')
sleep (1)

print (f' Começando em:\n1\n')
sleep (1)

print ('Boa sorte!\n\nJogo do Detetive\n')

sleep(2)

pergunta1 = str(input('Você telefonou para a vítima? [S/N]: ')).strip().upper()[0]
if pergunta1 != 'S' and pergunta1 != 'N':
  print ('Resposta inválida')
  exit()

pergunta2 = str(input('Você esteve no local do crime? [S/N]:')).strip().upper()[0]
if pergunta2 != 'S' and pergunta2 != 'N':
  print ('Resposta inválida')
  exit()

pergunta3 = str(input('Você mora perto da vítima? [S/N]:')).strip().upper()[0]
if pergunta3 != 'S' and pergunta3 != 'N':
  print ('Resposta inválida')
  exit()

pergunta4 = str(input('Você devia para a vítima? [S/N]:')).strip().upper()[0]
if pergunta4 != 'S' and pergunta4 != 'N':
  print ('Resposta inválida')
  exit()

pergunta5 = str(input('Você já trabalhou com a vítima? [S/N]: ')).strip().upper()[0]
if pergunta5 != 'S' and pergunta5 != 'N':
  print ('Resposta inválida')
  exit()

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


sleep(2)

print ('Com base na nossa investigacão...\n')

sleep (2)

if contador == 2:
  print ('"Você é Suspeito"')

elif contador ==3 or contador == 4:
  print ('"Você é Cúmplice"')

elif contador == 5:
  print ('"Você é o Assassino"')

else:
  print ('"Você é inocente"')
