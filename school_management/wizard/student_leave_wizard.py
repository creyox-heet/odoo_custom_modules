from odoo import fields, models
from odoo.exceptions import UserError

class StudentLeaveWizard(models.TransientModel):
    _name = 'student.leave.wizard'
    _description = 'Student Leave'

    student_id = fields.Many2one('student.student', string="Student",
                                readonly=True)
    date = fields.Date(string="Date")
    reason = fields.Char(string="Reason")

    def create_leave(self):
        self.ensure_one()
        if not self.student_id:
            raise UserError("Student not found")

        self.env['student.leave'].create({
            'student_id': self.student_id.id,
            'date': self.date,
            'reason': self.reason,
        })
        return {'type': 'ir.actions.act_window_close'}