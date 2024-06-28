import tkinter as tk
from tkinter import messagebox
import time

class JuegoDeRanas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de las Ranas Saltarinas")
        self.show_presentation()

    def show_presentation(self):
        self.clear_window()

        title = tk.Label(self.root, text="Juego de las Ranas Saltarinas", font=('Arial', 24))
        title.pack(pady=20)
        
        creators = tk.Label(self.root, text="Creadores: Josué Justavino y Angelika Pérez", font=('Arial', 18))
        creators.pack(pady=10)
        
        start_button = tk.Button(self.root, text="Iniciar Juego", font=('Arial', 18), command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        self.clear_window()
        self.init_game_variables()
        self.setup_game_ui()
        self.root.after(1000, self.actualizar_tiempo)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def init_game_variables(self):
        self.turno = "verde"
        self.estado = ['m', 'm', 'm', ' ', 'v', 'v', 'v']  # 'm' para marrón, 'v' para verde, ' ' para piedra vacía
        self.tiempo = 0
        self.start_time = time.time()

    def setup_game_ui(self):
        self.canvas = tk.Canvas(self.root, width=700, height=100)
        self.canvas.grid(row=0, column=0, columnspan=7)
        
        self.botones = []
        for i in range(7):
            b = tk.Button(self.root, text='', font=('Arial', 18), width=8, height=4,
                          command=lambda i=i: self.mover_rana(i))
            b.grid(row=1, column=i)
            self.botones.append(b)
        
        self.actualizar_botones()
        
        self.label_tiempo = tk.Label(self.root, text=f"Tiempo: {self.tiempo}s", font=('Arial', 18))
        self.label_tiempo.grid(row=2, column=0, columnspan=7)
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.game_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Juego", menu=self.game_menu)
        self.game_menu.add_command(label="Reiniciar", command=self.reset_game)
        self.game_menu.add_command(label="Salir", command=self.root.quit)

    def actualizar_tiempo(self):
        self.tiempo += 1
        self.label_tiempo.config(text=f"Tiempo: {self.tiempo}s")
        self.root.after(1000, self.actualizar_tiempo)
    
    def actualizar_botones(self):
        self.canvas.delete("all")
        colores = {'m': 'brown', 'v': 'green', ' ': 'lightgrey'}
        for i in range(7):
            if self.estado[i] == 'm':
                self.canvas.create_oval(i * 100 + 10, 10, i * 100 + 90, 90, fill='saddlebrown')
            elif self.estado[i] == 'v':
                self.canvas.create_oval(i * 100 + 10, 10, i * 100 + 90, 90, fill='green')
            else:
                self.canvas.create_oval(i * 100 + 10, 10, i * 100 + 90, 90, fill='lightgrey')
    
    def mover_rana(self, i):
        if self.turno == "verde" and self.estado[i] == 'v':
            if i - 1 >= 0 and self.estado[i - 1] == ' ':
                self.estado[i], self.estado[i - 1] = self.estado[i - 1], self.estado[i]
                self.turno = "marrón"
            elif i - 2 >= 0 and self.estado[i - 2] == ' ' and self.estado[i - 1] == 'm':
                self.estado[i], self.estado[i - 2] = self.estado[i - 2], self.estado[i]
                self.turno = "marrón"
        elif self.turno == "marrón" and self.estado[i] == 'm':
            if i + 1 < 7 and self.estado[i + 1] == ' ':
                self.estado[i], self.estado[i + 1] = self.estado[i + 1], self.estado[i]
                self.turno = "verde"
            elif i + 2 < 7 and self.estado[i + 2] == ' ' and self.estado[i + 1] == 'v':
                self.estado[i], self.estado[i + 2] = self.estado[i + 2], self.estado[i]
                self.turno = "verde"
        self.actualizar_botones()
        self.verificar_ganador()
    
    def verificar_ganador(self):
        if self.estado == ['v', 'v', 'v', ' ', 'm', 'm', 'm']:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            messagebox.showinfo("Juego Terminado", f"¡Felicidades! Lo lograste en {elapsed_time:.2f} segundos.")
            self.reset_game()
    
    def reset_game(self):
        self.init_game_variables()
        self.actualizar_botones()

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoDeRanas(root)
    root.mainloop()
