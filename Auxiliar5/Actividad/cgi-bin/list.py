# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('Content-type: text/html\r\n\r\n')

import cgi
from db import DB

db = DB('localhost', 'root', '', 'pizza')
data = db.get_data()
tabla = """
            <div class="container ">
            <table class="table">
        <thead>
        <tr>
        <th scope="col">Nombre</th>
        <th scope="col">Dirección</th>
        <th scope="col">Tipo</th>
        <th scope="col">Archivo</th>
        </tr>
        </thead>
        <tbody>
        """
for p in data:
    tabla+=f""" 
          <tr>
        <td>{p[0]}</td>
        <td>{p[1]}</td>
        <td>{p[2]}</td>
        <td>{p[3]}</td>
        </tr>
        """

tabla+="""
    </tbody>
    </table>
    </div> """

with open('templates/template.html','r') as template:
    file = template.read()
    print(file.format('Pedidos', tabla))