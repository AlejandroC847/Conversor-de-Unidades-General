## @file conversion_logic.py
# @brief Logica principal de la conversion, realiza los calculos necesarios
# @author Alejandro Cortés
# @version 0.2

#region Importaciones
from enum import Enum, auto
from colorama import Fore, Style, init

#endregion

#region --------------------Variables e Inicializaciones--------------------
class ConversionSystems(Enum):
    TEMPERATURA = auto()
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
init(autoreset=True) #Inicializar colorama
BOLD = Style.BRIGHT #Atajo para negritas

#endregion

# -------------------------Funciones auxiliares-------------------------

def _enter_to_continue():
    input(f"{Fore.YELLOW}Presione enter para continuar...\n")

def get_system_name_by_value(value: int ) -> str | None:
    try:
        return ConversionSystems(value).name
    except ValueError:
        print(f"{Fore.LIGHTRED_EX}Ingresaste un valor invalido, el valor debe ser entero dentro del rango")
        return None

def get_system_value_by_name(name: str) -> int | None:
    try:
        if name.upper() in ConversionSystems.__members__:
            return ConversionSystems[name.upper()].value
    except ValueError:
        print(f"{Fore.LIGHTRED_EX}Ingresaste un valor invalido, el valor debe ser un nombre de sistema permitido")
        return None

# -------------------------Funciones de Conversion-------------------------

