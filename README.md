# 🚀 Conversor de Unidades General - v1.0

## 👋 Bienvenido al Conversor de Unidades General

Desarrollado por Alejandro Cortés, este programa es una herramienta versátil diseñada para simplificar la conversión entre una amplia gama de unidades en diversas categorías.
Ya sea que necesites convertir longitudes de Angstroms a Parsecs, masas de gramos a libras, o temperaturas de Celsius a Kelvin, este conversor te lo pone fácil.

El programa está disponible en dos modos de ejecución: una **interfaz de línea de comandos (CLI)** para conversiones rápidas y una **interfaz gráfica de usuario (GUI)** intuitiva construida con `CustomTkinter` para una experiencia más visual.

## ✨ Características Principales

  * **Amplia Cobertura de Unidades:** Soporta conversiones en múltiples categorías y sus respectivas unidades.
  * **Modo CLI:** Realiza conversiones directamente desde tu terminal, ideal para scripts o automatización.
  * **Modo GUI:** Interfaz gráfica amigable para una interacción visual y sencilla.
  * **Detección Flexible de Unidades:** Reconoce múltiples alias para cada unidad (ej. "m", "metro", "meter" para metros).
  * **Resultados Claros:** Muestra las conversiones de forma legible y contextualizada.

## 📦 Categorías de Conversión Soportadas

Actualmente, el conversor maneja las siguientes categorías de unidades:

  * **TEMPERATURA:** Celsius, Kelvin, Fahrenheit.
  * **LONGITUD:** Angstroms, Nanómetros, Micrones, Milímetros, Centímetros, Metros, Kilómetros, Pulgadas, Pies, Yardas, Millas, Millas Náuticas, Unidades Astronómicas, Años Luz, Parsecs.
  * **MASA:** Gramos, Quilates, Miligramos, Centigramos, Decigramos, Decagramos, Hectogramos, Kilogramos, Toneladas Métricas, Onzas, Libras, Piedra, Toneladas Cortas (EEUU), Toneladas Largas (Reino Unido).
  * **VOLUMEN:** Mililitros, Centímetros Cúbicos, Litros, Metros Cúbicos, Cucharaditas (US/UK), Cucharadas (US/UK), Onzas Líquidas (US/UK), Tazas (US), Pintas (US/UK), Cuartos de Galón (US/UK), Galones (US/UK), Pulgadas Cúbicas, Pies Cúbicos, Yardas Cúbicas.
  * **ENERGÍA:** Joules, Kilojulios, Calorías Termales, Calorías de Alimentos, Pie-Libras, Unidades Térmicas Británicas, Kilovatio-Horas.
  * **ÁREA:** Milímetros Cuadrados, Centímetros Cuadrados, Metros Cuadrados, Hectáreas, Kilómetros Cuadrados, Pulgadas Cuadradas, Pies Cuadrados, Yardas Cuadradas, Acres, Millas Cuadradas.
  * **VELOCIDAD:** Centímetros por Segundo, Metros por Segundo, Kilómetros por Hora, Pies por Segundo, Millas por Hora, Nudos, Mach.
  * **TIEMPO:** Microsegundos, Milisegundos, Segundos, Minutos, Horas, Días, Semanas, Años.
  * **POTENCIA:** Vatios, Kilovatios, Caballos de Fuerza (EEUU), Pie-Libras/Minuto, Unidades Térmicas Británicas/Minuto.
  * **ÁNGULOS:** Grados, Radianes, Grados Centesimales.
  * **PRESIÓN:** Atmósferas, Bares, Kilopascales, Milímetros de Mercurio, Pascales, Libras por Pulgada Cuadrada.
  * **DATOS:** Bits, Cuarteto (Nibble), Byte, Kilobit, Kibibit, Kilobyte, Kibibyte, Megabit, Mebibit, Megabyte, Mebibyte, Gigabit, Gibibit, Gigabyte, Gibibyte, Terabit, Tebibit, Terabyte, Tebibyte, Petabit, Pebibit, Petabyte, Pebibyte, Exabit, Exbibit, Exabyte, Exbibyte, Zettabit, Zebibit, Zettabyte, Zebibyte, Yottabit, Yobibit, Yottabyte, Yobibyte.

