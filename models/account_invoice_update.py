# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoice_update(models.Model):
    _inherit="account.invoice"

    def _tipo_cambio(self):
        sql="""
                select id
                from tipo_cambio
                ORDER BY fecha_cambio DESC LIMIT 1
            """
        self.env.cr.execute(sql)
        consulta = self.env.cr.dictfetchone()
        try:
            aux=self.env['tipo.cambio'].search([('id','=',consulta['id'])])
        except:
            return
        return aux

    tipo_cambio_id = fields.Many2one('tipo.cambio','Tipo de Cambio', default=_tipo_cambio)
    # l10n_mx_edi_cfdi_uuid = fields.Char(string='Fiscal Folio', readonly=True, store=True,
    #                                     help='Folio in electronic invoice, is returned by SAT when send to stamp.',
    #                                     compute='_compute_cfdi_values')

AccountInvoice_update()
