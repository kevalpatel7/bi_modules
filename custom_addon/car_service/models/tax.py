from odoo import fields,models,api, _


class tax(models.Model):
	_name='tax.details'
	_description="details of Mechanic" 


	name=fields.Char(string='tax name')
	garage_id=fields.Many2one('mech.details')
	tax_ids=fields.Many2many('mech.details','tax_garage_rel','tax_id','garage_id',string='garage')
	value=fields.Integer(string='% value')