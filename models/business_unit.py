# -*- coding: utf-8 -*-
from odoo import models, fields

class BusinessUnit(models.Model):
    _name = 'mmc.business.unit'
    _description = 'Unidad de Negocio para Selector de Región'
    _order = 'name'

    name = fields.Char(string='Nombre de Unidad de Negocio', required=True, translate=True)
    # code = fields.Char(string='Código') # Lo activaremos si necesitamos un identificador interno

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'El nombre de la Unidad de Negocio debe ser único.'),
    ]