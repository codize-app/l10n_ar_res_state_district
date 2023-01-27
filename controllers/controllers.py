# -*- coding: utf-8 -*-
# from odoo import http


# class ResDistrict(http.Controller):
#     @http.route('/res_district/res_district/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_district/res_district/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_district.listing', {
#             'root': '/res_district/res_district',
#             'objects': http.request.env['res_district.res_district'].search([]),
#         })

#     @http.route('/res_district/res_district/objects/<model("res_district.res_district"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_district.object', {
#             'object': obj
#         })
