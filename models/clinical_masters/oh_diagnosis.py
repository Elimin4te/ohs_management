# -*- coding: utf-8 -*-

from odoo import models, fields


class OhDiagnosis(models.Model):
    """Modelo para Diagnósticos basado en CIE-11"""
    _name = 'oh.diagnosis'
    _description = 'Diagnósticos (CIE-11)'
    _order = 'code, name'

    name = fields.Char(
        string='Diagnóstico',
        required=True,
        help='Descripción/Nombre del diagnóstico según CIE-11'
    )
    code = fields.Char(
        string='Código CIE-11',
        required=True,
        help='Código CIE-11 del diagnóstico (Ej: BA00.0, 1B21.1)'
    )
    description = fields.Text(
        string='Descripción Completa',
        help='Detalle completo de la patología según CIE-11'
    )
    is_notifiable = fields.Boolean(
        string='Notificable',
        default=False,
        help='Indica si es un diagnóstico de declaración obligatoria para la Vigilancia Epidemiológica'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad del diagnóstico'
    )
    category_id = fields.Many2one(
        'oh.diagnosis.category',
        string='Clasificación',
        help='Clasificación funcional del diagnóstico según CIE-11 (permite agrupar para reportes)'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)',
         'El código CIE-11 del diagnóstico debe ser único.'),
    ]

