# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhMedicinePresentation(models.Model):
    """Modelo para Maestro de Presentaciones de Medicinas"""
    _name = 'oh.medicine.presentation'
    _description = 'Maestro de Presentaciones de Medicinas'
    _order = 'presentation_type, name'

    name = fields.Char(
        string='Presentación',
        required=True,
        help='Nombre de la Presentación (Ej: Comprimido, Ampolla, Vacuna)'
    )
    presentation_type = fields.Selection(
        [
            ('solid', 'Sólida'),
            ('liquid', 'Líquida'),
            ('gas', 'Gas'),
            ('biological', 'Biológica'),
            ('other', 'Otra'),
        ],
        string='Tipo de Presentación',
        required=True,
        help='Clasificación del formato físico de la presentación'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle del formato o su administración'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la presentación'
    )

