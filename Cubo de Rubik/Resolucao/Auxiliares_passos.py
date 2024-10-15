from Rotacoes import *
import pandas as pd



def verifica_laranja_topo(cubo:pd.DataFrame):
    dicionario = []
    i = 1
    red = cubo['R'].values
    for j in range(i, len(red), 2):
        meio = red[j]
        if meio[0] == "O":
            dicionario.append(i)
        i += 2
    return dicionario
        

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
    face_destino = faces.get(cor)
    valor_atual = faces.get(face_atual)

    direcao = valor_atual - face_destino
    if direcao == 1:
        return 1
    elif direcao == 2:
        return 2
    elif direcao > 2 or direcao < 0:
        return -1
    elif direcao == 0:
        return 0


def mapear_quina(cubo:pd.DataFrame):
    dicionario = {}
    for col in df.columns:
        if col not in ['O']:
            dicionario[col] = []
            for i in range(0, len(df), 2):
                if df.iloc[i, df.columns.get_loc(col)][0] == "O":
                    dicionario[col].append(i)
    
    return dicionario


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


def verificar_quinas(cubo:pd.DataFrame):#Inacabada
    pass


def verificar_movimento(cubo:pd.DataFrame, id:int, face:str):
    if id == 3:
        if face == 'Y' and cubo.loc[5, 'R'][0] == "O":
            if cubo.loc[1, 'R'][0] == "O":
                return -1
            return 0
        elif face == 'B' and cubo.loc[1, 'R'][0] == "O":
            if cubo.loc[3, 'R'][0] == "O":
                return -1
            return 0
        elif face == 'G' and cubo.loc[7, 'R'][0] == "O":
            if cubo.loc[5, 'R'][0] == "O":
                return -1
            return 0
        elif face == 'W' and cubo.loc[3, 'R'][0] == "O":
            if cubo.loc[7, 'R'][0] == "O":
                return -1
            return 0
        return 1
    
    if id == 5:
        if face == 'Y' and cubo.loc[3, 'R'][0] == "O":
            if cubo.loc[1, 'R'][0] == "O":
                return -1
            return 0
        elif face == 'B' and cubo.loc[7, 'R'][0] == "O":
            if cubo.loc[3, 'R'][0] == "O":
                return -1
            return 0
        elif face == 'G' and cubo.loc[1, 'R'][0] == "O":
            if cubo.loc[5, 'R'][0] == "O":
                return -1
            return 0
        elif face == 'W' and cubo.loc[5, 'R'][0] == "O":
            if cubo.loc[7, 'R'][0] == "O":
                return -1
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

