from odoo import fields,models,api, _
from datetime import datetime, timedelta,date


class car_receive(models.Model):
	_name = 'car.receive'

	token=fields.Char(string='Token no')
	customer=fields.Char(String='customer')
	vehicle=fields.Char(string='Vehicle')
	return_date=fields.Date(string='Return date')
	bill=fields.Integer(string="Remaining bill")
	damage=fields.Boolean(string='Is Vehicle damaged')
	fine=fields.Integer(string='Fine due for late delivery')
	today=fields.Date(string='Today',default=datetime.today(),readonly=True)
	parts_damage=fields.One2many('parts.add','rent_id',String="Add parts that are damaged")
	fine_damage=fields.Integer(string='Fine for damage',readonly=True)
	state = fields.Selection([
							('not','not confirm'),
							('done', 'Locked'),
							],
							default = 'not')

	# @api.onchange('token')
	# def _token_data(self):
	# 	self.return_date=self.token.return_date
	# 	self.bill=self.token.remaining
	# 	self.vehicle=self.token.Model_car
	# 	self.customer=self.token.customer
		
	@api.model
	@api.onchange('return_date','today','fine')
	def date_fine(self):
		print"======!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		if not self.return_date:
			return
		elif self.today>self.return_date:
			print "================today>return_date==============="
			#k=self.return_date-self.today
			d1=datetime.strptime(self.today,'%Y-%m-%d').date()
			d2=datetime.strptime(self.return_date,'%Y-%m-%d').date()
			print "===============type=================",d1
			k=d1-d2

			print"++++++++++++++++++++++++++++++++++++++",k.days
			self.fine=self.vehicle.rent*k.days
			self.bill=self.bill+self.vehicle.rent*k.days
		self.bill=self.bill+self.fine
	@api.onchange('parts_damage')
	def _fine_damage(self):
		total=0
		for i in self.parts_damage:
			total=total+i.price

		self.fine_damage=total
		self.bill=self.bill+self.fine_damage
	@api.multi
	def receive_car(self):
		self.write({'state':'done'
					})
		res=self.env['car.product'].search([('name','=',self.vehicle)])
		res.write({'stock':res.stock+1})
		

		
		

