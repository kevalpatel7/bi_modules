  # -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product pack',
    'version': '1.0',
    'category': 'product',
    'sequence': 120,
    'summary': 'Sample Module for pack products',
    'description': """product pack Module
    """,
    'website': 'https://www.browseinfo.in',
    'depends': ['base', 'sale','product','account_analytic_default','account','stock'],
    'data': [
            'wizard/bundle.xml',
            'views/product_pack.xml',
            'views/pack.xml',
           'views/sale_in.xml',
           'views/flour_lines.xml',
           'views/quotations_inherit.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

