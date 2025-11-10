# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhMedicineBrand(models.Model):
    """Modelo para Marcas de Medicinas"""
    _name = 'oh.medicine.brand'
    _description = 'Marca de Medicina'
    _order = 'name'

    name = fields.Char(
        string='Marca',
        required=True,
        help='Nombre de la marca comercial de la medicina (Ej: Tylenol, Advil)'
    )
    description = fields.Text(
        string='Descripción',
        help='Información adicional sobre la marca'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la marca'
    )

