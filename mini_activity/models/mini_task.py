from odoo import models, fields

class MiniTask(models.Model):
    _name = "mini.task"
    _description = "Mini Task"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Task Name",
        required=True,
    )

    description = fields.Text(
        string="Description"
    )

    user_id = fields.Many2one(
        "res.users",
        string="Assigned To",
    )

    deadline = fields.Date(
        string="Deadline",
    )

    company_id = fields.Many2one(
        "res.company",
        string="Company",
    )
