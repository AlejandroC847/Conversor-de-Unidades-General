"""
interfaz_cli.py

Interfaz de usuario en modo consola para el conversor de unidades.
Utiliza impresión por consola y entrada de datos mediante `input()`.

Autor: Alejandro Cortés
Versión: 1.0
"""


# ────────────────────── IMPORTACIONES ──────────────────────
from enum import Enum, auto
import os
import logging

from colorama import Fore, Style, init

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

# ────────────────────── VARIABLES GLOBALES / CONFIGURACION ──────────────────────
# Inicializar colorama para colores en la terminal
init(autoreset=True)
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

    TEMPERATURA = 1
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

logging.basicConfig(
    level=logging.ERROR,
    format="%(message)s"
)


# ────────────────────── FUNCIONES DE UTILIDAD ──────────────────────
def _clear_console() -> None:
    """ 
    Limpia la consola de acuerdo al sistema operativo.
    - Windows: comando `cls`
    - Otros sistemas: comando `clear`
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def _enter_to_continue() -> None:
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input(f"{Fore.YELLOW}Presione enter para continuar...\n")

def _show_system_menu() -> None:
    """Muestra el menú principal de selección de sistema de conversión."""
    _clear_console()
    print(f"{Fore.BLUE}{Style.BRIGHT}----------Conversor de Unidades----------")
    for system in ConversionSystems:
        #Obtiene numero de sistema, nombre, y lo muestra solo con inicial en mayuscula
        print(f"{Fore.CYAN}{system.value}. {system.name.replace("_", " ").title()}")
    print(f"{Fore.CYAN}0. Salir")

def _match_unit(user_input: str, units: dict) -> str | None:
    """
    Busca la unidad en el diccionario de unidades y devuelve la clave si la encuentra.

    Args:
        user_input (str): Unidad ingresada por el usuario.
        units (dict): Todos los alias asociados a una unidad.

    Returns:
        str | None: Retorna la unidad seleccionada por su alias como cadena o
        None si no existe ese alias.
    """

    for unit, aliases in units.items():
        if user_input.lower() in aliases:
            return unit
    return None

def get_convert_data(system: str, units: dict) -> tuple[float, str, str] | None:
    """
    Solicita al usuario los datos necesarios para realizar una conversión
    entre unidades (valor y unidades de entrada y de salida).

    Args:
        system (str): Nombre del sistema de conversión actual (por ejemplo, 'Temperatura').
        units (dict): Diccionario que mapea unidades a sus posibles alias.

    Returns:
        tuple[float, str, str] | None: Valor, unidad de entrada y de salida, si la entrada es
        válida. Devuelve None: Si el usuario decide cancelar y volver al menú principal.
    """

    value = from_unit = to_unit = None

    while True:
        _clear_console()
        print(f"{Fore.BLUE}--------------------{system}--------------------")

        # Mostrar unidades
        for i, unit in enumerate(units, start=1):
            print(f"{Fore.CYAN}{i}. {str(unit).replace("_", " ").title()}")
        print(f"{Fore.CYAN}0. Volver al menu principal")

        #Solicitar unidad de entrada
        if from_unit is None:
            chosen_unit = input(f"{Fore.YELLOW}Unidad de entrada: {Style.RESET_ALL}")
            if chosen_unit == "0":
                return None
            from_unit = _match_unit(chosen_unit, units)
            if from_unit is None:
                logging.error("%sERROR: Unidad ingresada invalida", Fore.RED)
                _enter_to_continue()
                continue
        else:
            print(f"{Fore.YELLOW}Unidad de entrada: {Style.RESET_ALL}{from_unit}")

        #Solicitar valor
        if value is None:
            try:
                value = float(input(f"{Fore.YELLOW}Valor: {Style.RESET_ALL}"))
            except ValueError:
                logging.error("%sERROR: Debes ingresar un número válido", Fore.RED)
                _enter_to_continue()
                continue
            except OverflowError:
                logging.error("%sERROR: El número es demasiado grande", Fore.RED)
                _enter_to_continue()
                continue
        else:
            print(f"{Fore.YELLOW}Valor: {Style.RESET_ALL}{value}")

        #Solicitar unidad de salida
        if to_unit is None:
            chosen_unit = input(f"{Fore.YELLOW}Unidad de salida: {Style.RESET_ALL}")
            if chosen_unit == "0":
                return None
            to_unit = _match_unit(chosen_unit, units)
            if to_unit is None:
                logging.error("%sERROR: Unidad ingresada invalida", {Fore.RED})
                _enter_to_continue()
                continue
        else:
            print(f"{Fore.YELLOW}Unidad de entrada: {Style.RESET_ALL}{to_unit}")

        return value, from_unit, to_unit

def convert_system(
    system: str,
    units: dict[str, tuple[str, ...]],
    converter_function
) -> tuple[float, str, float, str]| None:
    """
    Interfaz genérica para conversión de unidades.

    Args:
        system (str): Nombre del sistema de unidades (ej. 'TEMPERATURA').
        units (dict[str, tuple[str, ...]]): Diccionario con el nombre interno 
            de la unidad como clave y sus alias como tupla de strings.
        converter_function (callable): Función que recibe (valor, unidad_origen, unidad_destino)
            y devuelve el valor convertido.

    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen, 
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """
    result = get_convert_data(system, units)

    if result is None:
        return None

    value, from_unit, to_unit = result
    converted_value = converter_function(value, from_unit, to_unit)
    return value, from_unit, converted_value, to_unit

def convert_temperature_interface() -> tuple[float, str, float, str] | None:
    """
    Llamada para conversión de temperaturas.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "celsius": ("1", "c", "celsius"),
        "kelvin": ("2", "k", "kelvin"),
        "fahrenheit": ("3", "f", "fahrenheit"),
    }
    return convert_system("TEMPERATURA", units, convert_temperature)

