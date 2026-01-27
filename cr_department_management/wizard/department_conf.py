# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from odoo import models, fields,api
class DepartmentConf(models.TransientModel):
    _name = 'department.conf'
    _description = 'Department Configuration'

    type = fields.Selection([('create', 'Create'),('write', 'Write')], string="Type", default='create')
    name =  fields.Char(string="Name", required=True)
    code =  fields.Char(string="Code", required=True)
    department_id = fields.Many2one('department.department',string="Department")

    def action_write_department(self):
        if self.type == 'create':
            create_dept = {'name': self.name,
                           'code': self.code,}
            self.env['department.department'].create(create_dept)
        elif self.type == 'write':
            if self.department_id:
                self.department_id.write({'name':self.name,'code': self.code})


