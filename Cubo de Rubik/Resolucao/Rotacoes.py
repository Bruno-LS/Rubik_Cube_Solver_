from Movimentos_fixos import *
import pandas as pd



def r(cubo:pd.DataFrame, face:str):
    if face == 'W':
        Direita(cubo)
    elif face == 'Y':   #Amarelo é oposto logo movimentos invertidos
        Esquerda(cubo) 
    elif face == 'B':   #Azul é o Lado esquerdo logo precisa mover a face em relação ao branco
        Frente(cubo)
    elif face == 'G':   # É o contrario do azul logo as costas
        Costas(cubo)
    elif face == 'R':  
        Direita(cubo)
    elif face == 'O':
        Direita(cubo)
        

def r_linha(cubo:pd.DataFrame, face):
    if face == 'W':
        Direita_linha(cubo)
    elif face == 'Y':   #Amarelo é oposto logo movimentos invertidos
        Esquerda_linha(cubo) 
    elif face == 'B':   #Azul é o Lado esquerdo logo precisa mover a face em relação ao branco
        Frente_linha(cubo)
    elif face == 'G':   # É o contrario do azul logo as costas
        Costas_linha(cubo)
    elif face == 'R':  
        Direita_linha(cubo)
    elif face == 'O':
        Direita_linha(cubo)
    

def l(cubo:pd.DataFrame, face):
    if face == 'W':
        Esquerda(cubo)
    elif face == 'Y':
        Direita(cubo)
    elif face == 'B':
        Costas(cubo)
    elif face == 'G':
        Frente(cubo)
    elif face == 'R':
        Esquerda(cubo)
    elif face == 'O':
        Esquerda(cubo) 
    

def l_linha(cubo:pd.DataFrame, face):
    if face == 'W':
        Esquerda_linha(cubo)
    elif face == 'Y':
        Direita_linha(cubo)
    elif face == 'B':
        Costas_linha(cubo)
    elif face == 'G':
        Frente_linha(cubo)
    elif face == 'R':
        Esquerda_linha(cubo)
    elif face == 'O':
        Esquerda_linha(cubo)


def u(df:pd.DataFrame):
    df.loc[[0, 1, 2], 'W'], df.loc[[0, 1, 2], 'G'], df.loc[[0, 1, 2], 'Y'], df.loc[[0, 1, 2], 'B'], df.loc[[0, 1, 2], 'R'], df.loc[[2, 5, 8], 'R'], df.loc[[8, 7, 6], 'R'], df.loc[[6, 3, 0], 'R'] = (
        [*df.loc[[0, 1, 2], 'G'].values],
        [*df.loc[[0, 1, 2], 'Y'].values],
        [*df.loc[[0, 1, 2], 'B'].values],
        [*df.loc[[0, 1, 2], 'W'].values],

        [*df.loc[[6, 3, 0], 'R'].values],
        [*df.loc[[0, 1, 2], 'R'].values],
        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[8, 7, 6], 'R'].values]
    )


def u_linha(df:pd.DataFrame):
    df.loc[[0, 1, 2], 'W'], df.loc[[0, 1, 2], 'B'], df.loc[[0, 1, 2], 'Y'], df.loc[[0, 1, 2], 'G'], df.loc[[0, 1, 2], 'R'], df.loc[[2, 5, 8], 'R'], df.loc[[8, 7, 6], 'R'], df.loc[[6, 3, 0], 'R'] = (
        [*df.loc[[0, 1, 2], 'B'].values],
        [*df.loc[[0, 1, 2], 'Y'].values],
        [*df.loc[[0, 1, 2], 'G'].values],
        [*df.loc[[0, 1, 2], 'W'].values],

        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[8, 7, 6], 'R'].values],
        [*df.loc[[6, 3, 0], 'R'].values],
        [*df.loc[[0, 1, 2], 'R'].values]
    )


def d(df:pd.DataFrame):
    df.loc[[6, 7, 8], 'W'], df.loc[[6, 7, 8], 'B'], df.loc[[6, 7, 8], 'Y'], df.loc[[6, 7, 8], 'G'], df.loc[[0, 1, 2], 'O'], df.loc[[2, 5, 8], 'O'], df.loc[[8, 7, 6], 'O'], df.loc[[6, 3, 0], 'O'] = (
        [*df.loc[[6, 7, 8], 'B'].values],
        [*df.loc[[6, 7, 8], 'Y'].values],
        [*df.loc[[6, 7, 8], 'G'].values],
        [*df.loc[[6, 7, 8], 'W'].values],

        [*df.loc[[6, 3, 0], 'O'].values],
        [*df.loc[[0, 1, 2], 'O'].values],
        [*df.loc[[2, 5, 8], 'O'].values],
        [*df.loc[[8, 7, 6], 'O'].values]
    )
        

def d_linha(df:pd.DataFrame):
    df.loc[[6, 7, 8], 'W'], df.loc[[6, 7, 8], 'G'], df.loc[[6, 7, 8], 'Y'], df.loc[[6, 7, 8], 'B'], df.loc[[0, 1, 2], 'O'], df.loc[[2, 5, 8], 'O'], df.loc[[8, 7, 6], 'O'], df.loc[[6, 3, 0], 'O'] = (
        [*df.loc[[6, 7, 8], 'G'].values],
        [*df.loc[[6, 7, 8], 'Y'].values],
        [*df.loc[[6, 7, 8], 'B'].values],
        [*df.loc[[6, 7, 8], 'W'].values],

        [*df.loc[[2, 5, 8], 'O'].values],
        [*df.loc[[8, 7, 6], 'O'].values],
        [*df.loc[[6, 3, 0], 'O'].values],
        [*df.loc[[0, 1, 2], 'O'].values]
    )


def f(cubo:pd.DataFrame, face):
    if face == 'W':
        Frente(cubo)
    elif face == 'Y':
        Costas(cubo)
    elif face == 'B':
        Esquerda(cubo)
    elif face == 'G':
        Direita(cubo)
    elif face == 'R':   
        u(cubo)     
    elif face == 'O':
        d(cubo)      
    

def f_linha(cubo:pd.DataFrame, face):
    if face == 'W':
        Frente_linha(cubo)
    elif face == 'Y':
        Costas_linha(cubo)
    elif face == 'B':
        Esquerda_linha(cubo)
    elif face == 'G':
        Direita_linha(cubo)
    elif face == 'R':   
        u_linha(cubo)     
    elif face == 'O':
        d_linha(cubo) 


def b(cubo:pd.DataFrame, face):
    if face == 'W':
        Costas(cubo)
    elif face == 'Y':
        Frente(cubo)
    elif face == 'B':
        Direita(cubo)
    elif face == 'G':
        Esquerda(cubo)
    elif face == 'R':
        d(cubo)     
    elif face == 'O': 
        u(cubo)


def b_linha(cubo:pd.DataFrame, face):
    if face == 'W':
        Costas_linha(cubo)
    elif face == 'Y':
        Frente_linha(cubo)
    elif face == 'B':
        Direita_linha(cubo)
    elif face == 'G':
        Esquerda_linha(cubo)
    elif face == 'R':
        d_linha(cubo)     
    elif face == 'O':
        u_linha(cubo)



