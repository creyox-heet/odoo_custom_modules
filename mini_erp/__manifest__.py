# -*- coding: utf-8 -*-
# Part of Creyox Technologies.

{
    "name": "Odoo Example 2",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Practice",
    "summary": "Odoo Example 2",
    "license": "OPL-1",
    "version": "17.0.0.1",
    "description": "Odoo Example 2",
    "depends": ["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/company_view.xml",
        "views/employee_view.xml",
        "views/project_view.xml",
        "views/employee_search_view.xml",
        "views/employee_kanban_view.xml",
        "views/calender_view.xml",
        "views/hierarchical_view.xml",
        "views/actions.xml",
        "views/menus.xml"
     ],
    "installable": True,
    "application": True,
}
