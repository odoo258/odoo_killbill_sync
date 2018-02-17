# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartnerExt(models.Model):
	_inherit = 'res.partner'
	
	killbill_id = fields.Char('KillBill ID')