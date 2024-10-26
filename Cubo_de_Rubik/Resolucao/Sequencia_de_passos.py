from .Estrutura_cubo import df as cubo
from .Auxiliares_passos import *


def passo_1(cubo:pd.DataFrame):
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
                itera = iter(dicionario.items())
                continue

            elif id==3:
                if local == -1:
                    u_linha(cubo)
                elif local == 0:
                    u(cubo)
                elif local == 2:
                    u(cubo)
                    u(cubo)
                
                l_linha(cubo, str_face)
            elif id==5:
                if local == -1:
                    u(cubo)
                elif local == 0:
                    u_linha(cubo)
                elif local == 2:
                    u(cubo)
                    u(cubo)
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
    adjacentes = mapear_adjacentes_quinas(dicionario) 
    itera = iter(adjacentes.items())
    while adjacentes:
        try:
            face, indice = next(itera)
            str_face = str(face)
            if indice == []:
                continue
            id = int(indice[0])    
            direcao = verificar_centro(str_face, cubo.loc[id , face][0])
            localizacao = cubo.loc[id , face][0]

            if str_face == 'R':
                direcao_topo = mapear_quinas_opostas_vertical(cubo, id)
                girar_u(direcao_topo, cubo)

                r(cubo, localizacao)
                u(cubo)
                u(cubo)
                r_linha(cubo, localizacao)        
            
            elif id < 4 and str_face !='R':
                if id == 0:            
                    girar_u(direcao, cubo)

                    l_linha(cubo, localizacao)
                    u_linha(cubo)
                    l(cubo, localizacao)
                elif id == 2:
                    girar_u(direcao, cubo)
                        
                    r(cubo, localizacao)                                       
                    u(cubo)                   
                    r_linha(cubo, localizacao)

            elif id > 4 and str_face !='R':
                if id == 6:
                    girar_d(direcao, cubo)
                    
                    f(cubo, localizacao)
                    u(cubo)
                    u(cubo)
                    f_linha(cubo, localizacao)
                elif id == 8:
                    girar_d(direcao, cubo)
                    
                    r(cubo, localizacao)
                    u(cubo)
                    u(cubo)
                    r_linha(cubo, localizacao)

            dicionario = mapear_quina(cubo)
            adjacentes = mapear_adjacentes_quinas(dicionario)
            itera = iter(adjacentes.items())
        except StopIteration:
            break
    if verifica_primeira_camada(cubo) != False:
        piece = verifica_primeira_camada(cubo)
        for face, indice in piece:
            if indice == 6:
                l_linha(cubo, face)
                u_linha(cubo)
                l(cubo, face)
            elif indice == 8:
                r(cubo, face)                                       
                u(cubo)                   
                r_linha(cubo, face)
        passo_3(cubo)
           

def passo_4(cubo:pd.DataFrame):
    dicionario = auxiliar_passo4(cubo)
    # itera = iter(dicionario.items())
    if dicionario != False:
        while dicionario:
            try:
                itera = iter(dicionario.items())
                face_atual, face_destino = next(itera)
                str_face_atual = str(face_atual)
                str_face_destino = str(face_destino)

                direcao = verificar_centro(str_face_atual, str_face_destino)

                girar_u(direcao, cubo)

                lado = verifica_adjacente_meio(cubo, str_face_destino)
                if lado == 0:#Esquerda
                    u_linha(cubo)
                    l_linha(cubo, str_face_destino)
                    u(cubo)
                    l(cubo, str_face_destino)
                    u(cubo)
                    f(cubo, str_face_destino)
                    u_linha(cubo)
                    f_linha(cubo, str_face_destino)
                elif lado == 1:#Direita
                    u(cubo)
                    r(cubo, str_face_destino)
                    u_linha(cubo)
                    r_linha(cubo, str_face_destino)
                    u_linha(cubo)
                    f_linha(cubo, str_face_destino)
                    u(cubo)
                    f(cubo, str_face_destino)
                
                dicionario = auxiliar_passo4(cubo)
            except StopIteration:
                break
    else:
        piece = verificar_segunda_camada(cubo)
        if piece != False:
            face, lado = piece
            
            if lado == 3:#Esquerda
                u_linha(cubo)
                l_linha(cubo, face)
                u(cubo)
                l(cubo, face)
                u(cubo)
                f(cubo, face)
                u_linha(cubo)
                f_linha(cubo, face)
            elif lado == 5:#Direita
                u(cubo)
                r(cubo, face)
                u_linha(cubo)
                r_linha(cubo, face)
                u_linha(cubo)
                f_linha(cubo, face)
                u(cubo)
                f(cubo, face)
            passo_4(cubo)


