from odoo import fields,models,api, _
from datetime import datetime, timedelta



class car(models.Model):
	_name = 'car.product'

	name = fields.Char(string='Enter car name')
	rent = fields.Integer(string='Rent price')
	num_plate = fields.Char(string='Number plate')
	type_id = fields.Selection([('car','car'),('bike','bike')],string='Vehicle type')
	stock = fields.Integer(string = 'In stock')


	@api.multi
	def action_update(self):
		res=self.env['car.rent'].search([('Model_car.name','=',self.name)])
		# print "carrrrrrrrrrrrrrrrrrrr===================reeeeeeeeeeeeessssssssssss",res
		# for i in res:
		# 	print "iiii===========================",i
		# 	d1 = datetime.today().
		# 	d2 = i.return_date
		# 	if d1>d2:



