import pandas as pd


# Movimentos que não consideram a direção do cubo, abaixo a direção fixa que eles consideram
# Branco frente
# Azul direita
# Verde esquerda
# Laranja cima
# Vermelho fundo
# Amarelo costas

data = {
      "W": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9"],
      "R": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"],
      "G": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
      "O": ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"],
      "B": ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
      "Y": ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"] 
    }
cubo_embaralhado = {
      "W": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9"],
      "R": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"],
      "G": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
      "O": ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"],
      "B": ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
      "Y": ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"] 
}

df = pd.DataFrame(data)

def Direita(df:pd.DataFrame):#C
    # Movimento R face Branca ou L face Amarela ou F face Verde
    df.loc[[2, 5, 8], 'R'], df.loc[[6, 3, 0], 'Y'], df.loc[[2, 5, 8], 'O'], df.loc[[2, 5, 8], 'W'], df.loc[[0, 1, 2], 'G'], df.loc[[2, 5, 8], 'G'], df.loc[[8, 7, 6], 'G'], df.loc[[6, 3, 0], 'G'] = (
        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[6, 3, 0], 'Y'].values],
        [*df.loc[[2, 5, 8], 'O'].values],

        [*df.loc[[6, 3, 0], 'G'].values],
        [*df.loc[[0, 1, 2], 'G'].values],
        [*df.loc[[2, 5, 8], 'G'].values],
        [*df.loc[[8, 7, 6], 'G'].values]
    )


def Esquerda(df:pd.DataFrame):#C
    # Movimento L face Branca ou R face Amarela ou F face Azul
    df.loc[[0, 3, 6], 'R'], df.loc[[8, 5, 2], 'Y'], df.loc[[0, 3, 6], 'O'], df.loc[[0, 3, 6], 'W'], df.loc[[0, 1, 2], 'B'], df.loc[[2, 5, 8], 'B'], df.loc[[8, 7, 6], 'B'], df.loc[[6, 3, 0], 'B'] = (
        [*df.loc[[8, 5, 2], 'Y'].values],
        [*df.loc[[0, 3, 6], 'O'].values],    
        [*df.loc[[0, 3, 6], 'W'].values],
        [*df.loc[[0, 3, 6], 'R'].values],
        
        [*df.loc[[6, 3, 0], 'B'].values],
        [*df.loc[[0, 1, 2], 'B'].values],
        [*df.loc[[2, 5, 8], 'B'].values],
        [*df.loc[[8, 7, 6], 'B'].values]
    )


def Frente(df:pd.DataFrame):#C
    # Movimento R face Azul ou L face Verde ou F face Branca
    df.loc[[6, 7, 8], 'R'], df.loc[[0, 3, 6], 'G'], df.loc[[2, 1, 0], 'O'], df.loc[[2, 5, 8], 'B'], df.loc[[0, 1, 2], 'W'], df.loc[[2, 5, 8], 'W'], df.loc[[8, 7, 6], 'W'], df.loc[[6, 3, 0], 'W'] = (
        [*df.loc[[8, 5, 2], 'B'].values],
        [*df.loc[[6, 7, 8], 'R'].values],
        [*df.loc[[0, 3, 6], 'G'].values],
        [*df.loc[[0, 1, 2], 'O'].values],

        [*df.loc[[6, 3, 0], 'W'].values],
        [*df.loc[[0, 1, 2], 'W'].values],
        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[8, 7, 6], 'W'].values]
    )


def Costas(df:pd.DataFrame):#C
    # Movimento L face Azul ou R face Verde ou F face Amarela
    df.loc[[2, 1, 0], 'R'], df.loc[[8, 5, 2], 'G'], df.loc[[6, 7, 8], 'O'], df.loc[[0, 3, 6], 'B'], df.loc[[0, 1, 2], 'Y'], df.loc[[2, 5, 8], 'Y'], df.loc[[8, 7, 6], 'Y'], df.loc[[6, 3, 0], 'Y'] = (
        [*df.loc[[8, 5, 2], 'G'].values],
        [*df.loc[[6, 7, 8], 'O'].values],    
        [*df.loc[[0, 3, 6], 'B'].values],
        [*df.loc[[2, 1, 0], 'R'].values],
        
        [*df.loc[[6, 3, 0], 'Y'].values],
        [*df.loc[[0, 1, 2], 'Y'].values],
        [*df.loc[[2, 5, 8], 'Y'].values],
        [*df.loc[[8, 7, 6], 'Y'].values]
    )


