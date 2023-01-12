from odoo import tools, api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


class DoctorScheduleWizard(models.TransientModel):
    _name = "doctor.schedule.wizard"

    doctor_id = fields.Many2one('doctor.info')

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date End", required=True)

    working_schedual_line_ids = fields.One2many('doctor.schedule.line.wizard', 'doctor_schedual_id')

    def create_working_schedual(self):
        if self.date_from and self.date_to and self.working_schedual_line_ids:
            start = self.date_from
            end = self.date_to
            while start <= end:
                for elem in self.working_schedual_line_ids:
                    if str(elem.dayofweek) == str(start.weekday()):
                        check_if_there_is_schedual = self.env['doctor.working.schedule'].search([('doctor_id', '=', self.doctor_id.id), ('working_date', '=', start)])
                        if check_if_there_is_schedual:
                            raise ValidationError(' Already Exit Table Attendances')
                        else:
                            self.env['doctor.working.schedule'].create({
                                'doctor_id':self.doctor_id.id,
                                'dayofweek':elem.dayofweek,
                                'working_date':start,
                                'hour_from':elem.hour_from,
                                'hour_to':elem.hour_to
                            })
                start = start + timedelta(days=1)


class DoctorScheduleLine(models.TransientModel):
    _name = "doctor.schedule.line.wizard"

    doctor_schedual_id = fields.Many2one('doctor.schedule.wizard')
    dayofweek = fields.Selection([
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday')
    ], 'Week Day', required=True)
    hour_from = fields.Float(string='Time From', required=True)
    hour_to = fields.Float(string='Time To', required=True)