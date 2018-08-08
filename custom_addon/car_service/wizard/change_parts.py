from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp






class ChangeParts(models.TransientModel):
	_name = "change.parts"
	_description = "Change parts"

	parts_c=fields.One2many('many.change','part_id',String="Add parts to replase")




	@api.model
	@api.multi
	def default_get(self, default_fields):
		print "======ChangeParts======default=============",default_fields
		

		res = super(ChangeParts, self).default_get(default_fields)

		print "======ChangePickCity======default=============",self._context.get('active_id')
		mech = self.env['mech.details'].browse(self._context.get('active_id'))
		print "======ChangePickCity========car_rent=========",mech
		#print "resssssssssssssssssssssssssssssssssssssssssssss",self
		val=[]
		#w=self.env['mech.details'].search([('parts.id','=','mech.parts.id')])
		#print "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",w
	
		for i in mech.parts:
			print "=============iiiiiiiiiiiiiiiiiii==========",i.name.name,i.price
			
			
			val.append([0,0,{'name':i.name,'price':i.price}])

			print"rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrres",res
			
		res['parts_c'] = val

		res = self._convert_to_write(res)
		print "yoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyyo",res

		return res
		
	
	@api.multi
	def change_parts(self):
		print "============change_parts===keval========",self.parts_c,self._context
		self.ensure_one()
		for i in self.parts_c:
			value=i.get_parts_data()

			if i.name:
				i.name.write(value)
				print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
			else:
				self.env['mech.details'].create(value)
		print"enddddddddddddddddddddddddddddddddddddddddddddddddd"
		if self.env.context.get('active_model') == 'mech.details':
			print "yessssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
			mech = self.env['mech.details'].browse(self._context.get('active_ids',[]))
		
			print "==========mech====================",mech.parts


			print "==========self===parts==name========",self.parts_c
			v=[]
			d={}
			l=[]
			for i in mech.parts:
				l.append(i.id)
			k=0
			for j in self.parts_c:
				if k>=len(l):
					v.append([0,0,{'name':j.name,'price':j.price}])
				else:
					print"========jjjjjjjjjjjjjjjjj==========",j.name.name
				#d.update({'name':j.name,'price':j.price})
					v.append([1,l[k],{'name':j.name,'price':j.price}])
				k=k+1
				#v.append({'name':self.parts_c.name,'price':self.parts_c.price})
			print "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv",v
			mech.parts=v
			#mech.parts=([0,0,v[0]])
			# m=0
			# for i in mech.parts:

			# 	print"==========v[]==========",v[m]
			# 	print "iiiiiiiiiiiiiiiiiii",i
			# 	i=
			# 	m=m+1
			# for j in range(m,len(v)):
			# 	mech.parts = ([0,0,v[j]])
			# for i in v:
			# 	mech.update_part(i)
			#mech.parts= self._convert_to_write(mech.parts)






		return 
		

		
class ChangePartsT(models.TransientModel):

	_name='many.change'


	name=fields.Many2one('create.parts',string='Parts name')
	price=fields.Integer(related='name.price',string="Price")
	part_id=fields.Many2one('change.parts')
	garage_id=fields.Many2one('mech.details')

	@api.multi
	def get_parts_data(self):
		self.ensure_one()
		print "=======ttttttttttttttttttt==================",self.name
		return {
			'name': self.name.name  ,
			'price': self.price 
			
		}


