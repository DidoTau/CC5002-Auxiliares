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
</head>
<body>
<h1>Saludos</h1>
<form action="saluda.py" method=GET>
<input name="nombre">
<input type="submit" value="saluda">
</form>
""")
form = cgi.FieldStorage()
if "nombre" in form:
	print("<hr><h3>Buenos días", form["nombre"].value, "</h3>")

print("""
</body></html>
""")
