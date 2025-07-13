# 🚀 Conversor de Unidades General - v0.5

## 👋 ¡Bienvenido al Conversor de Unidades General\!

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

Para ejecutar este programa, necesitarás Python 3.x instalado.

1.  **Clona este repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```
    O descargalo manualmente.
2.  **Instala las dependencias necesarias:**
    ```bash
    pip install colorama customtkinter pillow
    ```
    O en caso de encontrarse en la carpeta de proyecto:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Uso

### Modo CLI (Consola/Terminal)

Para usar la calculadora en modo terminal, ejecuta el script de la siguiente manera:

```bash
python main.py cli #Tambien cuenta con alias como Terminal o T
```
En caso de no proporcionar un argumento, esta será la opción por defecto.

Una vez iniciado, el programa te guiará:

1.  Selecciona la **categoría** de unidad que deseas convertir (ej., `LONGITUD`, `TEMPERATURA`).
2.  Indica la **unidad de entrada**, el **valor** y la **unidad de salida** uno tras otro.

El programa devolverá la conversión:

```
>> 5.0 celsius equivalen a 278.15 kelvin.
```

### Modo GUI (Ventana Gráfica)

Para usar la calculadora con la interfaz gráfica, ejecuta:

```bash
python main.py gui #Tambien cuenta con alias como CTK o Custom TKinter
```

Se abrirá una ventana donde podrás seleccionar las unidades de entrada y salida, ingresar el valor y ver el resultado de forma interactiva.

## 💡 Sugerencias y Contribuciones

Este proyecto está en la versión 0.5, lo que significa que aún hay mucho espacio para mejoras y nuevas funcionalidades. ¡Toda retroalimentación, informes de errores y contribuciones son bienvenidos\!

Si deseas contribuir:

1.  Haz un "fork" del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz "commit" de ellos (`git commit -m 'feat: Añadir nueva funcionalidad X'`).
4.  Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5.  Abre un "Pull Request".

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

-----

### 🤔 Retroalimentación y Sugerencias Adicionales:

¡Hola, Alejandro\! Tu proyecto suena muy útil y la organización que le estás dando es excelente. Aquí tienes algunas preguntas y sugerencias que podrían complementar tu `README.md` o mejorar el proyecto en sí:

#### Para el `README.md`:

1.  **Capturas de Pantalla (Screenshots):** Para el modo GUI, ¡unas capturas de pantalla harían que tu `README` sea mucho más atractivo\! Un usuario potencial podrá ver inmediatamente cómo se ve y funciona tu interfaz.
2.  **Sección de Contacto:** ¿Cómo pueden contactarte los usuarios o colaboradores? Un correo electrónico o tu perfil de LinkedIn/Twitter podría ser útil.
3.  **Roadmap (Hoja de Ruta):** Si tienes planes futuros para el proyecto (ej., añadir más unidades, nuevas categorías, soporte para otras unidades compuestas como m/s² para aceleración), puedes incluir una pequeña sección de "Roadmap" para que los interesados sepan qué esperar.
4.  **Agradecimientos (Acknowledgements):** Si usaste recursos específicos, librerías que no sean las obvias, o si alguien te ayudó, una sección de agradecimientos es un buen detalle.

#### Para el Proyecto en Sí:

1.  **Consistencia en Nomenclatura de Unidades:** Es genial que manejes aliases. Asegúrate de que tus factores de conversión (`conversion_to_meters`, etc.) estén basados en nombres de unidades consistentes (ej., `milimetros_cuadrados` para la clave principal, y `mm2`, `mm^2`, etc., como aliases). Tu estructura actual de diccionarios es muy buena para esto.
2.  **Manejo de Errores Más Robusto en CLI:** Actualmente, el `print` y `_enter_to_continue()` no lanzan una excepción que detenga el flujo. Si el usuario ingresa una unidad inválida, quizás quieras:
      * Volver a pedir la entrada hasta que sea válida.
      * Lanzar una excepción (como ya lo hicimos en el ejemplo de la función `convert_lenght`) para que el programa maneje el error de forma más estructurada.
3.  **Unidades Compuestas:** ¿Considerarías unidades compuestas en el futuro, como densidad (kg/m³) o unidades de aceleración (m/s²)? Eso podría llevar tu conversor a otro nivel de complejidad, pero también de utilidad.
4.  **Archivos de Configuración/Datos:** Si tus listas de unidades y sus factores de conversión crecen mucho, podrías considerar moverlos a archivos externos (ej. JSON, YAML) que el programa lea al inicio. Esto facilita la edición de unidades sin tocar el código Python principal.
5.  **Pruebas Unitarias:** A medida que tu proyecto crece, las pruebas unitarias (`unittest` o `pytest`) son fundamentales. Te asegurarían que todas tus conversiones son correctas y que los cambios futuros no introducen errores.