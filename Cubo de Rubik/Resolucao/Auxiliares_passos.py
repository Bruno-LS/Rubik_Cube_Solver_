from Movimentacoes.Movimentos import *
import pandas as pd



def verifica_laranja_topo(cubo:pd.DataFrame):
    """
        Verifica quais meios da face Vermelha são laranjas, Retorna seu Index
    """
    lista = []
    red = cubo['R'].values
    for j in range(1, len(red), 2):
        if red[j][0] == "O":
            lista.append(j)
  
    return lista
        

def verificar_centro(face_atual, face_destino):

    """
       Recebe a face atual da peça e a face para a qual a peça precisa se locomover.
       Retorna:
        0 nenhum giro;
        1 um giro;
        2 dois giros; 
        -1 giro anti-horario.
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


def verifica_adjacente_meio(cubo:pd.DataFrame, face:str):
    """
        Verifica se o adjacente do meio superior da face oferecida é da face adjacente esquerda ou direita
        0: Esquerda
        1: Direita 
    """
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
 

def verifica_primeira_camada(cubo:pd.DataFrame):
    """
        Verifica se na primeira camada todas as peças são da cor do centro, ou seja, verifica se as peças estão no devido lugar, retorna a Coluna:Index da peça errada
    """
    for col in ['W', 'G', 'B', 'Y']:
        for i in range(6, len(cubo), 1):
            if cubo.iloc[i, cubo.columns.get_loc(col)][0] != col:
                return [(col, i)]
    return False


def verificar_segunda_camada(cubo:pd.DataFrame):
    """
        Verifica se na segunda camada todas as peças são da cor do centro, ou seja, verifica se as peças estão no devido lugar, retorna a Coluna:Index da peça errada
    """
    for col in ['W', 'G', 'B', 'Y']:
        for i in range(3, 6, 2):
            if cubo.iloc[i, cubo.columns.get_loc(col)][0] != col:
                return [(col, i)]
    return False


def verificar_terceira_camada(cubo:pd.DataFrame):
    """
        Verifica se todos as peças da primeira linha são iguais e pertencentes ao centro em questão e retorna o centro
    """
    for col in ['W', 'G', 'B', 'Y']:
        if cubo.iloc[0, cubo.columns.get_loc(col)][0] == col and cubo.iloc[1, cubo.columns.get_loc(col)][0] == col and cubo.iloc[2, cubo.columns.get_loc(col)][0] == col:
            return col
    return False


def verificar_movimento(cubo:pd.DataFrame, id:int, face:str):
    #poderá ser trocada pela função de "procurar peças no 'lado'"
    """
        Verifica se na face vermelha no movimento de L' ou R de uma peça laranja nas faces horizontais, há alguma peça laranja na mesma linha e retorna o movimento de giro nescessário 
    """
    if id == 3:
        if face == 'Y' and cubo.loc[5, 'R'][0] == "O":
            if cubo.loc[1, 'R'][0] == "O":
                if cubo.loc[7, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        elif face == 'B' and cubo.loc[1, 'R'][0] == "O":
            if cubo.loc[3, 'R'][0] == "O":
                if cubo.loc[5, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        elif face == 'G' and cubo.loc[7, 'R'][0] == "O":
            if cubo.loc[5, 'R'][0] == "O":
                if cubo.loc[3, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        elif face == 'W' and cubo.loc[3, 'R'][0] == "O":
            if cubo.loc[7, 'R'][0] == "O":
                if cubo.loc[1, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        return 1
    
    if id == 5:
        if face == 'Y' and cubo.loc[3, 'R'][0] == "O":
            if cubo.loc[1, 'R'][0] == "O":
                if cubo.loc[7, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        elif face == 'B' and cubo.loc[7, 'R'][0] == "O":
            if cubo.loc[3, 'R'][0] == "O":
                if cubo.loc[5, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        elif face == 'G' and cubo.loc[1, 'R'][0] == "O":
            if cubo.loc[5, 'R'][0] == "O":
                if cubo.loc[3, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        elif face == 'W' and cubo.loc[5, 'R'][0] == "O":
            if cubo.loc[7, 'R'][0] == "O":
                if cubo.loc[1, 'R'][0] == "O":
                    return 2
                return -1
            return 0
        return 1


def descobre_valor_por_centro(face:str):
    """
        Recebe um str entre [B, W, G, Y, R, O] e retorna o número que representa esta face.
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
        Localiza a {Face:index} das quinas de determinada Cor.
    """
    dicionario = {}
    for col in ['W', 'R', 'G', 'B', 'Y']:
        dicionario[col] = []
        for i in range(0, len(cubo), 2):
            
            if cubo.iloc[i, cubo.columns.get_loc(col)][0] == cor:
                dicionario[col].append(i)
    
    return dicionario


def mapear_adjacentes_quinas(dicionario:dict):
    """
        Localiza a {Face:Index} dos adjacentes laterais e do topo das quinas no cubo.
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
        Verifica dos meios das faces laterais quais possuem a cor laranja
    """
    dicionario = {}
    for col in ['W', 'G', 'B', 'Y']:
        dicionario[col] = []
        for i in range(1, len(cubo), 2):
            if cubo.iloc[i, cubo.columns.get_loc(col)][0] == "O":
                dicionario[col].append(i)
    
    return dicionario


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


def mapear_quinas_opostas_vertical(cubo:pd.DataFrame, id:int):
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


def auxiliar_passo4(cubo:pd.DataFrame):
    """
        Verifica se algum dos meios superiores das faces laterais, possui um adjacente vermelho em cima e retorna a coluna: face, desta peça
    """
    for col in ['W', 'G', 'B', 'Y']:
        meio = cubo.iloc[1, cubo.columns.get_loc(col)]
        if meio not in ['W2', 'B2', 'G2', 'Y2', 'R2', 'R4', 'R6', 'R8']:
            return {col: meio[0]}
        else:
            continue
    return False
       

def contar_vermelhos(cubo:pd.DataFrame):
    """
        Conta quantas quinas vermelhas estão na face vermelha
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
    """
        Printa o dataframe do cubo, num formato planificado do tipo
         R
        B W G Y
         O
    """
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
    for piece in cor:
        for col in ['W', 'G', 'B', 'Y']:
            if cubo.iloc[0, cubo.columns.get_loc(col)][0] == piece  and cubo.iloc[2, cubo.columns.get_loc(col)][0] == piece:
                face.append(col)  
    
    return face 
    

