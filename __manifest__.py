# -*- coding: utf-8 -*-
{
    'name': "Odoo BAT Datamart Reports",

    'summary': """
        Odoo BAT Datamart Reports""",

    'description': """
        Odoo BAT Datamart Reports
    """,

    'author': "Codize",
    'website': "http://www.codize.ar",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'report/maestrocliente.xml',
	'report/stockperiodo.xml',
	'report/ventasxcliente.xml'
    ],
    'demo': [],
}
