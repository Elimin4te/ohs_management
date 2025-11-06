{
    'name': 'OHS Management',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Occupational Health and Safety (SST) Management System',
    'description': """
        Sistema de Gestión de Salud y Seguridad en el Trabajo (SST)
        ===========================================================
        
        Este módulo proporciona una solución MVP para la gestión de Salud Ocupacional.
        Integra con módulos nativos de Odoo para:
        
        * Gestión de registros médicos de empleados
        * Certificados de aptitud laboral
        * Evaluaciones médicas pre-empleo
        * Control de inventario farmacéutico por sucursal
        
        Módulos requeridos:
        * hr (Gestión de Recursos Humanos)
        * hr_recruitment (Reclutamiento)
        * stock (Inventario)
    """,
    'author': 'Ricardo Marín',
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
        'stock',
    ],
    'data': [
        # Security files will be added here
        # 'security/ir.model.access.csv',
        
        # Views will be added here
        # 'views/ohs_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

