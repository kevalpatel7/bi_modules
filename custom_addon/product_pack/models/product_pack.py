# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields,models,api, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round

class Product_pack(models.Model):


	_inherit = "product.template"
	



	# @api.multi
	# @api.depends('Product')
	# def _cal_bill(self):
		
	# 	total=0
	# 	for i in self:
	# 		for j in i.Product:
	# 			if not j:
	# 				return
	# 			total += j.price
	# 	self.bill=total
	# 	print"yyoooooooooooo"


	@api.multi
	@api.onchange('want_cal','product')
	def _cal_price(self):
		self.ensure_one()
		if not self.want_cal:
			return
		total = 0
		print "selllllllllllllllllllllllllllllllllllllffffffffffffff",self.list_price
		#res = self.env['product.template'].browse(self._context.get('active_id'))
		for j in self:
			if j.want_cal == True:
				
					for i in j.product:
						print "=====================1============",i.price,i.qua
						total = total+i.name.lst_price*i.qua
					print "==============================total===============",total
			
		#k=self.list_price
		# res['list_price']=total
		self.list_price = total
		print "==============================self.list_price===============",self.list_price
		# k=[]

		return 


	
	is_pack=fields.Boolean(string='Is Product pack')
	product=fields.One2many('pack.details','Product_id',string='Product')
	#Product_id=fields.Many2one('bundle.pack')
	want_cal=fields.Boolean(string='Want to calculate')


	
	















	# @api.multi
	# @api.onchange('product')
	# def _update_onhanf_(self):
	# 	if not self.product:
	# 		return
	# 	for i in self:
	# 		if i.product:
	# 			a=[]
	# 			for j in i.product:
	# 				k=j.name.qty_available
	# 				k=k//j.qua
	# 				print "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",k
	# 				a.append(k)
	# 			b=min(a)
	# 			print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",b
	# 	self.qty_available=b
	# 	print ")))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"







	# 	return 
				
	# @api.model
	# def create(self,vals):

	# 	k=self.env['product.template'].browse(vals.get('qty_available'))
	# 	print"===================k================================",k._update_onhanf_()
	# 	vals.get('qty_available')
	# 	d=super(Product_pack, self).create(vals)
	# 	return d


	# @api.multi
	# def write(self,vals):
	# 	k=self.env['product.template'].browse(vals.get('qty_available'))
	# 	print"=====================k========write===========",k._update_onhanf_()
	# 	print"-----------------------------------------------------",vals.get('qty_available')
	# 	d=super(Product_pack, self).write(vals)
	# 	return d

class Product(models.Model):
	_inherit = "product.product"


	# @api.multi
	# def _compute_quantities_dict(self, lot_id, owner_id, package_id, from_date=False, to_date=False):
		

	# 		vals=super(Product,self)._compute_quantities_dict(lot_id, owner_id, package_id, from_date, to_date)
	# 		print"=========vals======================"
	# 		result = self.env['product.template'].search([('is_pack','=',True)])
			
			



	# 		domain_quant_loc, domain_move_in_loc, domain_move_out_loc = self._get_domain_locations()
	# 		domain_quant = [('product_id', 'in', self.ids)] + domain_quant_loc
	# 		dates_in_the_past = False
	# 		if to_date and to_date < fields.Datetime.now(): #Only to_date as to_date will correspond to qty_available
	# 			dates_in_the_past = True

	# 		domain_move_in = [('product_id', 'in', self.ids)] + domain_move_in_loc
	# 		domain_move_out = [('product_id', 'in', self.ids)] + domain_move_out_loc
	# 		if lot_id:
	# 			domain_quant += [('lot_id', '=', lot_id)]
	# 		if owner_id:
	# 			domain_quant += [('owner_id', '=', owner_id)]
	# 			domain_move_in += [('restrict_partner_id', '=', owner_id)]
	# 			domain_move_out += [('restrict_partner_id', '=', owner_id)]
	# 		if package_id:
	# 			domain_quant += [('package_id', '=', package_id)]
	# 		if dates_in_the_past:
	# 			domain_move_in_done = list(domain_move_in)
	# 			domain_move_out_done = list(domain_move_out)
	# 		if from_date:
	# 			domain_move_in += [('date', '>=', from_date)]
	# 			domain_move_out += [('date', '>=', from_date)]
	# 		if to_date:
	# 			domain_move_in += [('date', '<=', to_date)]
	# 			domain_move_out += [('date', '<=', to_date)]

	# 		Move = self.env['stock.move']
	# 		Quant = self.env['stock.quant']
	# 		domain_move_in_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_in
	# 		domain_move_out_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_out
	# 		moves_in_res = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_in_todo, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
	# 		moves_out_res = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_out_todo, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
	# 		quants_res = dict((item['product_id'][0], item['qty']) for item in Quant.read_group(domain_quant, ['product_id', 'qty'], ['product_id'], orderby='id'))
	# 		print"=====================quants_res========================",quants_res

	# 		if dates_in_the_past:
	# 			# Calculate the moves that were done before now to calculate back in time (as most questions will be recent ones)
	# 			domain_move_in_done = [('state', '=', 'done'), ('date', '>', to_date)] + domain_move_in_done
	# 			domain_move_out_done = [('state', '=', 'done'), ('date', '>', to_date)] + domain_move_out_done
	# 			moves_in_res_past = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_in_done, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
	# 			moves_out_res_past = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_out_done, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
			

	# 		if result:
	# 			on_hand_product = 0
	# 			list_on_hand = []
	# 			min_on_hand=0


	# 			for template in result:

	# 				print"insideeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
	# 				for product in template.product:
	# 					if product.qua > 0:
	# 						print" product.name.qty_available=================",product.name.
	# 						on_hand_product = product.name.qty_available // product.qua
	# 						list_on_hand.append(on_hand_product)
	# 						print"list_on_hand===========================",list_on_hand
	# 			min_on_hand=min(list_on_hand)

	# 			print"================min_on_hand========================",min_on_hand





	# 		res = dict()
	# 		for product in self.with_context(prefetch_fields=False):
	# 			res[product.id] = {}
	# 			if dates_in_the_past:
	# 				qty_available = quants_res.get(product.id, 0.0) - moves_in_res_past.get(product.id, 0.0) + moves_out_res_past.get(product.id, 0.0)
	# 			else:
	# 				qty_available = quants_res.get(product.id, 0.0)
	# 			res[product.id]['qty_available'] = float_round(min_on_hand, precision_rounding=product.uom_id.rounding)
	# 			res[product.id]['incoming_qty'] = float_round(moves_in_res.get(product.id, 0.0), precision_rounding=product.uom_id.rounding)
	# 			res[product.id]['outgoing_qty'] = float_round(moves_out_res.get(product.id, 0.0), precision_rounding=product.uom_id.rounding)
	# 			res[product.id]['virtual_available'] = float_round(
	# 				qty_available + res[product.id]['incoming_qty'] - res[product.id]['outgoing_qty'],
	# 				precision_rounding=product.uom_id.rounding)
	# 		print"================================res=====_inherit================",res
	# 		return res
