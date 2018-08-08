from odoo import fields,models,api, _
from odoo.exceptions import UserError


class mech(models.Model):
	
	_name="mech.details"
	_description="details of Mechanic" 

	@api.multi
	@api.depends('parts','mech_ids','garage_ids')
	def _cal_bill(self):
		total = 0
		service = 0
		fees=0
		for part in self:
			for res in part.parts:
				if not res:
					return
				total += res.price
		
			for res in part.mech_ids:
				service += res.rate
		
			fees = total + service

			for res in part.garage_ids:

				tax=(fees*res.value)/100
				fees=fees+tax


		self.bill=fees


		print '===========cal=========',part
		print '==========total=======',total

	@api.one
	@api.constrains('mech_ids','damage')
	def check_service(self):
		if not self.mech_ids.name:
			raise	UserError(_('Have to select atleast 1 Service'))





		
	#code=fields.Char()
	
	name=fields.Many2one('workers.details',string="Mechanic")
	mech_ids=fields.Many2many('service.details','mech_service_rel','mech_id','service_id',string="Service")
	customer=fields.Many2one('customer.details',String='Customer')
	vehical=fields.Selection((('c','4 wheeler'),('b','2 wheeler')))
	date=fields.Date(string="Order date")
	damage=fields.Selection([('yes','yes'),('no','no')],string=" Is Damage",default='no')
	parts = fields.One2many('parts.add','garage_id',String="Add parts to replase")
	engine=fields.Selection([('petrol','petrol'),('diesel','diesel')],string='Engine type')
	garage_ids=fields.Many2many('tax.details','tax_garage_rel','garage_id','tax_id',string='Tax',copy=False)
	bill=fields.Integer(String="Bill",readonly='1',compute='_cal_bill')
	state=fields.Selection([('cancel','cancel'),('done','confirm')],default='cancel')
	describe=fields.Text(string='Describe damage')
	payment=fields.Selection([('cash','cash'),('card','card')],string='Payment')
	#sevice_id=fields.Many2one('service.details',string='sevice_id')
	#tax_ids=fields.Many2many('service.details','service_mech_rel','tax_id','service_id',string='tax')
	#name=fields.Char(string=' Mechanic',required=True)
	#phone=fields.Char(string="Phone number",required=True,size=10)
	#city=fields.Selection((('a','Ahmedabad'), ('g','Goa'),('d','Delhi')),
				   #string='select city',required=True)
	
	#service_id=fields.One2many('customer.details','service_type',string="service_id")
	#experiance=fields.Integer(string="Experiance",required=True)
	modify=fields.One2many('parts.add','garage_id',String="Which part to modify")
	vehicals=fields.Many2one('car.product',string='select your vehicle')




	@api.onchange('vehical','vehicals')
	def onchange_rent(self):
		d={}
		
		
		if self.vehical=='c':
			print"====================",self.vehicals.type_id
			res=self.env['car.product'].search([('type_id','=','car')])
			print "res================================",res
			d['domain']={"vehicals":[("name",'=',[i.name for i in res])]}
		if  self.vehical=='b':
			res=self.env['car.product'].search([('type_id','=','bike')])
			d['domain']={"vehicals":[("name",'=',[i.name for i in res])]}
		print d
		
		
		return d




	@api.model
	def create(self,vals):
		print "==================================================",vals

		#if vals.get('name', _('New')) == _('New'):
		'''	if vehical in vals:

				if vehical==b:
					vals.update({'vehical':'b'})
				else :
					vals.update({'vehical':'c'})'''
		print"-----------m--------------",vals.get('damage')
		if vals.get('mech_ids')=='Washing' or vals.get('mech_ids')=='Painting' and vals.get('damage')=='yes':
				
			raise UserError(_('Please select service or Reparing if damage'))
		if not vals.get('mech_ids'):


			raise	UserError(_('Have to select atleast one Service'))


		fields=self.env['mech.details'].search([('mech_ids','=','Servicing')])
		print "=================fffffffffffffffffffffff===========",fields


		'''if vals.get('name', _('New')) == _('New'):
			if damage in vals:
				if damage==True:
					vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['damage']).next_by_code('mech.details') or _('New')
				else:
					 vals['name'] = self.env['ir.sequence'].next_by_code('mech.details') or _('New')'''
		result = super(mech, self).create(vals)
		print "====================================",vals
		return result


	@api.multi
	def write(self,vals):
		print "=======================write====1111111111====vals===================================",vals
		# if vals.get('mech_ids')=='Washing' or vals.get('mech_ids')=='Painting' and vals.get('damage')=='yes':
				
		# 	raise UserError(_('Please select service or Reparing if damage'))
		print "code==============================",vals.get('parts')
		# if  not self.mech_ids.code:
		# 	raise	UserError(_('Have to select atleast one Service'))
		# if not vals.get('mech_ids'):
		# 	raise	UserError(_('Have to select atleast one Service'))
		if vals.get('mech_ids'):
			for i in vals.get('mech_ids'):
				if not i[2]:
					raise	UserError(_('Have to select atleast one Service'))


		if vals.get('parts'):
			for i in vals.get('parts'):
				print "                     ",i



		result = super(mech, self).write(vals)
		print "================write======result==============",result
		return result

	@api.multi
	def action_cancel(self):
		print "==========action_cancel=================="
		for garage in self:
			garage.vehical = 'c'
		return
	@api.multi
	def action_confirm(self):

		self.write({'state':'done'})
	# @api.multi
	# def update_part(self,a):
	# 	#self.ensure_one()
	# 	#print"inside update==========================",self.parts.name,self.parts.price

	# 	print"iiiiiiiiinnnnnnnnnnnnnnnnn------------",self.parts
	# 	for j in self.parts:
	# 		print"yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",j
	# 		#print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",a
	# 		j.name=a['name']
	# 		j.price=a['price']
	# 			#m=a[i]
	# 	print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",a
			
		
	# 	self.parts.name=a['name']
	# 	self.parts.price=a['price']
	# 	return
	
		
		