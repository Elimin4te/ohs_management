# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhRelocationResult(models.Model):
    """Modelo para Resultados de Reubicación Laboral"""
    _name = 'oh.relocation.result'
    _description = 'Resultados de Reubicación Laboral'
    _order = 'code, name'

    name = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre del resultado de reubicación (Ej: Temporal, Permanente)'
    )
    code = fields.Char(
        string='Código',
        required=True,
        help='Código corto del resultado (Ej: TEMP, PERM)'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle o justificación del resultado de reubicación'
    )
    is_permanent = fields.Boolean(
        string='Es Permanente',
        default=False,
        help='Indica si el cambio de reubicación es permanente'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad del resultado de reubicación'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)',
         'El código del resultado de reubicación debe ser único.'),
    ]

