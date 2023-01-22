from odoo import tools, api, fields, models
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

# from odoo.exceptions import ValidationError


class PatientCard(models.Model):
    _name = "patient.info"
    _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(string="Name")
    date_of_birth = fields.Date(string="Brith Date")
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Sex")
    age = fields.Char(compute='onchange_age', string="Patient age", store=True)


    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Type Of Boold")
    rh = fields.Selection([('-+', '+'), ('--', '-')], string="Rh")

    appointment_ids = fields.One2many('appointment.info','patient_id',string="Appointment")

    dental_record_ids = fields.One2many('dental.record', 'patient_id', string="Procedure")


    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, index=True,
                                 string='Name In English')


    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            else:
                rec.age = " NO Brith Date!"
