# Importando funções
import pygame, random, time
from config import *

# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']

# definindo a função moverBloco(), que registra a posição do bloco
def moverBloco(bloco):
    bloco['objRect'].y += bloco['vel']

# Definindo a função moverTeclas(), que registra o movimento dos jogadores
def moverTeclas(teclas):
    teclas["esquerda"] = random.randint(0,1)
    teclas["direita"] = random.randint(0,1)
    teclas["baixo"] = random.randint(0,1)
    teclas["cima"] = random.randint(0,1)
    return teclas

# Definindo a função criarJogadores(), que cria os jogadores
def criarJogadores(NUMERODEJOGADORES):
    jogadores = []
    for i in range(0,NUMERODEJOGADORES):
        # Cores
        nivel_vermelho = random.randint(10, 200)
        nivel_verde = random.randint(10, 200)
        nivel_azul = random.randint(10, 200)
        #Posição inicial
        posX = (LARGURAJANELA/2 - TAMANHOBLOCO)
        posY = (ALTURAJANELA/2 - TAMANHOBLOCO)
        # Tempo de vida
        inicio = time.time()
        jogadores.append({'id':"j{}".format(i),'objRect': pygame.Rect(posX, posY, TAMANHOJOGADOR, TAMANHOJOGADOR), 'cor': (nivel_vermelho,nivel_verde,nivel_azul), 'vel': VELOCIDADEJOGADOR,'inicio': inicio})
    return jogadores