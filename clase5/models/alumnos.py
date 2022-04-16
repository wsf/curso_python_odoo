# -*- coding: utf-8 -*-
# importamos el servicio fields para poder crear los campos para guardar los datos de los alumnos
# importamos el servicio models para poder administrar la base de datos donde se guardarán los campos creados
from odoo import api, fields, models, _

# importo un servicio que me permite mostar alertas al usuario cuando sea necesario
from odoo.exceptions import ValidationError
# declaro una clase llamada Alumnos que hereda todas las propiedades de la clase model.Model
class Alumnos(models.Model):
    _name = "curso.alumnos"
    _description = "Alumnos Python Odoo"
    _order = "id desc"

    name = fields.Char(string='Nombre')
    edad = fields.Integer(string='Edad')
    sexo = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], required=True, default='femenino', tracking=True)

    @api.constrains('edad')
    def check_age(self):
        for rec in self:
            if rec.edad == 0 or rec.edad > 100:
                raise ValidationError(_("La edad inválida"))
