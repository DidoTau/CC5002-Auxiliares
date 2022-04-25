# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi 
import cgitb;
import sys
cgitb.enable()

print("Content-type: text/html")
print()
sys.stdout.reconfigure(encoding='utf-8')

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format('Pide tu pizza', """
        <div class="solicitud align-items-center">
        <h1 class="text-center">Pide tu pizza</h1>
        <div class="formulario"> 
            <form action="save_order.py" method ="post" enctype="multipart/form-data">
                <div class="form-group mb-2">
                    <label for="nombre">Nombre </label>
                    <input type="text" placeholder="Ingresa tu nombre" id="nombre" class ="form-control" minlength="5" maxlength="20" name ="nombre" required> 
                </div>
                <div class="form-group mb-2">
                    <label for="direccion">Dirección </label>
                    <input type="text" class ="form-control" placeholder="Direccion de entrega" minlength="10" maxlength="40" name ="direccion" id="direccion" required> 
                </div>
                <div class="form-group mb-2">
                    <label for="comentarios">Comentarios opcionales </label>
                    <textarea name="comentarios" id="comentarios" class = "form-control" cols="30" rows="2" maxlength="100"></textarea>
                </div>
                <div class="form-group mb-2">
                    <label for="tipo">Elige pizza </label>
                    <select name="tipo" class= "form-control" id ="tipo"required>
                        <option value="Vegetariana">Vegetariana</option>
                        <option value="Margarita">Margarita</option>
                        <option value="Cuatro quesos">Cuatro quesos</option>
                        <option value="Hawaiana">Hawaiana</option>
                    </select>
                </div>
                <div class="form-group mb-2">
                    <label for="cupon">Ingresa cupón </label> 
                    <input type="file" name="cupon" id="cupon" class="form-control" required>
                </div>
                <input type="submit" value="Enviar" class="btn btn-primary mb-2">
            </form>

        </div>
    </div>
    """))
