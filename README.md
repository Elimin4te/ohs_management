# Módulo de Gestión de Salud y Seguridad en el Trabajo (SST)

## Descripción

Este módulo proporciona una solución MVP (Producto Mínimo Viable) para la gestión de Salud Ocupacional y Seguridad en el Trabajo (SST) en Odoo v17. El módulo está diseñado para integrarse con los módulos nativos de Odoo como `hr`, `hr_recruitment` e `inventory` (stock), proporcionando funcionalidades esenciales para la gestión de la salud ocupacional en las organizaciones.

## Funcionalidades Principales

### 1. Gestión de Registros Médicos de Empleados
- Registro y seguimiento de historiales médicos de empleados
- Integración con el módulo `hr` para acceso directo desde los registros de empleados
- Almacenamiento seguro de información médica sensible

### 2. Certificados de Aptitud Laboral
- Gestión de certificados médicos de aptitud para el trabajo
- Control de fechas de vencimiento y renovaciones
- Alertas y notificaciones para certificados próximos a vencer

### 3. Evaluaciones Médicas Pre-Empleo
- Integración con el módulo `hr_recruitment` para procesos de selección
- Registro de evaluaciones médicas realizadas a candidatos
- Gestión del flujo de aprobación/rechazo basado en resultados médicos

### 4. Control de Inventario Farmacéutico por Sucursal
- Extensión del módulo de inventario (`stock`) para gestión de medicamentos
- Control de stock farmacéutico por sucursal/ubicación de la empresa
- Trazabilidad de medicamentos y suministros médicos

## Dependencias

Este módulo requiere los siguientes módulos de Odoo:
- `base` (Core de Odoo)
- `hr` (Gestión de Recursos Humanos)
- `hr_recruitment` (Reclutamiento)
- `stock` (Gestión de Inventario)

## Instalación

1. Copiar el directorio `ohs_management` a la carpeta de módulos de Odoo (por ejemplo, `addons`)
2. Actualizar la lista de aplicaciones en Odoo
3. Instalar el módulo "OHS Management" desde el menú de Aplicaciones

## Versión

- **Versión**: 17.0.1.0.0
- **Compatibilidad**: Odoo v17.0

## Licencia

Este módulo está bajo la licencia LGPL-3.

## Estado del Proyecto

Este módulo se encuentra en desarrollo activo. Las funcionalidades descritas se implementarán en fases sucesivas.

## Notas para Desarrolladores

Este módulo está diseñado para ser extensible y personalizable según las necesidades específicas de cada organización. Se recomienda revisar los modelos y vistas antes de realizar personalizaciones.