def convert_lenght_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de longitudes.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "angstroms": ("1", "å", "a", "an", "angstroms","angstrom", "ångström", "ångströms"),
        "nanometros": ("2", "nm", "nanometro", "nanometros", "nanometer", "nanometers"),
        "micrones": (
            "3", "µm", "um", "micrometro", "micrometros", "micron", "microns",
            "micrometer", "micrometers"
        ),
        "milimetros": ("4", "mm", "milimetro", "milimetros", "millimeter", "millimeters"),
        "centimetros": ("5", "cm", "centimetro", "centimetros", "centimeter", "centimeters"),
        "metros": ("6", "m", "metro", "meter", "metros", "meters"),
        "kilometros": ("7", "km", "kilometro", "kilometros", "kilometer", "kilometers"),
        "pulgadas": ("8", "in", "pulgada", "pulgadas", "inch", "inches"),
        "pies": ("9", "ft", "pie", "pies", "foot", "feet"),
        "yardas": ("10", "yd", "yarda", "yardas", "yard", "yards"),
        "millas": ("11", "mi", "milla", "millas", "mile", "miles"),
        "millas_nauticas": (
            "12", "nmi", "milla nautica", "millas nauticas", "nautical mile","nautical miles"
        ),
        "unidad_astronomica": (
            "13", "ua", "au", "unidad astronomica", "unidades astronomicas",
            "astronomical unit", "astronomical units"
        ),
        "anio_luz": (
            "14", "al", "ly", "año luz", "años luz", "light-year", "lightyear",
            "light-years", "lightyears"
        ),
        "parsec": ("15", "pc", "parsec", "parsecs")
    }

    return convert_system("LONGITUD", units, convert_length)

def convert_mass_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de masas.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "miligramos": ("1", "mg", "miligramo", "miligramos", "milligram", "milligrams"),
        "centigramos": ("2", "cg", "centigramo", "centigramos", "centigram", "centigrams"),
        "decigramos": ("3", "dg", "decigramo", "decigramos", "decigram", "decigrams"),
        "quilates": ("4", "ct", "q", "qi", "quilate", "quilates", "carat", "carats"),
        "gramos": ("5", "g", "gr", "gramo", "gramos", "gram", "grams"),
        "decagramos": ("6", "dag", "decagramo", "decagramos", "decagram", "decagrams"),
        "hectogramos": ("7", "hg", "hectogramo", "hectogramos", "hectogram", "hectograms"),
        "kilogramos": ("8", "kg", "kilogramo", "kilogramos", "kilogram", "kilograms"),
        "toneladas_metricas": (
            "9", "t", "ton", "tonelada", "toneladas", "tonelada metrica", "toneladas metricas",
            "tonne", "tonnes", "metric ton", "metric tons"
        ),
        "onzas": ("10", "oz", "onza", "onzas", "ounce", "ounces"),
        "libras": ("11", "lb", "libra", "libras", "pound", "pounds"),
        "piedra": ("12", "st", "piedra", "stone", "stones"),
        "toneladas_cortas_eeuu": (
            "13", "tc", "ston", "tonelada corta", "toneladas cortas", "short ton",
            "short tons", "us ton", "us tons"
        ),
        "toneladas_largas_uk": (
            "14", "lt", "tl", "tonelada larga", "toneladas largas", "long ton",
            "long tons", "uk ton", "uk tons"
        )
    }

    return convert_system("MASA", units, convert_mass)

