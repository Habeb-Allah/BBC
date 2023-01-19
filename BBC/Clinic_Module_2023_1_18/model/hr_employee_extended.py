# -*- coding: utf-8 -*-
from odoo import tools, api, fields, models
#from datetime import datetime
#from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    employee_category = fields.Selection([('doctor','Doctor'),('nurse','Nurse'),('receptionist','Receptionist')], 'Job Title', required = True)


