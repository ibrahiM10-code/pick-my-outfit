from db_manager import BaseDatos
from CTkMessagebox import CTkMessagebox as msgbox
import customtkinter as ctk

class NuevaRopa(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.bd = BaseDatos()
        self.geometry("700x500")
        self.title("Nueva Ropa.")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.input_nombre = ctk.CTkEntry(self, width=200, height=50 ,placeholder_text="Ingresa el nombre de la ropa.")
        self.input_nombre.grid(row=0, column=1)
        self.input_color = ctk.CTkEntry(self, width=200, height=50 ,placeholder_text="Ingresa el color de la ropa.")
        self.input_color.grid(row=1, column=1)
        self.input_categoria = ctk.CTkOptionMenu(self, width=200, height=50 ,values=self.bd.categorias_ropa())
        self.input_categoria.grid(row=2, column=1)
        self.nombre_ropa = self.input_nombre.get()
        self.agregar_ropa = ctk.CTkButton(self, text="Agregar ropa.", width=200, height=50, command=self.nueva_ropa)
        self.agregar_ropa.grid(row=3, column=1)
        self.mainloop()

    def nueva_ropa(self):
        self.id_categoria = self.bd.numero_categoria(self.input_categoria.get())
        try:
            self.bd.agregar_ropa(nombre=self.input_nombre.get() + " " + self.input_color.get(), categoria=self.id_categoria)
            msgbox(title="¡Nueva Ropa agregada!", icon="check", option_1="Ok", message=self.input_nombre.get() + " " + self.input_color.get() + " ha sido agregado correctamente.")
        except Exception as e:
            print("Ha ocurrido un error al agregar una nueva ropa.", e)
        