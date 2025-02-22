from typing import List, Tuple
from math import sqrt

def distancia_euclidiana(cidadeUm: Tuple[int,int], cidadeDois: Tuple[int,int]) -> float:
    return sqrt((((cidadeUm[0] - cidadeDois[0]) ** 2) + ((cidadeUm[1] - cidadeDois[1]) ** 2)))

def vizinho_mais_proximo(pontos: List[tuple[int,int]]) -> str:
    n_cidades = len(pontos)
    menor_distancia_total = float('inf')
    melhor_cidade_inicial = 0

    for cidade_inicio in range(n_cidades):
        caminho_guloso = [cidade_inicio]
        visitas = [False] * n_cidades
        visitas[cidade_inicio] = True
        distancia_total_atual = 0
        

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
                distancia_total_atual += menor_distancia

        distancia_total_atual += distancia_euclidiana(pontos[caminho_guloso[-1]], pontos[cidade_inicio])

        if distancia_total_atual < menor_distancia_total:
            menor_distancia_total = distancia_total_atual
            melhor_cidade_inicial = cidade_inicio
            melhor_caminho = [i+1 for i in caminho_guloso]

        caminho_guloso.append(cidade_inicio)

    
    string_retorno = f'A melhor cidade inicial é: {melhor_cidade_inicial + 1}. Distância total: {menor_distancia_total :.4f} \nCaminho: {melhor_caminho}'

    return string_retorno

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