from odoo import fields,models,api, _

class flour_lines(models.Model):

	_name='flour.lines'

	name = fields.Char(string='Name')
	account_analytic = fields.Many2one('account.analytic.account',string='Analytic account')
	code = fields.Char(string='Code')
	description=fields.Text(string='Description')
	flour_id=fields.Many2one('sale.order')
	

