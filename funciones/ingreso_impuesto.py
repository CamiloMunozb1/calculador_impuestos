import sqlite3 # Libreria de la base de datos sql para manejarla.

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db) # Conexion con la base de datos.
            self.cursor = self.conn.cursor() # Creacion del cursor para manejar la base de datos.
        except sqlite3.DatabaseError as error: 
            print(f'Error inesperado en la base de datos : {error}.')
            return
    
    def cierre_db(self):
        try:
            self.conn.close() # Cierre de la base de datos.
            print('Cierre de la base de datos exitoso.')
        except sqlite3.OperationalError as error:
            print(f'Error de opreacion en la base de datos : {error}.')

class IngresoImpuesto:
    def __init__(self,conexion):
        try:
            self.conexion = conexion # Conexion donde se pasa la base de datos.
            if not self.conexion: # Inspecciona si existe la conexion.
                print('No se encontro conexion con la base de datos.')
                return
        except sqlite3.OperationalError as error:
            print(f'Error operacional en la base de datos : {error}')
        
    def impuesto_anual(self):
        # Entradas de usuario.
        impuesto = float(input('Ingresa el impuesto ya calculado: '))
        año = str(input('Ingresa el año en el que se calculo el impuesto: ')).strip()
        if not impuesto or not año: # Validacion de ingreso de usuarios.
            print('Todos los datos deben estar completos.')
        try:
            # Entrada de datos en la base de datos.
            self.conexion.cursor.execute('''INSERT INTO impuesto_año(impuesto,año) VALUES (?,?)''',(impuesto,año))
            self.conexion.conn.commit()
            print('Datos ingresados con exito.')
        # Manejo de errores.
        except sqlite3.Error as error:
            print(f'Error inesperado en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inesperado en el programa : {error}.')
