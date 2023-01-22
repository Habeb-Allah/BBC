from odoo import tools, api, fields, models
#from datetime import datetime
#from odoo.exceptions import ValidationError


class DoctorCard(models.Model):
    _name = "doctor.info"

    employee_id = fields.Many2one('hr.employee',string="Doctor", domain="[('employee_category', '=', 'doctor')]")

    name = fields.Char(related='employee_id.name', string="Name", store=True)
    speciality = fields.Char(string="specialist")

    appointment_ids = fields.One2many('appointment.info', 'doctor_id', string="Appointments", readonly=True)
    working_schedule_ids = fields.One2many('doctor.working.schedule', 'doctor_id', string="Doctor Attendances Table")

    state_working_schedual = fields.Boolean(compute='check_availability_state')

    @api.model
    def check_availability_state(self):
        for elem in self:
            print(elem)
            elem.state_working_schedual = False
            if elem.working_schedule_ids:
                for ele in elem.working_schedule_ids:

                    check_for_appointment = self.env['appointment.info'].search_count([('start', '>=', ele.working_date),
                                                                                       ('stop', '<=', ele.working_date)])
                    if check_for_appointment >= 1:
                        ele.state = 'not_available'
                    else:
                        ele.state = 'available'

    def get_doctor_working_schedual_wizard_view(self):
        return {
            'name': 'Create Order OffCycle',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'doctor.schedule.wizard',
            'target': 'new',
            'context': {'default_doctor_id': self.id}
        }


class DoctorWorkingSchedule(models.Model):
    _name = "doctor.working.schedule"

    doctor_id = fields.Many2one('doctor.info')
    name = fields.Char(compute='_get_name', string="Appointment", store=True)

    state = fields.Selection([
        ('available', 'available'),
        ('not_available', ' Not Available')], string='Reservation', default='available')

    # state = fields.Selection([
    #     ('available', 'متاح'),
    #     ('not_available', 'غير متاح')], string='الحجز', default='available')

    dayofweek = fields.Selection([
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday')
    ], 'Week Day', required=True)
    working_date = fields.Date(string='Date')
    hour_from = fields.Float(string='Time From', required=True)
    hour_to = fields.Float(string='Time To', required=True)

    @api.depends('hour_from','hour_to')
    def _get_name(self):
        for elem in self:
            elem.name = ''
            if elem.hour_from and elem.hour_to:
                hour_from = '{0:02.0f}:{1:02.0f}'.format(*divmod(elem.hour_from * 60, 60))
                hour_to = '{0:02.0f}:{1:02.0f}'.format(*divmod(elem.hour_to * 60, 60))
                elem.name= str(hour_to)+'From'+'TO '+str(hour_from)

