# @file conversion_logic.py
# @brief Logica principal de la conversion, realiza los calculos necesarios
# @author Alejandro Cortés
# @version 0.7

#region Importaciones
from colorama import Fore, Style, init
from math import pi
#endregion

#region --------------------Variables e Inicializaciones--------------------
init(autoreset=True) #Inicializar colorama
BOLD = Style.BRIGHT #Atajo para negritas

#endregion

# -------------------------Funciones de Conversion-------------------------

def convert_temperature(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to celsius
    if from_unit == "celsius":
        value_in_celsius = value
    elif from_unit == "kelvin":
        value_in_celsius = value - 273.15
    elif from_unit == "farenheit":
        value_in_celsius = (value - 32) * 5/9
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion
    
    #region Convert from celsius
    if to_unit == "celsius":
        return value_in_celsius
    elif to_unit == "kelvin":
        return value_in_celsius + 273.15
    elif to_unit == "farenheit":
        return (value_in_celsius * (9/5)) + 32
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_length(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to meters
    if from_unit == "angstroms":
        value_in_meters = value / 1e10
    elif from_unit == "nanometros":
        value_in_meters = value / 1e9
    elif from_unit == "micrones":
        value_in_meters = value / 1e6
    elif from_unit == "milimetros":
        value_in_meters = value / 1000
    elif from_unit == "centimetros":
        value_in_meters = value / 100
    elif from_unit == "metros":
        value_in_meters = value 
    elif from_unit == "kilometros":
        value_in_meters = value * 1e3
    elif from_unit == "pulgadas":
        value_in_meters = value / 39.3701
    elif from_unit == "pies":
        value_in_meters = value / 3.28084 
    elif from_unit == "yardas":
        value_in_meters = value / 1.09361 
    elif from_unit == "millas":
        value_in_meters = value * 1609.34
    elif from_unit == "millas_nauticas":
        value_in_meters = value * 1852
    elif from_unit == "anio_luz":
        value_in_meters = value * 9.461e15
    elif from_unit == "unidad_astronomica":
        value_in_meters = value * 1.495978707e21
    elif from_unit == "parsec":
        value_in_meters = value * 3.086e16
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion
    
    #region Convert from meters
    if to_unit == "angstroms":
        return value_in_meters * 1e10
    elif to_unit == "nanometros":
        return value_in_meters * 1e9
    elif to_unit == "micrones":
        return value_in_meters * 1e6
    elif to_unit == "milimetros":
        return value_in_meters * 1000
    elif to_unit == "centimetros":
        return value_in_meters * 100
    elif to_unit == "metros":
        return value_in_meters
    elif to_unit == "kilometros":
        return value_in_meters / 1e3
    elif to_unit == "pulgadas":
        return value_in_meters * 39.3701
    elif to_unit == "pies":
        return value_in_meters * 3.28084 
    elif to_unit == "yardas":
        return value_in_meters * 1.09361 
    elif to_unit == "millas":
        return value_in_meters / 1609.34
    elif to_unit == "millas_nauticas":
        return value_in_meters / 1852
    elif to_unit == "unidad_astronomica":
        return value_in_meters / 1.495978707e11
    elif to_unit == "anio_luz":
        return value_in_meters / 9.461e15
    elif to_unit == "parsec":
        return value_in_meters / 3.086e16
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_mass(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to grams
    if from_unit == "miligramos":
        value_in_grams = value / 1000
    elif from_unit == "centigramos":
        value_in_grams = value / 100
    elif from_unit == "decigramos":
        value_in_grams = value / 10
    elif from_unit == "quilates":
        value_in_grams = value / 5
    elif from_unit == "gramos":
        value_in_grams = value
    elif from_unit == "decagramos":
        value_in_grams = value * 10
    elif from_unit == "hectogramos":
        value_in_grams = value * 100
    elif from_unit == "kilogramos":
        value_in_grams = value * 1000
    elif from_unit == "toneladas_metricas":
        value_in_grams = value * 1e6
    elif from_unit == "onzas":
        value_in_grams = value * 28.3495
    elif from_unit == "libras":
        value_in_grams = value * 453.592
    elif from_unit == "piedra":
        value_in_grams = value * 6350.29
    elif from_unit == "toneladas_cortas_eeuu":
        value_in_grams = value * 907185
    elif from_unit == "toneladas_largas_uk":
        value_in_grams = value * 10160000
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from grams
    if to_unit == "miligramos":
        return value_in_grams * 1000
    elif to_unit == "centigramos":
        return value_in_grams * 100
    elif to_unit == "decigramos":
        return value_in_grams * 10
    elif to_unit == "quilates":
        return value_in_grams * 5
    elif to_unit == "gramos":
        return value_in_grams 
    elif to_unit == "decagramos":
        return value_in_grams / 10
    elif to_unit == "hectogramos":
        return value_in_grams / 100
    elif to_unit == "kilogramos":
        return value_in_grams / 1000
    elif to_unit == "toneladas_metricas":
        return value_in_grams / 1e6
    elif to_unit == "onzas":
        return value_in_grams / 28.3495
    elif to_unit == "libras":
        return value_in_grams / 453.592
    elif to_unit == "piedra":
        return value_in_grams / 6350.29
    elif to_unit == "toneladas_cortas_eeuu":
        return value_in_grams / 907185
    elif to_unit == "toneladas_largas_uk":
        return value_in_grams / 10160000  
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_volume(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to milliliters
    if from_unit == "mililitros":
        value_in_milliliters = value
    elif from_unit == "centimetros_cubicos":
        value_in_milliliters = value
    elif from_unit == "litros":
        value_in_milliliters = value * 1e3
    elif from_unit == "metros_cubicos":
        value_in_milliliters = value * 1e6
    elif from_unit == "cucharaditas_us":
        value_in_milliliters = value * 4.92892
    elif from_unit == "cucharadas_us":
        value_in_milliliters = value * 14.7868
    elif from_unit == "onzas_liquidas_us":
        value_in_milliliters = value * 29.5735
    elif from_unit == "tazas_us":
        value_in_milliliters = value * 236.588
    elif from_unit == "pintas_us":
        value_in_milliliters = value * 473.176
    elif from_unit == "cuartos_de_galon_us":
        value_in_milliliters = value * 946.353
    elif from_unit == "galones_us":
        value_in_milliliters = value * 3785.41
    elif from_unit == "pulgadas_cubicas":
        value_in_milliliters = value * 16.3871
    elif from_unit == "pies_cubicos":
        value_in_milliliters = value * 28316.8
    elif from_unit == "yardas_cubicas":
        value_in_milliliters = value * 764555
    elif from_unit == "cucharaditas_uk":
        value_in_milliliters = value * 5.91939
    elif from_unit == "cucharadas_uk":
        value_in_milliliters = value * 17.7582
    elif from_unit == "onzas_liquidas_uk":
        value_in_milliliters = value * 28.4131
    elif from_unit == "pintas_uk":
        value_in_milliliters = value * 568.261
    elif from_unit == "cuartos_de_galon_uk":
        value_in_milliliters = value * 1136.52
    elif from_unit == "galones_uk":
        value_in_milliliters = value * 4546.09
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from milliliters
    if to_unit == "mililitros":
        return value_in_milliliters 
    elif to_unit == "centimetros_cubicos":
        return value_in_milliliters 
    elif to_unit == "litros":
        return value_in_milliliters / 1e3
    elif to_unit == "metros_cubicos":
        return value_in_milliliters / 1e6
    elif to_unit == "cucharaditas_us":
        return value_in_milliliters / 4.92892
    elif to_unit == "cucharadas_us":
        return value_in_milliliters / 14.7868
    elif to_unit == "onzas_liquidas_us":
        return value_in_milliliters / 29.5735
    elif to_unit == "tazas_us":
        return value_in_milliliters / 236.588
    elif to_unit == "pintas_us":
        return value_in_milliliters / 473.176
    elif to_unit == "cuartos_de_galon_us":
        return value_in_milliliters / 946.353
    elif to_unit == "galones_us":
        return value_in_milliliters / 3785.41
    elif to_unit == "pulgadas_cubicas":
        return value_in_milliliters / 16.3871
    elif to_unit == "pies_cubicos":
        return value_in_milliliters / 28316.8
    elif to_unit == "yardas_cubicas":
        return value_in_milliliters / 764555
    elif to_unit == "cucharaditas_uk":
        return value_in_milliliters / 5.91939
    elif to_unit == "cucharadas_uk":
        return value_in_milliliters / 17.7582
    elif to_unit == "onzas_liquidas_uk":
        return value_in_milliliters / 28.4131
    elif to_unit == "pintas_uk":
        return value_in_milliliters / 568.261
    elif to_unit == "cuartos_de_galon_uk":
        return value_in_milliliters / 1136.52
    elif to_unit == "galones_uk":
        return value_in_milliliters / 4546.09
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_energy(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert from
    if from_unit == "joules":
        value_in_joules = value
    elif from_unit == "kilojulios":
        value_in_joules = value * 1000
    elif from_unit == "calorias_termales":
        value_in_joules = value * 4.184
    elif from_unit == "calorias_alimentos":
        value_in_joules = value * 4184
    elif from_unit == "pie_libras":
        value_in_joules = value * 1.35582
    elif from_unit == "unidades_termicas_britanicas":
        value_in_joules = value * 1055.06
    elif from_unit == "kilovatio_horas":
        value_in_joules = value * 3.6e6
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from joules
    if to_unit == "joules":
        return value_in_joules
    elif to_unit == "kilojulios":
        return value_in_joules / 1000
    elif to_unit == "calorias_termales":
        return value_in_joules / 4.184
    elif to_unit == "calorias_alimentos":
        return value_in_joules / 4184
    elif to_unit == "pie_libras":
        return value_in_joules / 1.35582
    elif to_unit == "unidades_termicas_britanicas":
        return value_in_joules / 1055.06
    elif to_unit == "kilovatio_horas":
        return value_in_joules / 3.6e6
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_area(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to square millimeters
    if from_unit == "milimetros_cuadrados":
        value_in_square_millimeters = value
    elif from_unit == "centimetros_cuadrados":
        value_in_square_millimeters = value * 100
    elif from_unit == "metros_cuadrados":
        value_in_square_millimeters = value * 1e6
    elif from_unit == "hectareas":
        value_in_square_millimeters = value * 1e10
    elif from_unit == "kilometros_cuadrados":
        value_in_square_millimeters = value * 1e12
    elif from_unit == "pulgadas_cuadradas":
        value_in_square_millimeters = value * 645.16
    elif from_unit == "pies_cuadrados":
        value_in_square_millimeters = value * 92903
    elif from_unit == "yardas_cuadradas":
        value_in_square_millimeters = value * 836127
    elif from_unit == "acres":
        value_in_square_millimeters = value * 4046856422.4
    elif from_unit == "millas_cuadradas":
        value_in_square_millimeters = value * 2589988110336
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from square millimeters
    if to_unit == "milimetros_cuadrados":
        return value_in_square_millimeters
    elif to_unit == "centimetros_cuadrados":
        return value_in_square_millimeters / 100
    elif to_unit == "metros_cuadrados":
        return value_in_square_millimeters / 1e6
    elif to_unit == "hectareas":
        return value_in_square_millimeters / 1e10
    elif to_unit == "kilometros_cuadrados":
        return value_in_square_millimeters / 1e12
    elif to_unit == "pulgadas_cuadradas":
        return value_in_square_millimeters / 645.16
    elif to_unit == "pies_cuadrados":
        return value_in_square_millimeters / 92903
    elif to_unit == "yardas_cuadradas":
        return value_in_square_millimeters / 836127
    elif to_unit == "acres":
        return value_in_square_millimeters / 4046856422.4
    elif to_unit == "millas_cuadradas":
        return value_in_square_millimeters / 2589988110336
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")

def convert_speed(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to centimeters per second
    if from_unit == "centimetros_por_segundo":
        value_in_centimeter_per_second = value
    elif from_unit == "metros_por_segundo":
        value_in_centimeter_per_second = value * 100
    elif from_unit == "kilometros_por_hora":
        value_in_centimeter_per_second = value / 0.036
    elif from_unit == "pies_por_segundo":
        value_in_centimeter_per_second = value * 30.48
    elif from_unit == "millas_por_hora":
        value_in_centimeter_per_second = value * 44.706
    elif from_unit == "nudos":
        value_in_centimeter_per_second = value * 51.4444
    elif from_unit == "mach":
        value_in_centimeter_per_second = value * 34029
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from centimeters per second
    if to_unit == "centimetros_por_segundo":
        return value_in_centimeter_per_second
    elif to_unit == "metros_por_segundo":
        return value_in_centimeter_per_second / 100
    elif to_unit == "kilometros_por_hora":
        return value_in_centimeter_per_second * 0.036
    elif to_unit == "pies_por_segundo":
        return value_in_centimeter_per_second / 30.48
    elif to_unit == "millas_por_hora":
        return value_in_centimeter_per_second / 44.706
    elif to_unit == "nudos":
        return value_in_centimeter_per_second / 51.4444
    elif to_unit == "mach":
        return value_in_centimeter_per_second / 34029
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")

def convert_time(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to microseconds
    if from_unit == "microsegundos":
        value_in_microseconds = value
    elif from_unit == "milisegundos":
        value_in_microseconds = value * 1000
    elif from_unit == "segundos":
        value_in_microseconds = value * 1e6
    elif from_unit == "minutos":
        value_in_microseconds = value * 6e7
    elif from_unit == "horas":
        value_in_microseconds = value * 3.6e9
    elif from_unit == "dias":
        value_in_microseconds = value * 8.64e10
    elif from_unit == "semanas":
        value_in_microseconds = value * 6.048e11
    elif from_unit == "años":
        value_in_microseconds = value * 3.1536e13
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from microseconds
    if to_unit == "microsegundos":
        return value_in_microseconds
    elif to_unit == "milisegundos":
        return value_in_microseconds / 1000
    elif to_unit == "segundos":
        return value_in_microseconds / 1e6
    elif to_unit == "minutos":
        return value_in_microseconds / 6e7
    elif to_unit == "horas":
        return value_in_microseconds / 3.6e9
    elif to_unit == "dias":
        return value_in_microseconds / 8.64e10
    elif to_unit == "semanas":
        return value_in_microseconds / 6.048e11
    elif to_unit == "años":
        return value_in_microseconds / 3.1536e13
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_power(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert from
    if from_unit == "vatios":
        value_in_watts = value 
    elif from_unit == "kilovatios":
        value_in_watts = value * 1000
    elif from_unit == "caballos_de_fuerza_eeuu":
        value_in_watts = value * 745.7
    elif from_unit == "pie_libras_por_minuto":
        value_in_watts = value / 44.2537
    elif from_unit == "unidades_termicas_britanicas_por_minuto":
        value_in_watts = value / 0.056869
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert to
    if to_unit == "vatios":
        return value_in_watts
    elif to_unit == "kilovatios":
        return value_in_watts / 1000
    elif to_unit == "caballos_de_fuerza_eeuu":
        return value_in_watts / 745.7
    elif to_unit == "pie_libras_por_minuto":
        return value_in_watts * 44.2537
    elif to_unit == "unidades_termicas_britanicas_por_minuto":
        return value_in_watts * 0.056869
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_angle(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to grades
    if from_unit == "grados":
        value_in_grades = value
    elif from_unit == "radianes":
        value_in_grades = value / (pi / 180)
    elif from_unit == "grados_centesimales":
        value_in_grades = value / (200 / 180)
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from grades
    if to_unit == "grados":
        return value_in_grades
    elif to_unit == "radianes":
        return value_in_grades * (pi / 180)
    elif to_unit == "grados_centesimales":
        return value_in_grades * (200 / 180)
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_pressure(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to atmospheres
    if from_unit == "atmosferas":
        value_in_atmospheres = value
    elif from_unit == "bares":
        value_in_atmospheres = value / 1.01325
    elif from_unit == "kilopascales":
        value_in_atmospheres = value / 101.325
    elif from_unit == "milimetros_de_mercurio":
        value_in_atmospheres = value / 760
    elif from_unit == "pascales":
        value_in_atmospheres = value / 101325
    elif from_unit == "libras_por_pulgada_cuadrada":
        value_in_atmospheres = value / 14.6959
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from atmospheres
    if to_unit == "atmosferas":
        return value_in_atmospheres
    elif to_unit == "bares":
        return value_in_atmospheres * 1.01325
    elif to_unit == "kilopascales":
        return value_in_atmospheres * 101.325
    elif to_unit == "milimetros_de_mercurio":
        return value_in_atmospheres * 760
    elif to_unit == "pascales":
        return value_in_atmospheres * 101325
    elif to_unit == "libras_por_pulgada_cuadrada":
        return value_in_atmospheres * 14.6959
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    #endregion

def convert_data(value:float, from_unit:str, to_unit:str) -> float:
    #region Convert to bits
    if from_unit == "bits":
        value_in_bits = value
    elif from_unit == "cuarteto":
        value_in_bits = value * 4
    elif from_unit == "bytes":
        value_in_bits = value * 8
    elif from_unit == "kilobits":
        value_in_bits = value * 1000
    elif from_unit == "kibibits":
        value_in_bits = value * 1024
    elif from_unit == "kilobytes":
        value_in_bits = value * 8000
    elif from_unit == "kibibytes":
        value_in_bits = value * 8192
    elif from_unit == "megabits":
        value_in_bits = value * 1e6
    elif from_unit == "mebibits":
        value_in_bits = value * 1_048_576
    elif from_unit == "megabytes":
        value_in_bits = value * 8e6
    elif from_unit == "mebibytes":
        value_in_bits = value * 8_388_608
    elif from_unit == "gigabits":
        value_in_bits = value * 1e9
    elif from_unit == "gibibits":
        value_in_bits = value * 1_073_741_824
    elif from_unit == "gigabytes":
        value_in_bits = value * 8e9
    elif from_unit == "gibibytes":
        value_in_bits = value * 8_589_934_592
    elif from_unit == "terabits":
        value_in_bits = value * 1e12
    elif from_unit == "tebibits":
        value_in_bits = value * 1_099_511_627_776
    elif from_unit == "terabytes":
        value_in_bits = value * 8e12
    elif from_unit == "tebibytes":
        value_in_bits = value * 8_796_093_208_022
    elif from_unit == "petabits":
        value_in_bits = value * 1e15
    elif from_unit == "pebibits":
        value_in_bits = value * 1_125_899_906_842_624
    elif from_unit == "petabytes":
        value_in_bits = value * 8e15
    elif from_unit == "pebibytes":
        value_in_bits = value * 9_007_199_254_740_992
    elif from_unit == "exabits":
        value_in_bits = value * 1e18
    elif from_unit == "exbibits":
        value_in_bits = value * 1_152_921_504_606_846_976
    elif from_unit == "exabytes":
        value_in_bits = value * 8e18
    elif from_unit == "exbibytes":
        value_in_bits = value * 9_223_372_036_854_775_808
    elif from_unit == "zettabits":
        value_in_bits = value * 1e21
    elif from_unit == "zebibits":
        value_in_bits = value * 1_180_591_620_717_411_303_424
    elif from_unit == "zettabytes":
        value_in_bits = value * 8e21
    elif from_unit == "zebibytes":
        value_in_bits = value * 9_444_732_965_732_923_457_740_000
    elif from_unit == "yottabits":
        value_in_bits = value * 1e24
    elif from_unit == "yobibits":
        value_in_bits = value * 1_208_925_819_614_629_174_706_176
    elif from_unit == "yottabytes":
        value_in_bits = value * 8e24
    elif from_unit == "yobibytes":
        value_in_bits = value * 9_671_406_556_917_033_397_649_408
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de entrada invalida: '{from_unit}'.{Style.RESET_ALL}")
    #endregion

    #region Convert from bits
    if to_unit == "bits":
        return value_in_bits
    elif to_unit == "cuarteto":
        return value_in_bits / 4
    elif to_unit == "bytes":
        return value_in_bits / 8
    elif to_unit == "kilobits":
        return value_in_bits / 1000
    elif to_unit == "kibibits":
        return value_in_bits / 1024
    elif to_unit == "kilobytes":
        return value_in_bits / 8000
    elif to_unit == "kibibytes":
        return value_in_bits / 8192
    elif to_unit == "megabits":
        return value_in_bits / 1e6
    elif to_unit == "mebibits":
        return value_in_bits / 1_048_576
    elif to_unit == "megabytes":
        return value_in_bits / 8e6
    elif to_unit == "mebibytes":
        return value_in_bits / 8_388_608
    elif to_unit == "gigabits":
        return value_in_bits / 1e9
    elif to_unit == "gibibits":
        return value_in_bits / 1_073_741_824
    elif to_unit == "gigabytes":
        return value_in_bits / 8e9
    elif to_unit == "gibibytes":
        return value_in_bits / 8_589_934_592
    elif to_unit == "terabits":
        return value_in_bits / 1e12
    elif to_unit == "tebibits":
        return value_in_bits / 1_099_511_627_776
    elif to_unit == "terabytes":
        return value_in_bits / 8e12
    elif to_unit == "tebibytes":
        return value_in_bits / 8_796_093_208_022
    elif to_unit == "petabits":
        return value_in_bits / 1e15
    elif to_unit == "pebibits":
        return value_in_bits / 1_125_899_906_842_624
    elif to_unit == "petabytes":
        return value_in_bits / 8e15
    elif to_unit == "pebibytes":
        return value_in_bits / 9_007_199_254_740_992
    elif to_unit == "exabits":
        return value_in_bits / 1e18
    elif to_unit == "exbibits":
        return value_in_bits / 1_152_921_504_606_846_976
    elif to_unit == "exabytes":
        return value_in_bits / 8e18
    elif to_unit == "exbibytes":
        return value_in_bits / 9_223_372_036_854_775_808
    elif to_unit == "zettabits":
        return value_in_bits / 1e21
    elif to_unit == "zebibits":
        return value_in_bits / 1_180_591_620_717_411_303_424
    elif to_unit == "zettabytes":
        return value_in_bits / 8e21
    elif to_unit == "zebibytes":
        return value_in_bits / 9_444_732_965_732_923_457_740_000
    elif to_unit == "yottabits":
        return value_in_bits / 1e24
    elif to_unit == "yobibits":
        return value_in_bits / 1_208_925_819_614_629_174_706_176
    elif to_unit == "yottabytes":
        return value_in_bits / 8e24
    elif to_unit == "yobibytes":
        return value_in_bits / 9_671_406_556_917_033_397_649_408
    else:
        raise ValueError(f"{Fore.MAGENTA}Unidad de salida invalida: '{to_unit}'.{Style.RESET_ALL}")
    # endregion
