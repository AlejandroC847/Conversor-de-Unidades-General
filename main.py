# @file main.py
# @brief Conversor entre diversos tipos de unidades y escalas como temperatura, longitud, masa, etc.
# @author Alejandro Cortés
# @version 0.5

#region -------------------------Importaciones-------------------------
import sys
import os
from colorama import Fore, Style, init
#endregion

#region --------------------Variables globales e inicializaciones--------------------
ui_mode = False # False para edicion consola/terminal, True para edicion CTK
init(autoreset=True) #Inicializar colorama
BOLD = Style.BRIGHT #Atajo para negritas
#endregion

# -------------------------Funciones de utilidad-------------------------

def _clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def _enter_to_continue():
    input(f"{Fore.YELLOW}Presione enter para continuar...\n")

def _set_ui_mode():
    global ui_mode
    cli = ["0", "TERMINAL", "TER", "T", "FALSE", "CLI"]
    gui = ["1", "CUSTOMTKINTER", "CTKINTER", "CTK", "C", "TRUE", "GUI"]
    #Establecer modo de GUI
    if len(sys.argv) < 2:
        print(f"{Fore.WHITE}No se proporciono argumento, ejecutando edicion de consola.\n")
        ui_mode = False
    else:
        argument = sys.argv[1].upper()
        if argument in cli:
            print("Ejecutando edicion de consola")
            ui_mode = False
        elif argument in gui:
            print("Ejecutando edicion de Custom TKinter")
            ui_mode = True
        else:
            print(f"{Fore.RED}Argumento invalido!")
            _enter_to_continue()

# -------------------------Funcion Principal-------------------------
def main():
    _set_ui_mode()
    if ui_mode:
        try:
            from interfaces import interfaz_ctk
            #!PENDIENTE
            print(f"{Fore.GREEN}{BOLD}inicializar CTK, aun pendiente")
            interfaz_ctk.show_ui()
        except ImportError as e:
            print(f"{Fore.LIGHTRED_EX}No se pudo cargar el modulo!: {e}")
            _enter_to_continue()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}Error inesperado: {e}")
            _enter_to_continue()
    else:
        try:
            from interfaces import interfaz_terminal
            interfaz_terminal.start_interface()
        except ImportError as e:
            print(f"{Fore.LIGHTRED_EX}No se pudo cargar el modulo!: {e}")
            _enter_to_continue()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}Error inesperado: {e}")
            _enter_to_continue()

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

# -------------------------Flujo principal-------------------------
if __name__ == "__main__":
    main()