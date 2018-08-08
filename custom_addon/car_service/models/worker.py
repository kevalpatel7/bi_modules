from odoo import fields,models,api, _



class workers(models.Model):

	_name='workers.details'
	_description="details of workers" 


	name=fields.Char(string='Name')
	phone=fields.Char(string='phone' )
	address=fields.Char(string='address')
	gender=fields.Selection([('male','male'),('f','female')],string='gender')
	details=fields.Html(string='extra details')
	jobposition=fields.Char(string='job position')
	date=fields.Date(string='Date of joining')
	salary=fields.Integer(string='salary')






	