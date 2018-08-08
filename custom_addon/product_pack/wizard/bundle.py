from odoo import fields,models,api, _


class bundle(models.TransientModel):
	_name = "bundle.pack"




	@api.multi
	@api.onchange('name')
	def _change_(self):
		self.ensure_one()
		print"--------------------------------------------------"
		if self.name:
			k=[]
			print 'selslslslslsssssssssssssss',self.name.product
			for i in self.name.product:
				k.append([0,0,{'name':i.name,'qua':i.qua}])


			print"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",k
				
			self.product=k
		return




	#bundle=fields.Many2one('product.pack',string='bundle')
	#pack=fields.Boolean(string='Is Product pack',default=False)
	Qty=fields.Float(string="Qty")
	name=fields.Many2one('product.template')
	product=fields.One2many('bundle.transient','Product_id',string='Product')
	is_pack=fields.Boolean(related='name.is_pack',string="is pack")
	#bill=fields.Integer(string='Bill')




	@api.multi
	def add_bundle(self):
		self.ensure_one()

		print "_+___+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+"
		if self.env.context.get('active_model') == 'sale.order':
			sale = self.env['sale.order'].browse(self._context.get('active_id'))

			print"--------------------+++++++++-----------------------",sale.order_line

			v=[]
			for j in self.name.product:
				print "inside jjjjjjjjjjjjjjjjjjjjjjjj"
				v.append([0,0,{"product_id":j.name,"product_uom_qty":j.qua*self.Qty}])

			print"//////////////////////////////",v

			sale['order_line']=v
		return





	class bundleT(models.TransientModel):

		_name='bundle.transient'

		name=fields.Many2one('product.product')
		#price=fields.Integer(string='price')
		Product_id=fields.Many2one('bundle.pack')
		qua=fields.Float(string='Qty')
		#dis=fields.Text(string="Discription")
		customer_lead=fields.Float('Days')



	
