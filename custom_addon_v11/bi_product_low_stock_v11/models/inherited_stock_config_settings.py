# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api, _
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
	
	_inherit = ['res.config.settings']




	notification_base = fields.Selection([('on_hand','On hand quantity'),('fore_cast','Forecast')],string='Notification Based On',default='on_hand')
	notification_products = fields.Selection([('for_all','Global for all product'),('fore_product',' Individual for all products')],string='Min Quantity Based On',default='for_all')
	min_quantity = fields.Float(string = 'Quantity Limit')
	
	notification_user = fields.Many2one('res.users',string = 'Notify User')
	email_user = fields.Char( string="Email From") 
	low_stock_products=fields.One2many('low.stock.transient','stock_product',store=True)





	@api.onchange('notification_user')
	def _onchange_notification_user(self):

		res = self.env['res.company'].search([('name','=',self.notification_user.company_id.name)])
		print ("res=====================",res.email)
		self.email_user = res.email

		   


	#@api.depends('min_quantity','notification_base','notification_products')
	def action_list_products_(self):
		products_list=[]
		#print "1111111111111111111111111111111111",self.low_stock_products
		res = self.env['res.config.settings'].search([])
		res_ids=[]
		for ids in res:
			res_ids.append(ids.id)
		new_record=max(res_ids)
		for data in res:
			if data.id == new_record:
				products_dlt = [(2,dlt.id,0)for dlt in data.low_stock_products]
				

				data.low_stock_products = products_dlt

				if data.notification_base == 'on_hand':
					if data.notification_products == 'for_all':
						res = self.env['product.product'].search([('qty_available','<',data.min_quantity)])
						
						#print "for all ===================on hand",res
						for product in res:
							products_list.append([0,0,{'name':product.name,
													'limit_quantity':data.min_quantity,
													'stock_quantity':product.qty_available}])
			
					
					if data.notification_products == 'fore_product':
						#print self
						res = self.env['product.product'].search([])
						#print"for product================hand==========",res

						for product in res:
							if product.qty_available < product.min_quantity:
								products_list.append([0,0,{'name':product.name,
															'limit_quantity':product.min_quantity,
														'stock_quantity':product.qty_available}])


				if data.notification_base=='fore_cast':
					if data.notification_products=='for_all':
						res = self.env['product.product'].search([('virtual_available','<',data.min_quantity)])
						for product in res:
							products_list.append([0,0,{'name':product.name,
													'stock_quantity':product.virtual_available}])
					if data.notification_products == 'fore_product':
						res = self.env['product.product'].search([])

						for product in res:
							if product.virtual_available < product.min_quantity:
								products_list.append([0,0,{'name':product.name,
															'limit_quantity':product.min_quantity,
														'stock_quantity':product.virtual_available}])

					

				print( "222222222222222222222222222222222222222222222",products_list)
				data.low_stock_products = products_list
				#print "33333333333333333333333333333333333333"
		return 


	
		
	# def shedule_send_notification(self, cr, uid, context=None):
		
	# 	stock_config_obj=self.pool.get('stock.config.settings')
	# 	#print "yooooooooooooooooooooooooooooooooo"
	# 	stock_config_ids=self.pool.get('stock.config.settings').search(cr,uid,[])
	# 	for stock_config_id in stock_config_ids:
	# 		stock_config = stock_config_obj.browse(cr, uid, stock_config_id , context=context)
			
	# 		stock_config.action_low_stock_send()

	
	def action_low_stock_send(self):
		
		#print "before send===================================="
		res = self.env['res.config.settings'].search([])
		#print "resss====================================",res
		res_ids=[]
		for ids in res:
			res_ids.append(ids.id)
		mail_id=max(res_ids)
		# for data in res:
		# 	if data.id == mail_id:
		# 		data.action_list_products_()
		
		
		template_id = self.env.ref('bi_product_low_stock_v11.low_stock_email_template')
		#print "template_id========================",template_id
		#print "self_id============================",mail_id
		send = template_id.send_mail(mail_id, force_send=True)
		
		print ("3333333333333333333333333333333333333333333333333333333333333333")

		
		
		return True
	@api.model
	def get_values(self):
		print('get====================================================')
		res = super(ResConfigSettings,self).get_values()
		notification_base = self.env['ir.config_parameter'].sudo().get_param('bi_product_low_stock.notification_base')
		notification_products = self.env['ir.config_parameter'].sudo().get_param('bi_product_low_stock.notification_products')
		min_quantity = float(self.env['ir.config_parameter'].sudo().get_param('bi_product_low_stock.min_quantity'))
		notification_user = literal_eval(self.env['ir.config_parameter'].sudo().get_param('bi_product_low_stock.notification_user'))
		email_user = self.env['ir.config_parameter'].sudo().get_param('bi_product_low_stock.email_user')
		print ("userrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		res.update(
			notification_base = notification_base,
			notification_products = notification_products,
			min_quantity = min_quantity,
			notification_user = notification_user,
			email_user = email_user
			)
		print('end====================================================',email_user)
		return res


	@api.multi
	def set_values(self):
		print("set=============================")
		super(ResConfigSettings,self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('bi_product_low_stock.notification_base', self.notification_base)
		self.env['ir.config_parameter'].sudo().set_param('bi_product_low_stock.notification_products', self.notification_products)
		self.env['ir.config_parameter'].sudo().set_param('bi_product_low_stock.min_quantity', self.min_quantity)
		self.env['ir.config_parameter'].sudo().set_param('bi_product_low_stock.notification_user', self.notification_user.id)
		self.env['ir.config_parameter'].sudo().set_param('bi_product_low_stock.email_user', self.email_user)
		print('end set========================================================')






class low_stock_product(models.TransientModel):



	_name='low.stock.transient'


	name=fields.Char(string='Product name')
	stock_quantity=fields.Float(string='Quantity')
	limit_quantity=fields.Float(string='Quantity limit')
	stock_product=fields.Many2one('res.config.settings')

