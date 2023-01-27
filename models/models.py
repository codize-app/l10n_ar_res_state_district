# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResDistrict(models.Model):
    _name = 'res.state.district'

    name = fields.Char('Nombre')
    state_id = fields.Many2one('res.country.state', 'Provincia')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    district_id = fields.Many2one('res.state.district', 'Localidad')