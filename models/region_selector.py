# models/region_selector.py
from odoo import models, fields

class RegionSelector(models.Model):
    _name = 'res.company.region.selector'
    _description = 'Región disponible para selector web'
    _order = 'business_unit_id, name' # Ordenar por Unidad de Negocio y luego por nombre

    name = fields.Char(string="Nombre en Selector", required=True, help="Ej: Guatemala, Costa Rica, El Salvador. Este es el nombre que se mostrará en la lista desplegable.")
    company_id = fields.Many2one('res.company', string='Compañía', required=True)
    website_id = fields.Many2one('website', string='Sitio Web', required=True, ondelete='cascade',
                                 help="El sitio web específico al que esta configuración de región redirigirá.")
    country_id = fields.Many2one('res.country', string='País', related='company_id.country_id', store=True)
    flag_icon = fields.Binary(string="Ícono/Bandera")
    is_active = fields.Boolean(string="Activo en selector", default=True)
    
    business_unit_id = fields.Many2one(
        'mmc.business.unit',
        string='Unidad de Negocio',
        required=True,
        ondelete='restrict',  # evitamos borrar una Unidad de Negocio si tiene regiones asociadas
        help="Unidad de negocio a la que pertenece esta configuración regional del sitio web."
    )

 
    # Consideramos un constraint si una combinación de website y Business Unit debe ser única,
    # aunque un website_id ya es único por sí mismo.
    # El modelo actual permite múltiples 'name' para el mismo website_id si es necesario,
    # pero 'website_id' en 'res.company.region.selector' debería ser único si cada entrada es un destino.
    # Si el 'name' es "Guatemala" y el website_id es "store.redmusiccorp.com.gt", entonces website_id debe ser único por entrada.

    _sql_constraints = [
        ('website_id_uniq_for_selector', 'unique (website_id)', 'Cada sitio web solo puede tener una entrada en el selector de región.')
    ]
    