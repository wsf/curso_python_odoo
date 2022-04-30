from odoo import http
from odoo.http import request

class analitico_alumno(http.Controller):

    @http.route('/primer_api/', auth='user', website=True, csrf=False, method=['POST'])
    def primer_api(self):
        men = ""
        for i in [1,2,3,4,5]:
            men += "</br> <p> " + str(i*2) + '</p> <button type="alerta" onclick=\'alert("%s")\'>Clic para ver cartel de alerta</button> ' % (str(i))

        return men

    @http.route('/analitico_alumnos/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos(self, **datos):
        alumnos = request.env['curso.alumnos'].search([])
        men = ""
        for a in alumnos:
            men += a['name'] + " </br> "
        return str(men)

    @http.route('/analitico_alumnos2/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos2(self, **datos):
        alumnos = request.env['curso.alumnos'].browse(1)
        men = ""
        for a in alumnos:
            men += a['name'] + " </br> "
        return str(men)

    @http.route('/analitico_alumnos3/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos3(self, **datos):
        alumnos = request.env['curso.alumnos'].search([])

        return request.render('clase5.analitica_alumnos',{'alumnos':alumnos})

    @http.route('/uli/', auth='user', website=True, csrf=False, method=['POST'])
    def uli(self, **datos):
        q = "select * from curso_alumnos"
        request.cr.execute(q)
        alumnos = request.cr.fetchall()

        men = ""
        for a in alumnos:

            men += "<h1> "+ (a[1]) + "</h1>" + "</br>"

        return men


