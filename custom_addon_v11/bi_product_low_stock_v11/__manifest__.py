 # -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name': 'Product Low Stock Notification',
	'version': '11.0.1.0',
	'category': 'Low Stock Notification',
	'sequence':140 ,
	'summary': 'To send notification to user while stock is low',
	'description': """To send notification to user while stock is low
	""",
	'author':'Browseinfo',
	'website': 'https://www.browseinfo.in',
	'depends': ['base','sale','product','stock','mail','contacts'],
	'data': [
	'view/product_product_view.xml',
	'view/email_templete.xml',
	'view/stock_config_settings_views.xml',

	
	
	
	'data/low_stock_notification_cron.xml',
			
	],
	
	'test': [],
		
	
	'demo': [],
	'css': [],
	'installable': True,
	'auto_install': False,
	'application': False,
}