def convert_temperature(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    unit = {
        "celsius" : ("c", "celsius"),
        "kelvin" : ("k", "kelvin"),
        "farenheit" : ("f", "farenheit"),
    }

    #region Convert to celsius
    if from_unit_lower in unit["celsius"]:
        value_in_celsius = value
    elif from_unit_lower in unit["kelvin"]:
        value_in_celsius = value - 273.15
    elif from_unit_lower in unit["farenheit"]:
        value_in_celsius = (value - 32) * 5/9
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion
    
    #region Convert from celsius
    if to_unit_lower in unit["celsius"]:
            return value_in_celsius
    elif to_unit_lower in unit["kelvin"]:
        return value_in_celsius + 273.15
    elif to_unit_lower in unit["farenheit"]:
        return (value_in_celsius * (9/5)) + 32
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_lenght(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    unit = {
        "angstroms" : ("å", "a", "an", "angstroms","angstrom", "ångström", "ångströms"),
        "nanometros" : ("nm", "nanometro", "nanometros", "nanometer", "nanometers"),
        "micrones" : ("µm", "um", "micrometro", "micrometros", "micron", "microns", "micrometer", "micrometers"),
        "milimetros" : ("mm", "milimetro", "milimetros", "millimeter", "millimeters"),
        "centimetros" : ("cm", "centimetro", "centimetros", "centimeter", "centimeters"),
        "metros" : ("m", "metro", "meter"),
        "kilometros" : ("km", "kilometro", "kilometros", "kilometer", "kilometers"),
        "pulgadas" : ("in", "pulgada", "pulgadas", "inch", "inches"),
        "pies" : ("ft", "pie", "pies", "foot", "feet"),
        "yardas" : ("yd", "yarda", "yardas", "yard", "yards"),
        "millas" : ("mi", "milla", "millas", "mile", "miles"),
        "millas_nauticas" : ("nmi", "milla nautica", "millas nauticas", "nautical mile", "nautical miles"),
        "unidad_astronomica" : ("ua", "au", "unidad astronomica", "unidades astronomicas", "astronomical unit", "astronomical units"),
        "anio_luz" : ("al", "ly", "año luz", "años luz", "light-year", "lightyear", "light-years", "lightyears"),
        "parsec" : ("pc", "parsec", "parsecs")
    }
    
    #region Convert to meters
    if from_unit_lower in unit["angstroms"]:
        value_in_meters = value / 1e10
    elif from_unit_lower in unit["nanometros"]:
        value_in_meters = value / 1e9
    elif from_unit_lower in unit["micrones"]:
        value_in_meters = value / 1e6
    elif from_unit_lower in unit["milimetros"]:
        value_in_meters = value / 1000
    elif from_unit_lower in unit["centimetros"]:
        value_in_meters = value / 100
    elif from_unit_lower in unit["metros"]:
        value_in_meters = value 
    elif from_unit_lower in unit["kilometros"]:
        value_in_meters = value * 1e3
    elif from_unit_lower in unit["pulgadas"]:
        value_in_meters = value / 39.3701
    elif from_unit_lower in unit["pies"]:
        value_in_meters = value / 3.28084 
    elif from_unit_lower in unit["yardas"]:
        value_in_meters = value / 1.09361 
    elif from_unit_lower in unit["millas"]:
        value_in_meters = value * 1609.34
    elif from_unit_lower in unit["millas_nauticas"]:
        value_in_meters = value * 1852
    elif from_unit_lower in unit["anio_luz"]:
        value_in_meters = value * 9.461e15
    elif from_unit_lower in unit["unidad_astronomica"]:
        value_in_meters = value * 1.495978707e21
    elif from_unit_lower in unit["parsec"]:
        value_in_meters = value * 3.086e16
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion
    
    #region Convert from meters
    if to_unit_lower in unit["angstroms"]:
        return value_in_meters * 1e10
    elif to_unit_lower in unit["nanometros"]:
        return value_in_meters * 1e9
    elif to_unit_lower in unit["micrones"]:
        return value_in_meters * 1e6
    elif to_unit_lower in unit["milimetros"]:
        return value_in_meters * 1000
    elif to_unit_lower in unit["centimetros"]:
        return value_in_meters * 100
    elif to_unit_lower in unit["metros"]:
        return value_in_meters
    elif to_unit_lower in unit["kilometros"]:
        return value_in_meters / 1e3
    elif to_unit_lower in unit["pulgadas"]:
        return value_in_meters * 39.3701
    elif to_unit_lower in unit["pies"]:
        return value_in_meters * 3.28084 
    elif to_unit_lower in unit["yardas"]:
        return value_in_meters * 1.09361 
    elif to_unit_lower in unit["millas"]:
        return value_in_meters / 1609.34
    elif to_unit_lower in unit["millas_nauticas"]:
        return value_in_meters / 1852
    elif to_unit_lower in unit["unidad_astronomica"]:
        return value_in_meters / 1.495978707e11
    elif to_unit_lower in unit["anio_luz"]:
        return value_in_meters / 9.461e15
    elif to_unit_lower in unit["parsec"]:
        return value_in_meters / 3.086e16
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_mass(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "miligramos": ("mg", "miligramo", "miligramos", "milligram", "milligrams"),
        "centigramos": ("cg", "centigramo", "centigramos", "centigram", "centigrams"),
        "decigramos": ("dg", "decigramo", "decigramos", "decigram", "decigrams"),
        "quilates": ("ct", "q", "qi" "quilate", "quilates", "carat", "carats"),
        "gramos": ("g", "gr", "gramo", "gramos", "gram", "grams"),
        "decagramos": ("dag", "decagramo", "decagramos", "decagram", "decagrams"),
        "hectogramos": ("hg", "hectogramo", "hectogramos", "hectogram", "hectograms"),
        "kilogramos": ("kg", "kilogramo", "kilogramos", "kilogram", "kilograms"),
        "toneladas_metricas": ("t", "ton", "tonelada", "toneladas", "tonelada metrica", "toneladas metricas", "tonne", "tonnes", "metric ton", "metric tons"),
        "onzas": ("oz", "onza", "onzas", "ounce", "ounces"),
        "libras": ("lb", "libra", "libras", "pound", "pounds"),
        "piedra": ("st", "piedra", "stone", "stones"),
        "toneladas_cortas_eeuu": ("tc", "ston", "tonelada corta", "toneladas cortas", "short ton", "short tons", "us ton", "us tons"),
        "toneladas_largas_uk": ("lt", "tl", "tonelada larga", "toneladas largas", "long ton", "long tons", "uk ton", "uk tons")
    }
    
    #region Convert to grams
    if from_unit_lower in units["miligramos"]:
        value_in_grams = value / 1000
    elif from_unit_lower in units["centigramos"]:
        value_in_grams = value / 100
    elif from_unit_lower in units["decigramos"]:
        value_in_grams = value / 10
    elif from_unit_lower in units["quilates"]:
        value_in_grams = value / 5
    elif from_unit_lower in units["gramos"]:
        value_in_grams = value
    elif from_unit_lower in units["decagramos"]:
        value_in_grams = value * 10
    elif from_unit_lower in units["hectogramos"]:
        value_in_grams = value * 100
    elif from_unit_lower in units["kilogramos"]:
        value_in_grams = value * 1000
    elif from_unit_lower in units["toneladas_metricas"]:
        value_in_grams = value * 1e6
    elif from_unit_lower in units["onzas"]:
        value_in_grams = value * 28.3495
    elif from_unit_lower in units["libras"]:
        value_in_gram,s = value * 453.592
    elif from_unit_lower in units["piedra"]:
        value_in_grams = value * 6350.29
    elif from_unit_lower in units["toneladas_cortas_eeuu"]:
        value_in_grams = value * 907185
    elif from_unit_lower in units["toneladas_largas_uk"]:
        value_in_grams = value * 10160000
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from grams
    if to_unit_lower in units["miligramos"]:
        return value_in_grams * 1000
    elif to_unit_lower in units["centigramos"]:
        return value_in_grams * 100
    elif to_unit_lower in units["decigramos"]:
        return value_in_grams * 10
    elif to_unit_lower in units["quilates"]:
        return value_in_grams * 5
    elif to_unit_lower in units["gramos"]:
        return value_in_grams 
    elif to_unit_lower in units["decagramos"]:
        return value_in_grams / 10
    elif to_unit_lower in units["hectogramos"]:
        return value_in_grams / 100
    elif to_unit_lower in units["kilogramos"]:
        return value_in_grams / 1000
    elif to_unit_lower in units["toneladas_metricas"]:
        return value_in_grams / 1e6
    elif to_unit_lower in units["onzas"]:
        return value_in_grams / 28.3495
    elif to_unit_lower in units["libras"]:
        return value_in_grams / 453.592
    elif to_unit_lower in units["piedra"]:
        return value_in_grams / 6350.29
    elif to_unit_lower in units["toneladas_cortas_eeuu"]:
        return value_in_grams / 907185
    elif to_unit_lower in units["toneladas_largas_uk"]:
        return value_in_grams / 10160000  
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion


#region SIN TERMINAR
def convert_volume(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_energy(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_area(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_speed(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_time(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_power(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_angle(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_pressure(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")


def convert_data(value:float, from_unit:str, to_unit:str) -> float:
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    units = {
        "example" : ("value1, value2"),
    }

    #region Convert from
    if from_unit_lower in units["example"]:
        value_in = 0
    elif from_unit_lower in units["example"]:
        value_in = 0
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit_lower in units["example"]:
        return value_in
    elif to_unit_lower in units["example"]:
        return value_in
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    # endregion



#---testeo---
try:
    print(f"Tu conversion es: {convert_lenght(5, "kg","g")}")
except ValueError as e:
    print(f"{Fore.RED}ERROR: {e}")
finally:
    print("El programa continua...")
    _enter_to_continue()