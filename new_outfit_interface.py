from db_manager import BaseDatos
from CTkMessagebox import CTkMessagebox as msgbox
import customtkinter as ctk

class NuevoOutfit(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.bd = BaseDatos()
        self.geometry("900x500")
        self.title("Nuevo Outfit.")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.climas = ctk.StringVar(value="Frio")
        self.ocasiones = ctk.StringVar(value="Casual")
        self.poleras = ctk.StringVar(value="Polera")
        self.pantalones = ctk.StringVar(value="Pantalon")
        self.polerones = ctk.StringVar(value="Poleron")
        self.camisas = ctk.StringVar(value="Camisa")
        self.parkas = ctk.StringVar(value="Parka")
        self.input_nombre = ctk.CTkEntry(self,width=200, height=50,placeholder_text="Ingresa el nombre de este outfit.")
        self.input_nombre.grid(row=1, column=1)
        self.radio_clima_frio = ctk.CTkRadioButton(self, text="Frio", value="Frio", variable=self.climas)
        self.radio_clima_caluroso = ctk.CTkRadioButton(self, text="Caluroso", value="Caluroso", variable=self.climas, command=self.filtra_calor)
        self.radio_clima_templado = ctk.CTkRadioButton(self, text="Templado", value="Templado", variable=self.climas, command=self.filtra_clima)
        self.radio_clima_frio.grid(row=2, column=1)
        self.radio_clima_caluroso.grid(row=2, column=2)
        self.radio_clima_templado.grid(row=2, column=3)
        self.radio_ocasion_casual = ctk.CTkRadioButton(self, text="Casual", value="Casual", variable=self.ocasiones)
        self.radio_ocasion_semiformal = ctk.CTkRadioButton(self, text="Semi-Formal", value="Semi-Formal", variable=self.ocasiones, command=self.filtra_semi_formal)
        self.radio_ocasion_casual.grid(row=4, column=1)
        self.radio_ocasion_semiformal.grid(row=4, column=2)
        self.select_parka = ctk.CTkOptionMenu(self, width=200, height=50,values=self.bd.filtro_ropa(5), variable=self.parkas)
        self.select_poleron = ctk.CTkOptionMenu(self, width=200, height=50, values=self.bd.filtro_ropa(3), variable=self.polerones)
        self.select_camisa = ctk.CTkOptionMenu(self, width=200, height=50, values=self.bd.filtro_ropa(4), variable=self.camisas)
        self.select_polera = ctk.CTkOptionMenu(self, width=200, height=50, values=self.bd.filtro_ropa(1), variable=self.poleras)
        self.select_pantalon = ctk.CTkOptionMenu(self, width=200, height=50, values=self.bd.filtro_ropa(2), variable=self.pantalones)
        self.select_parka.grid(row=1, column=5)
        self.select_poleron.grid(row=2, column=5)
        self.select_camisa.grid(row=3, column=5)
        self.select_polera.grid(row=4, column=5)
        self.select_pantalon.grid(row=5, column=5)
        self.btn_agregar_outfit = ctk.CTkButton(self, text="Agregar outfit.", width=200, height=50, command=self.agrega_outfit)
        self.btn_agregar_outfit.grid(row=6, column=1)
        self.mainloop()

    def revisa_ropa(self):
        ropas = [self.poleras.get(), self.pantalones.get()]
        ropas_opcionales = [(self.camisas, "Camisa"), (self.polerones, "Poleron"), (self.parkas, "Parka")]
        ropas.extend([ropa.get() for ropa, por_defecto in ropas_opcionales if ropa.get() != por_defecto])
        return ropas
    
    def agrega_outfit(self):
        ropas = self.revisa_ropa()
        ropas_ids = self.bd.ropas_id(ropas)
        outfit_id = self.bd.ultimo_outfit()
        try:
            self.bd.agregar_outfit(nombre=self.input_nombre.get(), clima=self.climas.get(), ocasion=self.ocasiones.get())
            for i in range(len(ropas_ids)):
                self.bd.agregar_conjunto(id_outfit=outfit_id, id_ropa=ropas_ids[i])
            msgbox(title="¡Nuevo outfit agregado!", message="Este outfit ha sido agregado correctamente", icon="check", option_1="Ok")
        except Exception as e:
            print("Ha ocurrido un error al agregar un nuevo outfit:", e)
            
    def filtra_clima(self):
        self.select_parka.destroy()
    
    def filtra_semi_formal(self):
        self.select_parka.destroy()

    def filtra_calor(self):
        self.select_parka.destroy()
        self.select_poleron.destroy()