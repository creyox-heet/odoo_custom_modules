# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
from odoo import models, fields,api
class SendMailWizard(models.TransientModel):
    _name = 'send.mail.wizard'
    _description = 'Send Mail'

    student_id = fields.Many2one("student.student", string="Student Name" , required=True,readonly=True)
    subject = fields.Char(string="Subject")
    msg = fields.Html(string="Message",default="<p>hello,</p><p>Your message type here....</p>")
    email_to = fields.Char(string="Email To")

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        current_record = self.env["student.student"].search([("name","=",self.env.context.get("current_name"))])
        if 'student_id' not in res:
            res.update({'student_id': current_record.id})
        return res

    def action_send_email(self):
        self.email_to = self.env.context.get("email")
        mail_template = self.env.ref("cr_department_management.mail_template_for_student")
        mail_template.send_mail(self.id,force_send=True)
