# -*- coding: utf-8 -*-
{
    'name': "cb_bengkel",

    'summary': """
        Aplikasi Bengkel Ku""",

    'description': """
        Aplikasi Ini menggunakan Odoo 10.0
    """,

    'author': "aditditkudit",
    'website': "http://github.com/aditditkudit",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'New Module',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu_bengkel.xml',
        'views/res_partner.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,

}