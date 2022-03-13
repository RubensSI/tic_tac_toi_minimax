from game import emptySpot, token, checkWinner


def moveIA(tabuleiro, player):
    #Verificar todas as possibilidades
    possibilityMoves = getPosition(tabuleiro)
    bestValue = None
    bestMove = None

    # Considerando a melhor possibilidade para ganhar o jogo
    # Vamos descobrir o melhor movimento
    # pesquisando em todas as possibilidades
    for possibility in possibilityMoves:
        # O tabuleiro irá sofrer uma mudança
        # Acessando assim a nova lista de posições
        # Setando temporariamente assim a 'O' ou 'X'
        tabuleiro[possibility[0]][possibility[1]] = token[player]
        # Retornano o valor do miniMax que é o '0', '1' e o '-1'
        value = minimax(tabuleiro, player)
        # Limpando o tabuleiro
        tabuleiro[possibility[0]][possibility[1]] = emptySpot
        print(possibility, value)

        # Verificando se existe um melhor valor já setado na variavel
        if (bestValue is None):
            bestValue = value
            bestMove = possibility
        # Aqui a 'O' quer sempre o maior valor
        elif (player == 0):
            if (value > bestValue):
                bestValue = value
                bestMove = possibility
        # Aqui o 'X' quer sempre o menor valor
        elif (player == 1):
            if (value < bestValue):
                bestValue = value
                bestMove = possibility
    print("Probabilidade de vitoria:", bestValue*100, "%")
    # Acessando a lista de possibilidade da variável posições
    # Retornar o melhor movimento
    return bestMove[0], bestMove[1]


# O getPosition pega todas as posições vazias
def getPosition(tabuleiro):
    positions = []
    for i in range(3):
        for j in range(3):
            if (tabuleiro[i][j] == emptySpot):
                positions.append([i, j])

    return positions


aux = {
    "EMPATE": 0,
    "X": -1,
    "O": 1
}


def minimax(tabuleiro, player):
    #Aqui ele recebe o resultado  False ou True se a um ganhador
    winner = checkWinner(tabuleiro)
    if (winner):
        # Se existir um ganhador
        # aux recebe o ganhador e logo depois vai acessar o
        # dicionario de dados contendo chave e valor
        # pegando  o valor referente aquela chave 'X' , 'O' ou 'EMPATE'.
        return aux[winner]
    # Troco os jogadores
    player = (player + 1) % 2

    # A maquina vai testar as possibilidade, ou seja, as  jogadas do oponete
    possibilityMoves = getPosition(tabuleiro)
    bestValue = None

    for possibility in possibilityMoves:
        # O tabuleiro irá sofrer uma mudança
        # Acessando assim a nova lista de posições
        # Setando assim a 'O' ou 'X
        tabuleiro[possibility[0]][possibility[1]] = token[player]
        # Retornano o valor do miniMaxque é o '0', '1' e o '-1'
        value = minimax(tabuleiro, player)
        # Limpando o tabuleiro
        tabuleiro[possibility[0]][possibility[1]] = emptySpot

        # Verificando se existe um melhor valor já setado na variavel
        if (bestValue is None):
            bestValue = value
        # Aqui a 'O' quer sempre o maior valor
        # Vai verificar se o jagador é a vez da máquina
        elif (player == 0):
            if (value > bestValue):
                bestValue = value
        # Aqui o 'X' quer sempre o menor valor
        # Vai verificar se o jagador é o jogador é o X
        elif (player == 1):
            if (value < bestValue):
                bestValue = value

    # Retorna o melhor valor caso ele não entre em nenhuma destas condições
    return bestValue
