# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
from datetime import datetime

class barcode(osv.osv):
	_name = "barcode.barcode"
	_rec_name = "number"
 
	def _assign(self, cr, uid, ids,name, arg ,context=None):
		print "IIIIIIIIIIIIIIIIIII",ids
		res = {}
		for barcode in self.browse(cr, uid, ids, context=context):
			print "********************",barcode.description
			if barcode.description:
				res[barcode.id] = True
			else:
				res[barcode.id] = False
		return res

	_columns = {
                'number' : fields.char("Number"),
                'description': fields.many2one('product.product' , ' Description'),      
                'date': fields.datetime('Updated'),
                'assign': fields.function(_assign, string='Assigned',type='boolean'),
                }

class assigned(osv.osv):
	_inherit = "product.product"
	
	
