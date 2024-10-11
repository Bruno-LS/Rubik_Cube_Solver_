from Rotacoes import *
import pandas as pd
from Movimentos_fixos import df

def passo_1(cubo:pd.DataFrame):
    dicionario = mapear_meios(cubo)        
    
    i=0
    for face, indice in dicionario.items():
        str_face = str(face)
        if indice == []:
            continue
        id = int(indice[0])
        local = verificar_movimento(cubo, id, str_face)
        i+=1
        if id==7 or id == 1:
            f(cubo, face)
            dicionario = mapear_meios(cubo)
            continue  
        if id==3:
            if local == -1:
                u_linha(cubo)
            elif local == 0:
                u(cubo)
            else:
                l(cubo, face)
        if id==5:
            if local == -1:
                u(cubo, face)
            elif local == 0:
                u_linha(cubo)
            else:
                r(cubo, face)
        dicionario = mapear_meios(cubo)
    print(i)
        

def passo_2():
    pass


def passo_3():
    pass


def passo_4():
    pass


def passo_5():
    pass


def passo_6():
    pass


def passo_7():
    pass


def passo_8():
    pass




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
                        

def mapear_quina(cubo:pd.DataFrame, cor):#Inacabada
    pass


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

print_custom_df(df)



d(df)
l(df, 'W')
b_linha(df, 'W')
b_linha(df, 'W')
d_linha(df)
d_linha(df)
l_linha(df, 'W')
r(df, 'W')
d_linha(df)
d_linha(df)
l(df, 'W')
b_linha(df, 'W')
u(df)
l(df, 'W')
r_linha(df, 'W') 
d_linha(df)
d_linha(df)
r(df, 'W')
b(df, 'W')
r(df, 'W')
d(df)
r_linha(df, 'W')
r_linha(df, 'W')
u(df)
d_linha(df)
d_linha(df)
r_linha(df, 'W')
r_linha(df, 'W')
d(df)
f(df, 'W')
r_linha(df, 'W')
b_linha(df, 'W')



# caso 7 é bem especifico então tenho q dar uma olhada legal nisso


print("\n\n")
print_custom_df(df)
