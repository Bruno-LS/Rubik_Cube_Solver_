from Movimentacoes.Rotacoes_fixas import *
import pandas as pd



def r(cubo:pd.DataFrame, face:str):
    """
        Realiza a chamada da função que corresponde a um giro do lado direito, com a 'face' como referencia
    """
    movimento = {
    'W': Direita,
    'Y': Esquerda,
    'B': Frente,
    'G': Costas,
    'R': Direita,
    'O': Direita
    }
    movimento[face](cubo)
        

def r_linha(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado direito anti-horario, com a 'face' como referencia
    """
    movimento = {
    'W': Direita_linha,
    'Y': Esquerda_linha,
    'B': Frente_linha,
    'G': Costas_linha,
    'R': Direita_linha,
    'O': Direita_linha
    }
    movimento[face](cubo)
    

def l(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado esquerdo, com a 'face' como referencia
    """
    movimento = {
    'W': Esquerda,
    'Y': Direita,
    'B': Costas,
    'G': Frente,
    'R': Esquerda,
    'O': Esquerda
    }
    movimento[face](cubo) 
    

def l_linha(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado esquerdo anti-horario, com a 'face' como referencia
    """
    movimento = {
    'W': Esquerda_linha,
    'Y': Direita_linha,
    'B': Costas_linha,
    'G': Frente_linha,
    'R': Esquerda_linha,
    'O': Esquerda_linha
    }
    movimento[face](cubo)


def u(df:pd.DataFrame):
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no topo horario
    """
    df.loc[[0, 1, 2], 'W'], df.loc[[0, 1, 2], 'G'], df.loc[[0, 1, 2], 'Y'], df.loc[[0, 1, 2], 'B'], df.loc[[0, 1, 2], 'R'], df.loc[[5, 8], 'R'], df.loc[[7, 6], 'R'], df.loc[[3], 'R'] = (
        [*df.loc[[0, 1, 2], 'G'].values],
        [*df.loc[[0, 1, 2], 'Y'].values],
        [*df.loc[[0, 1, 2], 'B'].values],
        [*df.loc[[0, 1, 2], 'W'].values],

        [*df.loc[[6, 3, 0], 'R'].values],
        [*df.loc[[1, 2], 'R'].values],
        [*df.loc[[5, 8], 'R'].values],
        [*df.loc[[7], 'R'].values]
    )


def u_linha(df:pd.DataFrame):
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no topo anti-horario
    """
    df.loc[[0, 1, 2], 'W'], df.loc[[0, 1, 2], 'B'], df.loc[[0, 1, 2], 'Y'], df.loc[[0, 1, 2], 'G'], df.loc[[0, 1, 2], 'R'], df.loc[[5, 8], 'R'], df.loc[[7, 6], 'R'], df.loc[[3], 'R'] = (
        [*df.loc[[0, 1, 2], 'B'].values],
        [*df.loc[[0, 1, 2], 'Y'].values],
        [*df.loc[[0, 1, 2], 'G'].values],
        [*df.loc[[0, 1, 2], 'W'].values],

        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[7, 6], 'R'].values],
        [*df.loc[[3, 0], 'R'].values],
        [*df.loc[[1], 'R'].values]
    )


def d(df:pd.DataFrame):
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no fundo horario
    """
    df.loc[[6, 7, 8], 'W'], df.loc[[6, 7, 8], 'B'], df.loc[[6, 7, 8], 'Y'], df.loc[[6, 7, 8], 'G'], df.loc[[0, 1, 2], 'O'], df.loc[[5, 8], 'O'], df.loc[[7, 6], 'O'], df.loc[[3], 'O'] = (
        [*df.loc[[6, 7, 8], 'B'].values],
        [*df.loc[[6, 7, 8], 'Y'].values],
        [*df.loc[[6, 7, 8], 'G'].values],
        [*df.loc[[6, 7, 8], 'W'].values],

        [*df.loc[[6, 3, 0], 'O'].values],
        [*df.loc[[1, 2], 'O'].values],
        [*df.loc[[5, 8], 'O'].values],
        [*df.loc[[7], 'O'].values]
    )
        

def d_linha(df:pd.DataFrame):
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no fundo anti-horario
    """
    df.loc[[6, 7, 8], 'W'], df.loc[[6, 7, 8], 'G'], df.loc[[6, 7, 8], 'Y'], df.loc[[6, 7, 8], 'B'], df.loc[[0, 1, 2], 'O'], df.loc[[5, 8], 'O'], df.loc[[7, 6], 'O'], df.loc[[3], 'O'] = (
        [*df.loc[[6, 7, 8], 'G'].values],
        [*df.loc[[6, 7, 8], 'Y'].values],
        [*df.loc[[6, 7, 8], 'B'].values],
        [*df.loc[[6, 7, 8], 'W'].values],

        [*df.loc[[2, 5, 8], 'O'].values],
        [*df.loc[[7, 6], 'O'].values],
        [*df.loc[[3, 0], 'O'].values],
        [*df.loc[[1], 'O'].values]
    )


def f(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado frontal, com a 'face' como referencia
    """
    movimento = {
    'W': Frente,
    'Y': Costas,
    'B': Esquerda,
    'G': Direita,
    'R': u,
    'O': d
    }
    movimento[face](cubo)      
    

def f_linha(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado frontal anti-horario, com a 'face' como referencia
    """
    movimento = {
    'W': Frente_linha,
    'Y': Costas_linha,
    'B': Esquerda_linha,
    'G': Direita_linha,
    'R': u_linha,
    'O': d_linha
    }
    movimento[face](cubo) 


def b(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado traseiro, com a 'face' como referencia
    """
    movimento = {
    'W': Costas,
    'Y': Frente,
    'B': Direita,
    'G': Esquerda,
    'R': d,
    'O': u
    }
    movimento[face](cubo)


def b_linha(cubo:pd.DataFrame, face):
    """
        Realiza a chamada da função que corresponde a um giro do lado traseiro anti-horario, com a 'face' como referencia
    """
    movimento = {
    'W': Costas_linha,
    'Y': Frente_linha,
    'B': Direita_linha,
    'G': Esquerda_linha,
    'R': d_linha,
    'O': u_linha
    }
    movimento[face](cubo)
    

def movimentos_passo5(cubo:pd.DataFrame):
    f(cubo, 'W')
    r(cubo, 'W')
    u(cubo)
    r_linha(cubo, 'W')
    u_linha(cubo)
    f_linha(cubo, 'W')


def movimentos_passo6(cubo:pd.DataFrame, face):
    r(cubo, face)
    u(cubo)
    r_linha(cubo, face)
    u(cubo)
    r(cubo, face)
    u(cubo)
    u(cubo)
    r_linha(cubo, face)


def movimentos_passo8(cubo:pd.DataFrame, face, lado):
    if lado == 1:
        u(cubo)
        l(cubo, face)
        r_linha(cubo, face)
        f(cubo, face)
        f(cubo, face)
        l_linha(cubo, face)
        r(cubo, face)
        u(cubo)
        f(cubo, face)
        f(cubo, face)
    elif lado == -1:
        u_linha(cubo)
        r_linha(cubo, face)
        l(cubo, face)
        f(cubo, face)
        f(cubo, face)
        l_linha(cubo, face)
        r(cubo, face)
        u_linha(cubo)
        f(cubo, face)
        f(cubo, face)



