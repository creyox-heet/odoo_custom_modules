from odoo import models,fields

class Project(models.Model):
    _name="mini.project"
    _description = "Project"

    p_name = fields.Char(string="Project name",required=True)
    employee_ids = fields.Many2many("mini.employee",string="Employees")



