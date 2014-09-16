# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tienda(osv.osv):
    _name = 'co.tienda'
    _descripton = 'co Tienda'
    
    _columns = {
        'name': fields.char('Nombre de la tienda'),
        'address': fields.char('Tienda'),

   
    }
tienda()
