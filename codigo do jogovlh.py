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
