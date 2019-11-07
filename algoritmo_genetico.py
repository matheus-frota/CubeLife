import numpy as np
import random
import funcoes_jogo as fj

# Definindo função gerarPopulacao(), que recebe os jogadores e seta uma X quantidade de jogadas
# para os jogadores de forma aleatória.
def gerarPopulacao(jogadores, NUM_JOGADAS):
    jogadores_teclas = {}
    # Laço para criar as jogadas de cada jogador
    for jogador in jogadores:
        jogadores_teclas[jogador["id"]] = []
        for jogadas in range(NUM_JOGADAS):
            aux = {}
            aux["direita"] = random.randint(0,1)
            aux["esquerda"] = random.randint(0,1)
            aux["baixo"] = random.randint(0,1)
            aux["cima"] = random.randint(0,1)
            jogadores_teclas[jogador["id"]].append(aux)
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
def eletismo(movimentoJogadores, NUM_JOGADORES):
    # Variáveis auxiliares
    informacaoDeJogadorETempo = {}
    jogadoreSelecionados = []
    # Identificando quantidade de jogadores que serão selecionados
    quantidadeJogadores = quantidadeDeJogadoreSelecionados(NUM_JOGADORES)
    # Reorganizando informações do dicionario, em um dicionario menor com apenas a informação do tempo de vida
    for id in movimentoJogadores.keys():
        informacaoDeJogadorETempo[id] = movimentoJogadores[id][-1]
    jogadoresOrdenados = ordenarValoresDicionario(informacaoDeJogadorETempo)
    return jogadoresOrdenados[0],filtrarDicionarioComApenasJogadoresSelecionados(movimentoJogadores,nomeJogador(jogadoresOrdenados[:quantidadeJogadores]))

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
    # Variáveis auxiliares
    novosJogadores = []
    movimentoJogadorFilho = {}
    quantidadeJogadores = len(jogadoresSelecionados)
    identificacaoJogadores = list(jogadoresSelecionados.keys())
    gruposJogadoresParaRecombinacao = formarGrupos(identificacaoJogadores,quantidadeJogadores)
    for jogador1,jogador2 in gruposJogadoresParaRecombinacao:
        controleParaMudarOJogador = 0
        novosJogadoresFilhos = fj.criarJogadores(None,2)
        caracteristicasJogador1 = fj.criarJogadores(jogador1,1)
        caracteristicasJogador2 = fj.criarJogadores(jogador2,1)
        for jogadorFilho in novosJogadoresFilhos:
            movimentoJogadorFilho[jogadorFilho["id"]] = []
            for movimentosJogador1,movimentosJogador2 in zip(jogadoresSelecionados[jogador1],jogadoresSelecionados[jogador2]):
                #movimentoJogadorFilho[jogadorFilho["id"]].append()
                if (type(movimentosJogador1) == dict) & (type(movimentosJogador2) == dict) & (controleParaMudarOJogador == 0): 
                    movimentoJogadorFilho[jogadorFilho["id"]].append({"direita":movimentosJogador1["direita"],"esquerda":movimentosJogador1["esquerda"],"baixo":movimentosJogador2["baixo"],"cima":movimentosJogador2["cima"]})
                elif (type(movimentosJogador1) == dict) & (type(movimentosJogador2) == dict) & (controleParaMudarOJogador == 1): 
                    movimentoJogadorFilho[jogadorFilho["id"]].append({"direita":movimentosJogador2["direita"],"esquerda":movimentosJogador2["esquerda"],"baixo":movimentosJogador1["baixo"],"cima":movimentosJogador1["cima"]})
            controleParaMudarOJogador = 1
        movimentoJogadorFilho[jogador1],movimentoJogadorFilho[jogador2] =  jogadoresSelecionados[jogador1],jogadoresSelecionados[jogador2]
        novosJogadores.extend(novosJogadoresFilhos)
        novosJogadores.extend(caracteristicasJogador1)
        novosJogadores.extend(caracteristicasJogador2)
    return novosJogadores, movimentoJogadorFilho

