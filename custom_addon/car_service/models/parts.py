from odoo import fields,models,api, _




class parts(models.Model):
	_name="parts.add"
	_description="new parts"

	#def _init_(self)

	name=fields.Many2one('create.parts',string='Parts')
	price=fields.Integer(related='name.price',string="Price")

	garage_id=fields.Many2one('mech.details',string='Garage')
	buy=fields.Selection([('yes','yes'),('no','no')],string='Want to buy')
	seller1=fields.Many2one('email.details',string='Seller')
	#item=fields.Selection((('glass','glass'), ('engine','engine'),('wheel','wheel'),('head','head light')),
                   #string='select parts')
	email = fields.Char(related='seller1.email',string='Email')
	phone = fields.Char(related='seller1.phone',string='Phone')
	description=fields.Html(string='Description')
	state=fields.Selection([('not','not confirm'),('done','confirm')],default='not')
	rent_id=fields.Many2one('car.receive')
	#want_buy=fields.Boolean(string='want to buy')
	#seller=fields.Many2one('res.partner',string='seller')
	#buy=fields.Char(string='Buy')
	#item=fields.Char(string='item to buy')


	@api.one
	def confirm_buy(self):
		self.write({'state':'done',
					'buy':'yes'
					})
	@api.multi
	def update_part(self,a):
		print"inside parts=========================="

		self.write({'parts':a})



