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
    categoria = fields.Char(string="Categoría", compute='_cal_categoria', store=True)
    cursos = fields.Many2one('curso.cursos',string="Cursos")
    persona = fields.Many2many('res.partner', string="Persona", tracking=True, help='Seleccione un tutor')

    @api.onchange('edad')
    def check_edad_menor_10(self):
        if self.edad < 10 and  self.edad > 0:

            return {'warning': {'title': _("Warning"), 'message': 'Menor de edad'}}

    @api.depends('edad')
    def _cal_categoria(self):
        edad = self[0]['edad']
        if edad > 17:
            self[0]['categoria'] =  "Mayor de Edad"
        else:
            self[0]['categoria']  = "Menor de Edad"


    @api.constrains('edad')
    def check_age(self):
        for rec in self:
            if rec.edad == 0 or rec.edad > 100:
                raise ValidationError("La edad inválida")


    def cant_mayores(self):
        cant = 0
        for e in self:
            if e.edad > 17:
                cant = cant + 1


        mensaje = f'La cantidad de mayores de edad es: {cant}'
        raise ValidationError(mensaje)
