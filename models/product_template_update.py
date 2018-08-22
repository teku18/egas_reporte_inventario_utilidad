from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit='product.template'

    standard_price = fields.Float(
        'Cost', compute='_compute_standard_price', store=True,
        inverse='_set_standard_price', search='_search_standard_price',
        digits=dp.get_precision('Product Price'), groups="base.group_user",
        help="Cost used for stock valuation in standard price and as a first price to set in average/fifo. "
             "Also used as a base price for pricelists. "
             "Expressed in the default unit of measure of the product. ")
