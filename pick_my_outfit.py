from db_manager import BaseDatos
from CTkMessagebox import CTkMessagebox as msgbox
import customtkinter as ctk

class OutfitDelDia(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.bd = BaseDatos()
        self.geometry("900x500")
        self.title("Tu Outfit para hoy.")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)
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
        self.label_tipo_clima = ctk.CTkLabel(self, text="Tipo de clima:")
        self.label_tipo_clima.grid(row=2, column=1)
        self.radio_clima_frio = ctk.CTkRadioButton(self, text="Frio", value="Frio", variable=self.climas)
        self.radio_clima_caluroso = ctk.CTkRadioButton(self, text="Caluroso", value="Caluroso", variable=self.climas)
        self.radio_clima_templado = ctk.CTkRadioButton(self, text="Templado", value="Templado", variable=self.climas)
        self.radio_clima_frio.grid(row=2, column=2)
        self.radio_clima_caluroso.grid(row=2, column=3)
        self.radio_clima_templado.grid(row=2, column=4)
        self.label_ocasion = ctk.CTkLabel(self, text="Ocasion")
        self.label_ocasion.grid(row=3, column=1)
        self.radio_ocasion_casual = ctk.CTkRadioButton(self, text="Casual", value="Casual", variable=self.ocasiones)
        self.radio_ocasion_formal = ctk.CTkRadioButton(self, text="Formal", value="Formal", variable=self.ocasiones)
        self.radio_ocasion_semiformal = ctk.CTkRadioButton(self, text="Semi-Formal", value="Semi-Formal", variable=self.ocasiones)
        self.radio_ocasion_casual.grid(row=3, column=2)
        self.radio_ocasion_formal.grid(row=3, column=3)
        self.radio_ocasion_semiformal.grid(row=3, column=4)
        self.mi_outfit = ctk.CTkButton(self, text="Genera mi outfit.", width=200, height=50, command=self.tu_outfit)
        self.mi_outfit.grid(row=4, column=1)
        self.mainloop()

    def tu_outfit(self):
        try:
            oft = self.bd.elige_outfit(clima=self.climas.get(), ocasion=self.ocasiones.get())
            final_outfit = [oft[conjunto] for conjunto in range(len(oft))]
            msgbox(title="¡Este es tu outfit!", option_1="Ok", message=f"Tu outfit para hoy es: {' + '.join(final_outfit)}")
        except Exception as err:
            print("Ha ocurrido un error al elegir un outfit." , err)