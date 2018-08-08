from odoo import fields,models,api, _
from odoo.exceptions import UserError

class Aadhar(models.Model):
	_inherit = "res.partner"


	Aadhar_id=fields.Char(string='Aadhar ID')




	@api.model
	def create(self,vals):
		print"==============vals=================",vals
		k=self.env['res.partner'].browse(vals.get('Aadhar_id'))
		print "========================kkkkkkkkkk======================",k
		
		if k:
			if len(vals.get('Aadhar_id'))!=12:
				raise UserError(_('Aadhar id must be 12 digit long'))

		

		if k:
			m=self.env['res.partner'].search([('Aadhar_id','=',vals.get('Aadhar_id'))])

				
		print "-------------------------------------",m
		if m:
			print "inside m=========================="
			raise UserError(_('Aadhar_id already there try something else'))






		Ad=super(Aadhar, self).create(vals)
		return Ad



	@api.multi
	def write(self,vals):
		print"==============vals of write=================",vals
		k=self.env['res.partner'].browse(vals.get('Aadhar_id'))
		print "========================kkkkkkkkkk======================",k
		#i=vals.get('name')
		if k:
			if len(vals.get('Aadhar_id'))!=12:
				raise UserError(_('Aadhar id must be 12 digit long'))
		if k:
			m=self.env['res.partner'].search([('Aadhar_id','=',vals.get('Aadhar_id'))])
			print "=+++++++++++++++++++++=",m

			if m:

				raise UserError(_('Aadhar_id already there try something else'))



		Ad=super(Aadhar, self).write(vals)
		return Ad

	
		














