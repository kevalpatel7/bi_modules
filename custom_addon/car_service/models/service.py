from odoo import fields,models,api, _





class service(models.Model):
	
	_name="service.details"
	_description="details of Mechanic" 



	name=fields.Char(string='Servicing',required=True)
	mech_id=fields.Many2one('mech.details')
	code=fields.Char(string="code")
	service_ids=fields.Many2many('mech.details','mech_service_rel','service_id','mech_id',string="mech")
	rate=fields.Integer(string='rate')

	@api.multi
	def action_cancel(self):
		print "==========action_cancel====service=============="
		for service in self:
			garage_id = self.env['mech.details'].search([])
			garage_id.action_cancel()
		return

	@api.multi
	@api.depends('service_ids')
	def name_get(self):
		result=[]
		print "=======================self mech name===============",self
		for a in self:
		
			name =a.name + ' | ' + str(a.rate)
			result.append((a.id,name))

		return result


