from odoo import fields, models

class StockLot(models.Model):
    _inherit = 'stock.lot'

    days_to_expiration = fields.Integer(string='Days to expiration')
    suggested_action = fields.Selection(string='Suggested Action', selection=[
        ('none', 'None'),
        ('discount', 'Discount'),
        ('return', 'Return'),
        ('dispose', 'Dispose'),
    ])