# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class lineas_stock(osv.osv):
    _name = 'co.lineas.stock'
    _descripton = 'CO Lineas_stock'
    
    _columns = {
        'multimedia_id': fields.many2one('co.multimedia','Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'Tipo Medio'),
        'tienda_id':fields.many2one('Código'),
        'quantity':fields.integer('Cantidad'),
   
    }
lineas_stock()


class tiendas(osv.osv):
    _inherit = 'co.tienda'
    
    _columns = {
        'line_ids': fields.one2many('co.lineas.stock', 'tienda_id', 'stock'),
   
    }
tiendas()