## 🛠️ Instalación

Para ejecutar este programa, necesitarás Python instalado (Preferentemente Python 3.10+).

1.  **Obtén los archivos del proyecto:**
  - Clona este repositorio:
    ```bash
    git clone https://github.com/AlejandroC847/Conversor-de-Unidades-General.git
    cd Conversor-de-Unidades-General
    ```
  - O descargalo manualmente. 
2.  **Instala las dependencias necesarias:**
    ```bash
    pip install colorama customtkinter pillow screeninfo
    ```
    O en caso de encontrarse en la carpeta de proyecto:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Uso

### Modo CLI (Consola/Terminal)

Para usar la calculadora en el modo de consola, ejecuta el script de la siguiente manera (desde la raíz del proyecto):

```bash
python main.py cli #Tambien cuenta con alias como Terminal o T
```

Una vez iniciado, el programa te guiará:

1.  Selecciona la **categoría** de unidad que deseas convertir (ej., `LONGITUD`, `TEMPERATURA`). El sistema soporta errores al colocar tu opción.
![CLI - Menú Principal de la Consola](assets/CLI%20-%20Menu%20principal.png)


2.  Indica la **unidad de entrada**, el **valor** y la **unidad de salida** uno tras otro. Puedes usar alias en los sistemas, o su número en la lista.

El programa devolverá la conversión correspondiente:
![CLI - Conversión correcta de LONGITUD](assets/CLI%20-%20SubMenu%20Ej.1.png)

También puede manejar errores de entrada del usuario:
![CLI - Conversión fallida de VOLUMEN](assets/CLI%20-%20SubMenu%20Ej.2.png)

### Modo GUI (Ventana Gráfica)

Para usar la calculadora con la interfaz gráfica, ejecuta:

```bash
python main.py gui #Tambien cuenta con alias como CTK o Custom TKinter
```

En caso de no proporcionar un argumento, esta será la opción por defecto.

Se abrirá una ventana donde podrás seleccionar el sistema de conversión que desees. Además, un interruptor ofrece la capacidad de alternar entre tema claro y tema oscuro (por defecto, se muestra el tema del dispositivo).

![GUI - Menú de selección de sistema](assets/GUI%20-%20Menu-Principal.png)

Al seleccionar algún sistema, se abrirá una ventana emergente propia de dicho sistema donde se deberán seleccionar las unidades de entrada y salida e ingresar el valor para poder ver el resultado de forma dinámica.
![GUI - Menú de selección de sistema](assets/GUI%20-%20Conversor-temperatura.png)
![GUI - Menú de selección de sistema](assets/GUI%20-%20Conversor-tiempo.png)


## 💡 Sugerencias y Contribuciones

Este proyecto está en la versión 1.0, lo que significa que aún hay mucho espacio para mejoras y nuevas funcionalidades. ¡Toda retroalimentación, informes de errores y contribuciones son bienvenidos\!

Si deseas contribuir:

1.  Haz un "fork" del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz "commit" de ellos (`git commit -m 'feat: Añadir nueva funcionalidad X'`).
4.  Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5.  Abre un "Pull Request".

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## ✉️ Contacto

¿Tienes preguntas, sugerencias, quieres ver mis otros proyectos o simplemente quieres saludar? ¡No dudes en contactarme y acceder a mis redes!

* **Correo Electrónico:** Puedes enviarme un mensaje directamente [aquí](mailto:alejandrocortes847@gmail.com).
* **Issue:** Abre un [Issue](https://github.com/AlejandroC847/Conversor-de-Unidades-General/issues) de este repo.
* **GitHub:** Visita mi perfil de GitHub [aquí](https://github.com/AlejandroC847).
* **Portafolio (GitHub Pages):** Explora mi trabajo en mi página personal [aquí](https://alejandroc847.github.io).

---