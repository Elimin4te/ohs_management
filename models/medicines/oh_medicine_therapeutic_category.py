# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhMedicineTherapeuticCategory(models.Model):
    """Modelo para Categorías Terapéuticas de Medicinas"""
    _name = 'oh.medicine.therapeutic.category'
    _description = 'Categoría Terapéutica'
    _order = 'name'

    name = fields.Char(
        string='Categoría Terapéutica',
        required=True,
        help='Nombre de la categoría terapéutica (Ej: Analgésico/Antipirético, AINE)'
    )
    description = fields.Text(
        string='Descripción',
        help='Descripción detallada de la categoría terapéutica'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad de la categoría terapéutica'
    )

