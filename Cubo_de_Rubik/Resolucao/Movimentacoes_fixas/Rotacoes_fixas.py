import pandas as pd


# Movimentos que não consideram a direção do cubo, abaixo a direção fixa que eles consideram
# Branco frente
# Azul direita
# Verde esquerda
# Laranja cima
# Vermelho fundo
# Amarelo costas


def Direita(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado direito horario
    """
    df.loc[[2, 5, 8], 'R'], df.loc[[6, 3, 0], 'Y'], df.loc[[2, 5, 8], 'O'], df.loc[[2, 5, 8], 'W'], df.loc[[0, 1, 2], 'G'], df.loc[[5, 8], 'G'], df.loc[[7, 6], 'G'], df.loc[[3], 'G'] = (
        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[6, 3, 0], 'Y'].values],
        [*df.loc[[2, 5, 8], 'O'].values],

        [*df.loc[[6, 3, 0], 'G'].values],
        [*df.loc[[1, 2], 'G'].values],
        [*df.loc[[5, 8], 'G'].values],
        [*df.loc[[7], 'G'].values]
    )


def Esquerda(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado esquerdo horario
    """
    df.loc[[0, 3, 6], 'R'], df.loc[[8, 5, 2], 'Y'], df.loc[[0, 3, 6], 'O'], df.loc[[0, 3, 6], 'W'], df.loc[[0, 1, 2], 'B'], df.loc[[5, 8], 'B'], df.loc[[7, 6], 'B'], df.loc[[3], 'B'] = (
        [*df.loc[[8, 5, 2], 'Y'].values],
        [*df.loc[[0, 3, 6], 'O'].values],    
        [*df.loc[[0, 3, 6], 'W'].values],
        [*df.loc[[0, 3, 6], 'R'].values],
        
        [*df.loc[[6, 3, 0], 'B'].values],
        [*df.loc[[1, 2], 'B'].values],
        [*df.loc[[5, 8], 'B'].values],
        [*df.loc[[7], 'B'].values]
    )


def Frente(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado frontal horario
    """
    df.loc[[6, 7, 8], 'R'], df.loc[[0, 3, 6], 'G'], df.loc[[2, 1, 0], 'O'], df.loc[[2, 5, 8], 'B'], df.loc[[0, 1, 2], 'W'], df.loc[[5, 8], 'W'], df.loc[[7, 6], 'W'], df.loc[[3], 'W'] = (
        [*df.loc[[8, 5, 2], 'B'].values],
        [*df.loc[[6, 7, 8], 'R'].values],
        [*df.loc[[0, 3, 6], 'G'].values],
        [*df.loc[[0, 1, 2], 'O'].values],

        [*df.loc[[6, 3, 0], 'W'].values],
        [*df.loc[[1, 2], 'W'].values],
        [*df.loc[[5, 8], 'W'].values],
        [*df.loc[[7], 'W'].values]
    )


def Costas(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado traseiro horario
    """
    df.loc[[2, 1, 0], 'R'], df.loc[[8, 5, 2], 'G'], df.loc[[6, 7, 8], 'O'], df.loc[[0, 3, 6], 'B'], df.loc[[0, 1, 2], 'Y'], df.loc[[5, 8], 'Y'], df.loc[[7, 6], 'Y'], df.loc[[3], 'Y'] = (
        [*df.loc[[8, 5, 2], 'G'].values],
        [*df.loc[[6, 7, 8], 'O'].values],    
        [*df.loc[[0, 3, 6], 'B'].values],
        [*df.loc[[2, 1, 0], 'R'].values],
        
        [*df.loc[[6, 3, 0], 'Y'].values],
        [*df.loc[[1, 2], 'Y'].values],
        [*df.loc[[5, 8], 'Y'].values],
        [*df.loc[[7], 'Y'].values]
    )


def Direita_linha(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado direito anti-horario
    """
    df.loc[[2, 5, 8], 'W'], df.loc[[6, 3, 0], 'Y'], df.loc[[2, 5, 8], 'O'], df.loc[[2, 5, 8], 'R'], df.loc[[0, 1, 2], 'G'], df.loc[[5, 8], 'G'], df.loc[[7, 6], 'G'], df.loc[[3], 'G'] = (
        [*df.loc[[2, 5, 8], 'R'].values],
        [*df.loc[[2, 5, 8], 'O'].values],
        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[6, 3, 0], 'Y'].values],

        [*df.loc[[2, 5, 8], 'G'].values],
        [*df.loc[[7, 6], 'G'].values],    
        [*df.loc[[3, 0], 'G'].values],
        [*df.loc[[1], 'G'].values]
    )


def Esquerda_linha(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado esquerdo anti-horario
    """
    df.loc[[0, 3, 6], 'R'], df.loc[[8, 5, 2], 'Y'], df.loc[[0, 3, 6], 'O'], df.loc[[0, 3, 6], 'W'], df.loc[[0, 1, 2], 'B'], df.loc[[5, 8], 'B'], df.loc[[7, 6], 'B'], df.loc[[3], 'B'] = (
        [*df.loc[[0, 3, 6], 'W'].values],
        [*df.loc[[0, 3, 6], 'R'].values],    
        [*df.loc[[8, 5, 2], 'Y'].values],
        [*df.loc[[0, 3, 6], 'O'].values],    
        
        [*df.loc[[2, 5, 8], 'B'].values],
        [*df.loc[[7, 6], 'B'].values],    
        [*df.loc[[3, 0], 'B'].values],
        [*df.loc[[1], 'B'].values]
    )


def Frente_linha(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado frontal anti-horario
    """
    df.loc[[6, 7, 8], 'R'], df.loc[[0, 3, 6], 'G'], df.loc[[2, 1, 0], 'O'], df.loc[[8, 5, 2], 'B'], df.loc[[0, 1, 2], 'W'], df.loc[[5, 8], 'W'], df.loc[[7, 6], 'W'], df.loc[[3], 'W'] = (
        [*df.loc[[0, 3, 6], 'G'].values],
        [*df.loc[[2, 1, 0], 'O'].values],    
        [*df.loc[[8, 5, 2], 'B'].values],
        [*df.loc[[6, 7, 8], 'R'].values],    

        [*df.loc[[2, 5, 8], 'W'].values],
        [*df.loc[[7, 6], 'W'].values],    
        [*df.loc[[3, 0], 'W'].values],
        [*df.loc[[1], 'W'].values]
    )
    

def Costas_linha(df:pd.DataFrame):#C
    """
        Realiza uma troca nas posições das peças do cubo, com a face Branca como referencia realiza um giro no lado traseiro anti-horario
    """
    df.loc[[0, 1, 2], 'R'], df.loc[[6, 3, 0], 'B'], df.loc[[8, 7, 6], 'O'], df.loc[[2, 5, 8], 'G'], df.loc[[0, 1, 2], 'Y'], df.loc[[5, 8], 'Y'], df.loc[[7, 6], 'Y'], df.loc[[3], 'Y'] = (
        [*df.loc[[6, 3, 0], 'B'].values],
        [*df.loc[[8, 7, 6], 'O'].values],        
        [*df.loc[[2, 5, 8], 'G'].values],
        [*df.loc[[0, 1, 2], 'R'].values],

        [*df.loc[[2, 5, 8], 'Y'].values],
        [*df.loc[[7, 6], 'Y'].values],    
        [*df.loc[[3, 0], 'Y'].values],
        [*df.loc[[1], 'Y'].values]
    )




