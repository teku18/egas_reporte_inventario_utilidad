# -*- encoding: utf-8 -*-
###############################################################################
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 Egas - www.egas.com.mx
#    All Rights Reserved.
###############Credits######################################################
#    Coded by: Edgar Gustavo gustavo.hernandez@smartqs.com
#    Planified by: Edgar Gustavo
#    Finance by: Egas.
#    Audited by: Edgar Gustavo
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Egas Inventario Utilidad",

    'summary': """se realiza modificaciones al reporte de inventario""",

    'description': """
        se realiza modificaciones al reporte de inventario, y se crean metodos los cuales traen
        diccionarios, listas y listas con diccionarios, de igual manera se crea un nuevo grupo
        llamado 'Tipo de Cambio' los cuales solo los agregados a este podran interactuar con el
        modulo, esa configuracion se encuentra en security.
    """,

    'author': "Edgar Gustavo",
    'website': "http://www.egasPrueba.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product' ,'stock', 'sale'],

    # Poner los XML a cargar
    'data': [
        #'templates.xml',
        'views/tipo_cambio.xml',
        'views/account_invoice_views_update.xml',
        'report/report_stockpicking_operations_update.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'active':False,
    'installable': True,
    'application':True,
}