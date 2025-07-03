# @file Conversor de unidades - vPython.
# @brief Conversor entre diversos tipos de unidades y escalas como 
# @author Alejandro Cortés
# @version 0.1

#region Importaciones
import sys
import os
from enum import Enum, auto
from colorama import Fore, Style, init
#endregion

#region Variables globales e inicializaciones
ui_mode = False # False para edicion consola/terminal, True para edicion CTK
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

init(autoreset=True)
BOLD = Style.BRIGHT
#endregion

#$ Funciones

def main():
    #set_ui_mode() # !SOLO PARA PRUEBAS
    if ui_mode:
        print(f"{Fore.GREEN}{BOLD}inicializar CTK, aun pendiente")
    else:
        show_terminal_ui()

def set_ui_mode():
    global ui_mode
    #Establecer modo de GUI
    if len(sys.argv) < 2:
        print(f"{Fore.WHITE}No se proporciono argumento, ejecutando edicion de consola.\n")
        ui_mode = True
    else:
        argument = sys.argv[1].upper()
        if argument == "0" or argument == "TERMINAL" or argument == "T" or argument == "TER" or argument == "FALSE":
            print("Ejecutando edicion de consola")
            ui_mode = False
        elif (argument == "1" or argument == "CUSTOMTKINTER" or argument == "CTK" or argument == "CTKINTER" or argument == "True"):
            print("Ejecutando edicion de Custom TKinter")
            ui_mode = True
        else:
            print(f"{Fore.RED}Argumento invalido!")
            enter_to_continue()

def show_terminal_ui():
    #Entrada de sistema de conversion
    while(True):
        clear_console()
        print(f"{Fore.BLUE}{BOLD}Conversor de unidades\n\n")
        print("Elije tu sistema de conversion:")
        print("-" * 32)
        get_enum("ConversionSystems")
        
        sistema = input("Que tipo de sistema quieres converitr?: ")
        
        if sistema.upper() not in ConversionSystems.__members__:
            print(f"{Fore.MAGENTA}No es una opcion valida!!")
            enter_to_continue()
            continue
        else:
            break
    
    #Sub menu de 
    print(sistema)

def get_enum(enum_name):
    if enum_name == "ConversionSystems":
        for i in range(1, len(ConversionSystems) + 1):
            print(f"> {ConversionSystems(i).name}")
    else:
        print(f"{Fore.MAGENTA}No se encontro la enumeracion\n")

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enter_to_continue():
    input(f"{Fore.YELLOW}Presione enter para continuar...\n")

#! SE PUEDEN BORRAR
def prueba_colores():
    print(f"{Fore.BLACK}Texto color negro normal")
    print(f"{Fore.LIGHTBLACK_EX}Texto color negro brillante colorama")
    print(f"{Fore.RED}Texto color rojo colorama")
    print(f"{Fore.LIGHTRED_EX}Texto color rojo brillante colorama")
    print(f"{Fore.GREEN}Texto color verde colorama")
    print(f"{Fore.LIGHTGREEN_EX}Texto color verde brillante colorama")
    print(f"{Fore.YELLOW}Texto color amarillo colorama")
    print(f"{Fore.LIGHTYELLOW_EX}Texto color amarillo brillante colorama")
    print(f"{Fore.BLUE} Texto color azul colorama")
    print(f"{Fore.LIGHTBLUE_EX} Texto color azul brillante colorama")
    print(f"{Fore.MAGENTA}Texto color magenta colorama")
    print(f"{Fore.LIGHTMAGENTA_EX}Texto color magenta brillante colorama")
    print(f"{Fore.CYAN}Texto color cian colorama")
    print(f"{Fore.LIGHTCYAN_EX}Texto color cian brillante colorama")
    print(f"{Fore.WHITE}Texto color blanco colorama")
    print(f"{Fore.LIGHTWHITE_EX}Texto color blanco brillante colorama")
    
    print(f"{Style.DIM}Texto brillo dim")
    print(f"{Style.NORMAL}Texto brillo normal")
    print(f"{Style.BRIGHT}Texto brillo brillante")

#Flujo principal
if __name__ == "__main__":
    main()
    #prueba_colores()