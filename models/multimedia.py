# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name = 'co.multimedia'
    _descripton = 'co Multimedia'
    
    _columns = {
        'title': fields.char('Titulo'),
        'release_date': fields.date('Fecha de publicacion'),
        'code':fields.char('Código'),
        'categoria_id':fields.many2one('co.categoria','Categoría'),
        'medio_ids':fields.many2many(
            'co.tipo.medio',
            'co_multimedia_medio_rel',
            'multimedia_id',
            'medio_id'),
    }
multimedia()
