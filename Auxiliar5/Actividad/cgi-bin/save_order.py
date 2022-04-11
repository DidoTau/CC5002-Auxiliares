# -*- coding: utf-8 -*-
import cgi
from db import DB
import os
import filetype

print('Content-type: text/html \r\n\r\n')

db = DB('localhost', 'root', '', 'pizza')
form = cgi.FieldStorage()

fileobj = form['cupon']
MAX_FILE_SIZE= 100000 

if fileobj.filename:
    tipo = filetype.guess(fileobj.file).mime
    size = os.fstat(fileobj.file.fileno()).st_size
    if tipo != 'application/pdf':
        print('Error, formato no válido.')
    elif size > MAX_FILE_SIZE:
        print('Error, archivo muy grande.')
else:
    print("Error, archivo no subido.")


data = (form['nombre'].value, form['direccion'].value, form['comentarios'].value, form['tipo'].value, fileobj)

db.save_order(data)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="../css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pedido</title>

</head>

<body>
Pedido ingresado con éxito!
</body>
</html>
""")