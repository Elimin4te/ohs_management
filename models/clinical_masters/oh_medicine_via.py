# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhMedicineVia(models.Model):
    """Modelo para Vías de Administración de Medicinas"""
    _name = 'oh.medicine.via'
    _description = 'Vías de Administración de Medicinas'
    _order = 'via_type, name'

    name = fields.Char(
        string='Vía de Administración',
        required=True,
        help='Nombre específico de la vía (Ej: Vía Oral (VO), Intravenosa (IV))'
    )
    via_type = fields.Selection(
        [
            ('enteral', 'Enteral'),
            ('parenteral', 'Parenteral'),
            ('topical', 'Tópica'),
        ],
        string='Tipo de Vía',
        required=True,
        help='Clasificación principal de la vía de administración'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle o justificación de la vía de administración'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la vía de administración'
    )

