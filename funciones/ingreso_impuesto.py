import sqlite3

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.DatabaseError as error:
            print(f'Error inesperado en la base de datos : {error}.')
            return
    
    def cierre_db(self):
        try:
            self.conn.close()
            print('Cierre de la base de datos exitoso.')
        except sqlite3.OperationalError as error:
            print(f'Error de opreacion en la base de datos : {error}.')

class IngresoImpuesto:
    def __init__(self,conexion):
        try:
            self.conexion = conexion
            if not self.conexion:
                print('No se encontro conexion con la base de datos.')
                return
        except sqlite3.OperationalError as error:
            print(f'Error operacional en la base de datos : {error}')
        
    def impuesto_anual(self):
        impuesto = float(input('Ingresa el impuesto ya calculado: '))
        año = str(input('Ingresa el año en el que se calculo el impuesto: ')).strip()
        if not impuesto or not año:
            print('Todos los datos deben estar completos.')
        try:
            self.conexion.cursor.execute('''INSERT INTO impuesto_año(impuesto,año) VALUES (?,?)''',(impuesto,año))
            self.conexion.conn.commit()
            print('Datos ingresados con exito.')
        except sqlite3.Error as error:
            print(f'Error inesperado en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inesperado en el programa : {error}.')
