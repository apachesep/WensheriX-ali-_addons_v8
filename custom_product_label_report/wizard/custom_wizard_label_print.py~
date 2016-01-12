# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2015-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import fields, osv




class print_label_action_wizard(osv.osv_memory):
	_name="print.label.action.wizard"
	_columns={
				'type_code': fields.selection([('qr_code', 'QR Code'),('pro_barcode', 'Barcode')], required=True),
				'num_print':fields.char('No. of Print'),
				}
	
	def btn_clik_action(self,cr,uid,ids,context=None):
		data={}
		data['ids'] = ids
		data['form'] = self.read(cr, uid, ids, ['type_code','num_print'])[0]
		print "5%%%%%%%%%%%%%",data['form']
		data['form']['context'] = context
		data['model'] = 'product.product'
		print "5%%%%%%%%%%%%%"
		return self.pool['report'].get_action(cr, uid, [], 'custom_product_label_report.product_label_report_template_id', data=data, context=context)



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
