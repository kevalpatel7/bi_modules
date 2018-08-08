from odoo import fields,models,api, _


class email(models.Model):
	_name='email.details'
	_description="details of emails" 


	name=fields.Char(string='seller')
	email=fields.Char(string='email')
	phone=fields.Char(string="phone number")
	#garage_id=fields.Many2one('mech.details')
	#tax_ids=fields.Many2many('mech.details','tax_garage_rel','tax_id','garage_id',string='garage')
