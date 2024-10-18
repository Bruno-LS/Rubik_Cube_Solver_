from Rotacoes import *
import pandas as pd



def verifica_laranja_topo(cubo:pd.DataFrame):
    lista = []
    red = cubo['R'].values
    for j in range(1, len(red), 2):
        meio = red[j]
        if meio[0] == "O":
            lista.append(j)
  
    return lista
        

def verificar_centro(face_atual, cor):

    # retorna 0 para nenhum giro e se for movimento horario 1 para um giro e 2 para dois giros e se for anti-horario retorna -1
    faces={
        'B':(1),
        'W':(2),
        'G':(3),
        'Y':(4),
        'R':(5),
        'O':(6)
    }
    valor_atual = faces.get(face_atual)
    face_destino = faces.get(cor)

    direcao = valor_atual - face_destino
    if direcao == 1 or direcao == -3:
        return 1
    elif direcao == 2 or direcao == -2:
        return 2
    elif direcao > 2 or direcao == -1:
        return -1
    elif direcao == 0:
        return 0


def descobre_valor_por_centro(face:str):
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


def mapear_quina(cubo:pd.DataFrame):
    dicionario = {}
    for col in df.columns:
        if col not in ['O']:
            dicionario[col] = []
            for i in range(0, len(df), 2):
                if df.iloc[i, df.columns.get_loc(col)][0] == "O":
                    dicionario[col].append(i)
    
    adjacentes = mapear_adjacentes_quinas(dicionario)
    return adjacentes


def mapear_adjacentes_quinas(dicionario:dict):
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
    # verificar nos indices 3, 5 primeiro e depois no 'O' nos indices impares e depois nos indices 1 e 7 das faces W, G, Y, B
    dicionario = {}
    for col in df.columns:
        if col not in ['R', 'O']:
            dicionario[col] = []
            for i in range(1, len(df), 2):
                if df.iloc[i, df.columns.get_loc(col)][0] == "O":
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
    b(df, 'W')
    r(df, 'W')
    f_linha(df, 'W')
    d_linha(df)
    r(df, 'W')
    r(df, 'W')
    d(df)
    d(df)
    u_linha(df)
    r(df, 'W')
    r(df, 'W')
    d_linha(df)
    r_linha(df, 'W')
    b_linha(df, 'W')
    r_linha(df, 'W')
    d(df)
    d(df)
    r(df, 'W')
    l_linha(df, 'W')
    u_linha(df)
    b(df, 'W')
    l_linha(df, 'W')
    d(df)
    d(df)
    r_linha(df, 'W')
    l(df, 'W')
    d(df)
    d(df)
    b(df, 'W')
    b(df, 'W')
    l_linha(df, 'W')
    d_linha(df)


def mapear_quinas_opostas(cubo:pd.DataFrame, id:int):
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
    
    lista = []
    red = cubo['R'].values
    for j in range(1, len(red), 2):
        meio = red[j]
        if meio[0] == "R":
            lista.append(j)
    return lista
        

def movimentos_passo5(cubo:pd.DataFrame):
    f(cubo, 'W')
    r(cubo, 'W')
    u(cubo)
    r_linha(cubo, 'W')
    u_linha(cubo)
    f_linha(cubo, 'W')


def print_custom_cubo(df):
    # Separar as colunas por suas respectivas letras
    rows_R = df["R"].values.reshape(3, 3)
    rows_O = df["O"].values.reshape(3, 3)
    rows_b = df["B"].values.reshape(3, 3)
    rows_w = df["W"].values.reshape(3, 3)
    rows_g = df["G"].values.reshape(3, 3)
    rows_y = df["Y"].values.reshape(3, 3)

    rows_main = [list(b) + list(w) + list(g) + list(y) for b, w, g, y in zip(rows_b, rows_w, rows_g, rows_y)]

    # Exibindo as linhas de R, parte central e O
    for row in rows_R:
        print(f"         |{'|'.join(row)}|")
    for row in rows_main:
        print(f"|{'|'.join(row)}|")
    for row in rows_O:
        print(f"         |{'|'.join(row)}|")
