# -*- coding: utf-8 -*-
#################################################################################
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
#################################################################################
{
  "name"                 :  "Website Quotation Images",
  "summary"              :  """Website Quotation Images permits you to add product images in the sales order and product quotation according to your need. Also, the sent invoice has the product images in the sales order or quotation. Apart from that, the customer preview also shows the product images. The Odoo admin can choose to show Odoo Website Quotation Images according to their requirement.""",
  "category"             :  "Website",
  "version"              :  "1.0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-Website-Quotation-Images.html",
  "description"          :  """Website Quotation Images authorizes the Odoo admin to show product images on the order quotations or sales orders in Odoo with just a click.
                              website quotation images
                              Odoo website quotation images
                               quotations images
                               quotation images
                               website product images
                               product images
                               show images in odoo quotation
                               show images in odoo sales orders
                               images in sales order
                               images in order quotation
  """,
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=website_quote_image",
  "depends"              :  [
                             'sale_management',
                             'website_sale',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'views/website_quotation.xml',
                             'views/sale_order_view.xml',
                             'report/sale_report.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  25,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}
