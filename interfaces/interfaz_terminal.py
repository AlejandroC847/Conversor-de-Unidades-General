# @file interfaz_terminal.py
# @brief Interfaz de Usuario para modo de consola, se basa en prints para mostrar contenido
# @author Alejandro Cortés
# @version 0.5

#region Importaciones
import os
from colorama import Fore, Style, init
from enum import Enum, auto
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
BOLD = Style.BRIGHT
#endregion

# -------------------------Funciones de utilidad-------------------------

def _clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def _enter_to_continue():
    input(f"{Fore.YELLOW}Presione enter para continuar...\n")

def _show_system_menu():
    _clear_console()
    print(f"{Fore.BLUE}{BOLD}----------Conversor de Unidades----------")
    for system in ConversionSystems:
        #Obtiene numero de sistema, nombre, y lo muestra solo con inicial en mayuscula
        print(f"{Fore.CYAN}{system.value}. {system.name.replace("_", " ").title()}")       
    print(f"{Fore.CYAN}0. Salir")

def get_data(system, units):
    value = None
    from_unit = None
    to_unit = None
    chosen_unit = None
    
    while(True):
        _clear_console()
        print(f"{Fore.BLUE}--------------------{system}--------------------")
        
        i=1
        for unit in units:
            print(f"{Fore.CYAN}{i}. {str(unit)}")
            i+=1
        print(f"{Fore.CYAN}0. Volver al menu principal")
        
        #Si ya se ingresaron datos
        if from_unit is None:
            chosen_unit = input(f"{Fore.YELLOW}Elije tu unidad de entrada: {Style.RESET_ALL}")
            if chosen_unit == "0":
                return None
            for unit in units:
                if chosen_unit.lower() in units[unit]:
                    from_unit = unit
                    break
            if from_unit is None:
                print(f"{Fore.RED}ERROR: Unidad ingresada invalida")
                _enter_to_continue()
                continue
        else:
            print(f"{Fore.YELLOW}Elije tu unidad de entrada: {Style.RESET_ALL}{from_unit}")
        
        if value is None:
            try:
                value = float(input(f"{Fore.YELLOW}Ingresa tu valor: {Style.RESET_ALL}"))
            except Exception as e:
                print(f"{Fore.RED}ERROR: {e}")
                _enter_to_continue()
                continue
        else:
            print(f"{Fore.YELLOW}Ingresa tu valor: {Style.RESET_ALL}{value}")
            
        if to_unit is None:
            chosen_unit = input(f"{Fore.YELLOW}Elije tu unidad de salida: {Style.RESET_ALL}")
            if chosen_unit == "0":
                return None
            for unit in units:
                if chosen_unit.lower() in units[unit]:
                    to_unit = unit
                    break
            if to_unit is None:
                print(f"{Fore.RED}ERROR: Unidad ingresada invalida")
                _enter_to_continue()
                continue
        else:#No se supone que se muestre este else
            print(f"{Fore.YELLOW}Elije tu unidad de entrada: {Style.RESET_ALL}{to_unit}")
            
        return (value, from_unit, to_unit)

def convert_temperature_interface():
    SYSTEM = "TEMPERATURA"
    units = {
        "celsius" : ("1", "c", "celsius"),
        "kelvin" : ("2", "k", "kelvin"),
        "farenheit" : ("3", "f", "farenheit"),
    }
    
    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_temperature(result[0], result[1], result[2])
    else:
        return None
    
    return (result[0], result[1], converted_value, result[2])

