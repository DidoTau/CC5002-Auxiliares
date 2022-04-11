import mysql.connector
import hashlib
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_order(self, data):
        # Procesar archivo

        fileobj = data[4]
        filename = fileobj.filename
        
        sql = "SELECT COUNT(id) FROM cupon"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1
        filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30]
        filename_hash += f"_{total}"
        # guardar archivo
        try:
            open(f"media/img/{filename_hash}", "wb").write(fileobj.file.read())
            sql_file = '''
                INSERT INTO cupon (nombre, path) 
                VALUES (%s, %s)
                '''
            self.cursor.execute(sql_file, (filename, filename_hash))  
           

            # guardar pedido
            id_cupon = self.cursor.getlastrowid()
            sql ='''
                INSERT INTO pedidos (nombre, direccion, comentarios, tipo, cupon) 
                VALUES (%s, %s, %s, %s, %s)
                '''
            self.cursor.execute(sql, data[:4]+ (id_cupon,))  # ejecuto la consulta
            self.db.commit()                # modifico la base de datos
        except:
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def get_data(self):
        # Procesar archivo
        sql = '''
            SELECT p.nombre, p.direccion, p.tipo, c.nombre FROM pedidos p
            LEFT JOIN cupon c
            ON p.cupon = c.id
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()