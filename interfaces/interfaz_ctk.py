# @file interfaz_ctk.py
# @brief Interfaz de Usuario para modo CTK, se basa en la libreria CustomTkinter para mostrar ventana y objetos.
# @author Alejandro Cortés
# @version 0.6

#region Importaciones
import customtkinter as ctk
from logic.conversion_logic import (
    convert_temperature,
    convert_lenght,
    convert_mass,
    convert_volume,
    convert_energy,
    convert_area,
    convert_speed,
    convert_time,
    convert_power,
    convert_angle,
    convert_pressure,
    convert_data
)
#endregion

#region Variables e inicializaciones
#endregion

# -------------------------Funciones de utilidad-------------------------

def start_interface():
    #Ventana principal
    principal = ctk.CTk()
    principal.title("Ventana principal")
    principal.geometry("256x256+256+256")

    #Ventana secundaria
    secundaria = ctk.CTkToplevel()
    secundaria.title("Ventana secundaria")
    secundaria.geometry("256x256+720+256")

    principal.mainloop()

start_interface()