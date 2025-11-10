{
    'name': 'Gestión de Salud Ocupacional',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Sistema de Gestión de Salud y Seguridad en el Trabajo (SST)',
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
        * product (Productos)
        * uom (Unidades de Medida)
    """,
    'author': 'Ricardo Marín',
    'icon': '/ohs_management/static/description/icon.png',
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
        'stock',
        'product',
        'uom',
    ],
    'data': [
        # Security files
        'security/ir.model.access.csv',
        
        # Default data - Occupational Masters
        'data/occupational_masters/oh_relocation_result_data.xml',
        'data/occupational_masters/oh_limitation_data.xml',
        'data/occupational_masters/oh_aptitude_recommendation_data.xml',
        'data/occupational_masters/oh_rest_origin_data.xml',
        
        # Default data - Medicines
        'data/medicines/oh_medicine_via_data.xml',
        'data/medicines/oh_medicine_therapeutic_category_data.xml',
        'data/medicines/oh_medicine_presentation_data.xml',
        'data/medicines/oh_medicine_brand_data.xml',
        'data/medicines/oh_medicine_master_data.xml',
        'data/medicines/oh_dose_frequency_data.xml',
        'data/medicines/oh_treatment_duration_data.xml',
        
        # Default data - Clinical Masters
        'data/clinical_masters/oh_partner_ivss_data.xml',
        'data/clinical_masters/oh_partner_insurance_data.xml',
        'data/clinical_masters/oh_diagnosis_category_data.xml',
        'data/clinical_masters/oh_diagnosis_data.xml',
        'data/clinical_masters/oh_specialty_data.xml',
        
        # Menu Configuration
        'views/menu_configuration_view.xml',
        
        # Occupational Masters Views
        'views/occupational_masters/oh_relocation_result_view.xml',
        'views/occupational_masters/oh_limitation_view.xml',
        'views/occupational_masters/oh_aptitude_recommendation_view.xml',
        'views/occupational_masters/oh_origin_view.xml',
        
        # Medicines Views
        'views/medicines/oh_product_extension_view.xml',
        'views/medicines/oh_medicine_via_view.xml',
        'views/medicines/oh_dose_frequency_view.xml',
        'views/medicines/oh_treatment_duration_view.xml',
        'views/medicines/oh_medicine_presentation_view.xml',
        'views/medicines/oh_medicine_therapeutic_category_view.xml',
        'views/medicines/oh_medicine_brand_view.xml',
        'views/medicines/oh_medicine_master_view.xml',
        
        # Clinical Masters Views
        'views/clinical_masters/oh_partner_ivss_view.xml',
        'views/clinical_masters/oh_partner_insurance_view.xml',
        'views/clinical_masters/oh_exam_view.xml',
        'views/clinical_masters/oh_diagnosis_category_view.xml',
        'views/clinical_masters/oh_diagnosis_view.xml',
        'views/clinical_masters/oh_specialty_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

