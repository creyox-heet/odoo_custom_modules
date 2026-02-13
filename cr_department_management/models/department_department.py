# -*- coding: utf-8 -*-
# Part of Creyox Technologies.

from odoo import models , fields,api,_

class DepartmentDepartment(models.Model):
    _name = "department.department"
    _description = "Department"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    sequence_code =  fields.Char('Sequence code', readonly=True,
                                copy=False, default=lambda self: self.env[
                                'ir.sequence'].next_by_code('department.department'))

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company
    )
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code",required=True)
    no_of_students = fields.Integer(string="Number of Students",compute="_compute_no_of_students",store=True)
    staff_ids = fields.Many2many('employee.employee',string="Staff Members")
    hod_id = fields.Many2one('employee.employee',string="HOD",domain="[('is_hod', '=', True)]")
    student_ids = fields.One2many('student.student','department_id',string="Students",domain="[('type', '=','internal')]")
    notes = fields.Html(string="Notes")
    active = fields.Boolean(string="Active", default=True)


    @api.depends("student_ids")
    def _compute_no_of_students(self):
        for r in self:
            self.no_of_students = len(r.student_ids)

    def open_current_department_tree(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'view_mode': 'tree',
            'target': 'new',
            'res_model': 'department.department',
            'domain': [('id', '=', self.id)],
        }

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}:{record.code}"

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None,order=None):
        if name:
            args = ['|',('name',operator,name), ('code', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid,order=order)

    def action_download_xlsx(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/report/excel_download/{self.id}',
            'target': 'new',  
        }

    def action_display_notification(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Display Notification",
                'message': "get notify button is clicked...",
                'sticky': True,
                'type': 'success'
            }
        }

    def action_all_user_notify(self):
        users = self.env["res.partner"].search([("company_id",'=',1)])
        print(users)
        notifications = []
        for user in users:
            notifications.append(((self.env.cr.dbname,"res.partner",user.id),"simple_notification",{
                'type': 'success',
                'title': 'Stage Update',
                'message': "testing of realtime notification",
                'sticky': True,
            }))
        self.env["bus.bus"]._sendmany(notifications)

        print(self.create_uid)


