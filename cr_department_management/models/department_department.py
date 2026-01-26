# -*- coding: utf-8 -*-
# Part of Creyox Technologies.

from odoo import models , fields,api

class DepartmentDepartment(models.Model):
    _name = "department.department"
    _description = "Department"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code",required=True)
    no_of_students = fields.Integer(string="Number of Students",compute="_compute_no_of_students",store=True)
    staff_ids = fields.Many2many('employee.employee',string="Staff Members")
    hod_id = fields.Many2one('employee.employee',string="HOD")
    student_ids = fields.One2many('student.student','department_id',string="Students")
    notes = fields.Html(string="Notes")
    active = fields.Boolean(string="Active", default=True)

    @api.depends("student_ids")
    def _compute_no_of_students(self):
        if self.student_ids:
            self.no_of_students = len(self.student_ids)


