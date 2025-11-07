# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhExam(models.Model):
    """Modelo para Exámenes Médicos"""
    _name = 'oh.exam'
    _description = 'Exámenes Médicos'
    _order = 'exam_type, name'

    name = fields.Char(
        string='Nombre del Examen',
        required=True,
        help='Nombre del examen médico (Ej: Audiometría, Rayos X Tórax)'
    )
    code = fields.Char(
        string='Código',
        help='Código interno del examen (Ej: AUDI01)'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle del examen o requisitos previos'
    )
    exam_type = fields.Selection(
        [
            ('lab', 'Laboratorio'),
            ('image', 'Imagenología'),
            ('functional', 'Funcional'),
            ('other', 'Otros'),
        ],
        string='Tipo de Examen',
        required=True,
        help='Clasificación del examen médico'
    )
    is_pre_employment = fields.Boolean(
        string='Pre-Ingreso',
        default=False,
        help='Marca si es un examen requerido en el protocolo de Pre-Ingreso'
    )
    estimated_cost = fields.Monetary(
        string='Costo Estimado',
        currency_field='currency_id',
        help='Costo referencial para presupuestos o seguimiento administrativo'
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        default=lambda self: self.env.company.currency_id,
        required=True,
        help='Moneda para el costo estimado'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad del examen'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)',
         'El código del examen debe ser único.'),
    ]

