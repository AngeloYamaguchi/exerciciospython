from time import sleep
c = ('\033[m',         #sem cores
    '\033[0;30;41m',  #1 vermelho
    '\033[0;30;42m',  #2 verde
    '\033[0;30;43m',  #3 amarelo
    '\033[0;30;44m'   #4 azul
    '\033[0;30;45m',  #5 roxo
    '\033[7;30m'      #6 branco


)
def ajuda(com):
    título(f'Acessando o manual do Comando\'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[0],end='')
    sleep(1)

def título(msg,cor =0):
    tam = len(msg)
    print(c[cor],end='')
    print('~'*30)
    print(msg)
    print('~'*30)
    print(c[0],end='')


#Programa Principal
comando = ' '
while True:
    título("Sistema de Ajuda Help",4)
    comando = str(input("Função ou Biblioteca  >"))
    if comando.upper() == 'FiM':
        break

    else:
        ajuda(comando)
título('Até logo',1)


