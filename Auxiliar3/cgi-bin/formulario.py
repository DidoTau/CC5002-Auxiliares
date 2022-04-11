# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi 
import cgitb 
import sys

cgitb.enable()
print("Content-type:text/html")
print()
form = cgi.FieldStorage()

print("<html><body>Buena hermanito, los datos que ingresaste son: <br>")
for key in form.keys():
    print("""
        <p> %s %s </p>
            """%(key, form[key].value))

print("</body></html>")