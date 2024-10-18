from Movimentos import *
import pandas as pd



def verifica_laranja_topo(cubo:pd.DataFrame):
    """
        Verifica quais meios da face Vermelha são laranjas, Retorna seu Index
    """
    lista = []
    red = cubo['R'].values
    for j in range(1, len(red), 2):
        meio = red[j]
        if meio[0] == "O":
            lista.append(j)
  
    return lista
        

def verificar_centro(face_atual, face_destino):

    """
       Recebe a face atual da peça e a face para a qual a peça precisa se locomover.
       Retorna 0 para nenhum giro, se for movimento horario: 1 para um giro e 2 para dois giros, se for anti-horario: retorna -1
    """
    faces={
        'B':(1),
        'W':(2),
        'G':(3),
        'Y':(4),
        'R':(5),
        'O':(6)
    }
    Centro_atual = faces.get(face_atual)
    Centro_destino = faces.get(face_destino)

    direcao = Centro_atual - Centro_destino
    if direcao == 1 or direcao == -3:
        return 1
    elif direcao == 2 or direcao == -2:
        return 2
    elif direcao > 2 or direcao == -1:
        return -1
    elif direcao == 0:
        return 0


def descobre_valor_por_centro(face:str):
    """
        Recebe um str entre [B, W, G, Y, R, O] e retorna O número que representa esta face.
    """
    faces={
        'B':(1),
        'W':(2),
        'G':(3),
        'Y':(4),
        'R':(5),
        'O':(6)
    }
    centro = faces.get(face)
    return centro


def descobre_centro_por_valor(id:int):
    """
        Recebe um int entre [1, 2, 3, 4, 5, 6] e retorna a face que este número representa.
    """
    faces={
        (1):'B',
        (2):'W',
        (3):'G',
        (4):'Y',
        (5):'R',
        (6):'O'
    }
    centro = faces.get(id)
    return centro


def mapear_quina(cubo:pd.DataFrame, cor='O'):
    """
        Localiza a {Face:index} das quinas de determinada "cor" = default: 'O'.
    """
    dicionario = {}
    for col in cubo.columns:
        if col not in ['O']:
            dicionario[col] = []
            for i in range(0, len(cubo), 2):
                if cubo.iloc[i, cubo.columns.get_loc(col)][0] == cor:
                    dicionario[col].append(i)
    
    return dicionario


def mapear_adjacentes_quinas(dicionario:dict):
    """
        Localiza a {Face:Index} dos adjacentes laterais das quinas no cubo.
        Adjacente Lateral: Todo adjacente que não estiver tanto no topo quanto na base do cubo.
    """
    adjacentes = {}
    for face, indice in dicionario.items():
        if indice == []:
                continue
        str_face = str(face)    
        for id in indice:
            if str_face != 'R':

                local = descobre_valor_por_centro(str_face)
                if id == 0:
                    if local - 1 < 1:
                        local+=5
                    face_anterior = descobre_centro_por_valor(local-1)
                    if face_anterior not in adjacentes:
                        adjacentes[face_anterior] = []
                    adjacentes[face_anterior].append(2)            
                elif id == 6:
                    if local - 1 < 1:
                        local+=5
                    face_anterior = descobre_centro_por_valor(local-1)
                    if face_anterior not in adjacentes:
                        adjacentes[face_anterior] = []
                    adjacentes[face_anterior].append(8)            
                elif id == 2:
                    if local + 1 > 4:
                        local-=4
                    face_anterior = descobre_centro_por_valor(local+1)
                    if face_anterior not in adjacentes:
                        adjacentes[face_anterior] = []
                    adjacentes[face_anterior].append(0)            
                elif id == 8:
                    if local + 1 > 4:
                        local-=4
                    face_anterior = descobre_centro_por_valor(local+1)
                    if face_anterior not in adjacentes:
                        adjacentes[face_anterior] = []
                    adjacentes[face_anterior].append(6)
            else:
                adjacentes[str_face] = []
                for i in dicionario.get(str_face):
                    adjacentes[str_face].append(i)
    return adjacentes
            

def mapear_meios(cubo:pd.DataFrame):
    """
        Verificar nos indices 3, 5 primeiro e depois na face O nos indices impares e depois nos indices 1 e 7 das faces W, G, Y, B.
    """
    dicionario = {}
    for col in cubo.columns:
        if col not in ['R', 'O']:
            dicionario[col] = []
            for i in range(1, len(cubo), 2):
                if cubo.iloc[i, cubo.columns.get_loc(col)][0] == "O":
                    dicionario[col].append(i)
    
    return dicionario


