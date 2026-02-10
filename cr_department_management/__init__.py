# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from . import models
from . import wizard
from odoo.exceptions import ValidationError

def _post_init_employee(env):
    env["employee.employee"].create({
        "name":"Demo",
        "email":"demo@gmail.com"
    })

def _check_sale_module_installed(env):
    sale_module = env["ir.module.module"].search([("name","=","sale_management"),("state","=","installed")])
    if not sale_module:
        raise  ValidationError("Installation Aborted: This module requires 'Sales Management' (sale_management)")

def _uninstall_sale_module(env):
    sale_module = env["ir.module.module"].search([("name","=","sale_management"),("state","=","installed")])
    if sale_module:
        sale_module.button_uninstall()
