from odoo import models,fields
class MyAbstractModel(models.AbstractModel):
    _name = 'my.abstract.model'
    _description = 'My Abstract Model'

    date = fields.Date(string="Date")