def convert_volume_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de volumen.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "mililitros": ("1", "ml", "mililitro", "mililitros", "milliliter", "milliliters"),
        "centimetros_cubicos": (
            "2", "cm3", "cm^3", "centimetro cubico", "centimetros cubicos",
            "cubic centimeter", "cubic centimeters"
        ),
        "litros": ("3", "l", "lt", "litro", "litros", "liter", "liters"),
        "metros_cubicos": (
            "4", "m3", "m^3", "metro cubico", "metros cubicos", "cubic meter", "cubic meters"
        ),
        "cucharaditas_us": (
            "5", "tsp", "cucharadita", "cucharaditas", "teaspoon",
            "teaspoons", "us tsp", "us teaspoon"
        ),
        "cucharadas_us": (
            "6", "tbsp", "cucharada", "cucharadas", "tablespoon", "tablespoons",
            "us tbsp", "us tablespoon"
        ),
        "onzas_liquidas_us": (
            "7", "fl oz", "onza liquida", "onzas liquidas", "fluid ounce", "fluid ounces",
            "us fl oz", "us fluid ounce"
        ),
        "tazas_us": ("8", "cup", "taza", "tazas", "cups", "us cup", "us cups"),
        "pintas_us": ("9", "pt", "pinta", "pintas", "pint", "pints", "us pint", "us pints"),
        "cuartos_de_galon_us": (
            "10", "qt", "cuarto de galon", "cuartos de galon", "quart",
            "quarts", "us qt", "us quart"
        ),
        "galones_us": (
            "11", "gal", "galon", "galones", "gallon", "gallons", "us gal", "us gallon"
        ),
        "pulgadas_cubicas": (
            "12", "in3", "in^3", "pulgada cubica", "pulgadas cubicas", "cubic inch", "cubic inches"
        ),
        "pies_cubicos": (
            "13", "ft3", "ft^3", "pie cubico", "pies cubicos", "cubic foot", "cubic feet"
        ),
        "yardas_cubicas": (
            "14", "yd3", "yd^3", "yarda cubica", "yardas cubicas", "cubic yard", "cubic yards"
        ),
        "cucharaditas_uk": (
            "15", "uk tsp", "cucharadita uk", "cucharaditas uk", "uk teaspoon", "uk teaspoons"
        ),
        "cucharadas_uk": (
            "16", "uk tbsp", "cucharada uk", "cucharadas uk", "uk tablespoon", "uk tablespoons"
        ),
        "onzas_liquidas_uk": (
            "17", "uk fl oz", "onza liquida uk", "onzas liquidas uk",
            "uk fluid ounce", "uk fluid ounces"
        ),
        "pintas_uk": ("18", "uk pt", "pinta uk", "pintas uk", "uk pint", "uk pints"),
        "cuartos_de_galon_uk": (
            "19", "uk qt", "cuarto de galon uk", "cuartos de galon uk", "uk quart", "uk quarts"
        ),
        "galones_uk": ("20", "uk gal", "galon uk", "galones uk", "uk gallon", "uk gallons")
    }

    return convert_system("VOLUMEN", units, convert_volume)

def convert_energy_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de energía.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "joules": ("1", "j", "joule", "joules"),
        "kilojulios": ("2", "kj", "kilojulio", "kilojulios", "kilojoule", "kilojoules"),
        "calorias_termales": (
            "3", "cal", "caloria termal", "calorias termales", "caloría termal",
            "calorías termales", "thermal calorie", "thermal calories"
        ),
        "calorias_alimentos": (
            "4", "kcal", "Cal", "caloria alimento", "calorias alimentos", "caloría alimento",
            "calorías alimentos", "food calorie", "food calories", "kilocalorie", "kilocalories"
        ), # Nota: 'Cal' con 'C' mayúscula a menudo se refiere a kcal en nutrición
        "pie_libras": ("5", "ft-lb", "pie-libra", "pie-libras", "foot-pound", "foot-pounds"),
        "unidades_termicas_britanicas": (
            "6", "btu", "unidad termica britanica", "unidades termicas britanicas",
            "british thermal unit", "british thermal units"
        ),
        "kilovatio_horas": (
            "7", "kwh", "kw-h", "kilovatio hora", "kilovatio horas",
            "kilowatt-hour", "kilowatt-hours"
        )
    }

    return convert_system("ENERGIA", units, convert_energy)

