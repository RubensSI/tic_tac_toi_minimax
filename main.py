from game import createBoard, makeMove,  getInputValid, printBoard, checkWinner,  checkMove

from minimax import moveIA

# Criando a lógica do jogo da velha
tabuleiro = createBoard()
winner = checkWinner(tabuleiro)
player = 1

while(not winner):
    printBoard(tabuleiro)
    print("######## Jogo da Velha ######")
    # # Definindo a jogada da IA
    if(player == 0):
        i, j = moveIA(tabuleiro, player)
    else:
        i = getInputValid("Digite a linha: ")
        j = getInputValid("Digite a coluna: ")

    # Verificando o movimento do jogador
    if(checkMove(tabuleiro, i, j)):
        makeMove(tabuleiro, i, j, player)
        # Trocando os jogadores ou alternando entre 0 e 1
        player = (player + 1) % 2
    else:
        print("Posicao oculpada")

    winner = checkWinner(tabuleiro)


printBoard(tabuleiro)
if(winner == "X"):
    print("Resultado: Jogador", winner, 'venceu')
elif(winner == "O"):
    print("Resultado: Jogador", winner, 'venceu')
else:
    print('O jogo deu EMPATE')

print("######## FIM DE JOGO ########")
