# -*- coding: utf-8 -*-

from odoo import models, fields


class OhDoseFrequency(models.Model):
    """Modelo para Maestro de Frecuencias de Dosis"""
    _name = 'oh.dose.frequency'
    _description = 'Maestro de Frecuencias de Dosis'
    _order = 'factor_per_day desc, name'

    name = fields.Char(
        string='Frecuencia',
        required=True,
        help='Texto descriptivo de la frecuencia (Ej: "Cada 8 Horas")'
    )
    factor_per_day = fields.Integer(
        string='Dosis por Día',
        required=True,
        help='Número de dosis en un día (Ej: 3 para cada 8 horas)'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la frecuencia'
    )

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'La frecuencia de dosis debe ser única.'),
    ]

