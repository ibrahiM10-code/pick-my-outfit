from new_clothes_interface import NuevaRopa
from new_outfit_interface import NuevoOutfit
from pick_my_outfit import OutfitDelDia
from outfits_list import MisOutfits
import customtkinter as ctk

class PantallaInicio(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Bienvenido.")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.boton_eleccion_outfit = ctk.CTkButton(self, width=140, height=60, text="Elige un outfit para hoy.", command=self.abrir_eleccion_outfit)
        self.boton_eleccion_outfit.grid(row=0, column=1)
        self.boton_nueva_ropa = ctk.CTkButton(self, width=140, height=60, text="Agregar ropa nueva.", command=self.abrir_nueva_ropa)
        self.boton_nueva_ropa.grid(row=1, column=1)
        self.boton_nuevo_outfit = ctk.CTkButton(self, width=140, height=60, text="Agregar nuevos outfits.", command=self.abrir_nuevo_outfit)
        self.boton_nuevo_outfit.grid(row=2, column=1)
        self.boton_listar_outfits = ctk.CTkButton(self, width=140, height=60, text="Ver mis outfits.", command=self.abrir_listar_outfits)
        self.boton_listar_outfits.grid(row=3, column=1)
        self.ventana_eleccion_outfit = None
        self.ventana_agregar_ropa = None
        self.ventana_agregar_outfit = None
        self.ventana_ver_outfits = None
        self.mainloop()

    def abrir_eleccion_outfit(self):
        if self.ventana_eleccion_outfit is None or not self.ventana_eleccion_outfit.winfo_exists():
            self.ventana_eleccion_outfit = OutfitDelDia()  
        else:
            self.ventana_eleccion_outfit.deiconify()
            self.ventana_eleccion_outfit.focus()

    def abrir_nueva_ropa(self):
        if self.ventana_agregar_ropa is None or not self.ventana_agregar_ropa.winfo_exists():
            self.ventana_agregar_ropa = NuevaRopa()  
        else:
            self.ventana_agregar_ropa.deiconify()
            self.ventana_agregar_ropa.focus()

    def abrir_nuevo_outfit(self):
        if self.ventana_agregar_outfit is None or not self.ventana_agregar_outfit.winfo_exists():
            self.ventana_agregar_outfit = NuevoOutfit()  
        else:
            self.ventana_agregar_outfit.deiconify()
            self.ventana_agregar_outfit.focus()

    def abrir_listar_outfits(self):
        if self.ventana_ver_outfits is None or not self.ventana_ver_outfits.winfo_exists():
            self.ventana_ver_outfits = MisOutfits()  
        else:
            self.ventana_ver_outfits.deiconify()
            self.ventana_ver_outfits.focus()