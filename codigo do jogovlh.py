#função para criar o tabuleiro
def print_tabuleiro(tab):
    print()
    for linha in tab:
        print(" | ".join(linha))
        print("-" * 5)
    print()

# função para checar vitoria 
def checar_vitoria(tab, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([tab[i][j] == jogador for j in range(3)]) or all([tab[j][i] == jogador for j in range(3)]):
            return True
    if all([tab[i][i] == jogador for i in range(3)]) or all([tab[i][2-i] == jogador for i in range(3)]):
        return True
    return False

# função para checar empate 
def checar_empate(tab):
    for linha in tab:
        if " " in linha:
            return False
    return False

# Criaação do tabuleiro
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador_atual = "X"

while True:
    print_tabuleiro(tabuleiro)
    
    # Entrada do jogador
    try:
        linha = int (input(f"jogador {jogador_atual}, escolha a linha (0, 1 ou 2):"))
        coluna = int (input(f"jogador {jogador_atual}, escolha a coluna (0, 1 ou 2)"))
    except ValueError :
        print("Entrada inválida . Digite números entra 0 e 2.\n")
        continue
    if linha not in range(3) or caluna not in range(3):
        print("Posição inválida. Tente novamente.\n")
        continue
    if tabuleiro[linha][coluna] != "":
        print("Espaço já ocupado. Tente novamente.\n")
        continue

    # Marca a jogada no tabuleiro
    
    tabuleiro[linha][coluna] = jogador_atual

    # Verificar vitória

    if checar_vitoria(tabuleiro , jogador_atual):
        print_tabuleiro(tabuleiro)
        print(f"🎉 Jogador {jogador_atual} venceu! 🎉")
        break

    # Verificar empa

    if checar_empate(tabuleiro):
        print_tabuleiro(tabuleiro)
        print("🤝 Empate!")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"