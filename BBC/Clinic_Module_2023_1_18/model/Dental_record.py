from odoo import tools, api, fields, models
#from datetime import datetime
#from odoo.exceptions import ValidationError


class DoctorCard(models.Model):
    _name = "dental.record"
    patient_id = fields.Many2one('patient.info', string="patient", required=True)
    last_vist_date = fields.Date(string="Last Vist Date")
    chief_complaint = fields.Selection([('Pain', 'Pain'),('Swelling','Swelling'),('Caries', 'Caries'),('Esthetice', 'Esthetice'),('Routine_Visit', 'Routine Visit'),], string="Chief Complaint")
    check1 = fields.Boolean(string="Others")
    Other = fields.Text(string="Chief Complaint Comments")
    medical_history = fields.Selection([('Allergies', 'Allergies'),('Rheumatic_fever','Rheumatic Fever'),('Familial', 'Familial'),('Cardiac_Disease', 'Cardiac Disease'),('Asthma', 'Asthma'), ('Common_childhood_Disease', 'Common Childhood Disease'),('Kidney_Disease', 'Kidney Disease'),('Blood_Dysrasias', 'Blood Dysrasias'),('Diabetes', 'Diabetes'),], string="Medical History")
    check2 = fields.Boolean(string="Others")
    Other_2 = fields.Text(string="Medical History Comments")
    previous_dental_histo = fields.Selection([('Extraction', 'Extraction'),('Periodontal','Periodontal'),('Drug_sensitivity', 'Drug sensitivity'),('Flouride_Therapy', 'Flouride Therapy'),('Pulp_Therapy', 'Pulp Therapy'),  ], string="Previous Dental History")
    check3 = fields.Boolean(string="Others")
    Other_3 = fields.Text(string="Previous Dental Comments")
    x_RAY = fields.Binary(string="X_RAY")
    comment_x_RAY = fields.Text(string="X_RAY Comments")
    provisional_dlagnosis = fields.Text(string="Provisional Diagnosis")
    investigations = fields.Text(string="Investigations")
    dlagnosis = fields.Text(string="Diagnosis")
    treatmentplan = fields.Text(string="Treatment Plan")
    procedure = fields.Text(string="Procedure")
    next_applointment = fields.Datetime(string="Next Appointment")
    comments = fields.Text(string="Comments")










   # @api.model
#     def check_availability_state(self):
#         for elem in self:
#             print
#             elem.state_working_schedual = False
#             if elem.working_schedule_ids:
#                 for ele in elem.working_schedule_ids:
#
#                     check_for_appointment = self.env['appointment.info'].search_count([('start', '>=', ele.working_date),
#                                                                                        ('stop', '<=', ele.working_date)])
#                     if check_for_appointment >= 1:
#                         ele.state = 'not_available'
#                     else:
#                         ele.state = 'available'
#
#     def get_doctor_working_schedual_wizard_view(self):
#         return {
#             'name': 'Create Order OffCycle',
#             'type': 'ir.actions.act_window',
#             'view_type': 'form',
#             'view_mode': 'form',
#             'res_model': 'doctor.schedule.wizard',
#             'target': 'new',
#             'context': {'default_doctor_id': self.id}
#         }
#
#
# class DoctorWorkingSchedule(models.Model):
#     _name = "doctor.working.schedule"
#
#     doctor_id = fields.Many2one('doctor.info')
#     name = fields.Char(compute='_get_name', string='الدوام', store=True)
#
#     state = fields.Selection([
#         ('available', 'متاح'),
#         ('not_available', 'غير متاح')], string='الحجز', default='available')
#
#     # state = fields.Selection([
#     #     ('available', 'متاح'),
#     #     ('not_available', 'غير متاح')], string='الحجز', default='available')
#
#     dayofweek = fields.Selection([
#         ('0', 'الاثنين'),
#         ('1', 'الثلثاء'),
#         ('2', 'الاربعاء'),
#         ('3', 'الخميس'),
#         ('4', 'الجمعة'),
#         ('5', 'السبت'),
#         ('6', 'الأحد')
#     ], 'يوم الاسبوع', required=True)
#     working_date = fields.Date(string='التاريخ')
#     hour_from = fields.Float(string='الساعة من', required=True)
#     hour_to = fields.Float(string='الساعة الى', required=True)
#
#     @api.depends('hour_from','hour_to')
#     def _get_name(self):
#         for elem in self:
#             elem.name = ''
#             if elem.hour_from and elem.hour_to:
#                 hour_from = '{0:02.0f}:{1:02.0f}'.format(*divmod(elem.hour_from * 60, 60))
#                 hour_to = '{0:02.0f}:{1:02.0f}'.format(*divmod(elem.hour_to * 60, 60))
#                 elem.name= str(hour_to)+'دوام من '+'الى '+str(hour_from)
#
