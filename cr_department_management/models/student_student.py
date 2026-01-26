# -*- coding: utf-8 -*-
# Part of Creyox Technologies.

from odoo import models, fields,api


class StudentStudent(models.Model):
    _name = "student.student"
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",required=True)
    image = fields.Binary(string="Image")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Zip")
    state_id = fields.Many2one("res.country.state",string="State")
    country_id = fields.Many2one("res.country",string="Country")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    barcode = fields.Char(string="Barcode",readonly=True)
    department_id = fields.Many2one("department.department",string="Department")
    type = fields.Selection([("internal","Internal"),("external","External")],string="Type",default="internal")
    notes = fields.Html(string="Notes")
    remarks = fields.Text(string="Remarks")
    is_cr = fields.Boolean(string="CR",default=True)
    cr_start_date = fields.Date(string="Start Date")
    cr_end_date = fields.Date(string="End Date")
    no_of_votes = fields.Integer(string="Number of Votes")
    active = fields.Boolean(string="Active")

    @api.onchange("mobile")
    def _onchange_mobile(self):
        self.ensure_one()
        if self.mobile:
            self.barcode = self.mobile
