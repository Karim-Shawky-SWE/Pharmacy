from odoo import fields, models

class MedicineUsage(models.Model):
    _name = 'medicine.usage'
    _description = 'Medicine Usage'

    name = fields.Char(string='Name', required=True)
    parent_category = fields.Char(string='Parent Category', required=True)
    product_ids = fields.Many2one(comodel_name='product.template', string='Products')
