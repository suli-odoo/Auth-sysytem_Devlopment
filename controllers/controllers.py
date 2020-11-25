# -*- coding: utf-8 -*-
from odoo import http

# class Auth(http.Controller):
#     @http.route('/auth/auth/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auth/auth/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auth.listing', {
#             'root': '/auth/auth',
#             'objects': http.request.env['auth.auth'].search([]),
#         })

#     @http.route('/auth/auth/objects/<model("auth.auth"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auth.object', {
#             'object': obj
#         })