## @file interfaz_terminal.py
# @brief Interfaz de Usuario para edicion de consola, se basa en prints para mostrar contenido
# @author Alejandro Cortés
# @version 0.3

#region Importaciones
import os
from colorama import Fore, Style, init
from logic.conversion_logic import (
    ConversionSystems,
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
    print("-" * 40)
    for system in ConversionSystems:
        #Obtiene numero de sistema, nombre, y lo muestra solo con inicial en mayuscula
        print(f"{Fore.CYAN}{system.value}. {system.name.replace("_", " ").title()}")       
    print(f"{Fore.CYAN}0. Salir")

def get_data(system): #!PENDIENTE
    pass
    #from_unit = ""
    #to_unit = ""
    
    #if :
    #return None
    #return [value,from_unit, to_unit]

def convert_temperature_interface():
    value = None
    from_unit = None
    to_unit = None
    chosen_unit = None
    units = {
        "celsius" : ("0", "c", "celsius"),
        "kelvin" : ("1", "k", "kelvin"),
        "farenheit" : ("2", "f", "farenheit"),
    }
    
    while(True):
        _clear_console()
        print(f"{Fore.BLUE}--------------------TEMPERATURA--------------------")
        
        i=1
        for unit in units:
            print(f"{Fore.CYAN}{i}. {str(unit)}")
            i+=1
        print(f"{Fore.CYAN}0. Volver al menu principal")
        
        #Si ya se ingresaron datos
        if from_unit is None:
            chosen_unit = input(f"{Fore.YELLOW}Elije tu unidad de entrada: {Style.RESET_ALL}")
            for unit in units:
                if chosen_unit in units[unit]:
                    from_unit = unit
                    break
            if from_unit is None:
                print(f"{Fore.RED}ERROR: Unidad ingresada invalida")
                continue
        else:
            print(f"{Fore.YELLOW}Elije tu unidad de entrada: {Style.RESET_ALL}{from_unit}")
        
        if value is None:
            try:
                value = float(input(f"{Fore.YELLOW}Ingresa tu valor: {Style.RESET_ALL}"))
            except Exception as e:
                print(f"{Fore.RED}ERROR: {e}")
                continue
        else:
            print(f"{Fore.YELLOW}Ingresa tu valor: {Style.RESET_ALL}{value}")
            
        if to_unit is None:
            chosen_unit = input(f"{Fore.YELLOW}Elije tu unidad de salida: {Style.RESET_ALL}")
            for unit in units:
                if chosen_unit in units[unit]:
                    to_unit = unit
                    break
            if from_unit is None:
                print(f"{Fore.RED}ERROR: Unidad ingresada invalida")
                continue
        else:
            print(f"{Fore.YELLOW}Elije tu unidad de entrada: {Style.RESET_ALL}{to_unit}")
            
        print(f"La llamada a la funcion es: {value}, {from_unit}, {to_unit}")
        converted_value = convert_temperature(value, from_unit, to_unit)
        return (value, from_unit, converted_value, to_unit)
    

def convert_lenght_interface():
    pass

def convert_mass_interface():
    pass

def convert_volume_interface():
    pass

def convert_energy_interface():
    pass

def convert_area_interface():
    pass

def convert_speed_interface():
    pass

def convert_time_interface():
    pass

def convert_power_interface():
    pass

def convert_angle_interface():
    pass

def convert_pressure_interface():
    pass

def convert_data_interface():
    pass


def start_interface():
    chosen_system = None
    system_alias = {
        "TEMPERATURA": ["tmp", "temp", "temperatura", "temperature", "temperaturas", "temperatures"],
        "LONGITUD": ["l", "len", "long", "longitud", "length", "distancia", "distances"],
        "MASA": ["mass", "masa", "peso", "weight", "m"],
        "VOLUMEN": ["vol", "volumen", "volume"],
        "ENERGIA": ["e", "en", "eng", "energia", "energy", "nrg"],
        "AREA": ["area", "surface", "superficie"],
        "VELOCIDAD": ["vel", "velocidad", "speed", "velocity"],
        "TIEMPO": ["time", "tiempo", "duracion", "duration"],
        "POTENCIA": ["pow", "potencia", "power"],
        "ANGULOS": ["ang", "angulo", "angulos", "angle", "angles"],
        "PRESION": ["pres", "pressure", "presion"],
        "DATOS": ["data", "datos", "bytes", "bits"]
    }
        
    while(True):
        _show_system_menu()
        sistema = input(f"{Fore.YELLOW}Elije tu sistema de conversion: {Style.RESET_ALL}")
        
        if int(sistema) == 0:
            break
        elif int(sistema) in range(13):
            chosen_system = int(sistema)
        else:    
            for system in system_alias:
                if sistema in system_alias[system]:
                    chosen_system = str(system)
        if chosen_system is None:
            print(f"{Fore.MAGENTA}No es una opcion valida!!")
            continue
        else:
            print(f"Se eligio el sistema: {ConversionSystems(chosen_system).name}...")
            #conversion = get_data(str(ConversionSystems(chosen_system).name))
            #if conversion is None:
            conversion = None
            #    continue
            
            try:
                match chosen_system:
                    case ConversionSystems.TEMPERATURA.value:
                        result = convert_temperature_interface()
                    case ConversionSystems.LONGITUD.value:
                        result = convert_lenght(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.MASA.value:
                        result = convert_mass(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.VOLUMEN.value:
                        result = convert_volume(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.ENERGIA.value:
                        result = convert_energy(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.AREA.value:
                        result = convert_area(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.VELOCIDAD.value:
                        result = convert_speed(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.TIEMPO.value:
                        result = convert_time(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.POTENCIA.value:
                        result = convert_power(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.ANGULOS.value:
                        result = convert_angle(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.PRESION.value:
                        result = convert_pressure(conversion[0],conversion[1],conversion[2])
                    case ConversionSystems.DATOS.value:
                        result = convert_data(conversion[0],conversion[1],conversion[2])
                print(f">>{result[0]} {result[1]} equivalen a {result[2]} {result[3]}")
                _enter_to_continue()
            except ValueError as e:
                print(f"{Fore.RED}ERROR: {e}")
                
    #SEGUIR CON TEMP, CAMBIAR A OTRO O SALIR

    print(f"{Fore.BLUE}Saliendo del programa...")
    _enter_to_continue()

