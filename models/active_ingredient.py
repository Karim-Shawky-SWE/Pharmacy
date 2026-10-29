from odoo import fields, models

class PharmacyActiveIngredient(models.Model):
    _name = 'active.ingredient'
    _description = 'Medicine active ingredient'

    name = fields.Char(string='Active Ingredient', required=True)

    product_ids = fields.Many2many(comodel_name='product.template', string='Products')