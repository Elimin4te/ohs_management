# -*- coding: utf-8 -*-

from odoo import models, fields


class OhTreatmentDuration(models.Model):
    """Modelo para Maestro de Duración de Tratamiento"""
    _name = 'oh.treatment.duration'
    _description = 'Maestro de Duración de Tratamiento'
    _order = 'number_of_days, name'

    name = fields.Char(
        string='Duración',
        required=True,
        help='Texto descriptivo de la duración (Ej: "7 Días")'
    )
    number_of_days = fields.Integer(
        string='Número de Días',
        required=True,
        help='Número de días del tratamiento (Ej: 7)'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la duración'
    )

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'La duración de tratamiento debe ser única.'),
    ]

