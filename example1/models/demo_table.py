# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from odoo import models,fields
class DemoTable(models.Model):
    _name = 'demo.table'
    _description = 'Demo Table'

    name = fields.Char(required=True,string='Name')
    desc = fields.Text(required=True,string='Description')
    age = fields.Integer(required=True,string='Age')
    salary = fields.Float(required=True,string='Salary')
    gender = fields.Selection([("male","Male"),("female","Female")],string='Gender',required=True)
    birth_date = fields.Date()