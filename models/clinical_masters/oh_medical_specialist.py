# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OhMedicalSpecialist(models.Model):
    """Modelo para Especialistas Médicos"""
    _name = 'oh.medical.specialist'
    _description = 'Especialistas Médicos'
    _order = 'user_id'

    user_id = fields.Many2one(
        'res.users',
        string='Usuario',
        required=True,
        help='Vínculo al usuario de Odoo. Permite la autenticación, acceso y firma de documentos digitales'
    )
    specialty_ids = fields.One2many(
        'oh.medical.specialist.line',
        'specialist_id',
        string='Especialidades',
        help='Contenedor de todas las especialidades y sus registros asociados'
    )
    principal_specialty_id = fields.Many2one(
        'oh.specialty',
        string='Especialidad Principal',
        compute='_compute_principal_specialty',
        store=False,
        help='Especialidad principal del especialista (donde is_principal=True)'
    )
    principal_reg = fields.Char(
        string='Registro Principal',
        compute='_compute_principal_reg',
        store=False,
        help='Registro Profesional de la especialidad marcada como principal'
    )
    is_active = fields.Boolean(
        string='Activo',
        default=True,
        help='Estado de disponibilidad del especialista'
    )

    _sql_constraints = [
        ('user_unique', 'unique(user_id)',
         'Un usuario solo puede tener un registro de especialista médico.'),
    ]

    @api.depends('specialty_ids.is_principal', 'specialty_ids.specialty_id')
    def _compute_principal_specialty(self):
        """Calcula la especialidad principal"""
        for record in self:
            principal_lines = record.specialty_ids.filtered(lambda line: line.is_principal)
            if principal_lines:
                # Tomar la primera especialidad principal (debería haber solo una)
                record.principal_specialty_id = principal_lines[0].specialty_id
            else:
                record.principal_specialty_id = False

    @api.depends('specialty_ids.is_principal', 'specialty_ids.professional_reg')
    def _compute_principal_reg(self):
        """Calcula el registro profesional de la especialidad principal"""
        for record in self:
            principal_lines = record.specialty_ids.filtered(lambda line: line.is_principal)
            if principal_lines:
                # Tomar el registro de la primera especialidad principal
                record.principal_reg = principal_lines[0].professional_reg
            else:
                record.principal_reg = False

    def name_get(self):
        """Personaliza la visualización del nombre del especialista"""
        result = []
        for record in self:
            name = record.user_id.name or 'Sin Usuario'
            if record.principal_specialty_id:
                name += f" - {record.principal_specialty_id.name}"
            if record.principal_reg:
                name += f" ({record.principal_reg})"
            result.append((record.id, name))
        return result

