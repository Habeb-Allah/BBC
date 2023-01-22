# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'The Clinic',
    "version": "15.0.0.0",
    "summary": "Clinic Pations",
    "author": "Habeb-Allah Ahmed",
    'depends': ['hr', 'sale_management','account_accountant'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hr_edited_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/sale_order_view.xml',
        'views/Dental_record.xml',
        # 'views/account.xml',
        'views/sessions_view.xml',
        'views/menu_items.xml',
        'wizard/doctor_working_schedual_view.xml'
    ],
    'images': ['static/description/icon.png'],

    'installable': True,
    "application": True,
    "auto_install": False,


}
