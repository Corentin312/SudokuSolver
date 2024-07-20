import numpy as np
import itertools

import keyboard

def attendre_espace():
    print("Appuyez sur la touche espace pour continuer...")
    keyboard.wait('space')

# Generer la liste des solutions possibles pour une case donnee
def generate_list_possible_case(initial_case: np.array) -> list:
    possible_case = []
    possible_digits = [i for i in range(1, 10) if i not in initial_case]
    possible_indices = [(i, j) for i in range(3) for j in range(3) if initial_case[i][j] == 0]
    # Générer toutes les combinaisons possibles
    perm_digits = list(itertools.permutations(possible_digits))
    # Créer une liste pour stocker les différentes configurations de la case
    possible_case = []
    # Pour chaque combinaison, créer une nouvelle configuration de la case
    for perm in perm_digits:
        new_case = initial_case.copy()  # Copier la grille initiale
        for k in range(len(perm)):
            i, j = possible_indices[k]
            new_case[i, j] = perm[k]
        possible_case.append(new_case)
    return possible_case    


def verify_column(grid: np.array, column: int) -> bool:
    column_values = grid[:, column]
    return all(np.sum(column_values == i) <= 1 for i in range(1, 10))

def verify_row(grid: np.array, row: int) -> bool:
    row_values = grid[row, :]
    return all(np.sum(row_values == i) <= 1 for i in range(1, 10))

def solve(initial_grid: np.array) -> np.array:
    possible_grid = [initial_grid]
    # Pour chaque case de la grille
    for k in range(9):
        i, j = k//3, k%3
        print("Analyzing case", i+1, j+1)
        print("Number of possible grids:", len(possible_grid))
        # Générer la liste des configurations possibles pour la case
        case = initial_grid[3*i:3*(i+1), 3*j:3*(j+1)]
        possible_cases = generate_list_possible_case(case)
        new_possible_grid = []
        # Pour chaque configuration de grille possible
        for grid in possible_grid:
            # Pour chaque configuration possible de la case
            for possible_case in possible_cases:
                new_grid = grid.copy()
                # Mettre à jour la grille
                new_grid[3*i:3*(i+1), 3*j:3*(j+1)] = possible_case
                # Vérifier si la configuration est valide
                are_valid_rows = all(verify_row(new_grid, row) for row in range(3*i, 3*(i+1)))
                are_valid_columns = all(verify_column(new_grid, column) for column in range(3*j, 3*(j+1)))
                if are_valid_rows and are_valid_columns:
                    # Si la configuration est valide, l'ajouter à la liste des configurations possibles
                    new_possible_grid.append(new_grid)
        possible_grid = new_possible_grid        
    return possible_grid



# case = initial_grid[0:3, 0:3]
# possible_case = generate_list_possible_case(case)
# print(len(possible_case))
# valid_pos = 0
# for case in possible_case:
#     print(case)
#     new_grid = initial_grid.copy()
#     new_grid[0:3, 0:3] = case
#     valid_rows = all(verify_row(new_grid, row) for row in range(3))
#     print(valid_rows)
#     valid_columns = all(verify_column(new_grid, column) for column in range(3))
#     print(valid_columns)
#     if valid_rows and valid_columns:
#         valid_pos += 1
#     attendre_espace()
# print(valid_pos)

if __name__ == "__main__":
    initial_grid = np.array([[0, 0, 0, 3, 0, 7, 4, 0, 0],
                             [9, 0, 0, 0, 0, 4, 0, 0, 8],
                             [3, 7, 0, 0, 0, 0, 0, 6, 0],
                             [8, 2, 0, 9, 0, 0, 6, 0, 0],
                             [0, 0, 1, 2, 0, 0, 9, 0, 4],
                             [0, 4, 0, 0, 3, 8, 0, 5, 0],
                             [2, 0, 8, 6, 9, 0, 7, 0, 0],
                             [0, 9, 0, 0, 0, 0, 0, 0, 0],
                             [7, 5, 0, 0, 0, 0, 0, 0, 6]])
    possible_grid = solve(initial_grid)
    print(len(possible_grid))
    print(possible_grid[0])
    print(possible_grid)
