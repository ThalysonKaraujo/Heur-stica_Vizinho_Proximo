from typing import List, Tuple
from math import sqrt

def distancia_euclidiana(cidadeUm: Tuple[int,int], cidadeDois: Tuple[int,int]) -> float:
    return sqrt((((cidadeUm[0] - cidadeDois[0]) ** 2) + ((cidadeUm[1] - cidadeDois[1]) ** 2)))

def vizinho_mais_proximo(pontos: List[tuple[int,int]]) -> Tuple[List[int], float]:
    n_cidades = len(pontos)
    caminho_guloso = [0]
    visitas = [False] * n_cidades
    visitas[0] = True
    distancia_total = 0

    for _ in range(n_cidades - 1):
        ultimo = caminho_guloso[-1]
        prox_cidade = None
        menor_distancia = float('inf')
        

        for i in range(n_cidades):
            if not visitas[i]:
                distancia = distancia_euclidiana(pontos[ultimo], pontos[i])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    prox_cidade = i
                    
        if prox_cidade is not None:
            caminho_guloso.append(prox_cidade)
            visitas[prox_cidade] = True
            distancia_total += menor_distancia


    distancia_total += distancia_euclidiana(pontos[caminho_guloso[-1]], pontos[0])
    caminho_guloso.append(0)
    caminho_guloso_retorno = [i+1 for i in caminho_guloso]

    return caminho_guloso_retorno, distancia_total

def principal():
    pontos_berlin52 = [
        (565, 575), (25, 185), (345, 750), (945, 685), (845, 655),
        (880, 660), (25, 230), (525, 1000), (580, 1175), (650, 1130),
        (1605, 620), (1220, 580), (1465, 200), (1530, 5), (845, 680),
        (725, 370), (145, 665), (415, 635), (510, 875), (560, 365),
        (300, 465), (520, 585), (480, 415), (835, 625), (975, 580),
        (1215, 245), (1320, 315), (1250, 400), (660, 180), (410, 250),
        (420, 555), (575, 665), (1150, 1160), (700, 580), (685, 595),
        (685, 610), (770, 610), (795, 645), (720, 635), (760, 650),
        (475, 960), (95, 260), (875, 920), (700, 500), (555, 815),
        (830, 485), (1170, 65), (830, 610), (605, 625), (595, 360),
        (1340, 725), (1740, 245)
    ]
    print(vizinho_mais_proximo(pontos_berlin52))

if __name__ == '__main__':
    principal()

