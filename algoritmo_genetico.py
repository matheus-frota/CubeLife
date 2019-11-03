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

# Definindo função divisivelPorDois(), para ver se o numero é divisivel por 2. Para evitar que tenha
# quantidade de jogadores impares
divisivelPorDois = lambda x : x if x%2 == 0 else x+1

# Definindo função de quantidadeDeJogadoreSelecionados(), retorna a quantidade de jogadores
def quantidadeDeJogadoreSelecionados(NUM_JOGADORES):
    if NUM_JOGADORES%2 == 0:
        return divisivelPorDois(int(NUM_JOGADORES/2))
    elif NUM_JOGADORES%2 != 0:
        return divisivelPorDois(int(round(NUM_JOGADORES/2,0)))

# Definindo função ordenarDicionario().
def ordenarValoresDicionario(dicionario):
    # Variavel auxiliar
    armazenarResultadoOrdenado = []
    for i in sorted(dicionario, key = dicionario.get, reverse = True):
        armazenarResultadoOrdenado.append((i,dicionario[i]))
    return armazenarResultadoOrdenado

# Definindo função filtrarDicionario(), para filtrar apenas os jogadores selecionados do dicionário ordenado.
filtrarDicionarioComApenasJogadoresSelecionados = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y)])

# Definindo função temporaria nomeJogador(), para criar uma lista com os nomes dos jogadores selecionados
nomeJogador = lambda x : [i[0] for i in x]

# Definindo função de selecionar os melhores individuos.
# Usando estratégia de eletismo para essa selecao.
def eletismo(jogadores, NUM_JOGADORES):
    # Variáveis auxiliares
    informacaoDeJogadorETempo = {}
    # Identificando quantidade de jogadores que serão selecionados
    quantidadeJogadores = quantidadeDeJogadoreSelecionados(NUM_JOGADORES)
    # Reorganizando informações do dicionario, em um dicionario menor com apenas a informação do tempo de vida
    for id in jogadores.keys():
        informacaoDeJogadorETempo[id] = jogadores[id][-1]
    jogadoresOrdenados = ordenarValoresDicionario(informacaoDeJogadorETempo)
    return filtrarDicionarioComApenasJogadoresSelecionados(jogadores,nomeJogador(jogadoresOrdenados[:quantidadeJogadores]))

# Definindo função formarGrupos(), para formar os grupos dos jogadores para o crossover.
def formarGrupos(identificacaoJogadores, quantidadeJogadores):
    divisor = int(quantidadeJogadores/2)
    gruposJogadores = []
    identificacaoJogadores = np.random.permutation(identificacaoJogadores)
    for jogador1,jogador2 in zip(identificacaoJogadores[:divisor],identificacaoJogadores[divisor:]):
        gruposJogadores.append((jogador1,jogador2))
    return gruposJogadores

# Definindo função de crossover dos indivíduos e gerando novos indivíduos.
def crossover(jogadoresSelecionados):
    quantidadeJogadores = len(jogadoresSelecionados)
    identificacaoJogadores = list(jogadoresSelecionados.keys())
    gruposJogadores = formarGrupos(identificacaoJogadores,quantidadeJogadores)
    for jogador1,jogador2 in gruposJogadores:
        for movimentosJogador1,movimentoJogador2 in zip(jogadoresSelecionados[jogador1],jogadoresSelecionados[jogador2]):
            print(movimentosJogador1)
            print(movimentoJogador2)
        break