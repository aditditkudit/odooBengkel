# -*- coding: utf-8 -*-
from odoo import http

# class CbBengkel(http.Controller):
#     @http.route('/cb_bengkel/cb_bengkel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cb_bengkel/cb_bengkel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cb_bengkel.listing', {
#             'root': '/cb_bengkel/cb_bengkel',
#             'objects': http.request.env['cb_bengkel.cb_bengkel'].search([]),
#         })

#     @http.route('/cb_bengkel/cb_bengkel/objects/<model("cb_bengkel.cb_bengkel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cb_bengkel.object', {
#             'object': obj
#         })