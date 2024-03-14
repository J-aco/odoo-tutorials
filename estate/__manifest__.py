# odoo tutorial module

{
    'name': 'Real Estate',
    'category': 'Tutorials/RealEstate',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'data': [
        'data/ir.model.access.csv',
        'views/estate_property_views.xml',
    ]
}