def convert_area_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de área.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
    "milimetros_cuadrados": (
        "1", "mm2", "mm^2", "milimetro cuadrado", "milimetros cuadrados",
        "square millimeter", "square millimeters"
    ),
    "centimetros_cuadrados": (
        "2", "cm2", "cm^2", "centimetro cuadrado", "centimetros cuadrados",
        "square centimeter", "square centimeters"
    ),
    "metros_cuadrados": (
        "3", "m2", "m^2", "metro cuadrado", "metros cuadrados", "square meter", "square meters"
    ),
    "hectareas": ("4", "ha", "hectarea", "hectareas", "hectare", "hectares"),
    "kilometros_cuadrados": (
        "5", "km2", "km^2", "kilometro cuadrado", "kilometros cuadrados",
        "square kilometer", "square kilometers"
    ),
    "pulgadas_cuadradas": (
        "6", "in2", "in^2", "pulgada cuadrada", "pulgadas cuadradas", "square inch",
        "square inches"
    ),
    "pies_cuadrados": (
        "7", "ft2", "ft^2", "pie cuadrado", "pies cuadrados", "square foot", "square feet"
    ),
    "yardas_cuadradas": (
        "8", "yd2", "yd^2", "yarda cuadrada", "yardas cuadradas", "square yard", "square yards"
    ),
    "acres": ("9", "ac", "acre", "acres"),
    "millas_cuadradas": (
        "10", "mi2", "mi^2", "milla cuadrada", "millas cuadradas", "square mile", "square miles"
    )
}

    return convert_system("AREA", units, convert_area)

def convert_speed_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de velocidad.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "centimetros_por_segundo": (
            "1", "cm/s", "cmps", "centimetro por segundo", "centimetros por segundo",
            "centimeter per second", "centimeters per second"
        ),
        "metros_por_segundo": (
            "2", "m/s", "mps", "metro por segundo", "metros por segundo",
            "meter per second", "meters per second"
        ),
        "kilometros_por_hora": (
            "3", "km/h", "kph", "kilometro por hora", "kilometros por hora", "kilometer per hour",
            "kilometers per hour"
        ),
        "pies_por_segundo": (
            "4", "ft/s", "fps", "pie por segundo", "pies por segundo", "foot per second",
            "feet per second"
        ),
        "millas_por_hora": (
            "5", "mph", "milla por hora", "millas por hora", "mile per hour", "miles per hour"
        ),
        "nudos": ("6", "kn", "kt", "nudo", "nudos", "knot", "knots"),
        "mach": ("7", "mach", "ma") 
    }
    return convert_system("VELOCIDAD", units, convert_speed)

def convert_time_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de tiempo.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "microsegundos": (
            "1", "µs", "us", "microsegundo", "microsegundos", "microsecond", "microseconds"
        ),
        "milisegundos": ("2", "ms", "milisegundo", "milisegundos", "millisecond", "milliseconds"),
        "segundos": ("3", "s", "segundo", "segundos", "second", "seconds"),
        "minutos": ("4", "min", "minuto", "minutos", "minute", "minutes"),
        "horas": ("5", "h", "hr", "hora", "horas", "hour", "hours"),
        "dias": ("6", "d", "dia", "dias", "day", "days"),
        "semanas": ("7", "wk", "semana", "semanas", "week", "weeks"),
        "años": ("8", "yr", "año", "años", "year", "years")
    }

    return convert_system("TIEMPO", units, convert_time)

def convert_power_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de potencia.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "vatios": ("1", "w", "vatio", "vatios", "watt", "watts"),
        "kilovatios": ("2", "kw", "kilovatio", "kilovatios", "kilowatt", "kilowatts"),
        "caballos_de_fuerza_eeuu": (
            "3", "hp", "caballo de fuerza", "caballos de fuerza", "horsepower", "us hp"
        ),
        "pie_libras_por_minuto": (
            "4", "ft-lb/min", "pie-libra por minuto","pie-libras por minuto",
            "foot-pound per minute", "foot-pounds per minute"
        ),
        "unidades_termicas_britanicas_por_minuto": (
            "5", "btu/min", "unidad termica britanica por minuto",
            "unidades termicas britanicas por minuto", "british thermal unit per minute",
            "british thermal units per minute"
        )
    }

    return convert_system("PODER", units, convert_power)

