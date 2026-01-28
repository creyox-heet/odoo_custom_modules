# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from odoo import models, fields,api
class DepartmentConf(models.TransientModel):
    _name = 'split.sale.wiz'
    _description = 'Split'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Customer")

    def action_for_split(self):
        self.ensure_one()
        if self.partner_id:
                self.partner_id.write({'split':True})
