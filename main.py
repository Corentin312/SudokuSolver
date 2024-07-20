import tkinter as tk
import numpy as np
from solver import solve


class SudokuGrid(tk.Frame):
    def __init__(self, parent, size=9):
        super().__init__(parent)
        self.parent = parent
        self.size = size
        self.grid_cells = []
        self.initUI()

    def initUI(self):
        # Création des cellules de la grille
        for i in range(self.size):
            row = []
            for j in range(self.size):
                entry = tk.Entry(self, width=2, font=('Arial', 18, 'bold'), justify='center')
                entry.grid(row=i, column=j, padx= (1,10) if (j == 2 or j == 5) else 1, pady=(1,10) if (i == 2 or i == 5) else 1) 
                row.append(entry)
            self.grid_cells.append(row)
        
        

    def get_grid_values(self):
        # Récupérer les valeurs de la grille sous forme de liste 2D
        grid_values = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                value = self.grid_cells[i][j].get()
                if value == '':
                    row.append(0)
                else:
                    try:
                        num = int(value)
                        if 1 <= num <= 9:
                            row.append(num)
                        else:
                            row.append(0)
                            self.grid_cells[i][j].delete(0, tk.END)
                    except ValueError:
                        row.append(0)
                        self.grid_cells[i][j].delete(0, tk.END)
            grid_values.append(row)
        return grid_values

    def clear_grid(self):
        # Effacer toutes les entrées de la grille
        for i in range(self.size):
            for j in range(self.size):
                self.grid_cells[i][j].delete(0, tk.END)
                # Remettre la couleur du texte en noir
                self.grid_cells[i][j].config(fg='black')
                
    def submit_grid(self):
        # Récupérer les valeurs de la grille
        grid_values = self.get_grid_values()
        # Afficher les valeurs de la grille
        print(grid_values)
        initial_grid = np.array(grid_values)
        possible_grid = solve(initial_grid)
        solution = possible_grid[0]
        # Afficher la solution dans la grille en bleu sauf les cases de la grille initiale
        for i in range(self.size):
            for j in range(self.size):
                if initial_grid[i][j] == 0:
                    self.grid_cells[i][j].delete(0, tk.END)
                    self.grid_cells[i][j].insert(0, str(solution[i][j]))
                    self.grid_cells[i][j].config(fg='blue')
        
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Sudoku Grid")

    # Créer une instance de la classe SudokuGrid
    sudoku_grid = SudokuGrid(root)
    sudoku_grid.pack(padx=10, pady=10)

    # Créer un bouton pour soumettre la grille qui appelle la méthode submit_grid
    submit_button = tk.Button(root, text="Submit", command=sudoku_grid.submit_grid)
    submit_button.pack()
    root.mainloop()
