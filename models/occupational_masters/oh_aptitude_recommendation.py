# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhAptitudeRecommendation(models.Model):
    """Modelo para Recomendaciones de Aptitud"""
    _name = 'oh.aptitude.recommendation'
    _description = 'Recomendaciones de Aptitud'
    _order = 'evaluation_type, name'

    name = fields.Char(
        string='Recomendación',
        required=True,
        help='Recomendación de aptitud (Ej: Revisión en 3 Meses, Referir a Traumatología)'
    )
    evaluation_type = fields.Selection(
        [
            ('pre_employment', 'Pre-Empleo'),
            ('periodic', 'Periódica'),
            ('post_vacation', 'Post-Vacaciones'),
            ('reintegration', 'Reintegración'),
        ],
        string='Tipo de Evaluación',
        required=True,
        help='Tipo de evaluación médica a la que aplica la recomendación'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle o justificación para la aplicación de la recomendación'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la recomendación de aptitud'
    )