def verificar_movimento(cubo:pd.DataFrame, id:int, face:str):
    if id == 3:
        if face == 'Y' and cubo.loc[5, 'R'][0] == "O":
            if cubo.loc[1, 'R'][0] == "O":
                return -1
            elif cubo.loc[7, 'R'][0] == "O":
                return 2
            return 0
        elif face == 'B' and cubo.loc[1, 'R'][0] == "O":
            if cubo.loc[3, 'R'][0] == "O":
                return -1
            elif cubo.loc[5, 'R'][0] == "O":
                return 2
            return 0
        elif face == 'G' and cubo.loc[7, 'R'][0] == "O":
            if cubo.loc[5, 'R'][0] == "O":
                return -1
            elif cubo.loc[3, 'R'][0] == "O":
                return 2
            return 0
        elif face == 'W' and cubo.loc[3, 'R'][0] == "O":
            if cubo.loc[7, 'R'][0] == "O":
                return -1
            elif cubo.loc[1, 'R'][0] == "O":
                return 2
            return 0
        return 1
    
    if id == 5:
        if face == 'Y' and cubo.loc[3, 'R'][0] == "O":
            if cubo.loc[1, 'R'][0] == "O":
                return -1
            elif cubo.loc[7, 'R'][0] == "O":
                return 2
            return 0
        elif face == 'B' and cubo.loc[7, 'R'][0] == "O":
            if cubo.loc[3, 'R'][0] == "O":
                return -1
            elif cubo.loc[5, 'R'][0] == "O":
                return 2
            return 0
        elif face == 'G' and cubo.loc[1, 'R'][0] == "O":
            if cubo.loc[5, 'R'][0] == "O":
                return -1
            elif cubo.loc[3, 'R'][0] == "O":
                return 2
            return 0
        elif face == 'W' and cubo.loc[5, 'R'][0] == "O":
            if cubo.loc[7, 'R'][0] == "O":
                return -1
            elif cubo.loc[1, 'R'][0] == "O":
                return 2
            return 0
        return 1 


def teste(cubo:pd.DataFrame):
    b(cubo, 'W')
    r(cubo, 'W')
    f_linha(cubo, 'W')
    d_linha(cubo)
    r(cubo, 'W')
    r(cubo, 'W')
    d(cubo)
    d(cubo)
    u_linha(cubo)
    r(cubo, 'W')
    r(cubo, 'W')
    d_linha(cubo)
    r_linha(cubo, 'W')
    b_linha(cubo, 'W')
    r_linha(cubo, 'W')
    d(cubo)
    d(cubo)
    r(cubo, 'W')
    l_linha(cubo, 'W')
    u_linha(cubo)
    b(cubo, 'W')
    l_linha(cubo, 'W')
    d(cubo)
    d(cubo)
    r_linha(cubo, 'W')
    l(cubo, 'W')
    d(cubo)
    d(cubo)
    b(cubo, 'W')
    b(cubo, 'W')
    l_linha(cubo, 'W')
    d_linha(cubo)


def mapear_quinas_opostas(cubo:pd.DataFrame, id:int):
    """
        Recebe o indice de uma quina laranja na face Vermelha e mapeia se a quina espacialmente oposta à ela na face laranja é ou não laranja também.
    """
    if id == 0:
        if cubo.loc[6, 'O'][0] != 'O':
            return 0
        elif cubo.loc[8, 'O'][0] != 'O':         
            return 1
        elif cubo.loc[2, 'O'][0] != 'O':
            return 2
        elif cubo.loc[0, 'O'][0] != 'O':
            return -1
    
    elif id == 2:
        if cubo.loc[8, 'O'][0] != 'O':
            return 0
        elif cubo.loc[2, 'O'][0] != 'O':         
            return 1
        elif cubo.loc[0, 'O'][0] != 'O':
            return 2
        elif cubo.loc[6, 'O'][0] != 'O':
            return -1
    
    elif id == 6:
        if cubo.loc[0, 'O'][0] != 'O':
            return 0
        elif cubo.loc[6, 'O'][0] != 'O':         
            return 1
        elif cubo.loc[8, 'O'][0] != 'O':
            return 2
        elif cubo.loc[2, 'O'][0] != 'O':
            return -1
    
    elif id == 8:
        if cubo.loc[2, 'O'][0] != 'O':
            return 0
        elif cubo.loc[0, 'O'][0] != 'O':         
            return 1
        elif cubo.loc[6, 'O'][0] != 'O':
            return 2
        elif cubo.loc[8, 'O'][0] != 'O':
            return -1


def verifica_primeira_camada(cubo:pd.DataFrame):
    for col in cubo.columns:
        if col not in ['R', 'O']:
            for i in range(6, len(cubo), 1):
                if cubo.iloc[i, cubo.columns.get_loc(col)][0] != col:
                    return [(col, i)]
    return False


