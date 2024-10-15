from Rotacoes import *
import pandas as pd
from Movimentos_fixos import df
from Auxiliares_passos import *

def passo_1(cubo:pd.DataFrame):#faltando 2u
    dicionario = mapear_meios(cubo)        
    
    i=0
    for face, indice in dicionario.items():
        str_face = str(face)
        if indice == []:
            continue
        id = int(indice[0])
        local = verificar_movimento(cubo, id, str_face)
        i+=1
        if id==7 or id == 1:
            f(cubo, face)
            dicionario = mapear_meios(cubo)
            continue  
        if id==3:
            if local == -1:
                u_linha(cubo)
            elif local == 0:
                u(cubo)
            else:
                l(cubo, face)
        if id==5:
            if local == -1:
                u(cubo, face)
            elif local == 0:
                u_linha(cubo)
            else:
                r(cubo, face)
        dicionario = mapear_meios(cubo)
    print(i)
        

def passo_2(cubo:pd.DataFrame):
    dicionario = verifica_laranja_topo(cubo)

    for id in dicionario:
        if id == 1:
            face = 'Y'
            centro_destino = cubo.loc[1 ,'Y'][0]
        elif id == 3:
            face = 'B'
            centro_destino = cubo.loc[1 ,'B'][0]
        elif id == 5:
            face = 'G'
            centro_destino = cubo.loc[1 ,'G'][0]
        elif id == 7:
            face = 'W'
            centro_destino = cubo.loc[1 ,'W'][0]
        direcao = verificar_centro(face, centro_destino)

        if direcao == 0:
            f(cubo, face)
            f(cubo, face)
        elif direcao == 1:
            u(cubo)
            f(cubo, face)
            f(cubo, face)
        elif direcao == 2:
            u(cubo)
            u(cubo)
            f(cubo, face)
            f(cubo, face)
        else:
            u_linha(cubo)
            f(cubo, face)
            f(cubo, face)
        

def passo_3(cubo:pd.DataFrame):#falta mapear os adjacentes, e saber como será a orientação
    dicionario = mapear_quina(cubo)
    
    for face, indice in dicionario.items():
        str_face = str(face)
        if indice == []:
            continue
        id = int(indice[0])
        direcao = verificar_centro(str_face, cubo.loc[id , face][0])

        if str_face == 'R':
            #mapear local da quina na face laranja
            r(cubo, face)
            u(cubo)
            u(cubo)
            r_linha(cubo, face)
            continue  
        if id < 4:
            if id == 0:            
                if direcao == -1:
                    u_linha(cubo)
                elif direcao == 1:
                    u(cubo)
                elif direcao == 2:
                    u(cubo)
                    u(cubo)
                else:
                    l_linha(cubo, face)
                    u(cubo)
                    l(cubo, face)
            else:
                if direcao == -1:
                    u_linha(cubo)
                elif direcao == 1:
                    u(cubo)
                elif direcao == 2:
                    u(cubo)
                    u(cubo)
                else:
                    r(cubo, face)
                    u_linha(cubo)
                    r_linha(cubo, face)
        if id > 4:
            if direcao == -1:
                u_linha(cubo)
            elif direcao == 1:
                u(cubo)
            elif direcao == 2:
                u(cubo)
                u(cubo)
            else:
                r(cubo, face)
                u(cubo)
                u(cubo)
                r_linha(cubo, face)
        dicionario = mapear_quina(cubo)


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




print("\n\n")
print_custom_df(df)
