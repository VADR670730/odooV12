# -*- coding: utf-8 -*-

from odoo import models, fields, api



class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'
    number_of_packs = fields.Integer('Nombre de packs')
