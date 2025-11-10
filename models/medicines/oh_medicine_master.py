# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhMedicineMaster(models.Model):
    """Modelo para Maestro Conceptual de Medicina (Sustancias Activas)"""
    _name = 'oh.medicine.master'
    _description = 'Maestro Conceptual de Medicina'
    _order = 'name'

    name = fields.Char(
        string='Sustancia Activa',
        required=True,
        help='Nombre de la Sustancia Activa (Ej: Ketoprofeno)'
    )
    therapeutic_category_id = fields.Many2one(
        'oh.medicine.therapeutic.category',
        string='Categoría Terapéutica',
        help='Clasificación terapéutica del medicamento'
    )
    product_ids = fields.One2many(
        'product.template',
        'oh_master_medicine_id',
        string='Productos',
        help='Lista de todas las presentaciones/SKUs de producto vinculados'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la sustancia activa'
    )

