from odoo import fields, models

class StudentLeave(models.Model):
    _name = "student.leave"
    _description = "Student Leave"

    student_id = fields.Many2one('student.student', string="Student")
    student_name = fields.Char(string="unused",related="student_id.name")

    stud_email = fields.Char(string="email", related="student_id.email")
    date = fields.Date(string="Date")
    reason = fields.Char(string="Reason")