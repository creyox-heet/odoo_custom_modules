from odoo import models,fields

class Events(models.Model):
    _name="events.table"
    _description = "events table"
    name = fields.Char(string="Event Name")
    start_date = fields.Datetime(string="Event Start Time")
    end_date = fields.Datetime(string="Event End Time")
    delay = fields.Float(string="Event Delay(hour)")


