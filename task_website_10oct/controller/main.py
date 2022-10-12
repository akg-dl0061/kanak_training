# -*- coding: utf-8 -*-

from odoo import api, models
from odoo import http
from odoo.http import request


class ShowResult(http.Controller):

    @http.route('/show-result', type='json', auth='public', website=True)
    def all_product(self, button_id):
        values = {}
        product_data = request.env['product.template'].sudo().search([])
        customer_data = request.env['res.partner'].sudo().search([])
        if button_id == 'show_product_btn':
            values["data"] = request.env['ir.ui.view']._render_template('task_website_10oct.all_record',{'data_list':product_data})
        else:
            values["data"] = request.env['ir.ui.view']._render_template('task_website_10oct.all_record',{'data_list':customer_data})   
        return values