from odoo import fields, models

class MedicineUsage(models.Model):
    _name = 'medicine.usage'
    _description = 'Medicine Usage'

    name = fields.Char(string='Name', required=True)
    product_ids = fields.Many2many(comodel_name='product.template', string='Products')
