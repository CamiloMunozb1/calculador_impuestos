# Funciones importadas para las funcionalidades.
from funciones.calculadora_impuestos import operacion_impuestos
from funciones.ingreso_impuesto import IngresoDB, IngresoImpuesto
from funciones.mostrar_impuestos import IngresoDB, MostrarDatos
from dotenv import load_dotenv
import os

# Importacion de las variables de entorno.
load_dotenv()
ruta_db = os.getenv('RUTA_DB') # Ruta de la base de datos.
conexion = IngresoDB(ruta_db) # Conexion a la base de datos.

while True:
    print('''
            1. Calcular impuesto (Por año).
            2. Añadir impuesto y año.
            3. Mostrar todos los impuestos registrados.
            4. Salir.
        ''')
    try:
        # Entrada de usuarios.
        usuario = str(input('Ingresa la opcion que deseas: ')).strip()
        if not usuario: # Validacion de campo.
            print('Selecciona una opcion por favor.')
            break
        # Opciones del menu de usuario.
        elif usuario == '1':
            operacion_impuestos()
        elif usuario == '2':
            guardado = IngresoImpuesto(conexion)
            guardado.impuesto_anual()
        elif usuario == '3':
            mostrar = MostrarDatos(conexion)
            mostrar.impuestos_visibles()
        elif usuario == '4': # Salida del programa.
            print('Gracias por visitar y registar sus impuestos.')
            break
        else:
            print('Por favor ingresa una opcion valida del 1-4.') # Si no se registra una entrada valida, salta este error.
        input('\nPresiona enter para continuar...')
    # Manejo de errores.
    except ValueError:
        print('Error de digitacion por favor vuelve a ingresar un valor valido.')
    except Exception as error:
        print(f'Error inesperado en el programa : {error}.')
