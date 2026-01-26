# -*- coding: utf-8 -*-
# Part of Creyox Technologies.

from odoo import models, fields,api

class EmployeeEmployee(models.Model):
    _name = "employee.employee"
    _description = "Employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Zip Code")
    state_id = fields.Many2one('res.country.state', string="State")
    country_id = fields.Many2one('res.country', string="Country")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Float(string="Age")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    barcode = fields.Char(string="Barcode",readonly=True)
    job_time = fields.Selection([('full_time', 'Full Time'),('part_time', 'Part Time')], string="Job Time", default='full_time')
    notes = fields.Html(string="Notes")
    remarks = fields.Text(string="Remarks")
    is_hod = fields.Boolean(string="Is HOD?",default=True)
    active = fields.Boolean(string="Active", default=True)

    @api.onchange("mobile")
    def _onchange_mobile(self):
        self.ensure_one()
        if self.mobile:
            self.barcode = self.mobile