def convert_angle_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de ángulos.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "grados": ("1", "°", "deg", "grado", "grados", "degree", "degrees"),
        "radianes": ("2", "rad", "radian", "radianes", "radian", "radians"),
        "grados_centesimales": (
            "3", "gon", "grad", "gradian", "gradianes", "grado centesimal", "grados centesimales"
        )
    }

    return convert_system("ANGULOS", units, convert_angle)

def convert_pressure_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de presión.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "atmosferas": ("1", "atm", "atmosfera", "atmosferas", "atmosphere", "atmospheres"),
        "bares": ("2", "bar", "bares"),
        "kilopascales": ("3", "kpa", "kilopascal", "kilopascales", "kilopascal", "kilopascals"),
        "milimetros_de_mercurio": (
            "4", "mmhg", "milimetro de mercurio", "milimetros de mercurio",
            "millimeter of mercury", "millimeters of mercury"
        ),
        "pascales": ("5", "pa", "pascal", "pascales"),
        "libras_por_pulgada_cuadrada": (
            "6", "psi", "libra por pulgada cuadrada", "libras por pulgada cuadrada",
            "pound per square inch", "pounds per square inch"
        )
    }

    return convert_system("PRESION", units, convert_pressure)

def convert_data_interface() -> tuple[float, str, float, str]:
    """
    Llamada para conversión de datos.
    
    Returns:
        tuple[float, str, float, str] | None: Una tupla con (valor_original, unidad_origen,
        valor_convertido, unidad_destino) o None si la entrada no es válida.
    """

    units = {
        "bits": ("1", "bit", "bits"),
        "cuarteto": ("2", "nibble", "nibbles", "cuarteto", "cuartetos"),
        "bytes": ("3", "b", "byte", "bytes"),
        "kilobits": ("4", "kb", "kilobit", "kilobits"),
        "kibibits": ("5", "kib", "kibibit", "kibibits"),
        "kilobytes": ("6", "kb", "kilobyte", "kilobytes"),
        "kibibytes": ("7", "kib", "kibibyte", "kibibytes"),
        "megabits": ("8", "mb", "megabit", "megabits"),
        "mebibits": ("9", "mib", "mebibit", "mebibits"),
        "megabytes": ("10", "mb", "megabyte", "megabytes"),
        "mebibytes": ("11", "mib", "mebibyte", "mebibytes"),
        "gigabits": ("12", "gb", "gigabit", "gigabits"),
        "gibibits": ("13", "gib", "gibibit", "gibibits"),
        "gigabytes": ("14", "gb", "gigabyte", "gigabytes"),
        "gibibytes": ("15", "gib", "gibibyte", "gibibytes"),
        "terabits": ("16", "tb", "terabit", "terabits"),
        "tebibits": ("17", "tib", "tebibit", "tebibits"),
        "terabytes": ("18", "tb", "terabyte", "terabytes"),
        "tebibytes": ("19", "tib", "tebibyte", "tebibytes"),
        "petabits": ("20", "pb", "petabit", "petabits"),
        "pebibits": ("21", "pib", "pebibit", "pebibits"),
        "petabytes": ("22", "pb", "petabyte", "petabytes"),
        "pebibytes": ("23", "pib", "pebibyte", "pebibytes"),
        "exabits": ("24", "eb", "exabit", "exabits"),
        "exbibits": ("25", "eib", "exbibit", "exbibits"),
        "exabytes": ("26", "eb", "exabyte", "exabytes"),
        "exbibytes": ("27", "eib", "exbibyte", "exbibytes"),
        "zettabits": ("28", "zb", "zettabit", "zettabits"),
        "zebibits": ("29", "zib", "zebibit", "zebibits"),
        "zettabytes": ("30", "zb", "zettabyte", "zettabytes"),
        "zebibytes": ("31", "zib", "zebibyte", "zebibytes"),
        "yottabits": ("32", "yb", "yottabit", "yottabits"),
        "yobibits": ("33", "yib", "yobibit", "yobibits"),
        "yottabytes": ("34", "yb", "yottabyte", "yottabytes"),
        "yobibytes": ("35", "yib", "yobibyte", "yobibytes")
    }

    return convert_system("DATOS", units, convert_data)

