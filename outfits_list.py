from CTkMessagebox import CTkMessagebox as msgbox
from db_manager import BaseDatos
import customtkinter as ctk

class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bd = BaseDatos()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        lista_nombres = self.get_nombres()
        for nombre in range(len(lista_nombres)):
            self.boton = ctk.CTkButton(self, width=200, height=50, corner_radius=4, text=lista_nombres[nombre], fg_color="black", command=lambda n=lista_nombres[nombre]: self.mostrar_outfit(n))
            self.eliminar = ctk.CTkButton(self, fg_color="red", hover_color=("black", "black"),text="Eiminar outfit.")
            self.boton.grid(row=nombre, column=1, pady=20)
            self.eliminar.grid(row=nombre, column=2, pady=20)
        

    def get_nombres(self):
        lista = self.bd.lista_outfits()
        nombres = []
        prev = ""
        for i in range(len(lista)):
            if lista[i][0] != prev:
                nombres.append(lista[i][0])
                prev = lista[i][0]
            else:
                continue
        return nombres
    
    def mostrar_outfit(self, nombre_outfit: str):
        lista_conjunto = self.bd.filtro_outfit(nombre_outfit)
        outfit_seleccionado = [lista_conjunto[conjunto] for conjunto in range(len(lista_conjunto))]
        msgbox(title=nombre_outfit, option_1="Ok", message=' '.join(outfit_seleccionado))


class MisOutfits(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.my_frame = MyFrame(master=self, width=900, height=350, fg_color="transparent")
        self.my_frame.grid(row=1, column=1, columnspan=2)
        self.mainloop()

