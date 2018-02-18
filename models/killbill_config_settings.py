# -*- coding: utf-8 -*-
from odoo import fields, models,api,_
from odoo.exceptions import ValidationError


class killbillConfiguration(models.TransientModel):
    _inherit = 'account.config.settings'

    group_discount_per_so_line = fields.Selection([
        (0, 'Unactive KillBill on Partner and Invoice Form'),
        (1, 'Activate KillBill on Partner and Invoice Form')
        ], "Killbill ID",
        implied_group='odoo_killbill_sync.group_killbill_id_per_partner_form'
        )

    kb_username = fields.Char('Username')
    kb_password = fields.Char('Password')
    api_url = fields.Char('API Address')
    
    def execute(self):
    	if self.group_discount_per_so_line:
    		if not self.kb_username or not self.kb_password or not self.api_url:
    			raise ValidationError(_("Please fill all the three fields of Username,Password and URL of API."))
        elif not self.group_discount_per_so_line:
            self.kb_username = False
            self.kb_password = False
            self.api_url = False

    	return super(killbillConfiguration, self).execute()

    @api.multi
    def set_killbill_api_user(self):
        kb_username = self[0].kb_username or ''
        self.env['ir.config_parameter'].set_param('kb_username', kb_username)

    @api.multi
    def set_killbill_password(self):
        kb_password = self[0].kb_password or ''
        self.env['ir.config_parameter'].set_param('kb_password', kb_password)

    @api.multi
    def set_killbill_api_url(self):
        api_url = self[0].api_url or ''
        self.env['ir.config_parameter'].set_param('api_url', api_url)

    @api.multi
    def get_default_killbill_credentials(self, fields=None):
        get_param = self.env['ir.config_parameter'].get_param
        kb_username = get_param('kb_username', default='')
        kb_password = get_param('kb_password', default='')
        api_url = get_param('api_url', default='')
        return {
            'kb_username': kb_username,
            'kb_password': kb_password,
            'api_url' : api_url
        }