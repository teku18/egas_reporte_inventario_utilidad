# -*- coding: utf-8 -*-
from odoo import api, fields, models
import datetime

class tipo_cambio(models.Model):
    _name='tipo.cambio'

    name=fields.Float(string='Tipo Cambio', required=True)
    fecha_cambio=fields.Date(string='Fecha', required=True, default=datetime.datetime.now())

tipo_cambio()