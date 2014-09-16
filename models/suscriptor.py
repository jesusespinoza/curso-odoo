# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _descripton = 'co.Suscriptor'
    
    _columns = {
        'name': fields.char('Nombre'),
        'identification': fields .char('cedula'),
        'address': fields.text('Direccion'),
    }
    
suscriptor()
    
