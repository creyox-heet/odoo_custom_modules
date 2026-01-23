from odoo import models,fields

class Company(models.Model):
    _name="mini.company"
    _description = "Mini Company"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Company Name",tracking=True)
    employee_ids = fields.One2many("mini.employee","company_id",string="Employees",tracking=True)
