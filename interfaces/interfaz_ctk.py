# @file interfaz_ctk.py
# @brief Interfaz de Usuario para modo CTK, se basa en la libreria CustomTkinter para mostrar ventana y objetos.
# @author Alejandro Cortés
# @version 0.7

#region Importaciones
import customtkinter as ctk
from enum import Enum, auto


from logic.conversion_logic import (
    convert_temperature,
    convert_length,
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

from screeninfo import get_monitors
#endregion

class ConversionSystems(Enum):
    TEMPERATURA = 0
    LONGITUD    = auto()
    MASA        = auto()
    VOLUMEN     = auto()
    ENERGIA     = auto()
    AREA        = auto()
    VELOCIDAD   = auto()
    TIEMPO      = auto()
    POTENCIA    = auto()
    ANGULOS     = auto()
    PRESION     = auto()
    DATOS       = auto()
screen_size = get_monitors()[0]

class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("system")
        super().__init__()
        self.title("Conversor de Unidades")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        win_width = int(screen_width * 0.3)
        win_height = int(screen_height * 0.4)
        self.win_position = f"{int((screen_width-win_width)/2.5)}+{int((screen_height-win_height)/2.5)}"
        self.geometry(f"{win_width}x{win_height}+{self.win_position}")   
        self.configure(padx = 20, pady=20)
        self.grid_rowconfigure(0, weight=1)     # Fila del header
        self.grid_rowconfigure(1, weight=1)     # Fila del content
        self.grid_columnconfigure(0, weight=1)  # Columna general
        self.resizable("false", "false")
        #Crear frame encabezado
        self.header_frame = ctk.CTkFrame(
            master=self,
            border_width=2,
            border_color=("gray70", "gray30"),
            corner_radius=18,
            fg_color=("white", "#1E1E1E")
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")
        self.header_frame.columnconfigure(0, weight=1)
        self.header_frame.columnconfigure(1, weight=10)  # Centrada
        self.header_frame.columnconfigure(2, weight=1)
        self.header_frame.rowconfigure(0, weight=1)
        
        #Titulo de ventana principal
        self.title_label = ctk.CTkLabel(
            master=self.header_frame,
            text="Conversor de Unidades",
            font=("Arial", 22, "bold"),
            text_color=("black", "white"),
            bg_color="transparent"
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")

        #Switch modo luz/oscuridad
        self.appearance_mode = ctk.BooleanVar(value=ctk.get_appearance_mode() == "Dark")
        self.switch_light_dark = ctk.CTkSwitch(
            master=self.header_frame,
            text="Modo oscuro",
            width=60,
            height=25,
            fg_color=("#00cfff", "#005f8f"),
            bg_color="transparent",
            text_color=("black", "white"),
            font=("Arial", 12, "bold"),
            variable= self.appearance_mode,
            command = self.toogle_appearance_mode
        )        
        self.switch_light_dark.grid(row=0, column=2, padx=8, pady=8, sticky="nse")
        
        #Frame de contenido
        self.content_frame = ctk.CTkFrame(
            master=self,
            border_width=2,
            border_color=("gray70", "gray30"),
            corner_radius=18,
            fg_color=("white", "#1E1E1E")
        )
        self.content_frame.grid(row=1, column=0, pady=(20, 10), sticky="nsew")
        self.content_frame.columnconfigure((0,1,2), weight=1)
        self.content_frame.rowconfigure((0,1,2,3), weight=1)
        
        #Crear Botones de Sistemas
        for i in range(len(ConversionSystems)):
            row = i // 3
            col = i % 3
            system = ConversionSystems(i)
            self.selected_system = ctk.StringVar(value= ConversionSystems.TEMPERATURA.name) #Gestionar que Sistema de unidades se utiliza
            
            button = ctk.CTkButton(
            master = self.content_frame,
            text = system.name.title(),
            fg_color=("#007ACC", "#1E90FF"),
            hover_color=("#A0CFFF", "#005F99"),
            border_color=("black", "white"),
            text_color=("black", "white"),
            corner_radius=8,
            font=("Arial", 16, "bold"),
            command = lambda s=system: self.instanciar_ventana(s.name)
            )
            button.grid(row=row, column=col, pady= 20, padx=8)
        
        #Boton de salida
        self.exit_button = ctk.CTkButton(
            master=self.content_frame,
            text="Salir",
            text_color = ("gray10", "white"),
            fg_color = ("gray70", "gray30"),
            hover_color = ("gray60", "gray40"),
            border_width = 2,
            corner_radius = 10,
            font = ("Arial", 16),
            command = lambda : self.destroy()
        )
        self.exit_button.grid(row=5, column=1, pady=4)
    
    def toogle_appearance_mode(self):
        if self.switch_light_dark.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
    
    def instanciar_ventana(self, value):
        SecApp(master = self, conversion_system = value)
        
    def on_resize(self, event):
        print(f"Tamaño actual: {event.width}x{event.height}")

class SecApp(ctk.CTkToplevel):
    def __init__(self, master = None, conversion_system = "Conversión de ..."):
        super().__init__(master = master)
        self.conversion_system = conversion_system
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        win_width = int(screen_width * 0.2)
        win_height = int(screen_height * 0.4)
        self.win_position = f"{int((screen_width-win_width)/2.5)}+{int((screen_height-win_height)/2.5)}"
        self.geometry(f"{win_width}x{win_height}+{self.win_position}")
        self.title("Conversión de " + self.conversion_system.title())
        self.grab_set()
        self.focus_set()
        self.resizable("false","false")
        
        #Frame Principal
        self.main_frame = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        #Titulo de Sistema
        self.title_label = ctk.CTkLabel(
            master = self.main_frame,
            text = self.conversion_system,
            font=("Arial", 18, "bold"),
            text_color=("black", "white"),
            bg_color="transparent"
        )
        self.title_label.pack(pady=(0,20), fill="x")
        
        
        #Unidad de Entrada
        self.units_map = self.get_units_display_map(self.conversion_system)
        self.display_units = list(self.units_map.values())  # Para mostrar en el combobox

        self.entry_unity = self.get_logical_generic_unity(self.display_units[0])
        
        self.entry_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color="transparent"
        )
        self.entry_frame.pack(fill="x", pady=(0, 10))
        
        self.from_unity_label = ctk.CTkLabel(
            master=self.entry_frame, 
            text = "Unidad de entrada",
            font=("Arial", 16),
            fg_color=("white", "#1E1E1E"),
            text_color=("black", "white"),
            corner_radius=10
        )
        self.from_unity_label.pack(anchor="w")
        
        self.from_unity_combobox = ctk.CTkComboBox(
            master = self.entry_frame,
            values = self.display_units,
            #width = max_lenght * 10 ,
            height = 35,
            button_color = ("gray75", "gray25"),
            button_hover_color=("gray60", "gray40"),
            dropdown_fg_color=("white", "black"),
            dropdown_font=("Helvetica", 14),
            text_color = ("black", "white"),
            font = ("Arial", 16),
            state = "normal",
            justify="center",
            command = lambda x : self.set_entry_unity(self.get_logical_entry_unit())
        )
        self.from_unity_combobox.pack(pady=(5, 0), fill ="x")
        
        self.entry_value_label = ctk.CTkLabel(
            master=self.main_frame, 
            text = "Valor",
            font=("Arial", 16),
            fg_color=("white", "#1E1E1E"),
            text_color=("black", "white"),
            corner_radius=10
        )
        self.entry_value_label.pack(anchor="w", pady=(10,0))
        
        self.entry_value_input = ctk.CTkEntry(
            master=self.main_frame,
            placeholder_text="Ingrese su valor",
            #width=250,
            height=35,
            font=("Arial", 16),
            border_width=2,
            corner_radius=10,
            text_color=("black", "white"),
            fg_color=("white", "#2D2D2D"),
            placeholder_text_color=("gray40", "gray70")
        )
        self.entry_value_input.pack(fill="x", pady=(5,10))
        self.entry_value_input.bind("<KeyRelease>", lambda event: self.convert_values()) #Luego de soltar una tecla al ingresar en input.
        
        #Unidad de Salida
        self.exit_unity = self.get_logical_generic_unity(self.display_units[0])
        
        self.exit_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color="transparent"
        )
        self.exit_frame.pack(fill="x", pady=(0,10))
        
        self.to_unity_label = ctk.CTkLabel(
            master=self.exit_frame, 
            text = "Unidad de salida",
            font=("Arial", 16),
            fg_color=("white", "#1E1E1E"),
            text_color=("black", "white"),
            corner_radius=10
        )
        self.to_unity_label.pack(anchor="w")
        
        self.to_unity_combobox = ctk.CTkComboBox(
            master = self.exit_frame,
            values = self.display_units,
            #width = max_lenght * 10 ,
            height = 35,
            button_color = ("gray75", "gray25"),
            button_hover_color=("gray60", "gray40"),
            dropdown_fg_color=("white", "black"),
            dropdown_font=("Helvetica", 14),
            text_color = ("black", "white"),
            font = ("Arial", 16),
            state = "normal",
            justify="center",
            command = lambda x : self.set_exit_unity(self.get_logical_exit_unit())
        )
        self.to_unity_combobox.pack(pady=(5, 0), fill ="x")
        
        #Valor de salida
        self.exit_value_label = ctk.CTkLabel(
            master = self.main_frame,
            text = "Esperando datos...",
            font=("Arial", 14),
            text_color=("gray10", "gray90"),
        )
        self.exit_value_label.pack(pady=(10,20), fill="x")

        #Boton para volver
        self.back_button = ctk.CTkButton(
            master = self.main_frame,
            text = "Volver",
            command = self.cerrar_toplevel 
        )
        self.back_button.pack(pady=(0, 10), fill="x")
    
    def get_units_display_map(self, conversion_system):
        match ConversionSystems[conversion_system]:
            case ConversionSystems.TEMPERATURA:
                units = ["celsius", "farenheit", "kelvin"]
            case ConversionSystems.LONGITUD:
                units = ["angstroms", "nanometros", "micrones", "milimetros", "centimetros", "metros", "kilometros", "pies", "yardas", "millas", "millas_nauticas", "anio_luz", "unidad_astronomica", "parsec"]
            case ConversionSystems.MASA:
                units = ["miligramos", "centigramos", "decigramos", "quilates", "gramos", "decagramos", "hectogramos", "kilogramos", "toneladas_metricas", "onzas", "libras", "piedra", "toneladas_cortas_eeuu", "toneladas_largas_uk"]
            case ConversionSystems.VOLUMEN:
                units = ["mililitros", "centimetros_cubicos", "litros", "metros_cubicos", "cucharaditas_us", "cucharadas_us", "onzas_liquidas_us", "tazas_us", "pintas_us", "cuartos_de_galon_us", "galones_us", "pulgadas_cubicas", "pies_cubicos", "yardas_cubicas", "cucharaditas_uk", "cucharadas_uk", "onzas_liquidas_uk", "pintas_uk", "cuartos_de_galon_uk", "galones_uk"]
            case ConversionSystems.ENERGIA:
                units = ["joules", "kilojulios", "calorias_termales", "calorias_alimentos", "pie_libras", "unidades_termicas_britanicas", "kilovatio_horas"]
            case ConversionSystems.AREA:
                units = ["milimetros_cuadrados", "centimetros_cuadrados", "metros_cuadrados", "hectareas", "kilometros_cuadrados", "pulgadas_cuadradas", "pies_cuadrados", "yardas_cuadradas", "acres", "millas_cuadradas"]
            case ConversionSystems.VELOCIDAD:
                units = ["centimetros_por_segundo", "metros_por_segundo", "kilometros_por_hora", "pies_por_segundo", "millas_por_hora", "nudos", "mach"]
            case ConversionSystems.TIEMPO:
                units = ["microsegundos", "milisegundos", "segundos", "minutos", "horas", "dias", "semanas", "años"]
            case ConversionSystems.POTENCIA:
                units = ["vatios", "kilovatios", "caballos_de_fuerza_eeuu", "pie_libras_por_minuto", "unidades_termicas_britanicas_por_minuto"]
            case ConversionSystems.ANGULOS:
                units = ["grados", "radianes", "grados_centesimales"]
            case ConversionSystems.PRESION:
                units = ["atmosferas", "bares", "kilopascales", "milimetros_de_mercurio", "pascales", "libras_por_pulgada_cuadrada"]
            case ConversionSystems.DATOS:
                units = ["bits", "cuarteto", "bytes", "kilobits", "kibibits", "kilobytes", "kibibytes", "megabits", "mebibits", "megabytes", "mebibytes", "gigabits", "gibibits", "gigabytes", "gibibytes", "terabits", "tebibits", "terabytes", "tebibytes", "petabits", "pebibits", "petabytes", "pebibytes", "exabits", "exbibits", "exabytes", "exbibytes", "zettabits", "zebibits", "zettabytes", "zebibytes", "yottabits", "yobibits", "yottabytes", "yobibytes"]
            case _:
                units = []

        # Generar un diccionario {valor_logico: "Valor Amigable"}
        return {unit: unit.replace("_", " ").capitalize() if "_" not in unit else " ".join(word.capitalize() for word in unit.split("_")) for unit in units}

    def get_logical_entry_unit(self):
        selected_display_value = self.from_unity_combobox.get()

        # Invertir el diccionario para buscar la clave lógica
        reverse_units_map = {v: k for k, v in self.units_map.items()}
        selected_logical_value = reverse_units_map[selected_display_value]
        return selected_logical_value
    
    def get_logical_exit_unit(self):
        selected_display_value = self.to_unity_combobox.get()

        # Invertir el diccionario para buscar la clave lógica
        reverse_units_map = {v: k for k, v in self.units_map.items()}
        selected_logical_value = reverse_units_map[selected_display_value]
        return selected_logical_value
    
    def get_logical_generic_unity(self, unity):
        value = unity
        return value.replace(" ", "_").lower()

    
    def set_entry_unity(self, unity):
        self.entry_unity = unity.lower()
        self.convert_values()
    
    def set_exit_unity(self, unity):
        self.exit_unity = unity.lower()
        self.convert_values()

    def convert_values(self):
        exit_value = 0.0
        if self.entry_value_input.get() == "":
            self.exit_value_label.configure(text = "Esperando datos...")
            return
        try:
            entry_value = float(self.entry_value_input.get())
        except ValueError:
            self.exit_value_label.configure(text="Error! Debes ingresar un Número valido!")
        except Exception as e:
            self.exit_value_label.configure(text=f"Error inesperado: {e}")
        else:
            match ConversionSystems[self.conversion_system]:
                case ConversionSystems.TEMPERATURA:
                    exit_value = convert_temperature(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.LONGITUD:
                    exit_value = convert_length(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.MASA:
                    exit_value = convert_mass(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.VOLUMEN:
                    exit_value = convert_volume(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.ENERGIA:
                    exit_value = convert_energy(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.AREA:
                    exit_value = convert_area(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.VELOCIDAD:
                    exit_value = convert_speed(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.TIEMPO:
                    exit_value = convert_time(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.POTENCIA:
                    exit_value = convert_power(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.ANGULOS:
                    exit_value = convert_angle(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.PRESION:
                    exit_value = convert_pressure(entry_value, self.entry_unity, self.exit_unity)
                case ConversionSystems.DATOS:
                    exit_value = convert_data(entry_value, self.entry_unity, self.exit_unity)

            self.exit_value_label.configure(text=str(exit_value))
    

    def cerrar_toplevel(self):
        self.destroy()

def start_interface():
    main_window = App()
    main_window.mainloop()

if __name__ == "__main__":
    #start_interface()
    app = App()
    SecApp(master = app, conversion_system = "TEMPERATURA", position= "700+200")
    app.mainloop()