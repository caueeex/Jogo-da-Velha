def imprimir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def verificar_vencedor(tabuleiro, jogador):
    
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def jogo_da_velha():
    tabuleiro = [" " for _ in range(9)]  
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            jogada = int(input("Escolha uma posição (1-9): ")) - 1 
            if jogada < 0 or jogada > 8:
                print("Posição inválida. Escolha um número entre 1 e 9.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 9.")
            continue

        if tabuleiro[jogada] != " ":
            print("Posição já ocupada. Tente novamente.")
            continue

        tabuleiro[jogada] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            break

        if " " not in tabuleiro:
            imprimir_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedores.")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"  

if __name__ == "__main__":
    jogo_da_velha()
