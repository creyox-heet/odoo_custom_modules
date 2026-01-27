# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
{
    "name": "CR Department Management",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Practice",
    "summary": "CR Department Management",
    "license": "OPL-1",
    "version": "17.0.0.1",
    "description": "CR Department Management",
    "depends": ["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/actions.xml",
        "views/department_conf_view.xml",
        "views/department_view.xml",
        "views/employee_view.xml",
        "views/student_view.xml",
        "views/smart_button_of_students_view.xml",
        "views/menus.xml"
     ],
    "installable": True,
    "application": True,
}
