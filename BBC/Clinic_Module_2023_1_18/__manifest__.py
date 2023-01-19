# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "Clinic",
    "version": "15.0.0.0",
    "summary": "Clinic Pations",
    "author": "Amin Osman",
    "depends": ['hr', 'sale','account'],
    "data": [
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
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/icon.png"],

}
