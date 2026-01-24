from odoo import fields, models

class Student(models.Model):
    _name = "student.student"
    _description = "Student"
    _inherit = "my.abstract.model"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email", required=True)
    leave_ids = fields.One2many('student.leave', 'student_id', string="Leaves")

    def action_leave_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Student Leave",
            "res_model": "student.leave.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_student_id": self.id},
        }