def passo_5(cubo:pd.DataFrame):
    
    vermelhos = contar_vermelhos(cubo)
    if len(vermelhos) == 3 and [3, 5] in vermelhos:    
      movimentos_passo5(cubo)
    elif len(vermelhos) == 3 and [3, 5] not in vermelhos:
        u(cubo)
        movimentos_passo5(cubo)

    elif len(vermelhos) == 2 and (1 in vermelhos and 3 in vermelhos):
        movimentos_passo5(cubo)
        passo_5(cubo)

    elif len(vermelhos) == 2 and (1 in vermelhos and 5 in vermelhos):
        u_linha(cubo)
        movimentos_passo5(cubo)
        passo_5(cubo)

    elif len(vermelhos) == 2 and (5 in vermelhos and 7 in vermelhos):
        u_linha(cubo)
        u_linha(cubo)
        movimentos_passo5(cubo)
        passo_5(cubo)

    elif len(vermelhos) == 2 and (3 in vermelhos and 7 in vermelhos):
        u(cubo)
        movimentos_passo5(cubo)
        passo_5(cubo)

    elif len(vermelhos) == 0 or vermelhos == []:
        movimentos_passo5(cubo)
        passo_5(cubo)

 
def passo_6(cubo:pd.DataFrame):
    vermelhos = contar_vermelhos(cubo)
    quinas_iguais = procurar_quinas_iguais(cubo, 'R')
    faces_horizontais = [item for item in cubo.columns if item not in ['R', 'O']]

    diferenca = list(set(faces_horizontais) - set(quinas_iguais))
    if len(vermelhos) == 1:#casos: 6 e 7
        dicionario = procurar_Peca(cubo, 'R')
        
        if all(all(v == 2 for v in valor) for valor in dicionario.values()):#caso 7
            
            if vermelhos[0] == 6:
                movimentos_passo6(cubo, 'W')

            elif vermelhos[0] == 8:
                u(cubo)
                movimentos_passo6(cubo, 'W')

            elif vermelhos[0] == 2:
                u(cubo)
                u(cubo)
                movimentos_passo6(cubo, 'W')

            elif vermelhos[0] == 0:
                u_linha(cubo)
                movimentos_passo6(cubo, 'W')

        elif all(all(v == 0 for v in valor) for valor in dicionario.values()):#caso 6
            
            if vermelhos[0] == 6:
                movimentos_passo6(cubo, 'W')
                passo_6(cubo)

            elif vermelhos[0] == 8:
                u(cubo)
                movimentos_passo6(cubo, 'W')
                passo_6(cubo)

            elif vermelhos[0] == 2:
                u(cubo)
                u(cubo)
                movimentos_passo6(cubo, 'W')
                passo_6(cubo)

            elif vermelhos[0] == 0:
                u_linha(cubo)
                movimentos_passo6(cubo, 'W')
                passo_6(cubo)

    elif len(vermelhos) == 0 or vermelhos == []:#casos: 4 e 5
        if len(quinas_iguais) == 2:#caso 4
            
            movimentos_passo6(cubo, diferenca[0])
            passo_6(cubo)

        elif len(quinas_iguais) == 1:#caso 5
            
            face = Orientar_Face_Direita(quinas_iguais[0])
            movimentos_passo6(cubo, face)
            passo_6(cubo)

    elif len(vermelhos) == 2:#casos: 1, 2 e 3
        if len(quinas_iguais) == 1:
            
            movimentos_passo6(cubo, quinas_iguais[0])
            passo_6(cubo)

        elif len(quinas_iguais) == 0 or quinas_iguais == []:
            localizacao = mapear_quina(cubo, 'R')
            chaves = list(localizacao.keys())
           
            if verificar_centro(chaves[0], chaves[1]) == 2 and localizacao[chaves[0]] - localizacao[chaves[1]] in [-1, 1]:#caso 2
                
                if localizacao[chaves[0]] == 0:
                    movimentos_passo6(cubo, chaves[0])
                    passo_6(cubo)
                    
                elif localizacao[chaves[0]] == 2:
                    movimentos_passo6(cubo, chaves[1])
                    passo_6(cubo)

            else: #Caso 1: dois opostos pela diagonal
                
                if verificar_centro(chaves[0], chaves[1]) == -1:
                    movimentos_passo6(cubo, chaves[0])
                    passo_6(cubo)
                    
                elif verificar_centro(chaves[1], chaves[0]) == -1:
                    movimentos_passo6(cubo, chaves[1])
                    passo_6(cubo)


