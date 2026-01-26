from odoo import fields, models,api

class Student(models.Model):
    _name = "student.student"
    _description = "Student"
    _inherit = "my.abstract.model"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email", required=True)
    leave_ids = fields.One2many('student.leave', 'student_id', string="Leaves")
    total_stud = fields.Integer(string="Total Students")
    def action_leave_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Student Leave",
            "res_model": "student.leave.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_student_id": self.id}
        }

    @api.onchange("phone")
    def _onchange_phone(self):
        if self.phone and 10 > len(self.phone):
            return {"warning":{"title":"Invalid","message":"Phone Number must be less than 10"}}
        return None

    def get_student_name(self):
        stud_env = self.env["student.student"].search([])
        name_list = stud_env.mapped("name")
        print(name_list)