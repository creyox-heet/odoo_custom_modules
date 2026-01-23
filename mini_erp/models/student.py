from odoo import models,fields

class Student(models.Model):
    _name="student.table"
    _description = "Student Table"

    name = fields.Char(string="Project name",required=True)
    parent_id = fields.Many2one("student.table",string="Parent")
    child_ids = fields.One2many("student.table","parent_id",string="Children")



