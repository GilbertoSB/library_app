# -*- coding: utf-8 -*-
{
    'name': "Library Managment",

    'summary': """
        Manage library book catalogue and lending.""",

    'description': """
        Manage library book catalogue and lending.
    """,

    'author': "M.T.S.",
    'website': "http://www.multitargetsolution.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/library_menu.xml',
        'views/book_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application':True,
}