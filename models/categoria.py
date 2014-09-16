# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class categoria(osv.osv):
    _name = 'co.categoria'
    _descripton = 'co Categoria'
    
    _columns = {
        'name': fields.char('Nombre'),
        'description': fields.text('Descripción'),
        'parent_id':fields.many2one('co.categoria', 'Padre'),
        'child_ids':fields.one2many('co.categoria', 'parent_id', 'Sub-categorías'),
    }
    
categoria()
