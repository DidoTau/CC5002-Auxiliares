#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print("")
print("""
<!DOCTYPE html>
<html>
<head>
<title>Genera Saludo</title>
<script language="JavaScript">
function validaNombre(){
    var TCode = document.getElementById('nombre').value;
    if( /[^a-zA-Z0-9]/.test( TCode ) ) {
       alert('Nombre informado no es correcto');
       return false;
    }
    return true;     
 }
</script>
</head>
<body>
<h1>Saludos</h1>
<form action="saluda.py" method=GET onSubmit="validaNombre();">
<input id="nombre" name="nombre">
<input type="submit" value="saluda">
</form>
""")
form = cgi.FieldStorage()
if "nombre" in form:
	print("<hr><h3>Buenos días", form["nombre"].value, "</h3>")

print("""
</body></html>
""")
