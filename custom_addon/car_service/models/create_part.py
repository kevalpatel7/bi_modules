from odoo import fields,models,api, _





class create_parts(models.Model):

	_name='create.parts'



	name=fields.Char(string='parts name',required=True)
	price=fields.Integer(string='Price')
