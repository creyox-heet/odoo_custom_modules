from odoo import fields, models,api

class Student(models.Model):
    _name = 'student.student.mark'
    _description = 'student marks'

    name = fields.Char()
    math = fields.Integer()
    science = fields.Integer()
    english = fields.Integer()
    total = fields.Integer(compute='_compute_total', store=True)

    @api.depends('math', 'science', 'english')
    def _compute_total(self):
        for student in self:
            student.total = student.math + student.science + student.english
