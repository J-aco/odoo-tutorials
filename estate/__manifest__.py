# odoo tutorial module

{
    'name': 'Real Estate',
    'category': 'Tutorials/RealEstate',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'data': [
        'data/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        
        'views/estate_menus.xml',
    ]
}