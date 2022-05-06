from odoo import http
from odoo.http import request

class analitico_alumno(http.Controller):

    @http.route('/primer_api/', auth='user', website=True, csrf=False, method=['POST'])
    def primer_api(self):
        men =  ""
        for i in [1,2,3,4,5]:
            men += "</br> <p> " + str(i*2) + '</p> <button type="alerta" onclick=\'alert("%s")\'>Clic para ver cartel de alerta</button> ' % (str(i))
        return men

    @http.route('/analitico_alumnos_seach/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_seach(self, **datos):

        domain = []
        domain = ['&', ('edad','<','18'), ('name','ilike','ale')]
        alumnos1 = request.env['curso.alumnos'].search(domain)

        domain = ['|', ('edad', '<', '18'), ('name', 'ilike', 'ale')]
        alumnos2 = request.env['curso.alumnos'].search(domain)

        #alumnos = alumnos1 | alumnos2

        #alumnos = alumnos1 & alumnos2

        alumnos = alumnos1 + alumnos2

        #alumnos.filtered(lambda r: r.edad == 12)

        alumnos = alumnos.mapped(lambda r: {'name':r.name, 'edad': r.edad * 100, 'curso':r.cursos.name})

        #alumnos.mapped('cursos.name')

        men = ""

        for a in alumnos:
            # m = f'<li> {a["name"]} - {str(a["edad"])}  </li> '
            m = f'<li> {a["name"]} - {str(a["edad"])}  - {a["curso"]} </li> '
            men += m
        return str(men)

    @http.route('/analitico_alumnos_browse/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_browse(self, **datos):
        alumnos = request.env['curso.alumnos'].browse(1)
        men = ""
        for a in alumnos:
            men += a['name'] + " </br> "
        return str(men)

    @http.route('/analitico_alumnos_qweb/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_qweb(self, **datos):
        alumnos = request.env['curso.alumnos'].search([])
        return request.render('clase5.analitica_alumnos',{'alumnos':alumnos})

    @http.route('/analitico_alumnos_sql/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_sql(self, **datos):
        q = "select * from curso_alumnos"
        request.cr.execute(q)
        alumnos = request.cr.fetchall()

        men = ""
        for a in alumnos:

            men += "<h1> "+ (a[1]) + "</h1>" + "</br>"

        return men


