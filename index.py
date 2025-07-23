from funciones.calculadora_impuestos import operacion_impuestos
from funciones.ingreso_impuesto import IngresoDB, IngresoImpuesto
from dotenv import load_dotenv
import os

load_dotenv()
ruta_db = os.getenv('RUTA_DB')
conexion = IngresoDB(ruta_db)

while True:
    print('''
            1. Calcular impuesto (Por año).
            2. Añadir impuesto y año.
            3. Mostrar todos los impuestos registrados.
            4. Salir.
        ''')
    try:
        usuario = str(input('Ingresa la opcion que deseas: ')).strip()
        if not usuario:
            print('Selecciona una opcion por favor.')
            break
        elif usuario == '1':
            operacion_impuestos()
        elif usuario == '2':
            guardado = IngresoImpuesto(conexion)
            guardado.impuesto_anual()
        elif usuario == '3':
            print('Opcion futura')
        elif usuario == '4':
            print('Gracias por visitar y registar sus impuestos.')
            break
        else:
            print('Por favor ingresa una opcion valida del 1-4.')
        input('\nPresiona enter para continuar...')
    except ValueError:
        print('Error de digitacion por favor vuelve a ingresar un valor valido.')
    except Exception as error:
        print(f'Error inesperado en el programa : {error}.')
