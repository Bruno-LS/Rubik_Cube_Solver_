
def quina_vermelhas(cubo:pd.DataFrame):
    """
        Verifica as quinas da face Vermelha , Retorna seu Index
    """
    red = cubo['R'].values
    for j in range(0, len(red), 2):
        meio = red[j]
        if meio[0] == "O":
            return j


def adjacentes_vermelhos(id):
    """
        Retorna a localização dos adjacentes as quinas vermelhas
    """
    if id == 0:
        return {'B':0, 'Y':2}
    elif id == 2:
        return {'Y':0, 'G':2}
    elif id == 6:
        return {'W':0, 'B':2}
    elif id == 8:
        return {'W':2, 'G':0}
    