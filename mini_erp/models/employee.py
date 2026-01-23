from odoo import models,fields

class Employee(models.Model):
    _name="mini.employee"
    _description = "Employee"
    name = fields.Char(string="Employee Name",required=True)
    age = fields.Integer(string="Age",required=True)
    company_id = fields.Many2one("mini.company",string="Company")
    project_ids = fields.Many2many("mini.project",string="Projects")



