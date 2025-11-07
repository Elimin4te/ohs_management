# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhLimitation(models.Model):
    """Modelo para Limitaciones Ocupacionales"""
    _name = 'oh.limitation'
    _description = 'Limitaciones Ocupacionales'
    _order = 'name'

    name = fields.Char(
        string='Restricción',
        required=True,
        help='Restricción breve de la limitación (Ej: No realizar movimientos repetitivos)'
    )
    description = fields.Text(
        string='Descripción',
        required=True,
        help='Detalle de la limitación: justificación y criterios de aplicación'
    )
    is_critical = fields.Boolean(
        string='Es Crítica',
        default=False,
        help='Indica si la limitación es de alto riesgo y requiere seguimiento prioritario'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la limitación ocupacional'
    )

