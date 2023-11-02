import datetime
import openpyxl
from openpyxl import Workbook

# Diccionario para almacenar los registros de horario de cada usuario
registros = {}

def iniciar_jornada(usuario):
    if usuario not in registros:
        registros[usuario] = {'horas_trabajadas': datetime.timedelta(), 'fecha': datetime.date.today()}
    else:
        print("Ya has iniciado una jornada hoy. Puedes pausar o finalizar la jornada actual.")

def pausar_jornada(usuario):
    if usuario in registros:
        if 'pausa' not in registros[usuario]:
            registros[usuario]['pausa'] = datetime.datetime.now()
            print("Jornada en pausa.")
        else:
            print("Ya has pausado la jornada. Puedes reanudarla.")

def reanudar_jornada(usuario):
    if usuario in registros and 'pausa' in registros[usuario]:
        pausa = registros[usuario]['pausa']
        registros[usuario]['horas_trabajadas'] += datetime.datetime.now() - pausa
        del registros[usuario]['pausa']
        print("Jornada reanudada.")

def terminar_jornada(usuario, workbook):
    if usuario in registros:
        if 'pausa' in registros[usuario]:
            reanudar_jornada(usuario)
        horas_trabajadas = registros[usuario]['horas_trabajadas']
        fecha = registros[usuario]['fecha']
        horas = int(horas_trabajadas.total_seconds() // 3600)
        minutos = int((horas_trabajadas.total_seconds() % 3600) // 60)
        segundos = int(horas_trabajadas.total_seconds() % 60)
        print(f"Terminaste la jornada con {horas} horas, {minutos} minutos y {segundos} segundos trabajados el {fecha}.")
        if fecha.month not in registros:
            registros[fecha.month] = datetime.timedelta()
        registros[fecha.month] += horas_trabajadas
        del registros[usuario]

        # Guardar el registro en el archivo Excel
        guardar_registro_en_excel(usuario, fecha, horas, minutos, segundos, workbook)

def guardar_registro_en_excel(usuario, fecha, horas, minutos, segundos, workbook):
    sheet_name = "Registros"
    if sheet_name not in workbook.sheetnames:
        workbook.create_sheet(sheet_name)
        worksheet = workbook[sheet_name]
        worksheet.append(["Usuario", "Fecha", "Horas", "Minutos", "Segundos"])

    worksheet = workbook[sheet_name]
    worksheet.append([usuario, fecha, horas, minutos, segundos])

# Crear un archivo Excel
workbook = Workbook()

# Ruta completa donde deseas guardar el archivo Excel
excel_ruta = r"E:\HorasTrabajadas\registros_horario.xlsx"

# Ejemplo de uso
while True:
    print("Opciones:")
    print("1. Iniciar jornada")
    print("2. Pausar jornada")
    print("3. Reanudar jornada")
    print("4. Terminar jornada")
    print("5. Guardar en Excel")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        usuario = input("Introduce tu nombre: ")
        iniciar_jornada(usuario)
    elif opcion == '2':
        usuario = input("Introduce tu nombre: ")
        pausar_jornada(usuario)
    elif opcion == '3':
        usuario = input("Introduce tu nombre: ")
        reanudar_jornada(usuario)
    elif opcion == '4':
        usuario = input("Introduce tu nombre: ")
        terminar_jornada(usuario, workbook)
    elif opcion == '5':
        excel_filename = "registros_horario.xlsx"
        workbook.save(excel_filename)
        print(f"Registros guardados en el archivo '{excel_filename}'.")
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
