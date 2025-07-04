
from colorama import Fore, Style, init

def show_terminal_ui():
    #Entrada de sistema de conversion
    while(True):
        _clear_console()
        print(f"{Fore.BLUE}{BOLD}Conversor de unidades\n\n")
        print("Elije tu sistema de conversion:")
        print("-" * 32)
        get_enum("ConversionSystems")
        
        sistema = input("Que tipo de sistema quieres converitr?: ")
        
        if sistema.upper() not in ConversionSystems.__members__:
            print(f"{Fore.MAGENTA}No es una opcion valida!!")
            _enter_to_continue()
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

resultado = 1e10 * 39.3701
print(resultado)
print(f"{resultado:.5e}") # Formato para notación científica con 5 decimales