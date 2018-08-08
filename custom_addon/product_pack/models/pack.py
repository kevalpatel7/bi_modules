# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields,models,api, _

class pack(models.Model):


	_name="pack.details"




	name=fields.Many2one('product.product' )
	price=fields.Float(string='Price')
	Product_id=fields.Many2one('product.template')
	qua=fields.Float(string="Qty" ,default=1.0)
	#dis=fields.Text(string="Discription")
	