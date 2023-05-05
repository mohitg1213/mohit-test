# -*- coding: utf-8 -*-
###############################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
###############################################################################
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    wk_image_small = fields.Binary(
        related='product_id.image_128',
        string="Product Image")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    wk_show_image = fields.Boolean(string='Show Image on Report')


class SaleOrderOption(models.Model):
    _inherit = "sale.order.option"

    wk_image_small = fields.Binary(
        related='product_id.image_128',
        string="Product Image")
