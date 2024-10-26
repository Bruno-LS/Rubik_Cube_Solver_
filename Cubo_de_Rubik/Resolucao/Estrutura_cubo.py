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


df = pd.DataFrame(data)