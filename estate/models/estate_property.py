from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(required=True)
    description = fields.Text()
    state = fields.Selection(
        string = 'State',
        selection = [('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="Current status of property listing",
        required=True,
        copy=False,
        default='new',
    )
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Datetime.add(fields.Datetime.today(), months=+3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (m²)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (m²)")
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection =[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Orientation of the Garden",
    )
    active = fields.Boolean(default=True)

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson_id = fields.Many2one('res.users', string="Sales Person", default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', copy=False, string="Buyer")
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="offers")

    total_area = fields.Float(compute="_compute_total_area", string="Total Area (m²)")
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'))
    