# Variavel que contém o local de vazio no tabuleiro
emptySpot = " "

# Token do jogadores
token = ["O", "X"]


# Criando o tabuleiro
def createBoard():
    tabuleiro = [
        [emptySpot, emptySpot, emptySpot],
        [emptySpot, emptySpot, emptySpot],
        [emptySpot, emptySpot, emptySpot],
    ]
    return tabuleiro


# Imprimindo o Tabuleiro
def printBoard(tabuleiro):
    for i in range(len(tabuleiro)):
        # Usando o metodo join para pegar todos os itens em um iteravél
        # e unindo em uma string tendo o pipe como separador
        print("|".join(tabuleiro[i]))
        if (i < 2):
            print("------")


# Obtendo os inputs validos, ou seja,
# Pegando a linha e coluna do jogador
def getInputValid(message):
    try:
        n = int(input(message))
        if (n >= 0 and n <= 2):
            return n
        else:
            print("Digite um numero de 0 ate 2")
            return getInputValid(message)
    except:
        print("Numero invalido")
        return getInputValid(message)


# Verificando se o movimento é valido
def checkMove(tabuleiro, x, y):
    # Se as posições do tabuleiro for igual a vazio ele retorna True
    # Ou seja a posição está disponivel
    if (tabuleiro[x][y] == emptySpot):
        return True
    else:
        return False


# Se movendo
def makeMove(tabuleiro, x, y, player):
    tabuleiro[x][y] = token[player]


# Verificando quem ganhou
def checkWinner(tabuleiro):
    # Percorrendo as linhas do tabuleiro e se na mesma linha tiver 3 elementos iguais já temos um ganhador
    for i in range(len(tabuleiro)):
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != emptySpot):
            return tabuleiro[i][0]

            # Percorrendo as colunas do tabuleiro e se na mesma coluna tiver 3 elementos iguais já temos um ganhador
    for i in range(len(tabuleiro)):
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != emptySpot):
            return tabuleiro[0][i]

            # Percorrendo as diagonais do tabuleiro e se na mesma diagonal tivermos 3 elementos iguais já temos um ganhador
    if (tabuleiro[0][0] != emptySpot and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        return tabuleiro[0][0]

    if (tabuleiro[0][2] != emptySpot and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        return tabuleiro[0][2]

    # Percorrendo o taboleiro atras de um campo em branco e caso tenha, os jagadores irão jogar novamente
    # Caso não tenha nenhum campo vazio ele sai do for e retorna empate
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if (tabuleiro[i][j] == emptySpot):
                return False

    return "EMPATE"

