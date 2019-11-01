import numpy as np
import random

# Definindo função gerarPopulacao(), que recebe a quantidade de jogadores e seta uma X quantidade de jogadas
# para os jogadores de forma aleatória.
def gerarPopulacao(NUM_JOGADORES, NUM_JOGADAS):
    jogadores_teclas = {}
    # Laço para criar as jogadas de cada jogador
    for jogador in range(0, NUM_JOGADORES):
        jogadores_teclas["j{}".format(jogador)] = []
        for jogadas in range(NUM_JOGADAS):
            aux = {}
            aux["direita"] = random.randint(0,1)
            aux["esquerda"] = random.randint(0,1)
            aux["baixo"] = random.randint(0,1)
            aux["cima"] = random.randint(0,1)
            jogadores_teclas["j{}".format(jogador)].append(aux)
    return jogadores_teclas

# Definindo função de selecionar os melhores individuos.
# Usando estratégia de eletismo para essa selecao.
def selecaoIndividuos(jogadores, NUM_JOGADORES):
    # Identificando quantidade de jogadores que serão selecionados
    if NUM_JOGADORES%2 == 0:
        qtd_selecao = NUM_JOGADORES/2
    elif NUM_JOGADORES%2 != 0:
        qtd_selecao = round(NUM_JOGADORES/2,0)

    # identificando jogadores com a melhor pontuação
    for id in jogadores.keys():
        print(id)
        print(jogadores[id][-1])