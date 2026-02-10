# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from email.policy import default

from dateutil.relativedelta import relativedelta
from odoo import models, fields,api
import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError


class StudentStudent(models.Model):
    _name = "student.student"
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name_search = ['department_id','dept_code']

    name = fields.Char(string="Name",required=True)
    image = fields.Binary(string="Image")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Zip")
    state_id = fields.Many2one("res.country.state",string="State")
    country_id = fields.Many2one("res.country",string="Country")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age",readonly=True,compute="_compute_age",store=True)
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    barcode = fields.Char(string="Barcode")

    department_id = fields.Many2one("department.department",string="Department")
    dept_code = fields.Char(related="department_id.code" , string="Dept Code")
    type = fields.Selection([("internal","Internal"),("external","External")],string="Type",default="internal")
    notes = fields.Html(string="Notes")
    remarks = fields.Text(string="Remarks")
    is_cr = fields.Boolean(string="CR",default=True)
    cr_start_date = fields.Date(string="Start Date")
    cr_end_date = fields.Date(string="End Date")
    no_of_votes = fields.Integer(string="Number of Votes")
    active = fields.Boolean(string="Active",default="True")


    @api.onchange("mobile")
    def _onchange_mobile(self):
        self.ensure_one()
        if self.mobile:
            self.barcode = self.mobile

    @api.depends("birthdate")
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                d1 = record.birthdate
                d2 = datetime.date.today()
                record.age = relativedelta(d2, d1).years
            else:
                record.age = 0

    # @api.onchange("name")
    # def _default_first_department_id(self):
    #     self.ensure_one()
    #     self.department_id = self.env["department.department"].search([], order='id asc', limit=1)

    @api.model
    def default_get(self, fields_list):
        print(fields_list)
        res = super().default_get(fields_list)
        print(res)
        if 'department_id' not in res:
            res.update({
                'department_id': self.env["department.department"].search([],limit=1).id
            })
        return res

    def print_name(self):
        print("Heet Nagapara")

    @api.constrains("cr_start_date","cr_end_date")
    def check_start_is_before_end_date(self):
        if self.cr_start_date and self.cr_end_date:
            if self.cr_start_date > self.cr_end_date:
                raise ValidationError("Start Date must be before End Date")

    def action_for_get_info_by_wizard(self):
        return {
            'name': "Send Mail",
            'type': 'ir.actions.act_window',
            'res_model': 'send.mail.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context':{"current_name":self.name,"email":self.email},
        }