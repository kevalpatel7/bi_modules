from odoo import fields,models,api, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError



class rent(models.Model):

	_name='car.rent'


	@api.multi
	@api.onchange('rent_price','payment')
	def _cal_bill(self):
		total=0
		for rent in self:
			if not rent:
				return
			if rent.Model_car:
				total=rent.rent_price*rent.Days-rent.payment
				rent.remaining=total
			
	@api.multi
	@api.onchange('Date','Days')
	def _call_date_(self):
		for my in self:
			if not my.Date:
				return
			d1=datetime.strptime(my.Date,'%Y-%m-%d').date()
			my.return_date=d1+timedelta(days=my.Days)



	@api.one
	@api.constrains('Days','remaining','payment')
	def _check_advance(self):
		if self.remaining>self.payment:
			raise UserError(_('Please pay more than half amount of bill in Advance'))


	@api.multi
	@api.constrains('Model_car')
	def _stock_vehicle(self):
		if self.Model_car.stock<=0:
			raise UserError(_('This Vehicle is out of stock'))


	@api.onchange('name','Model_car')
	def onchange_rent(self):
		d={}
		
		
		if self.name=='car':
			print"====================",self.Model_car.type_id
			res=self.env['car.product'].search([('type_id','=','car')])
			print "res================================",res
			d['domain']={"Model_car":[("name",'=',[i.name for i in res])]}
		if  self.name=='bike':
			res=self.env['car.product'].search([('type_id','=','bike')])
			d['domain']={"Model_car":[("name",'=',[i.name for i in res])]}
		print d
		
		self.rent_price=self.Model_car.rent
		self.number=self.Model_car.num_plate
		return d



	name=fields.Selection([('car','car'),('bike','bike')], default='car',string='Select type',required=True)
	Model_car=fields.Many2one('car.product',string='Select your Vehicle')
	# Model_bike=fields.Many2one('bike.product',string='Select bike')
	customer=fields.Many2one('customer.details',String='customer',required=True)
	rent_price=fields.Integer(string='Rent/Day',required=True)
	Date=fields.Date(string='Pickup date')
	Days=fields.Integer(string='Days for rent ')
	number=fields.Char(string='Number plate')
	payment=fields.Integer(string='Advance payment',required=True)
	remaining=fields.Integer( compute='_cal_bill',string='remaining bill')
	return_date=fields.Date(string='Dropoff date',compute='_call_date_')
	licence=fields.Binary(string='Upload your licence')
	city=fields.Selection([('a','Ahmedabad'), ('g','Goa'),('d','Delhi')],related='customer.city',string='Pickup city')
	cityd=fields.Selection([('Ahmedabad','Ahmedabad'),('Goa','Goa'),('Delhi','Delhi')],string='Dropoff city',required=True)
	phone=fields.Char(related='customer.phone',string='Phone number')
	state =fields.Selection([
							('not','Not confirm'),
							('done', 'Locked'),
							],
							default='not')
	rent_seq = fields.Char(string="Car rent No", readonly=True, copy=False)







	@api.model
	def create(self, vals):
		seq = self.env['ir.sequence'].next_by_code('car.rent') or '/'
		vals['rent_seq'] = seq
		return super(rent, self).create(vals)

	# @api.model
	# def create(self,vals):
	# 	a=vals.get('remaining')
	# 	b=vals.get('payment')
	# 	d=vals.get('Days')
	# 	print"====================a,b,d=====",a,b,d
	# 	tot=(b*d)/2

	# 	if a>tot:

	# 		raise UserError(_('Please pay more than half amount of bill in Advance'))
		
	# 	result = super(rent, self).create(vals)

	# 	return result

	# @api.multi
	# def write(self,vals):
	# 	print "+++++++++++++++++++++++++++++++++++++++",vals

	# 	a=self.remaining
	# 	print"---------------------------------------",a
	# 	b=vals.get('payment')
	# 	d=self.Days
	# 	tot=(b*d)/2

	# 	if b:
	# 		if a>tot:

	# 			raise UserError(_('Please pay more than half amount of bill in Advance'))


	# 	result=super(rent,self).write(vals)
	@api.multi
	def confirm_rent(self):
		self.ensure_one()
		self.write({'state':'done'
					})
		res=self.env['car.product'].search([('name','=',self.Model_car.name)])
		print "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",res
		res.write({'stock':self.Model_car.stock-1})
		reg=self.env['car.receive']
		print"reeeeeeeeeeeeeeeeeeggggggggggggggggggg",reg
		reg.create({'token':self.rent_seq,'customer':self.customer.name,
			'vehicle':self.Model_car.name,'return_date':self.return_date,'bill':self.remaining})
		
		

		# for i in res:
		# 	print "iiiiiiii",i.name
		# 	if i.name==self.Model_car.name:
		# 		print"ifffffffffffffffffff",i.name
		# 		i.write({'stock':self.Model_car.stock-1})




	@api.multi
	def new_car(self):
		res=self.env['car.product']
		print "===========krval==================",res
		res.create({'name':'TATA',
			'rent':3000,
			'num_plate':'GJ-1-FF-1245',
			'type_id':'car'})
		
		print "reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",res
		return res



	@api.multi
	@api.depends('rent_seq')
	def name_get(self):
		result=[]
		print "=======================self mech name===============",self
		for a in self:
		
			name =a.rent_seq 
			print"pppppppppppppppppppppppppppppppppp"
			result.append((a.id,name))
			print"lllllllllllllllllllllllllllllllll",result

		return result

	@api.model
	def name_search(self, name='', args=None, operator='ilike', limit=100):
		args = args or []
		domain = []
		print ("============name==111================",name)
		if name:
			print ("============name===================",name)
			domain = ['|', ('rent_seq', operator, name + '%'),('phone','=ilike',name + '%')]
			print ("============domain===================",domain)
		#if operator in expression.NEGATIVE_TERM_OPERATORS:
				#self.domain = ['&', '!'] + domain[1:]
		

		res =  super(rent,self).search(domain + args, limit=limit ).name_get()

		print "===========aaaaaaaaaaaaaaaaaaaaa==============="
		return res











