import sqlite3
import pandas as pd

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
            print(f'Error de opeacion en la base de datos : {error}.')
    
class MostrarDatos:
    def __init__(self,conexion):
        try:
            self.conexion = conexion
            if not self.conexion:
                print('No se encontro la conexion con la base de datos.')
                return
        except sqlite3.OperationalError as error:
            print(f'Error de operacion en la base de datos : {error}.')
    
    def impuestos_visibles(self):
        try:
            query = '''
                    SELECT
                        impuesto,
                        año
                    FROM impuesto_año
                    '''
            resultado_df = pd.read_sql_query(query, self.conexion.conn)
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print('No se encontraron registros.')
        except sqlite3.OperationalError as error:
            print(f'Error de operacion en la base de datos : {error}.')
        except Exception as error:
            print(f'Error inespedado en el programa : {error}.')