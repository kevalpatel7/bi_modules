from odoo import api, fields, models, _



class sendemail(models.TransientModel):

	_name = "mail.low.stock"


	name_to = fields.Char(string='Send email To')
	name_from = fields.Char(string='Send email from')
	mail_body = fields.Html(string='Body of the mail')



	@api.model
	@api.multi
	def default_get(self, default_fields):

		res = super(sendemail, self).default_get(default_fields)
		print "=======================res=================",res

		result = self.env['stock.low.notification'].browse(self._context.get('active_id'))
		print"==================name============================",result.notification_user.email
		res['name_to'] = result.notification_user.email
		res['mail_body'] = "Hiiiiiiiiiiiiiiiiiiiiiiii"
		print "res================after===============",res


		#res = self._convert_to_write(res)

		return res


	@api.multi
	def send_mail_stock_low(self):
	# user_id = self.user_target.id
	# body = self.message_target
		print "before============"
		mail_details = {'subject': "Message subject",
         'body': self.mail_body,
         #s'partner_ids': [(user_target)]
         } 
		print "mail_details=============",mail_details
		mail = self.env['mail.thread']
		print"after==========================",mail
		mail.message_post(type="notification", subtype="mt_comment", **mail_details)

	






