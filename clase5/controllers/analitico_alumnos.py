from odoo import http
from odoo.http import request
import json


class analitico_alumno(http.Controller):

    @http.route('/prueba_ale/', auth='user', method=['GET'])
    def prueba_ale(self, **datos):
        alumnos = request.env['curso.alumnos'].search([])
        r_json = alumnos.read(['name'])
        r_str_json = json.dumps(r_json)
        r_json = json.loads(r_str_json)
        return r_str_json

    @http.route('/form_alumnos_ida/', auth='user', website=True, csrf=False, method=['POST'])
    def form_alumnos_ida(self):

        return request.render('clase5.form_alumnos_ida')


    @http.route('/form_alumnos_vuelta/', auth='user', website=True, csrf=False, method=['POST'])
    def form_alumnos(self, **datos):

        try:

            nombre = datos['nombre']
            apellido = datos['apellido']

            if 'masculino' in datos.keys():
                m = datos['masculino']

            f = datos['femenino']

            html = f'<li> Te muestro el nombre ingresado en el formulario: -> {nombre} </br>'
            html += '<a href="http://localhost:8069/abm-alumnos"> Ir al menú </a> '
            return html


        except Exception as e:
            mensaje_error = f"Ocurrió el siguiente error {str(e)}"
            return mensaje_error

    @http.route('/primer_api/', auth='user', website=True, csrf=False, method=['GET'])
    def primer_api(self):
        men =  ""
        for i in [1,2,3,4,5]:
            men += "</br> <p> " + str(i*2) + '</p> <button type="alerta" onclick=\'alert("%s")\'>Clic para ver cartel de alerta</button> ' % (str(i))
        return men

    @http.route('/analitico_alumnos_seach/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_seach(self, **datos):


        #domain = ['|',('edad','<','18'), ('name','ilike','ale')]

        condi = ('edad', '=', '45')
        domain = [condi]
        alumnos1 = request.env['curso.alumnos'].search(domain)

        domain = ['|', ('edad', '<', '18'), ('name', 'ilike', 'ale')]
        alumnos2 = request.env['curso.alumnos'].search(domain)

        #alumnos = alumnos1 | alumnos2

        #alumnos = alumnos1 & alumnos2

        #alumnos = alumnos1 + alumnos2

        alumnos = alumnos2 - alumnos1

        alumnos = alumnos.filtered(lambda r: r.edad == 12)

        alumnos = alumnos.mapped(lambda r: {'name':r.name, 'edad': r.edad * 100, 'curso':r.cursos.name})

        #alumnos.mapped('cursos.name')

        men = ""

        for a in alumnos:
            # m = f'<li> {a["name"]} - {str(a["edad"])}  </li> '
            m = f'<li> {a["name"]} - {str(a["edad"])} - {a["curso"]}  </li> '
            men += m
        return str(men)

    @http.route('/analitico_alumnos_browse/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_browse(self, **datos):

        alumnos = request.env['curso.alumnos'].browse([1,2,4])
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

    @http.route('/analitico_alumnos_sql2/', auth='user', website=True, csrf=False, method=['POST'])
    def analitico_alumnos_sql2(self, **datos):
        q = "select * from curso_alumnos"

        q = """
                 select 
         a.name,a.sexo,a.edad,
         c."name" 
         from
         public.curso_alumnos a
         inner join 
         public.curso_cursos c
         on a.cursos = c.id
         
         where (1=1)
        """

        q = q.replace("(1=1)","a.edad < 18 and (1=1)")
        q = q.replace("(1=1)","a.name like '%ale%' and (1=1)")

        request.cr.execute(q)
        alumnos = request.cr.fetchall()

        men = ""
        for a in alumnos:
            men += f"<li> {a[0]} - {a[1]} - {a[2]} </li>"
        return men
