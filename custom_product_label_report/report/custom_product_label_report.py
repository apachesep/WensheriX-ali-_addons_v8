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

import time
from openerp.osv import osv
from openerp.tools.translate import _
from openerp.report import report_sxw
#from elaphe.upc import UpcA
from datetime import datetime
from openerp.modules.module import get_module_resource


class product_label_report(report_sxw.rml_parse):


    def __init__(self, cr, uid, name, context=None):
        super(product_label_report, self).__init__(cr, uid, name, context=context)
        self.init_bal_sum = 0.0
        self.localcontext.update({

            'time': time,
            'get_date':self.get_date,
            })

    def get_date(self,date):
        if date:
            date_list = date.split(' ')
            date1 = datetime.strptime(date_list[0], '%Y-%m-%d')
            date1 = date1.strftime('%d-%b-%y')
        return date1

class test_report_template_id(osv.AbstractModel):
    _name = 'report.custom_product_label_report.product_label_report_template_id'
    _inherit = 'report.abstract_report'
    _template = 'custom_product_label_report.product_label_report_template_id'
    _wrapped_report_class = product_label_report

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
