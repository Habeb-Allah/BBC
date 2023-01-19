

from odoo import tools, api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


class AppointmentCard(models.Model):
    _name = "appointment.info"

    name = fields.Char(compute='_compute_name', string="Appointments",stored=True)
    doctor_id = fields.Many2one('doctor.info', string="Doctor Responsible" , required = True)
    patient_id = fields.Many2one('patient.info', string="Patient", required = True)
    appointment_info = fields.Text(string="Appointment Info")
    allday = fields.Boolean('All Day', default=False)
    start = fields.Datetime(
        'Start', required=True, tracking=True, default=fields.Date.today,
        help="Start date of an event, without time for full days events")
    stop = fields.Datetime(
        'Stop', required=True, tracking=True, default=lambda self: fields.Datetime.today() + timedelta(hours=1),
        compute='_compute_stop', readonly=False, store=True)
    display_time = fields.Char('Event Time', compute='_compute_display_time')
    start_date = fields.Date(
        'Start Date', store=True, tracking=True,
        compute='_compute_dates', inverse='_inverse_dates')
    stop_date = fields.Date(
        'End Date', store=True, tracking=True,
        compute='_compute_dates', inverse='_inverse_dates')
    duration = fields.Float('Duration (Hours)', compute='_compute_duration', store=True, readonly=False)

    @api.depends('allday', 'start', 'stop')
    def _compute_dates(self):
        for meeting in self:
            if meeting.allday and meeting.start and meeting.stop:
                meeting.start_date = meeting.start.date()
                meeting.stop_date = meeting.stop.date()
            else:
                meeting.start_date = False
                meeting.stop_date = False

    @api.depends('start', 'duration')
    def _compute_stop(self):
        duration_field = self._fields['duration']
        self.env.remove_to_compute(duration_field, self)
        for event in self:
            event.stop = event.start and event.start + timedelta(minutes=round((event.duration or 1.0) * 60))
            if event.allday:
                event.stop -= timedelta(seconds=1)

    def _get_duration(self, start, stop):
        if not start or not stop:
            return 0
        duration = (stop - start).total_seconds() / 3600
        return round(duration, 2)

    @api.depends('stop', 'start')
    def _compute_duration(self):
        for event in self:
            event.duration = self._get_duration(event.start, event.stop)

    def _inverse_dates(self):

        for meeting in self:
            if meeting.allday:
                enddate = fields.Datetime.from_string(meeting.stop_date)
                enddate = enddate.replace(hour=18)

                startdate = fields.Datetime.from_string(meeting.start_date)
                startdate = startdate.replace(hour=8)

                meeting.write({
                    'start': startdate.replace(tzinfo=None),
                    'stop': enddate.replace(tzinfo=None)
                })

    @api.depends('patient_id','start')
    def _compute_name(self):
        for elem in self:
            elem.name=False
            if elem.patient_id and elem.start:
                elem.name=str(elem.patient_id.name)+'-'+str(elem.start.strftime('%Y-%m-%d'))



    @api.constrains('start', 'stop')
    def _check_date(self):
        for rec in self:
            item_ids = self.env['appointment.info'].sudo().search([('start', '<=', rec.stop), ('stop', '>=', rec.start),('id', '<>', rec.id)])
            start_dates = [x.start for x in item_ids]
            stop_dates = [x.stop for x in item_ids]

            res = "\n\n".join("{} - {}".format(x+timedelta(hours=3), y+timedelta(hours=3)) for x, y in zip(start_dates, stop_dates))

            if item_ids:

                raise ValidationError("Timeslot includes another appointment, please try another timeslot.\n\nYou can "
                                      "pick any time slot not in: \n\n %s" % res)

