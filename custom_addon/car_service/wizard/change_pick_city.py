import time

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class ChangePickCity(models.TransientModel):
	_name = "change.pick.city"
	_description = "Change Pick City"



	pick_city=fields.Selection([('a','Ahmedabad'), ('g','Goa'),('d','Delhi')], string='Pickup city')


	@api.model
	def default_get(self, default_fields):
		print "======ChangePickCity======default=============",default_fields
		res = super(ChangePickCity, self).default_get(default_fields)
		print "======ChangePickCity======default=============",self._context.get('active_id')
		car_rent = self.env['car.rent'].browse(self._context.get('active_id'))
		print "======ChangePickCity========car_rent=========",car_rent
		res['pick_city'] = car_rent.city
		return res


	@api.multi
	def change_city(self):
		print "============change_city===========",self.pick_city,self._context
		car_rent = self.env['car.rent'].browse(self._context.get('active_id'))
		car_rent.city = self.pick_city
		return 