"""
interfaz_ctk.py

Implementa la interfaz gráfica de usuario (GUI) usando CustomTkinter
para realizar conversiones de unidades. Integra funciones de conversión
desde el módulo `conversion_logic`.

Autor: Alejandro Cortés
Versión: 1.0
"""


# ────────────────────── IMPORTACIONES ──────────────────────
from enum import Enum, auto
import logging
from tkinter import TclError

from colorama import Fore, Style, init
import customtkinter as ctk
from screeninfo import get_monitors

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
    convert_data,
)


# ────────────────────── VARIABLES GLOBALES / CONFIGURACION ──────────────────────
init (autoreset=True)
BOLD = Style.BRIGHT

class ConversionSystems(Enum):
    """
    Enumeración de sistemas de conversión disponibles.

    Attributes:
        TEMPERATURA (int): Conversión de unidades de temperatura.
        LONGITUD (int): Conversión de unidades de longitud.
        MASA (int): Conversión de unidades de masa.
        VOLUMEN (int): Conversión de unidades de volumen.
        ENERGIA (int): Conversión de unidades de energía.
        AREA (int): Conversión de unidades de área.
        VELOCIDAD (int): Conversión de unidades de velocidad.
        TIEMPO (int): Conversión de unidades de tiempo.
        POTENCIA (int): Conversión de unidades de potencia.
        ANGULOS (int): Conversión de unidades angulares.
        PRESION (int): Conversión de unidades de presión.
        DATOS (int): Conversión de unidades de datos.
    """

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

