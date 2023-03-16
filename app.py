import sqlite3
import os
import time
from sty import fg

# funções do app
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def tela_inicial():
    db = sqlite3.connect('cadastro_de_usuarios.db')
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE usuarios(nome text, idade integer, email text)")
        db.commit()
    except:
        pass

    limpa()
    print(fg.yellow+'Cadastro de Usuarios'.upper())
    print(fg.white+'1 = cadastra novo usuario')
    print(fg.white+'2 = consulta de usuarios')
    print(fg.white+'3 = sair')
    ops = input('Escolha uma opção: ')

    if (ops == '1'):
        limpa()
        cadastro()
   
    elif (ops == '2'):
        limpa()
        consulta()

    elif (ops == '3'):
        sair()

    else:
        print('opção invalida')
        time.sleep(2)
        tela_inicial()

def cadastro():
    db = sqlite3.connect('cadastro_de_usuarios.db')
    cursor = db.cursor()

    limpa()
    print(fg.yellow+'Cadastrar novo usuario.'.upper())
    nome = input(fg.white+'Nome do usuario: ')
    print(fg.white+'Aguarde'.upper())
    time.sleep(1.5)
    limpa()
    print(fg.yellow+'Cadastrar novo usuario.'.upper())
    idade = input(fg.white+'Idade do usuario: ')
    print(fg.white+'Aguarde'.upper())
    time.sleep(1.5)
    limpa()
    print(fg.yellow+'Cadastrar novo usuario.'.upper())
    email = input(fg.white+'e-mail do usuario: ')
    print(fg.white+'Aguarde'.upper())
    time.sleep(1.5)

    cursor.execute("INSERT INTO usuarios VALUES('"+nome+"',"+str(idade)+",'"+email+"')")
    db.commit()
    db.close()
    escolha()

def escolha():
    limpa()
    print(fg.yellow+'Usuario cadastrado com sucesso'.upper())
    print(fg.white+'Deseja cadastrar outro usuario?')
    ops = input('S = Sim - N = Não -> ')

    if (ops == 'S'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        cadastro()

    elif (ops == 's'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        cadastro()
    
    elif (ops == 'N'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        tela_inicial()
    
    elif (ops == 'n'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        tela_inicial()

    else:
        print(fg.white+'opção invalida'.upper())
        time.sleep(1.5)
        escolha()

def consulta():
    limpa()
    print(fg.yellow+'Consulta de Usuarios'.upper())
    print(fg.white+'1 = Consulta geral')
    print(fg.white+'2 = Consulta por nome')
    print(fg.white+'3 = Voltar')
    ops = input('Escolha uma opção: ')
    
    if (ops == '1'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        consulta_geral()

    elif (ops == '2'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        consulta_nome()

    elif (ops == '3'):
        tela_inicial()

    else:
        print('opção invalida')
        time.sleep(1.5)
        consulta()


def consulta_geral():
    limpa()
    db = sqlite3.connect('cadastro_de_usuarios.db')
    cursor = db.cursor()
    consultar = "SELECT * FROM usuarios"
    cursor.execute(consultar)
    dados = cursor.fetchall()

    print(fg.yellow+'Lista de usuarios cadastrados no banco de dados'.upper())

    for linha in dados:
        print(fg.green+'Nome:', fg.white+linha[0])
        print(fg.green+'Idade:', fg.white+str(linha[1]))
        print(fg.green+'e-mail:', fg.white+linha[2], '\n')
        
    db.close()
    escolha2()

def consulta_nome():
    limpa()
    db = sqlite3.connect('cadastro_de_usuarios.db')
    cursor = db.cursor()
    print(fg.yellow+'Busca de usuarios no banco de dados'.upper())
    nome = input(fg.white+'Digite o nome para a busca: ')
    print(fg.white+'aguarde'.upper())
    time.sleep(1.5)
    limpa()

    consulta = "select nome, idade, email from usuarios where nome = '"+nome+"'"
    cursor.execute(consulta)
    dados = cursor.fetchall()

    if (dados != []):
        print(fg.yellow+'Lista de usuarios cadastrados no banco de dados'.upper())
        print(fg.yellow+'Resultado da busca'.upper())

        print(fg.green+'Nome:', fg.white+dados[0][0])
        print(fg.green+'Idade:', fg.white+str(dados[0][1]))
        print(fg.green+'e-mail:', fg.white+str(dados[0][2]), '\n')

        db.close()
        escolha2()
    else:
        print(fg.red+'Usuario não encontrado no banco de dados'.upper())
        print(fg.red+'Favor revisar e tentar novamente'.upper())
        print(fg.white+'')
        time.sleep(2.5)
        consulta_nome()

def escolha2():
    ops = input(fg.white+'V = Voltar - S = Sair - O = Outra consulta -> ')

    if (ops == 'V'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        tela_inicial()

    elif (ops == 'v'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        tela_inicial()

    elif (ops == 'S'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        sair()

    elif (ops == 's'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1.5)
        sair()

    elif (ops == 'o'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1)
        consulta()

    elif (ops == 'O'):
        print(fg.white+'aguarde'.upper())
        time.sleep(1)
        consulta()

    else:
        print(fg.white+'opção invalida'.upper())
        time.sleep(1.5)
        print('\n')
        escolha2()

def sair():
    limpa()
    print(fg.white+'Ate a proxima'.upper())
    time.sleep(2)
    limpa()

tela_inicial()