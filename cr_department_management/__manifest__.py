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
    "depends": ["base","mail","sale"],
    "data": [
        "security/security_data.xml",
        "security/ir.model.access.csv",
        "data/email_template.xml",
        "views/send_mail_wizard_view.xml",
        "report/department_report.xml",
        "report/ir_actions_report.xml",
        "data/ir_actions_server.xml",
        "data/ir_cron_data.xml",
        "data/ir_sequence.xml",
        "views/actions.xml",
        "views/department_conf_view.xml",
        "views/department_view.xml",
        "views/employee_view.xml",
        "views/student_view.xml",
        "views/menus.xml"
     ],
    "demo":[
        "demo/demo_data.xml"
    ],
    "post_init_hook":"_post_init_employee",
    "pre_init_hook":"_check_sale_module_installed",
    'uninstall_hook': '_uninstall_sale_module',
    "installable": True,
    "application": True,
}
