from odoo import fields, models


class EstatePropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer model"

    price = fields.Float(string="Price")
    status = fields.Selection(
        string = 'Status',
        selection = [('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False,
    )
    partner_id = fields.Many2one('res.partner', required=True, string="Buyer")
    property_id = fields.Many2one('estate.property', required=True, string="Property")