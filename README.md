# FichajesDeHorarios
SistemaDeFichajesDeHorarios

# Sistema de Fichaje Laboral con Python y Excel

Este es un sistema de fichaje laboral desarrollado en Python que permite a los usuarios registrar su tiempo de trabajo de una manera sencilla. Los registros se almacenan en un archivo Excel para su posterior análisis y seguimiento. A continuación, se proporciona una breve explicación sobre cómo funciona y cómo utilizarlo.

## Características

- **Iniciar Jornada**: Los usuarios pueden iniciar una nueva jornada de trabajo con esta opción. Cada jornada se registra con el nombre del usuario y la fecha actual.

- **Pausar Jornada**: Si un usuario necesita hacer una pausa durante su jornada de trabajo, puede usar esta opción para pausar el tiempo de trabajo.

- **Reanudar Jornada**: Cuando un usuario regresa de una pausa, puede reanudar la jornada para continuar el registro del tiempo de trabajo.

- **Terminar Jornada**: Al finalizar la jornada laboral, el usuario puede utilizar esta opción para registrar el tiempo total trabajado en horas, minutos y segundos. La información se almacena en un archivo Excel.

- **Guardar en Excel**: Se proporciona una opción para guardar todos los registros en un archivo Excel para su posterior análisis.

## Requisitos

Para utilizar este sistema, necesitarás:

- Python instalado en tu computadora.

- La biblioteca `openpyxl`, que puedes instalar utilizando `pip install openpyxl`.

## Cómo Utilizar

1. Ejecuta el script `fichaje_laboral.py` en tu entorno Python.

2. El sistema te mostrará un menú con opciones. Puedes elegir entre iniciar, pausar, reanudar, terminar una jornada o guardar los registros en un archivo Excel.

3. Cuando inicies una jornada, se te pedirá que ingreses tu nombre. El sistema registrará la fecha y hora de inicio.

4. Si necesitas hacer una pausa, selecciona la opción "Pausar jornada". Luego, puedes reanudar la jornada seleccionando la opción correspondiente.

5. Al finalizar tu jornada laboral, selecciona "Terminar jornada". El sistema calculará el tiempo trabajado y lo registrará. También te mostrará el tiempo trabajado en horas, minutos y segundos.

6. Para guardar los registros en un archivo Excel, selecciona la opción "Guardar en Excel".

7. Puedes repetir estos pasos para registrar todas tus jornadas laborales.

## Archivo Excel

Los registros se almacenan en un archivo Excel llamado "registros_horario.xlsx". Puedes encontrar este archivo en el directorio donde se encuentra el script `fichaje_laboral.py`.

## Notas Finales

Este sistema es una herramienta básica para el registro del tiempo de trabajo y puede ser útil para el seguimiento de tus horas laborales. Puedes personalizarlo y extenderlo según tus necesidades específicas. Ten en cuenta que los registros se almacenan en un archivo Excel local, por lo que es importante que lo respaldes regularmente y lo almacenes de manera segura.
