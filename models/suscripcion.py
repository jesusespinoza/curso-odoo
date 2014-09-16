# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

TIPOS = [
    ('oro', 'Plan ORO'),
    ('Plata', 'Plan PLATA'),
    ('bronce', 'Plan BRONCE'),
]
    

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _descripton = 'co.suscripcion'
    
    _columns = {
        'code': fields.char('Código'),
        'type': fields.selection(TIPOS, 'Tipo de suscripción'),
        'date_start':fields.date('Inicio suscripción'),
        'date_end':fields.date('Fin suscripción'),
        'active':fields.boolean('Activo'),
        'suscriptor_id':fields.many2one('co.suscriptor', 'Afiliado'),
    }
    
suscripcion()
