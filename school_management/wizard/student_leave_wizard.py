from odoo import fields, models

class StudentLeaveWizard(models.TransientModel):
    _name = 'student.leave.wizard'
    _description = 'Student Leave'

    student_id = fields.Many2one('student.student', string="Student",
                                readonly=True)
    date = fields.Date(string="Date")
    reason = fields.Char(string="Reason")