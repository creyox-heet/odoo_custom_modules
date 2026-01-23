from odoo import models, fields

class MiniTask(models.Model):
    _name = "mini.task"
    _description = "Mini Task"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Task Title", required=True)
    description = fields.Text(string="Description")
    priority = fields.Selection(
        [
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        default="medium",
    )