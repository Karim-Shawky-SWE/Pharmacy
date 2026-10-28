from odoo import fields, models, api
from odoo.exceptions import ValidationError

class product_template(models.Model):
    _inherit = 'product.template'

    active_ingredient_ids = fields.Many2many('model.name', string='Active Ingredients')
    consuming_way = fields.Selection([
        ('tablet', 'Tablets'),
        ('capsules', 'Capsules'),
        ('powder', 'Powder'),
        ('cream', 'Cream'),
        ('oral_solution', 'Oral solution'),
        ('injection', 'Injection'),
        ('eye_drops', 'Eye drops'),
        ('syrup', 'Syrups'),
        ('spray', 'Spray'),
        ('suppository', 'Suppository'),
        ('shampoo', 'Shampoo'),
    ], default='tablet', required=True)
    medicine_for = fields.Many2many('medicine.usage', string='Medicine For')

    strength = fields.Float(string='Strength', required=True)
    uom = fields.Many2one('uom.uom', string='Unit of Measure', required=True)

    tape = fields.Integer(string='Tape', required=True)
    bills = fields.Integer(string='Bills', required=True)

    @api.constrains('strength')
    def _check_strength(self):
        if self.strength <= 0:
            raise ValidationError('Strength must be greater than 0')
        elif self.strength > 10000:
            raise ValidationError('Strength must be less than 10000')

    @api.constrains('uom')
    def _check_uom(self):
        if self.uom == 'g' and self.strength >= 10:
            raise ValidationError('Strength must be less than or equal 10 g')
        elif self.uom == 'mg' and self.strength >= 3000:
            raise ValidationError('Strength must be less than or equal 3000 mg')

    @api.constrains('consuming_way', 'tape')
    def _check_tape_required(self):
        for rec in self:
            if rec.consuming_way in ('tablet', 'capsules') and not rec.tape:
                raise ValidationError("Tape is required for tablets and capsules.")
            if rec.tape <= 0 :
                raise ValidationError("Tape must be greater than 0")