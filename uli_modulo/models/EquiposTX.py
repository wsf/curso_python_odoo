from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EquiposTx(models.Model):
    _name = "xmv.equipostx"
    _description = "Equipos de Trasplante"
    _order = "name desc"

    name = fields.Char(string='Nombre Equipo Tx')
    contacto = fields.Char(string='Contacto')
    id_equipo = fields.Char(string='Id. Equipo', index=True)


    @api.constrains('id_equipo')
    def check_id_equipo(self):
        for rec in self:
            equipo = self.env['xmv.equipostx'].search([('id_equipo', '=', rec.id_equipo), ('id', '!=', rec.id)])
            if equipo:
                raise ValidationError("Name %s Already Exists" % (rec.id_equipo))
