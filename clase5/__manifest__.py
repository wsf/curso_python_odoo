# -*- coding: utf-8 -*-
{
    'name': 'Curso Python-Odoo 2022_v2',
    'version': '2',
    'summary': 'Ejercicio 1 - Práctica 5 v2',
    'sequence': -100,
    'description': """Curso Python-Odoo 2022_v2""",
    'author': 'Alejandro Sartorio',
    'maintainer': 'Alejandro Sartorio_2',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': ['base', 'website'],
    'data': ['views/alumnos.xml',
             'views/cursos.xml',
             'views/qweb/analitica_alumnos.xml',
             'security/ir.model.access.csv'
            ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
