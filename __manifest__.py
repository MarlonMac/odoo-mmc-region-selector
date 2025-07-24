{
    "name": "Region Selector",
    "version": "16.0.1.0.3", 
    "category": "Website",
    "summary": "Selector dinámico de región para sitios multicompañía, agrupado por unidad de negocio.",
    "author": "Marlon Macario",
    'website': 'link-gt.com', 
    "depends": ["website"],
    "data": [
        "security/ir.model.access.csv",       # Controles de acceso a los módulos (Actualizado)
        "views/region_selector_backend.xml",  # Vistas de Configuración de Regiones (actualizado)
        "views/business_unit_views.xml",      # Vistas de Unidad de Negocio (Nuevo), debe ir luego del xml backend porque depende de menús creados acá
        "views/region_selector_template.xml", # Plantilla del selector (actualizado)
    ],
    # "assets": { ... }, # Mantenemos por si queremos agregar assets en futuras versiones
    "installable": True,
    "application": False,
    "license": "LGPL-3", 
}