# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder_update(models.Model):
    _inherit="sale.order"

    tipo_cambio = fields.Float(string='Tipo de Cambio')
    x_studio_field_L75tD = fields.Integer(string='Petrolera')

SaleOrder_update()