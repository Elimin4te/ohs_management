# -*- coding: utf-8 -*-

from odoo import models, fields


class OhDiagnosisCategory(models.Model):
    """Modelo para Clasificación Funcional de Diagnóstico (CIE-11)"""
    _name = 'oh.diagnosis.category'
    _description = 'Clasificación de Diagnóstico (CIE-11)'
    _order = 'name'

    name = fields.Char(
        string='Categoría',
        required=True,
        help='Nombre de la categoría funcional de diagnóstico (Ej: Enfermedades del Sistema Circulatorio)'
    )
    description = fields.Text(
        string='Descripción',
        help='Breve descripción de los diagnósticos que agrupa esta categoría'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la categoría'
    )
    diagnosis_ids = fields.One2many(
        'oh.diagnosis',
        'category_id',
        string='Diagnósticos',
        help='Diagnósticos asociados a esta categoría'
    )
    diagnosis_count = fields.Integer(
        string='Número de Diagnósticos',
        compute='_compute_diagnosis_count',
        store=False
    )

    def _compute_diagnosis_count(self):
        """Calcula el número de diagnósticos en cada categoría"""
        for record in self:
            record.diagnosis_count = len(record.diagnosis_ids)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'La categoría de diagnóstico debe ser única.'),
    ]