def passo_7(cubo:pd.DataFrame):
    quinas = procurar_quinas_iguais(cubo, ['W', 'G', 'B', 'Y'])

    if len(quinas) >= 1:
        face = quinas[0]
        r(cubo, face)
        b_linha(cubo, face)
        r(cubo, face)
        f(cubo, face)
        f(cubo, face)
        r_linha(cubo, face)
        b(cubo, face)
        r(cubo, face)
        f(cubo, face)
        f(cubo, face)
        r(cubo, face)
        r(cubo, face)
    elif len(quinas) == 0 or quinas == []:
        face = 'W'
        r(cubo, face)
        b_linha(cubo, face)
        r(cubo, face)
        f(cubo, face)
        f(cubo, face)
        r_linha(cubo, face)
        b(cubo, face)
        r(cubo, face)
        f(cubo, face)
        f(cubo, face)
        r(cubo, face)
        r(cubo, face)
        passo_7(cubo)


def passo_8(cubo:pd.DataFrame):
    #mover terceira camada para os devidos centros com base no indice 0
    direcao = verificar_centro('W', cubo.iloc[0, cubo.columns.get_loc('W')][0])
    if direcao == -1:
        u_linha(cubo)
    elif direcao == 1:
        u(cubo)
    elif direcao == 2:
        u(cubo)
        u(cubo)
 
    face_traseira = verificar_terceira_camada(cubo)
    
    if verifica_primeira_camada(cubo) == False and verificar_segunda_camada(cubo) == False and face_traseira != False:
        face = Face_oposta(face_traseira)
        face_cm_peca = procurar_meio_superior(cubo, face)

        f(cubo, face)
        f(cubo, face)
        movimentos_passo8(cubo, face, verificar_centro(face_cm_peca, face))
    else:
        face = 'W'
        f(cubo, face)
        f(cubo, face)
        face_cm_peca = procurar_meio_superior(cubo, face)

        movimentos_passo8(cubo, face, verificar_centro(face_cm_peca, face))
        passo_8(cubo)




# teste(cubo)
# print_custom_cubo(cubo)
# print("Embaralhado\n\n")

# passo_1(cubo)
# print_custom_cubo(cubo)
# print("Passo 1\n\n")

# passo_2(cubo)
# print_custom_cubo(cubo)
# print("Passo 2\n\n")


# passo_3(cubo)
# print_custom_cubo(cubo)
# print("Passo 3\n\n")


# passo_4(cubo)
# print_custom_cubo(cubo)
# print("Passo 4\n\n")

# passo_5(cubo)
# print_custom_cubo(cubo)
# print("Passo 5\n\n")

# passo_6(cubo)
# print_custom_cubo(cubo)
# print("Passo 6\n\n")

# passo_7(cubo)
# print_custom_cubo(cubo)
# print("Passo 7\n\n")

# passo_8(cubo)
# print_custom_cubo(cubo)
# print("Passo 8\n\n")


