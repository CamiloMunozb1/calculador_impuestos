import sqlite3 # Libreria de la base de datos sql para manejarla.
import pandas as pd # Libreria pandas para mostrar los datos.

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
            print(f'Error de opeacion en la base de datos : {error}.')
    
class MostrarDatos:
    def __init__(self,conexion):
        try:
            self.conexion = conexion # Conexion donde se pasa la base de datos.
            if not self.conexion: # Inspecciona si existe la conexion.
                print('No se encontro la conexion con la base de datos.')
                return
        except sqlite3.OperationalError as error:
            print(f'Error de operacion en la base de datos : {error}.')
    
    def impuestos_visibles(self):
        try:
            # Consulta para la base de datos la cual nos muestra estos campos
            query = '''
                    SELECT
                        impuesto,
                        año
                    FROM impuesto_año
                    '''
            resultado_df = pd.read_sql_query(query, self.conexion.conn) # Usamos dataframe para mostrar los datos.
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print('No se encontraron registros.')
        # Manejo de errores.
        except sqlite3.OperationalError as error:
            print(f'Error de operacion en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inespedado en el programa : {error}.')