def auxiliar_passo4(cubo:pd.DataFrame):
    for col in cubo.columns:
        if col not in ['R', 'O']:
            meio = cubo.iloc[1, cubo.columns.get_loc(col)]
            if meio not in ['W2', 'B2', 'G2', 'Y2', 'R2', 'R4', 'R6', 'R8']:
                return {col: meio[0]}
            else:
                continue
    return False


def verifica_adjacente_meio(cubo:pd.DataFrame, face:str):
    if face == 'W':
        if cubo.iloc[7, df.columns.get_loc('R')][0] == 'B':
            return 0
        elif cubo.iloc[7, df.columns.get_loc('R')][0] == 'G':
            return 1
    elif face == 'B':
        if cubo.iloc[3, df.columns.get_loc('R')][0] == 'Y':
            return 0
        elif cubo.iloc[3, df.columns.get_loc('R')][0] == 'W':
            return 1
    elif face == 'Y':
        if cubo.iloc[1, df.columns.get_loc('R')][0] == 'G':
            return 0
        elif cubo.iloc[1, df.columns.get_loc('R')][0] == 'B':
            return 1
    elif face == 'G':
        if cubo.iloc[5, df.columns.get_loc('R')][0] == 'W':
            return 0
        elif cubo.iloc[5, df.columns.get_loc('R')][0] == 'Y':
            return 1
    

def verificar_segunda_camada(cubo:pd.DataFrame):
    for col in cubo.columns:
        if col not in ['R', 'O']:
            for i in range(3, 6, 2):
                if cubo.iloc[i, cubo.columns.get_loc(col)][0] != col:
                    return [(col, i)]
    return False
    

def contar_vermelhos(cubo:pd.DataFrame):
    """
        Contar quantas quinas vermelhas estão na face vermelha
    """
    lista = []
    red = cubo['R'].values
    for j in range(0, len(red), 2):
        if j != 4:
            meio = red[j]
            if meio[0] == "R":
                lista.append(j)
    return lista
        

def print_custom_cubo(cubo):
    # Separar as colunas por suas respectivas letras
    rows_R = cubo["R"].values.reshape(3, 3)
    rows_O = cubo["O"].values.reshape(3, 3)
    rows_b = cubo["B"].values.reshape(3, 3)
    rows_w = cubo["W"].values.reshape(3, 3)
    rows_g = cubo["G"].values.reshape(3, 3)
    rows_y = cubo["Y"].values.reshape(3, 3)

    rows_main = [list(b) + list(w) + list(g) + list(y) for b, w, g, y in zip(rows_b, rows_w, rows_g, rows_y)]

    # Exibindo as linhas de R, parte central e O
    for row in rows_R:
        print(f"         |{'|'.join(row)}|")
    for row in rows_main:
        print(f"|{'|'.join(row)}|")
    for row in rows_O:
        print(f"         |{'|'.join(row)}|")


def procurar_quinas_iguais(cubo:pd.DataFrame, cor):
    """
        Retorna as faces do cubo em que há duas quinas superiores iguais
    """
    face = []
    for col in cubo.columns:
        if col not in ['R', 'O']:
            for piece in cor:
                if cubo.iloc[0, cubo.columns.get_loc(col)][0] == piece  and cubo.iloc[2, cubo.columns.get_loc(col)][0] == piece:
                    face.append(col)  
    
    return face 
    

def Orientar_Face_Direita(face):
    if face == 'W':
        face_orientada = 'B'
    elif face == 'G':
        face_orientada = 'W'
    elif face == 'Y':
        face_orientada = 'G'
    elif face == 'B':
        face_orientada = 'Y'

    return face_orientada


def Orientar_Face_Esquerda(face):
    if face == 'W':
        face_orientada = 'G'
    elif face == 'G':
        face_orientada = 'Y'
    elif face == 'Y':
        face_orientada = 'B'
    elif face == 'B':
        face_orientada = 'W'

    return face_orientada    


def verificar_terceira_camada(cubo:pd.DataFrame, cor):
    """
        Verifica a primeira linha/terceira camada de todas as faces horizontais e retorna as que possuirem peças da cor selecionada.
    """
    dicionario = {}
    for col in cubo.columns:
            if col not in ['R', 'O']:
                dicionario[col] = []
                for i in range(0, 3, 1):
                    if cubo.iloc[i, cubo.columns.get_loc(col)][0] == cor:
                        dicionario[col].append(i)
    return dicionario

#Ideia: Criar uma função que receba a localização de duas peças:{Face:index} e o lado, em relação a face Branca, e determine se estão na mesma coluna de giro(lado)
#Ideia: Função para determinar se duas peças são opostas 