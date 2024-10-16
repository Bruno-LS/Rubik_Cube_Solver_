from Rotacoes import *
import pandas as pd
from Movimentos_fixos import df
from Auxiliares_passos import *

def passo_1(cubo:pd.DataFrame):#faltando o porao
    dicionario = mapear_meios(cubo)        
    
    itera = iter(dicionario.items())
    while dicionario:
        try:
            face, indice = next(itera)
            str_face = str(face)
            if indice == []:
                continue
            id = int(indice[0])
            local = verificar_movimento(cubo, id, str_face)
            
            if id==7 or id == 1:
                f(cubo, str_face)
                dicionario = mapear_meios(cubo)  
            elif id==3:
                if local == -1:
                    u_linha(cubo)
                elif local == 0:
                    u(cubo)
                elif local == 2:
                    u(cubo)
                    u(cubo)
                else:
                    l_linha(cubo, str_face)
            elif id==5:
                if local == -1:
                    u(cubo)
                elif local == 0:
                    u_linha(cubo)
                elif local == 2:
                    u(cubo)
                    u(cubo)
                else:
                    r(cubo, str_face)
            dicionario = mapear_meios(cubo)
            itera = iter(dicionario.items())
        except StopIteration:
            break
       


def passo_2(cubo:pd.DataFrame):
    dicionario = verifica_laranja_topo(cubo)
    
    while dicionario:
        index = dicionario[0]

        if index == 1:
            face = 'Y'
            centro_destino = cubo.loc[1 ,'Y'][0]
        elif index == 3:
            face = 'B'
            centro_destino = cubo.loc[1 ,'B'][0]
        elif index == 5:
            face = 'G'
            centro_destino = cubo.loc[1 ,'G'][0]
        elif index == 7:
            face = 'W'
            centro_destino = cubo.loc[1 ,'W'][0]
        direcao = verificar_centro(face, centro_destino)

        if direcao == 0:
            f(cubo, centro_destino)
            f(cubo, centro_destino)
        elif direcao == 1:
            u(cubo)
            f(cubo, centro_destino)
            f(cubo, centro_destino)
        elif direcao == 2:
            u(cubo)
            u(cubo)
            f(cubo, centro_destino)
            f(cubo, centro_destino)
        elif direcao == -1:
            u_linha(cubo)
            f(cubo, centro_destino)
            f(cubo, centro_destino)
      
        dicionario = verifica_laranja_topo(cubo)
        

def passo_3(cubo:pd.DataFrame):
    dicionario = mapear_quina(cubo)
    for face, indice in dicionario.items():
        str_face = str(face)
        if indice == []:
            continue
        id = int(indice[0])
        direcao = verificar_centro(str_face, cubo.loc[id , face][0])

        if str_face == 'R':
            direcao = mapear_quinas_opostas(cubo, id)
            if direcao == -1:
                u_linha(cubo)
            elif direcao == 1:
                u(cubo)
            elif direcao == 2:
                u(cubo)
                u(cubo)

            r(cubo, str_face)
            u(cubo)
            u(cubo)
            r_linha(cubo, str_face)
            dicionario = mapear_quina(cubo)        
        elif id < 4:
            if id == 0:            
                if direcao == -1:
                    u_linha(cubo)
                elif direcao == 1:
                    u(cubo)
                elif direcao == 2:
                    u(cubo)
                    u(cubo)
                else:
                    l_linha(cubo, str_face)
                    u(cubo)
                    l(cubo, str_face)
            else:
                if direcao == -1:
                    u_linha(cubo)
                elif direcao == 1:
                    u(cubo)
                elif direcao == 2:
                    u(cubo)
                    u(cubo)
                else:
                    r(cubo, str_face)
                    u_linha(cubo)
                    r_linha(cubo, str_face)
        elif id > 4:
            if direcao == -1:
                u_linha(cubo)
            elif direcao == 1:
                u(cubo)
            elif direcao == 2:
                u(cubo)
                u(cubo)
            else:
                r(cubo, str_face)
                u(cubo)
                u(cubo)
                r_linha(cubo, str_face)
        dicionario = mapear_quina(cubo)
        print(dicionario)
#houve movimento so errado

def passo_4():
    pass


def passo_5():
    pass


def passo_6():
    pass


def passo_7():
    pass


def passo_8():
    pass



# caso 6 é bem especifico então tenho q dar uma olhada legal nisso


teste(df)
print_custom_df(df)
print("Embaralhado\n\n")

passo_1(df)
print_custom_df(df)
print("Passo 1\n\n")

passo_2(df)
print_custom_df(df)
print("Passo 2\n\n")


passo_3(df)
print_custom_df(df)
print("Passo 3\n\n")
