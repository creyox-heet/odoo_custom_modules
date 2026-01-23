from odoo import fields, models

class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email", required=True)
    leave_ids = fields.One2many('student.leave', 'student_id', string="Leaves")

    def create_leave(self):
        wizard = self.env['student.leave.wizard'].create({
            'student_id': self.id
        })
        return {
            'name': _('Student Leave'),
            'type': 'ir.actions.act_window',
            'res_model': 'student.leave.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }