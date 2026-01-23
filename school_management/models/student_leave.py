from odoo import fields, models

class StudentLeave(models.Model):
    _name = "student.leave"
    _description = "Student Leave"

    student_id = fields.Many2one('student.student', string="Student")
    date = fields.Date(string="Date")
    reason = fields.Char(string="Reason")