def convert_lenght_interface():
    SYSTEM = "LONGITUD"
    units = {
        "angstroms" : ("1", "å", "a", "an", "angstroms","angstrom", "ångström", "ångströms"),
        "nanometros" : ("2", "nm", "nanometro", "nanometros", "nanometer", "nanometers"),
        "micrones" : ("3", "µm", "um", "micrometro", "micrometros", "micron", "microns", "micrometer", "micrometers"),
        "milimetros" : ("4", "mm", "milimetro", "milimetros", "millimeter", "millimeters"),
        "centimetros" : ("5", "cm", "centimetro", "centimetros", "centimeter", "centimeters"),
        "metros" : ("6", "m", "metro", "meter", "metros", "meters"),
        "kilometros" : ("7", "km", "kilometro", "kilometros", "kilometer", "kilometers"),
        "pulgadas" : ("8", "in", "pulgada", "pulgadas", "inch", "inches"),
        "pies" : ("9", "ft", "pie", "pies", "foot", "feet"),
        "yardas" : ("10", "yd", "yarda", "yardas", "yard", "yards"),
        "millas" : ("11", "mi", "milla", "millas", "mile", "miles"),
        "millas_nauticas" : ("12", "nmi", "milla nautica", "millas nauticas", "nautical mile", "nautical miles"),
        "unidad_astronomica" : ("13", "ua", "au", "unidad astronomica", "unidades astronomicas", "astronomical unit", "astronomical units"),
        "anio_luz" : ("14", "al", "ly", "año luz", "años luz", "light-year", "lightyear", "light-years", "lightyears"),
        "parsec" : ("15", "pc", "parsec", "parsecs")
    }
    
    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_lenght(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_mass_interface():
    SYSTEM = "MASA"
    units = {
        "miligramos": ("1", "mg", "miligramo", "miligramos", "milligram", "milligrams"),
        "centigramos": ("2", "cg", "centigramo", "centigramos", "centigram", "centigrams"),
        "decigramos": ("3", "dg", "decigramo", "decigramos", "decigram", "decigrams"),
        "quilates": ("4", "ct", "q", "qi" "quilate", "quilates", "carat", "carats"),
        "gramos": ("5", "g", "gr", "gramo", "gramos", "gram", "grams"),
        "decagramos": ("6", "dag", "decagramo", "decagramos", "decagram", "decagrams"),
        "hectogramos": ("7", "hg", "hectogramo", "hectogramos", "hectogram", "hectograms"),
        "kilogramos": ("8", "kg", "kilogramo", "kilogramos", "kilogram", "kilograms"),
        "toneladas_metricas": ("9", "t", "ton", "tonelada", "toneladas", "tonelada metrica", "toneladas metricas", "tonne", "tonnes", "metric ton", "metric tons"),
        "onzas": ("10", "oz", "onza", "onzas", "ounce", "ounces"),
        "libras": ("11", "lb", "libra", "libras", "pound", "pounds"),
        "piedra": ("12", "st", "piedra", "stone", "stones"),
        "toneladas_cortas_eeuu": ("13", "tc", "ston", "tonelada corta", "toneladas cortas", "short ton", "short tons", "us ton", "us tons"),
        "toneladas_largas_uk": ("14", "lt", "tl", "tonelada larga", "toneladas largas", "long ton", "long tons", "uk ton", "uk tons")
    }
    
    result = get_data(SYSTEM, units)
    
    if result is not None:
        converted_value = convert_mass(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_volume_interface():
    SYSTEM = "VOLUMEN"
    units = {
        "mililitros" : ("1", "ml", "mililitro", "mililitros", "milliliter", "milliliters"),
        "centimetros_cubicos": ("2", "cm3", "cm^3", "centimetro cubico", "centimetros cubicos", "cubic centimeter", "cubic centimeters"),
        "litros": ("3", "l", "lt", "litro", "litros", "liter", "liters"),
        "metros_cubicos": ("4", "m3", "m^3", "metro cubico", "metros cubicos", "cubic meter", "cubic meters"),
        "cucharaditas_us": ("5", "tsp", "cucharadita", "cucharaditas", "teaspoon", "teaspoons", "us tsp", "us teaspoon"),
        "cucharadas_us": ("6", "tbsp", "cucharada", "cucharadas", "tablespoon", "tablespoons", "us tbsp", "us tablespoon"),
        "onzas_liquidas_us": ("7", "fl oz", "onza liquida", "onzas liquidas", "fluid ounce", "fluid ounces", "us fl oz", "us fluid ounce"),
        "tazas_us": ("8", "cup", "taza", "tazas", "cups", "us cup", "us cups"),
        "pintas_us": ("9", "pt", "pinta", "pintas", "pint", "pints", "us pint", "us pints"),
        "cuartos_de_galon_us": ("10", "qt", "cuarto de galon", "cuartos de galon", "quart", "quarts", "us qt", "us quart"),
        "galones_us": ("11", "gal", "galon", "galones", "gallon", "gallons", "us gal", "us gallon"),
        "pulgadas_cubicas": ("12", "in3", "in^3", "pulgada cubica", "pulgadas cubicas", "cubic inch", "cubic inches"),
        "pies_cubicos": ("13", "ft3", "ft^3", "pie cubico", "pies cubicos", "cubic foot", "cubic feet"),
        "yardas_cubicas": ("14", "yd3", "yd^3", "yarda cubica", "yardas cubicas", "cubic yard", "cubic yards"),
        "cucharaditas_uk": ("15", "uk tsp", "cucharadita uk", "cucharaditas uk", "uk teaspoon", "uk teaspoons"),
        "cucharadas_uk": ("16", "uk tbsp", "cucharada uk", "cucharadas uk", "uk tablespoon", "uk tablespoons"),
        "onzas_liquidas_uk": ("17", "uk fl oz", "onza liquida uk", "onzas liquidas uk", "uk fluid ounce", "uk fluid ounces"),
        "pintas_uk": ("18", "uk pt", "pinta uk", "pintas uk", "uk pint", "uk pints"),
        "cuartos_de_galon_uk": ("19", "uk qt", "cuarto de galon uk", "cuartos de galon uk", "uk quart", "uk quarts"),
        "galones_uk": ("20", "uk gal", "galon uk", "galones uk", "uk gallon", "uk gallons")
    }

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_volume(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_energy_interface():
    SYSTEM = "ENERGIA"
    units = {
    "joules": ("1", "j", "joule", "joules"),
    "kilojulios": ("2", "kj", "kilojulio", "kilojulios", "kilojoule", "kilojoules"),
    "calorias_termales": ("3", "cal", "caloria termal", "calorias termales", "caloría termal", "calorías termales", "thermal calorie", "thermal calories"),
    "calorias_alimentos": ("4", "kcal", "cal", "caloria alimento", "calorias alimentos", "caloría alimento", "calorías alimentos", "food calorie", "food calories", "kilocalorie", "kilocalories"), # Nota: 'Cal' con 'C' mayúscula a menudo se refiere a kcal en nutrición
    "pie_libras": ("5", "ft-lb", "pie-libra", "pie-libras", "foot-pound", "foot-pounds"),
    "unidades_termicas_britanicas": ("6", "btu", "unidad termica britanica", "unidades termicas britanicas", "british thermal unit", "british thermal units"),
    "kilovatio_horas": ("7", "kwh", "kw-h", "kilovatio hora", "kilovatio horas", "kilowatt-hour", "kilowatt-hours")
}

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_energy(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_area_interface():
    SYSTEM = "AREA"
    units = {
    "milimetros_cuadrados": ("1", "mm2", "mm^2", "milimetro cuadrado", "milimetros cuadrados", "square millimeter", "square millimeters"),
    "centimetros_cuadrados": ("2", "cm2", "cm^2", "centimetro cuadrado", "centimetros cuadrados", "square centimeter", "square centimeters"),
    "metros_cuadrados": ("3", "m2", "m^2", "metro cuadrado", "metros cuadrados", "square meter", "square meters"),
    "hectareas": ("4", "ha", "hectarea", "hectareas", "hectare", "hectares"),
    "kilometros_cuadrados": ("5", "km2", "km^2", "kilometro cuadrado", "kilometros cuadrados", "square kilometer", "square kilometers"),
    "pulgadas_cuadradas": ("6", "in2", "in^2", "pulgada cuadrada", "pulgadas cuadradas", "square inch", "square inches"),
    "pies_cuadrados": ("7", "ft2", "ft^2", "pie cuadrado", "pies cuadrados", "square foot", "square feet"),
    "yardas_cuadradas": ("8", "yd2", "yd^2", "yarda cuadrada", "yardas cuadradas", "square yard", "square yards"),
    "acres": ("9", "ac", "acre", "acres"),
    "millas_cuadradas": ("10", "mi2", "mi^2", "milla cuadrada", "millas cuadradas", "square mile", "square miles")
}

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_area(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_speed_interface():
    SYSTEM = "VELOCIDAD"
    units = {
        "centimetros_por_segundo": ("1", "cm/s", "cmps", "centimetro por segundo", "centimetros por segundo", "centimeter per second", "centimeters per second"),
        "metros_por_segundo": ("2", "m/s", "mps", "metro por segundo", "metros por segundo", "meter per second", "meters per second"),
        "kilometros_por_hora": ("3", "km/h", "kph", "kilometro por hora", "kilometros por hora", "kilometer per hour", "kilometers per hour"),
        "pies_por_segundo": ("4", "ft/s", "fps", "pie por segundo", "pies por segundo", "foot per second", "feet per second"),
        "millas_por_hora": ("5", "mph", "milla por hora", "millas por hora", "mile per hour", "miles per hour"),
        "nudos": ("6", "kn", "kt", "nudo", "nudos", "knot", "knots"),
        "mach": ("7", "mach", "ma") 
    }

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_speed(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_time_interface():
    SYSTEM = "TIEMPO"
    units = {
        "microsegundos": ("1", "µs", "us", "microsegundo", "microsegundos", "microsecond", "microseconds"),
        "milisegundos": ("2", "ms", "milisegundo", "milisegundos", "millisecond", "milliseconds"),
        "segundos": ("3", "s", "segundo", "segundos", "second", "seconds"),
        "minutos": ("4", "min", "minuto", "minutos", "minute", "minutes"),
        "horas": ("5", "h", "hr", "hora", "horas", "hour", "hours"),
        "dias": ("6", "d", "dia", "dias", "day", "days"),
        "semanas": ("7", "wk", "semana", "semanas", "week", "weeks"),
        "años": ("8", "yr", "año", "años", "year", "years")
    }

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_time(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_power_interface():
    SYSTEM = "PODER"
    units = {
        "vatios": ("1", "w", "vatio", "vatios", "watt", "watts"),
        "kilovatios": ("2", "kw", "kilovatio", "kilovatios", "kilowatt", "kilowatts"),
        "caballos_de_fuerza_eeuu": ("3", "hp", "caballo de fuerza", "caballos de fuerza", "horsepower", "us hp"),
        "pie_libras_por_minuto": ("4", "ft-lb/min", "pie-libra por minuto", "pie-libras por minuto", "foot-pound per minute", "foot-pounds per minute"),
        "unidades_termicas_britanicas_por_minuto": ("5", "btu/min", "unidad termica britanica por minuto", "unidades termicas britanicas por minuto", "british thermal unit per minute", "british thermal units per minute")
    }

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_power(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_angle_interface():
    SYSTEM = "ANGULOS"
    units = {
        "grados": ("1", "°", "deg", "grado", "grados", "degree", "degrees"),
        "radianes": ("2", "rad", "radian", "radianes", "radian", "radians"),
        "grados_centesimales": ("3", "gon", "grad", "gradian", "gradianes", "grado centesimal", "grados centesimales")
    }

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_angle(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_pressure_interface():
    SYSTEM = "PRESION"
    units = {
        "atmosferas": ("1", "atm", "atmosfera", "atmosferas", "atmosphere", "atmospheres"),
        "bares": ("2", "bar", "bares"),
        "kilopascales": ("3", "kpa", "kilopascal", "kilopascales", "kilopascal", "kilopascals"),
        "milimetros_de_mercurio": ("4", "mmhg", "milimetro de mercurio", "milimetros de mercurio", "millimeter of mercury", "millimeters of mercury"),
        "pascales": ("5", "pa", "pascal", "pascales"),
        "libras_por_pulgada_cuadrada": ("6", "psi", "libra por pulgada cuadrada", "libras por pulgada cuadrada", "pound per square inch", "pounds per square inch")
    }

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_pressure(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def convert_data_interface():
    SYSTEM = "DATOS"
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

    result = get_data(SYSTEM, units)
    if result is not None:
        converted_value = convert_data(result[0], result[1], result[2])
    else:
        return None

    return (result[0], result[1], converted_value, result[2])

def start_interface():
    chosen_system = None
    system_alias = {
        "TEMPERATURA": ["1", "tmp", "temp", "temperatura", "temperature", "temperaturas", "temperatures"],
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
        
    while(True):
        if chosen_system is None:
            _show_system_menu()
            sistema = input(f"{Fore.YELLOW}Elije tu sistema de conversion: {Style.RESET_ALL}")
            
            if sistema == "0":
                break
            else:    
                system_number = 1
                for system in system_alias:
                    if sistema.lower() in system_alias[system]:
                        chosen_system = system_number
                        break
                    system_number +=1
            if chosen_system is None:
                print(f"{Fore.MAGENTA}No es una opcion valida!!")
                _enter_to_continue()
                continue
            
        print(f"Se eligio el sistema: {ConversionSystems(chosen_system).name}...") #Se quita rapidamente
            
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
            print(f">>{Fore.LIGHTGREEN_EX} {result[0]} {result[1]} equivalen a {result[2]} {result[3]}")
            
            print(f"{Fore.BLUE}Quieres cambiar de sistema?")
            print(f"{Fore.CYAN}1. Cambiar sistema")
            print(f"{Fore.CYAN}2. Seguir con {ConversionSystems(chosen_system).name}")
            print(f"{Fore.CYAN}3. Salir del programa")
            exit = input(f"{Fore.YELLOW}Elije el numero de tu opcion: {Style.RESET_ALL}")
            if exit == "1":
                print("Volviendo al menu principal...")
                chosen_system = None
            elif exit == "2":
                pass
            elif exit == "3":
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

