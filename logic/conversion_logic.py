"""
conversion_logic.py

Contiene funciones para convertir valores entre diferentes unidades de medida.
Realiza los cálculos necesarios para convertir entre diferentes sistemas de conversión

Autor: Alejandro Cortés
Versión: 1.0
"""


# ────────────────────── IMPORTACIONES ──────────────────────
from math import pi

from colorama import Fore, Style, init


# ────────────────────── VARIABLES GLOBALES / CONFIGURACION ──────────────────────
init(autoreset=True)    # Inicializa Colorama con autoreset en cada impresión
BOLD = Style.BRIGHT     # Atajo para aplicar estilo de negritas


# ────────────────────── FUNCIONES DE CONVERSIÓN ──────────────────────
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de temperatura entre Celsius, Kelvin y Fahrenheit.

    Args:
        value:  El valor numérico a convertir.
        from_unit: Unidad de origen ('celsius', 'kelvin', 'fahrenheit').
        to_unit: Unidad de destino ('celsius', 'kelvin', 'fahrenheit').

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si las unidades proporcionadas no son válidas.
    """

    to_celsius = {
        "celsius": lambda x:x,
        "kelvin": lambda x: x - 273.15,
        "fahrenheit": lambda x: (x - 32) * 5 / 9
    }
    from_celsius = {
        "celsius": lambda x: x,
        "kelvin": lambda x: x + 273.15,
        "fahrenheit": lambda x: x * 9 / 5 + 32
    }

    try:
        value_in_celsius = to_celsius[from_unit](value)
        return from_celsius[to_unit](value_in_celsius)
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad inválida: {e}.{Style.RESET_ALL}") from e

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de longitud entre diversas unidades métricas, imperiales y astronómicas.
    
    Admite valores en angstroms, nanometros, micrones, milimetros, centimetros,
    metros, kilometros, pulgadas, pies, yardas, millas, millas nauticas,
    unidad astronomica, año luz, parsec.
    
    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen.
        to_unit: Unidad de destino.

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si las unidades proporcionadas no son válidas.
    """

    to_meters = {
        "angstroms": 1e-10,
        "nanometros": 1e-9,
        "micrones": 1e-6,
        "milimetros": 1e-3,
        "centimetros": 1e-2,
        "metros": 1.0,
        "kilometros": 1e3,
        "pulgadas": 0.0254,
        "pies": 0.3048,
        "yardas": 0.9144,
        "millas": 1609.344,
        "millas_nauticas": 1852,
        "unidad_astronomica": 1.495978707e11,
        "anio_luz": 9.461e15,
        "parsec": 3.086e16
    }
    from_meters = {unit: 1 / factor for unit, factor in to_meters.items()}

    try:
        value_in_meters = value * to_meters[from_unit]
        return value_in_meters * from_meters[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de masa entre diversas unidades.

    Admite valores en miligramos, centigramos, decigramos, quilates, gramos, decagramos,
    hectogramos, kilogramos, toneladas metricas, onzas, libras, piedra,
    toneladas cortas eeuu, toneladas largas uk.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen.
        to_unit: Unidad de destino.

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si las unidades proporcionadas no son válidas.
    """

    to_grams = {
        "miligramos": 1e-3,
        "centigramos": 1e-2,
        "decigramos": 1e-1,
        "quilates": 0.2,
        "gramos": 1.0,
        "decagramos": 1e1,
        "hectogramos": 1e2,
        "kilogramos": 1e3,
        "toneladas_metricas": 1e6,
        "onzas": 28.3495,
        "libras": 453.592,
        "piedra": 6350.29,
        "toneladas_cortas_eeuu": 907185,
        "toneladas_largas_uk": 10160000
    }
    from_grams = {unit: 1 / factor for unit, factor in to_grams.items()}

    try:
        value_in_grams = value * to_grams[from_unit]
        return value_in_grams * from_grams[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de volumen entre diversas unidades.

    Admite valores en mililitros, centimetros cubicos, litros, metros cubicos, cucharaditas us,
    cucharadas us, onzas liquidas us, tazas us, pintas us, cuartos de galon us, galones us,
    pulgadas cubicas, pies cubicos, yardas cubicas, cucharaditas uk, cucharadas uk,
    onzas liquidas uk, pintas uk, cuartos de galon uk, galones uk.
    
    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen.
        to_unit: Unidad de destino.

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si las unidades proporcionadas no son válidas.
    """

    to_milliliters= {
        "mililitros" : 1.0,
        "centimetros_cubicos" : 1.0,
        "litros" : 1e3,
        "metros_cubicos" : 1e6,
        "cucharaditas_us" : 4.92892,
        "cucharadas_us" : 14.7868,
        "onzas_liquidas_us" : 29.5735,
        "tazas_us" : 236.588,
        "pintas_us" : 473.176,
        "cuartos_de_galon_us" : 946.353,
        "galones_us" : 3785.41,
        "pulgadas_cubicas" : 16.3871,
        "pies_cubicos" : 28316.8,
        "yardas_cubicas" : 764555,
        "cucharaditas_uk" : 5.91939,
        "cucharadas_uk" : 17.7582,
        "onzas_liquidas_uk" : 28.4131,
        "pintas_uk" : 568.261,
        "cuartos_de_galon_uk" : 1136.52,
        "galones_uk" : 4546.09,
    }
    from_milliliters = {unit: 1 / factor for unit, factor in to_milliliters.items()}

    try:
        value_in_milliliters = value * to_milliliters[from_unit]
        return value_in_milliliters * from_milliliters[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_energy(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de energía entre diferentes unidades.
    
    Admite valores en julios, kilojulios, calorias termales, calorias alimentos,
    pie-libras, unidades termicas britanicas, kilovatio-horas.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_joules = {
        "joules": 1.0,
        "kilojulios": 1000,
        "calorias_termales": 4.184,
        "calorias_alimentos": 4184,
        "pie_libras": 1.35582,
        "unidades_termicas_britanicas": 1055.06,
        "kilovatio_horas": 3.6e6
    }
    from_joules = {unit: 1 / factor for unit, factor in to_joules.items()}

    try:
        value_in_joules = value * to_joules[from_unit]
        return value_in_joules * from_joules[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_area(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de área entre diferentes unidades.

    Admite valores en .

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_square_millimeters = {
        "milimetros_cuadrados": 1.0,
        "centimetros_cuadrados": 100,
        "metros_cuadrados": 1e6,
        "hectareas": 1e10,
        "kilometros_cuadrados": 1e12,
        "pulgadas_cuadradas": 645.16,
        "pies_cuadrados": 92903,
        "yardas_cuadradas": 836127,
        "acres": 4046856422.4,
        "millas_cuadradas": 2589988110336,
    }
    from_square_millimeters = {unit: 1 / factor for unit, factor in to_square_millimeters.items()}

    try:
        value_in_square_millimeters = value * to_square_millimeters[from_unit]
        return value_in_square_millimeters * from_square_millimeters[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_speed(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de velocidad entre diferentes unidades.

    Admite valores en centimetros_por_segundo, metros_por_segundo, kilometros_por_hora,
    pies_por_segundo, millas_por_hora, nudos, mach.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_cm_per_second = {
        "centimetros_por_segundo": 1.0,
        "metros_por_segundo": 100,
        "kilometros_por_hora": 1000.0 / 36.0,
        "pies_por_segundo": 30.48,
        "millas_por_hora": 44.706,
        "nudos": 51.4444,
        "mach": 34029
    }
    from_cm_per_second = {unit: 1 / factor for unit, factor in to_cm_per_second.items()}

    try:
        value_in_cm_per_second = value * to_cm_per_second[from_unit]
        return value_in_cm_per_second * from_cm_per_second[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_time(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de tiempo entre diferentes unidades.

    Admite valores en microsegundos, milisegundos, segundos, minutos, horas, dias, semanas, años.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_microseconds = {
        "microsegundos": 1.0,
        "milisegundos": 1000,
        "segundos": 1e6,
        "minutos": 6e7,
        "horas": 3.6e9,
        "dias": 8.64e10,
        "semanas": 6.048e11,
        "años": 3.1536e13,
    }
    from_microseconds = {unit: 1 / factor for unit, factor in to_microseconds.items()}

    try:
        value_in_microseconds = value * to_microseconds[from_unit]
        return value_in_microseconds * from_microseconds[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_power(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de potencia entre diferentes unidades.

    Admite unidades como vatios, kilovatios, caballos de fuerza eeuu,
    pie libras por minuto, unidades termicas britanicas por minuto.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_watts= {
        "vatios": 1.0,
        "kilovatios": 1e3,
        "caballos_de_fuerza_eeuu": 745.7,
        "pie_libras_por_minuto": 0.02259698059,
        "unidades_termicas_britanicas_por_minuto": 17.58427263,
    }
    from_watts = {unit: 1 / factor for unit, factor in to_watts.items()}

    try:
        value_in_watts = value * to_watts[from_unit]
        return value_in_watts * from_watts[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_angle(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de ángulo entre diferentes unidades.

    Admite unidades como grados, radianes y gradians.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_grades = {
        "grados": value,
        "radianes":180 / pi,
        "grados_centesimales": 0.9,
    }
    from_grades = {unit: 1 / factor for unit, factor in to_grades.items()}

    try:
        value_in_grades = value * to_grades[from_unit]
        return value_in_grades * from_grades[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_pressure(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de presión entre diferentes unidades.

    Admite valores en atmosferas, bares, kilopascales, milimetros de mercurio,
    pascales y libras por pulgada cuadrada.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_atmospheres = {
        "atmosferas": 1.0,
        "bares": 0.9869232667,
        "kilopascales": 0.009869232667,
        "milimetros_de_mercurio": 0.001315789474,
        "pascales": 9.869232667e-06,
        "libras_por_pulgada_cuadrada": 0.06804618975
    }
    from_atmospheres = {unit: 1 / factor for unit, factor in to_atmospheres.items()}

    try:
        value_in_atmospheres = value * to_atmospheres[from_unit]
        return value_in_atmospheres * from_atmospheres[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e

def convert_data(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte un valor de almacenamiento de datos entre diferentes unidades.

    Admite valores en bits, cuarteto, bytes, kilobits, kibibits, kilobytes, kibibytes,
    megabits,     mebibits, megabytes, mebibytes, gigabits, gibibits, gigabytes, gibibytes,
    terabits, tebibits, terabytes, tebibytes, petabits, pebibits, petabytes, pebibytes,
    exabits, exbibits, exabytes, exbibytes, zettabits, zebibits, zettabytes, zebibytes,
    yottabits, yobibits, yottabytes y yobibytes.

    Args:
        value: Valor numérico a convertir.
        from_unit: Unidad de origen (en minúsculas y formato interno).
        to_unit: Unidad de destino (en minúsculas y formato interno).

    Returns:
        Valor convertido como float.

    Raises:
        ValueError: Si alguna de las unidades no es válida.
    """

    to_bits = {
        "bits": 1.0,
        "cuarteto": 4,
        "bytes": 8,
        "kilobits": 1000,
        "kibibits": 1024,
        "kilobytes": 8000,
        "kibibytes": 8192,
        "megabits": 1e6,
        "mebibits": 1_048_576,
        "megabytes": 8e6,
        "mebibytes": 8_388_608,
        "gigabits": 1e9,
        "gibibits": 1_073_741_824,
        "gigabytes": 8e9,
        "gibibytes": 8_589_934_592,
        "terabits": 1e12,
        "tebibits": 1_099_511_627_776,
        "terabytes": 8e12,
        "tebibytes": 8_796_093_208_022,
        "petabits": 1e15,
        "pebibits": 1_125_899_906_842_624,
        "petabytes": 8e15,
        "pebibytes": 9_007_199_254_740_992,
        "exabits": 1e18,
        "exbibits": 1_152_921_504_606_846_976,
        "exabytes": 8e18,
        "exbibytes": 9_223_372_036_854_775_808,
        "zettabits": 1e21,
        "zebibits": 1_180_591_620_717_411_303_424,
        "zettabytes": 8e21,
        "zebibytes": 9_444_732_965_732_923_457_740_000,
        "yottabits": 1e24,
        "yobibits": 1_208_925_819_614_629_174_706_176,
        "yottabytes": 8e24,
        "yobibytes": 9_671_406_556_917_033_397_649_408,
    }
    from_bits = {unit: 1 / factor for unit, factor in to_bits.items()}

    try:
        value_in_bits = value * to_bits[from_unit]
        return value_in_bits  * from_bits[to_unit]
    except KeyError as e:
        raise ValueError(f"{Fore.MAGENTA}Unidad invalida: {e}.") from e
