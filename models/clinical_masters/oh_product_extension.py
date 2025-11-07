# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    """Extensión del modelo product.template para gestión de medicinas"""
    _inherit = 'product.template'

    oh_is_medicine = fields.Boolean(
        string='Es Medicina',
        default=False,
        help='Marcador para identificar productos farmacéuticos'
    )
    oh_via_ids = fields.Many2many(
        'oh.medicine.via',
        'product_medicine_via_rel',
        'product_id',
        'via_id',
        string='Vías de Administración',
        help='Vías de administración disponibles para esta medicina'
    )

