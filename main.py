"""
main.py

Aplicación para convertir valores entre diferentes unidades
de medida (temperatura, longitud, masa, entre otros).

Autor: Alejandro Cortés
Versión: 1.0
"""


# ────────────────────── IMPORTACIONES ──────────────────────
import sys
import logging

from colorama import Fore, Style, init


# ────────────────────── VARIABLES GLOBALES / CONFIGURACION ──────────────────────
init(autoreset=True)    # Inicializa Colorama con autoreset en cada impresión
BOLD = Style.BRIGHT     # Atajo para aplicar estilo de negritas


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

# ────────────────────── FUNCIONES AUXILIARES ──────────────────────
def _enter_to_continue() -> None:
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input(f"{Fore.YELLOW}Presione enter para continuar...\n")


def _get_ui_mode() -> bool:
    """
    Determina el modo de interfaz a usar (CLI o GUI) según argumentos por consola.
    Si no se pasa argumento, se asume GUI.
    """
    cli_args = ["0", "TERMINAL", "TER", "T", "FALSE", "CLI"]
    gui_args = ["1", "CUSTOMTKINTER", "CTKINTER", "CTK", "C", "TRUE", "GUI"]

    if len(sys.argv) < 2:
        logger.info("No se proporcionó argumento. Ejecutando en modo GUI.")
        return True

    argument = sys.argv[1].strip().upper()
    if argument in cli_args:
        return False
    elif argument in gui_args:
        return True
    else:
        logger.error("¡Argumento inválido!")
        _enter_to_continue()
        return True  # Valor por defecto en caso de error


# ────────────────────── FUNCIÓN PRINCIPAL ──────────────────────
def main() -> None:
    """Punto de entrada principal de la aplicación."""
    ui_mode = _get_ui_mode()

    # pylint: disable=broad-except
    try:
        # pylint: disable=import-outside-toplevel
        if ui_mode:
            from interfaces.interfaz_ctk import start_interface
        else:
            from interfaces.interfaz_cli import start_interface

        logger.info(
            "Inicializando interfaz: %s", 
            "gráfica (GUI)..." if ui_mode else "de consola (CLI)..."
        )
        start_interface()
    except ImportError as e:
        logger.error("No se pudo cargar el módulo: %s", e)
        _enter_to_continue()
    except KeyboardInterrupt:
        logger.warning("Ejecución interrumpida por el usuario.")
    except Exception as e:
        logger.critical("Error inesperado: %s", e)
        _enter_to_continue()


# ────────────────────── PUNTO DE EJECUCIÓN ──────────────────────
if __name__ == "__main__":
    main()