def start_interface():
    """
    Inicializa la interfaz CLI. Solicita el sistema de conversion y llama a las funciones 
    correspondientes para convertir un determinado valor. Muestra el valor convertido
    """
    chosen_system = None
    system_alias = {
        "TEMPERATURA": [
            "1", "tmp", "temp", "temperatura", "temperature", "temperaturas", "temperatures"
        ],
        "LONGITUD": ["2", "l", "len", "long", "longitud", "length", "distancia", "distances"],
        "MASA": ["3", "mass", "masa", "peso", "weight", "m"],
        "VOLUMEN": ["4", "vol", "volumen", "volume"],
        "ENERGIA": ["5", "e", "en", "eng", "energia", "energy", "nrg"],
        "AREA": ["6", "area", "surface", "superficie"],
        "VELOCIDAD": ["7", "vel", "velocidad", "speed", "velocity"],
        "TIEMPO": ["8", "time", "tiempo", "duracion", "duration"],
        "POTENCIA": ["9", "pow", "potencia", "power"],
        "ANGULOS": ["10", "ang", "angulo", "angulos", "angle", "angles"],
        "PRESION": ["11", "pres", "pressure", "presion"],
        "DATOS": ["12", "data", "datos", "bytes", "bits"]
    }

    while True:
        if chosen_system is None:
            _show_system_menu()
            sistema = input(f"{Fore.YELLOW}Elije tu sistema de conversion: {Style.RESET_ALL}")

            if sistema == "0":
                break
            else:
                for i, system in enumerate(system_alias, start=1):
                    if sistema.lower() in system_alias[system]:
                        chosen_system = i
                        break

            if chosen_system is None:
                print(f"{Fore.MAGENTA}No es una opcion valida!!")
                _enter_to_continue()
                continue

        print(f"Se eligio el sistema: {ConversionSystems(chosen_system).name}...")

        match chosen_system:
            case ConversionSystems.TEMPERATURA.value:
                result = convert_temperature_interface()
            case ConversionSystems.LONGITUD.value:
                result = convert_lenght_interface()
            case ConversionSystems.MASA.value:
                result = convert_mass_interface()
            case ConversionSystems.VOLUMEN.value:
                result = convert_volume_interface()
            case ConversionSystems.ENERGIA.value:
                result = convert_energy_interface()
            case ConversionSystems.AREA.value:
                result = convert_area_interface()
            case ConversionSystems.VELOCIDAD.value:
                result = convert_speed_interface()
            case ConversionSystems.TIEMPO.value:
                result = convert_time_interface()
            case ConversionSystems.POTENCIA.value:
                result = convert_power_interface()
            case ConversionSystems.ANGULOS.value:
                result = convert_angle_interface()
            case ConversionSystems.PRESION.value:
                result = convert_pressure_interface()
            case ConversionSystems.DATOS.value:
                result = convert_data_interface()

        if result is not None:
            value, from_unit, converted_value, to_unit = result
            print(
                f">>{Fore.LIGHTGREEN_EX} {value} {from_unit} "
                f"equivalen a {converted_value} {to_unit}"
            )

            print(f"{Fore.BLUE}Quieres cambiar de sistema?")
            print(f"{Fore.CYAN}1. Cambiar sistema")
            print(f"{Fore.CYAN}2. Seguir con {ConversionSystems(chosen_system).name}")
            print(f"{Fore.CYAN}3. Salir del programa")
            user_choise = input(f"{Fore.YELLOW}Elije el numero de tu opcion: {Style.RESET_ALL}")
            if user_choise == "1":
                print("Volviendo al menu principal...")
                chosen_system = None
            elif user_choise == "2":
                pass
            elif user_choise == "3":
                print(f"{Fore.MAGENTA}Saliendo del programa...")
                _enter_to_continue()
                return
            else:
                print("Opcion no reconocida. Volviendo al menu principal...")
                chosen_system = None
                _enter_to_continue()

        else:
            print("Volviendo al menu principal...")
            chosen_system = None

    print(f"{Fore.MAGENTA}Saliendo del programa...")
    _enter_to_continue()
    return


# ────────────────────── PUNTO DE EJECUCIÓN ──────────────────────
if __name__ == "__main__":
    start_interface()
