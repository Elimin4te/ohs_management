# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhRestOrigin(models.Model):
    """Modelo para Origen/Causa de Reposo según Clasificación IVSS"""
    _name = 'oh.rest.origin'
    _description = 'Origen/Causa de Reposo (Clasificación IVSS)'
    _order = 'origin_type, name'

    name = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre de la causa de reposo (Ej: Accidente de Trabajo, Enfermedad Común)'
    )
    origin_type = fields.Selection(
        [
            ('common_illness', 'Enfermedad Común'),
            ('common_accident', 'Accidente Común'),
            ('professional_illness', 'Enfermedad Profesional'),
            ('work_accident', 'Accidente de Trabajo'),
            ('maternity', 'Maternidad'),
        ],
        string='Tipo de Origen',
        required=True,
        help='Clasificación principal según IVSS'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle o justificación para la clasificación del reposo'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad del origen/causa de reposo'
    )

