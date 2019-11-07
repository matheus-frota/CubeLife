import pygame, random, time
import funcoes_jogo as fj
import algoritmo_genetico as ag
from config import *

# inicializando pygame
pygame.init()
relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Cubo')
fonte = pygame.font.Font(None,40)

# criando jogadores
jogadores = fj.criarJogadores(None,NUMERODEJOGADORES)

# Gerando movimentos aleatorios iniciais dos jogadores
movimentacaoAleatoriaJogadores = ag.gerarPopulacao(jogadores,NUMERODEJOGADAS)

# definindo o dicionario que guardará as direcoes pressionadas
#teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}

# inicializando outras variáveis
contador = 0
geracao = 0
blocos = []
deveContinuar = True
controleDeAparicaoBlocos = True
CONTADORMOVIMENTOSJOGADOR = 0
controleEpocas = 0

# loop do jogo
while  deveContinuar:
    # checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deveContinuar = False
        '''
        # quando uma tecla é pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deveContinuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True
        # quando uma tecla é solta
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False
        # quando um botao do mouse é pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            blocos.append({'objRect': pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO), 'cor': BRANCO, 'vel': 1})
        '''
    contador += 1
    if contador >= ITERACOES:
        # adicionando um novo bloco
        contador = 0
        if controleDeAparicaoBlocos:
            for i in range(0,NUMERODEBLOCOS):
                posX = i*(LARGURAJANELA/NUMERODEBLOCOS)
                posY = -TAMANHOBLOCO
                velRandom = 5
                blocos.append({'objRect': pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO), 'cor': BRANCO, 'vel': velRandom})
            controleDeAparicaoBlocos = False
        elif controleDeAparicaoBlocos == False:
            for i in range(0,NUMERODEBLOCOS):
                posX = i*(LARGURAJANELA/NUMERODEBLOCOS) + 2*(NUMERODEBLOCOS)
                posY = -TAMANHOBLOCO
                velRandom = 5
                blocos.append({'objRect': pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO), 'cor': BRANCO, 'vel': velRandom})
            controleDeAparicaoBlocos = True

    # preenchendo o fundo de janela com a cor preta
    janela.fill(PRETO)

    # movendo o jogador
    for i,jogador in enumerate(jogadores[:]):
        try:
            fj.moverJogador(jogador, movimentacaoAleatoriaJogadores[jogador["id"]][CONTADORMOVIMENTOSJOGADOR], (LARGURAJANELA, ALTURAJANELA))
        except IndexError:
            fj.moverJogador(jogador, {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}, (LARGURAJANELA, ALTURAJANELA))
    
    # desenhando jogador
    for jogador in jogadores[:]:
        pygame.draw.rect(janela, jogador['cor'], jogador['objRect'])

    # checando se jogador bateu em algum bloco ou se bloco saiu da janela para retirá-lo da lista
    for i,jogador in enumerate(jogadores[:]):
        for bloco in blocos[:]:
            bateu = jogador['objRect'].colliderect(bloco['objRect'])
            if bateu:
                movimentacaoAleatoriaJogadores[jogador["id"]].append(time.time() - jogador["inicio"]) 
                blocos.remove(bloco)
                jogadores.remove(jogador)
                break

    # movendo e desenhando os blocos
    for bloco in blocos:
        fj.moverBloco(bloco)
        pygame.draw.rect(janela, bloco['cor'], bloco['objRect'])

    # Verificando se todos os jogadores já morreram
    if len(jogadores) == 0:
        # Não tem sentido pegar os jogadores, pois todos ja morreram!
        informacaoJogadorTempo,jogadoresSelecionados = ag.eletismo(movimentacaoAleatoriaJogadores, NUMERODEJOGADORES)
        jogadores, movimentacaoAleatoriaJogadores = ag.crossover(jogadoresSelecionados)
        print(informacaoJogadorTempo)
        contador = 0
        blocos = []
        controleDeAparicaoBlocos = True
        CONTADORMOVIMENTOSJOGADOR = 0
    
    # atualizando a janela
    CONTADORMOVIMENTOSJOGADOR+=1
    pygame.display.update()
    relogio.tick(20)
# encerrando módulos de Pygame
pygame.quit()