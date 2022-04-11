# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi 
import cgitb 

cgitb.enable()
print("Content-type:text/html")
print()



header = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title>Formulario</title>
    </head>
"""
body = """
    <body>
        <div class="jumbotron d-flex align-items-center min-vh-100">
            <div class="container p-3 my-3 border bg-light">
            Los datos ingresados son:
            <br>
        """

form = cgi.FieldStorage()

for key in form.keys():
    body+="""
        <p> %s: %s </p>
            """%(key, form[key].value)


body+= " </div></div></body></html>"

print(header+body)