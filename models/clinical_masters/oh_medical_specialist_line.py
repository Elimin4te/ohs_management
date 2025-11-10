# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OhMedicalSpecialistLine(models.Model):
    """Modelo para Líneas de Especialidades del Especialista Médico"""
    _name = 'oh.medical.specialist.line'
    _description = 'Línea de Especialidad del Especialista Médico'
    _order = 'is_principal desc, specialty_id'

    specialist_id = fields.Many2one(
        'oh.medical.specialist',
        string='Especialista',
        required=True,
        ondelete='cascade',
        help='Especialista médico al que pertenece esta especialidad'
    )
    specialty_id = fields.Many2one(
        'oh.specialty',
        string='Especialidad',
        required=True,
        help='Especialidad médica del especialista'
    )
    professional_reg = fields.Char(
        string='Registro Profesional',
        required=True,
        help='Número de Registro Profesional/Colegiatura para esta especialidad (Ej: Número del Colegio Médico)'
    )
    is_principal = fields.Boolean(
        string='Especialidad Principal',
        default=False,
        help='Indica si esta es la especialidad principal del especialista'
    )

    _sql_constraints = [
        ('specialist_specialty_unique', 'unique(specialist_id, specialty_id)',
         'Un especialista no puede tener la misma especialidad registrada más de una vez.'),
        ('professional_reg_unique', 'unique(professional_reg)',
         'El número de registro profesional debe ser único.'),
    ]

    @api.constrains('is_principal', 'specialist_id')
    def _check_principal_specialty(self):
        """Asegura que solo haya una especialidad principal por especialista"""
        for record in self:
            if record.is_principal:
                other_principals = self.search([
                    ('specialist_id', '=', record.specialist_id.id),
                    ('is_principal', '=', True),
                    ('id', '!=', record.id)
                ])
                if other_principals:
                    raise ValidationError(
                        'Solo puede haber una especialidad principal por especialista. '
                        'Desactive la otra especialidad principal antes de marcar esta como principal.'
                    )