def Orientar_Face_Direita(face):
    """
        Recebe uma face e retorna a face que vista de frente faça com que a primeira fique disposta à sua direita
    """
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
    """
        Recebe uma face e retorna a face que vista de frente faça com que a primeira fique disposta à sua esquerda
    """
    if face == 'W':
        face_orientada = 'G'
    elif face == 'G':
        face_orientada = 'Y'
    elif face == 'Y':
        face_orientada = 'B'
    elif face == 'B':
        face_orientada = 'W'

    return face_orientada    


def procurar_Peca(cubo:pd.DataFrame, cor):
    """
        Verifica a primeira linha/terceira camada de todas as faces horizontais e retorna as que possuirem peças da cor selecionada.
    """
    dicionario = {}
    for col in ['W', 'G', 'B', 'Y']:
        for i in range(0, 3, 1):
            if cubo.iloc[i, cubo.columns.get_loc(col)][0] == cor:
                dicionario[col] = []    
                dicionario[col].append(i)
    return dicionario
    

def Face_oposta(face):
    """
        Recebe uma face e retorna sua oposta
    """
    mapa = {'W': 'Y', 'B': 'G', 'R': 'O', 'Y': 'W', 'G': 'B', 'O': 'R'}
    return mapa.get(face)


def leitura(lista, cubo:pd.DataFrame):
    """
        Lê uma lista de movimentos com a seguinte estrutura 'Movimento':'Face' e executa os movimentos da lista
    """
    rotacao = {
        'r' :r,
        'r_':r_linha, 
        'l':l,
        'l_':l_linha,
        'f':f,
        'f_':f_linha,
        'b':b,
        'b_':b_linha,
        'd':d,
        'd_':d_linha,
        'u':u,
        'u_':u_linha
    }
    for movimento_face in lista:
       face = movimento_face[2]
       movimento = movimento_face[0]
       rotacao[movimento](cubo, face)


def girar_u(direcao, cubo:pd.DataFrame):
    if direcao == -1:
        u_linha(cubo)
    elif direcao == 1:
        u(cubo)
    elif direcao == 2:
        u(cubo)
        u(cubo)


def girar_d(direcao, cubo:pd.DataFrame):
    if direcao == -1:
        d(cubo)

    elif direcao == 1:
        d_linha(cubo)

    elif direcao == 2:
        d_linha(cubo)
        d_linha(cubo)   
#Ideia: Criar uma função que receba a localização de duas peças:{Face:index} e o lado, em relação a face Branca, e determine se estão na mesma coluna de giro(lado)
#Ideia: Função para determinar se duas peças são opostas 