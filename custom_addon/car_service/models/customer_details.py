from odoo import fields,models,api, _
from datetime import datetime, timedelta



class Customer(models.Model):

	_name = "customer.details"
	_description = "details of customer"



	@api.depends('Days')
	def _cal_date(self):
		for my in self:
			if not my.date1:
				return

			print "==========date==========",my.date1
			d1=datetime.strptime(my.date1,'%Y-%m-%d').date()
			print"==================d1====================="
			my.return_date = d1+timedelta(days=my.Days)




	# @api.model
	# def create(self,vals):
	# 	cus_obj=self.env['customer.details']
	# 	email_id=vals.get("phone",self.env.customer.details)
		
		
		
		








	name = fields.Char(string="Customer name",required=True)
	name_seq = fields.Char(string="Customer No", readonly=True, copy=False)
	phone = fields.Char(string="Phone number",size=10,required=True)
	#car=fields.Selection((('h','Honda'), ('b','BMW'),('t','Tesla')),
				   #string='select car',required=True)
	city = fields.Selection([('a','Ahmedabad'), ('g','Goa'),('d','Delhi')],
				   string='Select city',required=True)
	#service_type=fields.Many2one('mech.details',string="service")
	urgent = fields.Selection((('y','Yes'),('n','No')),string="Urgent")
	
	Days = fields.Integer(string = "Days takes")
	vehical = fields.Text(string = "Vehicle problem")
	#customer_line=fields.One2many('service.details','customer_id',string="lines of customer")
	date1 = fields.Date(string = "Date ",default = datetime.today().date())
	
	#service=fields.Many2one('mech.details',string="service")
	return_date = fields.Date(string = "Expected return date",store = True, compute = '_cal_date')
	state = fields.Selection([('urgent','urgent'),
							('not','not confirm'),
							('done', 'Locked'),
							],
							default = 'urgent')
	photo = fields.Binary(string = 'Photo')
	

	# @api.model
	# def default_get(self, default_fields):
	# 	print "============default=============",default_fields
	# 	res = super(Customer, self).default_get(default_fields)
	# 	print "============default after===========",default_fields
	# 	print "================res===========================",res
	# 	if res.get('date1'):
	# 		res['Days']=5
	# 	return res


	@api.one
	def action_urgent(self):
		print "==========action_cancel====customer=============="
		#self.urgent='y'
		self.write({'urgent':'y','Days':'1','state':'not'})

		return

	@api.one
	def action_confirm(self):
		self.write({'state':'done'
					})


	@api.model
	def create(self, vals):
		seq = self.env['ir.sequence'].next_by_code('customer.details') or '/'
		vals['name_seq'] = seq
		return super(Customer, self).create(vals)