def Direita_linha(df:pd.DataFrame):#C
    # Movimento R' face Branca ou L' face Amarela F' face Verde
    df.loc[[2, 5, 8], 'W'], df.loc[[6, 3, 0], 'Y'], df.loc[[2, 5, 8], 'O'], df.loc[[2, 5, 8], 'R'], df.loc[[0, 1, 2], 'G'], df.loc[[2, 5, 8], 'G'], df.loc[[8, 7, 6], 'G'], df.loc[[6, 3, 0], 'G'] = (
        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[2, 5, 8], 'O'].values],
        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[6, 3, 0], 'Y'].values],

        [*df.loc[[2, 5, 8], 'G'].values],
        [*df.loc[[8, 7, 6], 'G'].values],    
        [*df.loc[[6, 3, 0], 'G'].values],
        [*df.loc[[0, 1, 2], 'G'].values]
    )


def Esquerda_linha(df:pd.DataFrame):#C
    # Movimento L' face Branca ou R' face Amarela ou F' face Azul
    df.loc[[0, 3, 6], 'R'], df.loc[[8, 5, 2], 'Y'], df.loc[[0, 3, 6], 'O'], df.loc[[0, 3, 6], 'W'], df.loc[[0, 1, 2], 'B'], df.loc[[2, 5, 8], 'B'], df.loc[[8, 7, 6], 'B'], df.loc[[6, 3, 0], 'B'] = (
        [*df.loc[[0, 3, 6], 'W'].values],
        [*df.loc[[0, 3, 6], 'R'].values],    
        [*df.loc[[8, 5, 2], 'Y'].values],
        [*df.loc[[0, 3, 6], 'O'].values],    
        
        [*df.loc[[2, 5, 8], 'B'].values],
        [*df.loc[[8, 7, 6], 'B'].values],    
        [*df.loc[[6, 3, 0], 'B'].values],
        [*df.loc[[0, 1, 2], 'B'].values]
    )


def Frente_linha(df:pd.DataFrame):#C
# Movimento L' face Verde ou R' face Azul ou F' face Branca
    df.loc[[6, 7, 8], 'R'], df.loc[[0, 3, 6], 'G'], df.loc[[2, 1, 0], 'O'], df.loc[[8, 5, 2], 'B'], df.loc[[0, 1, 2], 'W'], df.loc[[2, 5, 8], 'W'], df.loc[[8, 7, 6], 'W'], df.loc[[6, 3, 0], 'W'] = (
        [*df.loc[[0, 3, 6], 'G'].values],
        [*df.loc[[2, 1, 0], 'O'].values],    
        [*df.loc[[8, 5, 2], 'B'].values],
        [*df.loc[[6, 7, 8], 'R'].values],    

        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[8, 7, 6], 'W'].values],    
        [*df.loc[[6, 3, 0], 'W'].values],
        [*df.loc[[0, 1, 2], 'W'].values]
    )
    

def Costas_linha(df:pd.DataFrame):#C
    # Movimento R' face Verde ou L' face Azul ou F' face Amarela
    df.loc[[0, 1, 2], 'R'], df.loc[[6, 3, 0], 'B'], df.loc[[8, 7, 6], 'O'], df.loc[[2, 5, 8], 'G'], df.loc[[0, 1, 2], 'W'], df.loc[[2, 5, 8], 'W'], df.loc[[8, 7, 6], 'W'], df.loc[[6, 3, 0], 'W'] = (
        [*df.loc[[6, 3, 0], 'B'].values],
        [*df.loc[[8, 7, 6], 'O'].values],        
        [*df.loc[[2, 5, 8], 'G'].values],
        [*df.loc[[0, 1, 2], 'R'].values],

        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[8, 7, 6], 'W'].values],    
        [*df.loc[[6, 3, 0], 'W'].values],
        [*df.loc[[0, 1, 2], 'W'].values]
    )


def print_custom_df(df):
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


# Nos loc's das funções retirar as redundancias ao virar as faces 
