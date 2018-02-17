# -*- coding: utf-8 -*-
{
    'name': "Odoo KillBill Sync",

    'summary': """
        Sync killbill payment api with odoo.
        So Partners account and his invoices will deal from killbill.
        (This part of code will improve)
        """,

    'description': """
        At the time of partner creation in odoo a partner will create on 
        KillBill and his killbill id will shown on partner form on the field name 
        killbill ID.Also at the time of invoice creation in odoo a invoice will 
        create on KillBill and his killbill invoice number will shown on partner form on 
        the field name killbill ID.And if payment done on killbill invoice on odoo will
        show as paid.
        (This part of code will improve)
    """,

    'author': "Wahab Ali Malik",
    'website': "http://www.yourcompany.com",
    'category': 'Payment Gateways',
    'data': [
        'security/res_partner_security.xml',
        'views/invoice_ext.xml',
        'views/killbill_config_settings.xml',
        'views/partner_ext.xml',
    ],
    'version': '0.1',
    'depends': ['base','account','connector'],
}