class ColorFormatter(logging.Formatter):
    """
    Formateador de logs que aplica colores según el nivel del mensaje.

    Niveles de color:
        DEBUG -> Magenta
        INFO -> Blanco
        WARNING -> Amarillo
        ERROR -> Rojo claro
        CRITICAL -> Rojo brillante (negritas)
    """
    COLORS = {
        logging.DEBUG: Fore.MAGENTA,
        logging.INFO: Fore.WHITE,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.LIGHTRED_EX,
        logging.CRITICAL: Fore.RED + BOLD,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        message = super().format(record)
        return f"{color}{message}{Style.RESET_ALL}"

# Configuración del logger
logger = logging.getLogger("conversor")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = ColorFormatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

screen_size = get_monitors()[0] # Tamaño real de la pantalla


# ────────────────────── CLASES DE INTERFAZ ──────────────────────
class App(ctk.CTk):
    """
    Clase principal de la aplicación de Conversor de Unidades.

    Esta clase gestiona la interfaz gráfica principal usando CustomTkinter.
    Crea la ventana, el encabezado con el título y el selector de modo
    claro/oscuro, y los botones para seleccionar el sistema de unidades
    a convertir.

    Hereda de:
        customtkinter.CTk: Clase base para ventanas de CustomTkinter.
    """

    def __init__(self):
        """
        Inicializa la ventana principal y sus elementos.

        Configura el tamaño de la ventana, crea los marcos de encabezado
        y contenido, añade el interruptor de modo claro/oscuro, y genera
        los botones correspondientes a cada sistema de unidades.
        """
        ctk.set_appearance_mode("system")
        super().__init__()
        self.title("Conversor de Unidades")
        win_width = int(screen_size.width * 0.3)
        win_height = int(screen_size.height * 0.4)
        self.win_position = (
            f"{int((screen_size.width - win_width) / 2.5)}+"
            f"{int((screen_size.height - win_height) / 2.5)}"
        )
        self.geometry(f"{win_width}x{win_height}+{self.win_position}")
        self.configure(padx = 20, pady=20)
        self.grid_rowconfigure(0, weight=1)     # Fila del header
        self.grid_rowconfigure(1, weight=1)     # Fila del content
        self.grid_columnconfigure(0, weight=1)  # Columna general
        #self.resizable("false", "false")

        try:
            self.iconbitmap("assets\\Conversor-Unidades-General.ico")
        except TclError as e:
            logging.error(
                "Advertencia: No se pudo cargar 'Conversor-Unidades-General.ico'"
                " para la ventana secundaria.\n{%s}", e
            )

        # ----- Frame encabezado -----
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

        # Título principal
        self.title_label = ctk.CTkLabel(
            master=self.header_frame,
            text="Conversor de Unidades",
            font=("Arial", 22, "bold"),
            text_color=("black", "white"),
            bg_color="transparent"
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")

        #Switch modo claro/oscuro
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

        # ----- Frame de contenido -----
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

        # Botones de sistemas
        for i in range(len(ConversionSystems)):
            row = i // 3
            col = i % 3
            system = ConversionSystems(i)
            self.selected_system = ctk.StringVar(value= ConversionSystems.TEMPERATURA.name)

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

        # Botón de salida
        self.exit_button = ctk.CTkButton(
            master=self.content_frame,
            text="Salir",
            text_color = ("gray10", "white"),
            fg_color = ("gray70", "gray30"),
            hover_color = ("gray60", "gray40"),
            border_width = 2,
            corner_radius = 10,
            font = ("Arial", 16),
            command = self.destroy
        )
        self.exit_button.grid(row=5, column=1, pady=4)

    def toogle_appearance_mode(self):
        """Cambia entre modo claro y oscuro de la interfaz."""
        if self.switch_light_dark.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def instanciar_ventana(self, value):
        """
        Crea una ventana secundaria para el sistema de unidades elegido.

        Args:
            value (str): Nombre del sistema de unidades seleccionado.
        """
        SecApp(master = self, conversion_system = value)

class SecApp(ctk.CTkToplevel):
    """
    Clase secundaria de la aplicación de Conversor de Unidades.
    
    Esta clase gestiona las ventanas emergentes adicionales qe se instancian al seleccionar
    alguna de las opciones de sistemas dentro de la ventana principal usando customtkinter.
    Crea una ventana con la unidad de entrada y de salida, un cuadro para ingresar el valor
    y el valor convertido en la parte inferior, asi como un botón para volver.

    Hereda de:
        customtkinter.CTkToplevel: Clase para gestionar ventanas secundarias.
    """

    def __init__(self, master = None, conversion_system = "Conversión de ..."):
        """
        Inicializa la ventana secundaria y sus elementos.
        Configura el tamaño de la ventana y su posición, y crea los marcos para contener a los
        elementos, que son el cuadro de entrada, los cuadros de opciones para las unidades,
        la etiqueta del valor de salida y el botón para volver.
        Args:
            master: El objeto al que pertenece o en el que se aloja. Por defecto se determina None.
            conversion_system: Cadena que indica el tipo de sistema de conversión.
            Por defecto se establece como "Conversión de ...".
        """
        super().__init__(master = master)
        self.conversion_system = conversion_system
        self.title("Conversión de " + self.conversion_system.title())
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        win_width = int(screen_width * 0.2)
        win_height = int(screen_height * 0.4)
        self.win_position = (
            f"{int((screen_width-win_width)/2.5)}+"
            f"{int((screen_height-win_height)/2.5)}"
        )
        self.geometry(f"{win_width}x{win_height}+{self.win_position}")
        self.update_idletasks()
        master.update_idletasks()
        self.grab_set()
        self.focus_set()
        self.resizable("false","false")

        # ----- Frame Principal -----
        self.main_frame = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título de Sistema
        self.title_label = ctk.CTkLabel(
            master = self.main_frame,
            text = self.conversion_system,
            font=("Arial", 18, "bold"),
            text_color=("black", "white"),
            bg_color="transparent"
        )
        self.title_label.pack(pady=(0,20), fill="x")

        # Unidad de Entrada
        self.units_map = self.get_units_display_map(self.conversion_system)
        self.display_units = list(self.units_map.values())  # Para mostrar en el combobox

        self.entry_unity = self.get_logical_generic_unity(self.display_units[0])

        # ----- Frame de Entrada -----
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
            height=35,
            font=("Arial", 16),
            border_width=2,
            corner_radius=10,
            text_color=("black", "white"),
            fg_color=("white", "#2D2D2D"),
            placeholder_text_color=("gray40", "gray70")
        )
        self.entry_value_input.pack(fill="x", pady=(5,10))
        self.entry_value_input.bind(
            "<KeyRelease>",
            lambda event: self.convert_values()
        ) # Luego de soltar una tecla al ingresar en input.

        # Unidad de Salida
        self.exit_unity = self.get_logical_generic_unity(self.display_units[0])

        # ----- Frame de Salida -----
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

        # Valor de salida
        self.exit_value_label = ctk.CTkLabel(
            master = self.main_frame,
            text = "Esperando datos...",
            font=("Arial", 18),
            text_color=("gray10", "gray90"),
            fg_color=("white", "#1E1E1E"),
            corner_radius=10
        )
        self.exit_value_label.pack(pady=(10,20), fill="x")

        # Botón para volver
        self.back_button = ctk.CTkButton(
            master = self.main_frame,
            text = "Volver",
            command = self.cerrar_toplevel
        )
        self.back_button.pack(pady=(0, 10), fill="x")

    def get_units_display_map(self, conversion_system: str) -> dict[str, str]:
        """
        Devuelve un diccionario que mapea las unidades lógicas
        (usadas internamente) a sus nombres amigables para mostrar
        en la interfaz.

        Args:
            conversion_system: Nombre del sistema de conversión.

        Returns:
            dict: {unidad_logica: "Unidad Amigable"}
        """
        match ConversionSystems[conversion_system]:
            case ConversionSystems.TEMPERATURA:
                units = ["celsius", "farenheit", "kelvin"]
            case ConversionSystems.LONGITUD:
                units = [
                    "angstroms", "nanometros", "micrones", "milimetros", "centimetros",
                    "metros", "kilometros", "pies", "yardas", "millas", "millas_nauticas",
                    "anio_luz", "unidad_astronomica", "parsec"
                ]
            case ConversionSystems.MASA:
                units = [
                    "miligramos", "centigramos", "decigramos", "quilates", "gramos", "decagramos",
                    "hectogramos", "kilogramos", "toneladas_metricas", "onzas", "libras",
                    "piedra", "toneladas_cortas_eeuu", "toneladas_largas_uk"
                ]
            case ConversionSystems.VOLUMEN:
                units = [
                    "mililitros", "centimetros_cubicos", "litros", "metros_cubicos",
                    "cucharaditas_us", "cucharadas_us", "onzas_liquidas_us", "tazas_us",
                    "pintas_us", "cuartos_de_galon_us", "galones_us", "pulgadas_cubicas",
                    "pies_cubicos", "yardas_cubicas", "cucharaditas_uk", "cucharadas_uk",
                    "onzas_liquidas_uk", "pintas_uk", "cuartos_de_galon_uk", "galones_uk"
                ]
            case ConversionSystems.ENERGIA:
                units = [
                    "joules", "kilojulios", "calorias_termales", "calorias_alimentos",
                    "pie_libras", "unidades_termicas_britanicas", "kilovatio_horas"
                ]
            case ConversionSystems.AREA:
                units = [
                    "milimetros_cuadrados", "centimetros_cuadrados", "metros_cuadrados",
                    "hectareas", "kilometros_cuadrados", "pulgadas_cuadradas", "pies_cuadrados",
                    "yardas_cuadradas", "acres", "millas_cuadradas"
                ]
            case ConversionSystems.VELOCIDAD:
                units = [
                    "centimetros_por_segundo", "metros_por_segundo", "kilometros_por_hora",
                    "pies_por_segundo", "millas_por_hora", "nudos", "mach"
                ]
            case ConversionSystems.TIEMPO:
                units = [
                    "microsegundos", "milisegundos", "segundos", "minutos", "horas", "dias",
                    "semanas", "años"
                ]
            case ConversionSystems.POTENCIA:
                units = [
                    "vatios", "kilovatios", "caballos_de_fuerza_eeuu", "pie_libras_por_minuto",
                    "unidades_termicas_britanicas_por_minuto"
                ]
            case ConversionSystems.ANGULOS:
                units = ["grados", "radianes", "grados_centesimales"]
            case ConversionSystems.PRESION:
                units = [
                    "atmosferas", "bares", "kilopascales", "milimetros_de_mercurio", "pascales",
                    "libras_por_pulgada_cuadrada"
                ]
            case ConversionSystems.DATOS:
                units = [
                    "bits", "cuarteto", "bytes", "kilobits", "kibibits", "kilobytes", "kibibytes",
                    "megabits", "mebibits", "megabytes", "mebibytes", "gigabits", "gibibits",
                    "gigabytes", "gibibytes", "terabits", "tebibits", "terabytes", "tebibytes",
                    "petabits", "pebibits", "petabytes", "pebibytes", "exabits", "exbibits",
                    "exabytes", "exbibytes", "zettabits", "zebibits", "zettabytes", "zebibytes",
                    "yottabits", "yobibits", "yottabytes", "yobibytes"
                ]
            case _:
                units = []

        # Generar un diccionario {valor_logico: "Valor Amigable"}
        return {
            unit: (
                unit.replace("_", " ").capitalize()
                if "_" not in unit
                else " ".join(word.capitalize() for word in unit.split("_"))
            )
            for unit in units
        }

    # ----- Obtener Unidades Lógicas -----
    def get_logical_entry_unit(self) -> str:
        """
        Obtiene el nombre lógico de la unidad seleccionada en entrada.

        Returns:
            str: Obtiene el nombre de la unidad de entrada reconocible para el programa
        """
        selected_display_value = self.from_unity_combobox.get()

        # Invertir el diccionario para buscar la clave lógica
        reverse_units_map = {v: k for k, v in self.units_map.items()}
        selected_logical_value = reverse_units_map[selected_display_value]
        return selected_logical_value

    def get_logical_exit_unit(self) -> str:
        """
        Obtiene el nombre lógico de la unidad seleccionada en salida.

        Returns:
            str: Obtiene el nombre de la unidad de salida reconocible para el programa
        """
        selected_display_value = self.to_unity_combobox.get()

        # Invertir el diccionario para buscar la clave lógica
        reverse_units_map = {v: k for k, v in self.units_map.items()}
        selected_logical_value = reverse_units_map[selected_display_value]
        return selected_logical_value

    def get_logical_generic_unity(self, unity):
        """
        Obtiene el nombre de unidad en minúsculas y remplazando '_' por un espacio ' '.

        Returns:
            str: Obtiene el nombre de la unidad de entrada reconocible para el programa
        """
        value = unity
        return value.replace(" ", "_").lower()

    # ----- Establecer Unidades -----
    def set_entry_unity(self, unity) -> None:
        """
        Configura la unidad de entrada y actualiza el resultado.

        Args:
            unity (str): Unidad de entrada como cadena.
        """
        self.entry_unity = unity.lower()
        self.convert_values()

    def set_exit_unity(self, unity) -> None:
        """
        Configura la unidad de salida y actualiza el resultado.

        Args:
            unity (str): Unidad de salida como cadena.
        """
        self.exit_unity = unity.lower()
        self.convert_values()

    # ----- Conversión de Valores -----
    def convert_values(self) -> None:
        """
        Convierte el valor ingresado en el campo de entrada
        y actualiza la etiqueta de resultado.
        """
        if self.entry_value_input.get() == "":
            self.exit_value_label.configure(text = "Esperando datos...")
            return
        try:
            entry_value = float(self.entry_value_input.get())
        except ValueError:
            self.exit_value_label.configure(text="Error! Debes ingresar un Número válido!")
            return
        except OverflowError:
            self.exit_value_label.configure(text="Error! El número es demasiado grande!")
            return
        except MemoryError:
            self.exit_value_label.configure(text="Error: Memoria insuficiente.")
            return
        except TclError:
            self.exit_value_label.configure(text="Error interno de la interfaz gráfica.")
            return
        except (TypeError, AttributeError, RuntimeError) as e:
            logging.error("Error inesperado: {%s}", e)
            self.exit_value_label.configure(
                text=(
                    "Error inesperado: Revisa los datos ingresados. "
                    "En caso de persistir reinicia el programa"
                )
            )
            return

        conversion_map = {
            ConversionSystems.TEMPERATURA: convert_temperature,
            ConversionSystems.LONGITUD: convert_length,
            ConversionSystems.MASA: convert_mass,
            ConversionSystems.VOLUMEN: convert_volume,
            ConversionSystems.ENERGIA: convert_energy,
            ConversionSystems.AREA: convert_area,
            ConversionSystems.VELOCIDAD: convert_speed,
            ConversionSystems.TIEMPO: convert_time,
            ConversionSystems.POTENCIA: convert_power,
            ConversionSystems.ANGULOS: convert_angle,
            ConversionSystems.PRESION: convert_pressure,
            ConversionSystems.DATOS: convert_data
        }

        func = conversion_map.get(ConversionSystems[self.conversion_system])

        if func:
            exit_value = func(entry_value, self.entry_unity, self.exit_unity)
            self.exit_value_label.configure(text=str(exit_value))

    # ----- Control de Ventanas -----
    def cerrar_toplevel(self) -> None:
        """Cierra la ventana toplevel."""
        self.destroy()


# ────────────────────── INICIO DE LA INTERFAZ ──────────────────────
def start_interface() -> None:
    """Inicia la interfaz gráfica principal."""
    main_window = App()
    main_window.mainloop()


# ────────────────────── PUNTO DE EJECUCIÓN ──────────────────────
if __name__ == "__main__":
    start_interface()
