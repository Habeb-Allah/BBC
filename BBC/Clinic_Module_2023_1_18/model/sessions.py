from odoo import fields, models, api


class ModelName (models.Model):
    _name = 'sessions.info'
    _description = 'Sessions Info'
    _order = 'date_sessions'

    patient_id = fields.Many2one('patient.info', string="Patient", required=True)
    appointment_id = fields.Many2one('appointment.info',string="Appointment")
    doctor_id = fields.Many2one('doctor.info', related='appointment_id.doctor_id', string="Responsible Doctor")
    sale_order_id = fields.Many2one('sale.order')
    date_sessions = fields.Datetime(string="Date Sessions")
    is_end = fields.Boolean(string="Sessions End")
    description_sessions = fields.Text(string="Description")

    _sql_constraints = [
        ('date_sessions_unique', 'unique (date_sessions, appointment_id)',
         "Date sessions already exists in this order"),
    ]
