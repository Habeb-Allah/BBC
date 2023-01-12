# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # # employee_id = fields.Many2one('hr.employee', string="Requester", default=lambda self: self.env.user.employee_id.id,
    #                               readonly=True)
    patient_id = fields.Many2one('patient.info', string='Patient', required=True)
    appointment_id = fields.Many2one('appointment.info', domain="[('patient_id', '=', patient_id)]")
    doctor_id = fields.Many2one('doctor.info', related='appointment_id.doctor_id', string='Doctor Responsible')

    sessions_ids = fields.One2many('sessions.info', inverse_name='sale_order_id', string='Sessions')
    count_sessions = fields.Integer(string='Sessions', compute='_compute_sessions')

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        if self.patient_id and self.patient_id.partner_id:
            self.partner_id = self.patient_id.partner_id.id

    @api.depends('sessions_ids')
    def _compute_sessions(self):
        for rec in self:
            rec.count_sessions = 0
            if rec.sessions_ids:
                rec.count_sessions = len(rec.sessions_ids)

    def action_view_sessions(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("cubes_beauty_center.sessions_info_act_window")
        action['context'] = {
            'default_patient_id': self.patient_id.id,
            'default_appointment_id': self.appointment_id.id,
            'default_sale_order_id': self.id,
            'default_doctor_id': self.doctor_id.id,
        }
        action['domain'] = [('sale_order_id', '=', self.id)]

        return action
