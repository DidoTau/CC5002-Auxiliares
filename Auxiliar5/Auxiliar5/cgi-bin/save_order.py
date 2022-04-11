# -*- coding: utf-8 -*-
import cgi
import os
import sys
import filetype
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'pizza')
form = cgi.FieldStorage()

fileobj = form['cupon']
MAX_FILE_SIZE= 100000 

if fileobj.filename:
    tipo = fileobj.type
    size = os.fstat(fileobj.file.fileno()).st_size
    if tipo != 'application/pdf':
        print('Error, formato no válido.{}'.format(tipo))
        sys.exit()
    if size > MAX_FILE_SIZE:
        print('Error, archivo muy grande.')
        sys.exit()
else:
    print("Error, archivo no subido.")


data = (form['nombre'].value, form['direccion'].value, form['comentarios'].value, form['tipo'].value, fileobj)

db.save_order(data)

with open('templates/template.html','r') as template:
        file = template.read()
        print(file.format('Pedido Ingresado', 
        """
        <div class="row justify-content-center  vw-100">
        <div class="alert alert-success col-6" role="alert">
            <h4 class="alert-heading">Pedido ingresado con éxito!</h4>
            <p>Tu pizza llegará en 30 minutos! Si no lo logramos, tu pedido será gratis!</p>
            <hr>
        </div>
        </div>

        """))