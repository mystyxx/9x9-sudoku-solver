def afficher_grille_sudoku(grille):
    print("+-------+-------+-------+")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("|-------+-------+-------|")
        line = ""
        for j in range(9):
            if j % 3 == 0:
                line += "| "
            if grille[i][j] == 0:
                line += ". "
            else:
                line += str(grille[i][j]) + " "
        line += "|"
        print(line)
    print("+-------+-------+-------+")

def saisir_grille_sudoku():
    print("Entrez les chiffres de la grille de Sudoku ligne par ligne. Ne mettez ni espace ni virgule entre les chiffres.")
    print("Utilisez '.' pour représenter les cases vides.")
    grille = []
    for i in range(9):
        while True:
            ligne = input(f"Entrez les chiffres de la ligne {i + 1} : ")
            if len(ligne) == 9 and all(c in '123456789.' for c in ligne):
                grille.append([int(c) if c != '.' else 0 for c in ligne])
                break
            else:
                print("Entrée invalide. Réessayez.")
    return grille

def est_valide(grille, row, col, num):
    """
    Vérifie si placer 'num' dans la case (row, col) de la grille est valide.
    """
    # Vérifie la ligne
    if num in grille[row]:
        return False
    
    # Vérifie la colonne
    for i in range(9):
        if grille[i][col] == num:
            return False
    
    # Vérifie le bloc 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grille[i][j] == num:
                return False
    
    return True

def resoudre_sudoku(grille):
    """
    Résout la grille de Sudoku en utilisant la méthode du backtracking.
    """
    def backtrack():
        # Trouver la prochaine case vide
        for row in range(9):
            for col in range(9):
                if grille[row][col] == 0:
                    # Essayer les chiffres de 1 à 9
                    for num in range(1, 10):
                        if est_valide(grille, row, col, num):
                            grille[row][col] = num
                            if backtrack():
                                return True
                            grille[row][col] = 0  # Backtrack
                    return False
        return True  # Toutes les cases sont remplies
    
    backtrack()

# Fonction principale
print("Bienvenue dans le programme de Sudoku !")
print("Entrez la grille de Sudoku (9 lignes de 9 chiffres ou '.' pour les cases vides).")
grille = saisir_grille_sudoku()

print("\nVoici la grille de Sudoku que vous avez entrée :")
afficher_grille_sudoku(grille)

# Résoudre la grille
resoudre_sudoku(grille)

print("\nVoici la grille de Sudoku résolue :")
afficher_grille_sudoku(grille)

