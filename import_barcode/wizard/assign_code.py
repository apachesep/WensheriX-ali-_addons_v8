# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
from datetime import datetime

class wizard_assign(osv.osv):
    _name = 'wizard.assign'
    _columns = {
        'barcode': fields.many2one('barcode.barcode','Barcode')
    }
    def code(self):