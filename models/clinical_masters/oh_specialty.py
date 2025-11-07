# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhSpecialty(models.Model):
    """Modelo para Especialidades Médicas"""
    _name = 'oh.specialty'
    _description = 'Especialidades Médicas'
    _order = 'is_occupational desc, name'

    name = fields.Char(
        string='Especialidad',
        required=True,
        help='Nombre de la especialidad médica (Ej: Medicina Ocupacional, Medicina General)'
    )
    is_occupational = fields.Boolean(
        string='Salud Ocupacional',
        default=False,
        help='Indica si la especialidad pertenece al área de Salud Ocupacional o SST'
    )
    description = fields.Text(
        string='Descripción',
        help='Detalle de la formación o alcance de la especialidad'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la especialidad'
    )

