# -*- coding: utf-8 -*-
# importamos el servicio fields para poder crear los campos para guardar los datos de los alumnos
# importamos el servicio models para poder administrar la base de datos donde se guardarán los campos creados
from odoo import api, fields, models, _
# importo un servicio que me permite mostar alertas al usuario cuando sea necesario

class Cursos(models.Model):
    _name = "curso.cursos"
    _description = "Cursos"

    name = fields.Char(string='Nombre del curso')
    profesor = fields.Char(string='Profesor')
    horario = fields.Char(string='Horarios')

