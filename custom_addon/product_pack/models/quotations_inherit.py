from odoo import fields,models,api, _

class quotations_construction(models.Model):


	_inherit = "sale.order"

	@api.multi
	@api.onchange('flour_lines')
	def _flour_line_sale(self):
		d={}
		if self.flour_lines:
			print"===================inside========================================="
		
					
			d['domain']={"flour_lines":[("name",'=',[i.name for i in self.flour_lines])]}
			print d
		return d



	flour_lines = fields.One2many('flour.lines','flour_id', string = 'Flour lines')

class saleorderline(models.Model):
	_inherit = "sale.order.line"


	# date= fields.Date(String='date')
	flour_lines=fields.Many2one('flour.lines',string='Floor')
	account_analytic = fields.Many2one('account.analytic.account',string='Analytic Account')
	code=fields.Char(string='Code')

