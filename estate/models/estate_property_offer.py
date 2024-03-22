from odoo import api, fields, models
from dateutil import relativedelta


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

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_expiry", inverse="_inverse_expiry", readonly=False)
    @api.depends("validity", "create_date")
    def _compute_expiry(self):
        try:
            for record in self:
                record.date_deadline = fields.Datetime.add(record.create_date, days=+record.validity)
        except:
            for record in self:
                record.date_deadline = fields.Datetime.add(fields.Datetime.today(), days=+record.validity)
    
    def _inverse_expiry(self):
        # Updates the Validity period to the difference between the create_date and the new deadline.
        # The days gets updated +1 as relativedelta must start counting from 0.
        try:
            for record in self:
                d1 = fields.Datetime.to_datetime(record.date_deadline)
                d2 = fields.Datetime.to_datetime(record.create_date)
                delta = relativedelta.relativedelta(d1, d2)
                record.validity = int(delta.days) +1
        except:
            for record in self:
                d1 = fields.Datetime.to_datetime(record.date_deadline)
                delta = relativedelta.relativedelta(d1, fields.Datetime.today())
                record.validity = int(delta.days) +1