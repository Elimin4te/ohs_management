# Módulo de Gestión de Salud y Seguridad en el Trabajo (SST)

## Descripción

Este módulo proporciona una solución MVP (Producto Mínimo Viable) para la gestión de Salud Ocupacional y Seguridad en el Trabajo (SST) en Odoo v17. El módulo está diseñado para integrarse con los módulos nativos de Odoo como `hr`, `hr_recruitment` e `inventory` (stock), proporcionando funcionalidades esenciales para la gestión de la salud ocupacional en las organizaciones.

## Estado del Proyecto

**Versión**: 17.0.1.0.0  
**Compatibilidad**: Odoo v17.0  
**Licencia**: LGPL-3

Este módulo se encuentra en **desarrollo activo**. Actualmente se ha implementado la capa de **maestros de datos** (master data) que sirve como base para las funcionalidades operativas que se desarrollarán en fases posteriores.

## Funcionalidades Implementadas

### Maestros de Datos (Master Data)

El módulo incluye tres categorías principales de maestros de datos que proporcionan la base para la gestión de salud ocupacional:

#### 1. Maestros Ocupacionales

Gestión de datos maestros relacionados con evaluaciones médicas ocupacionales y recomendaciones laborales:

- **Recomendaciones de Aptitud** (`oh.aptitude.recommendation`)
  - Recomendaciones médicas para evaluaciones (Pre-Empleo, Periódica, Post-Vacaciones, Reintegración)
  - Descripción y justificación de cada recomendación
  - Control de estado activo/inactivo

- **Limitaciones Ocupacionales** (`oh.limitation`)
  - Restricciones laborales que pueden aplicarse a empleados
  - Clasificación de limitaciones críticas
  - Descripción detallada de cada limitación

- **Resultados de Reubicación** (`oh.relocation.result`)
  - Catálogo de posibles resultados en procesos de reubicación laboral

- **Origen de Descanso** (`oh.origin`)
  - Clasificación del origen de períodos de descanso médico

#### 2. Maestros Clínicos

Gestión de información médica y clínica:

- **Especialidades Médicas** (`oh.specialty`)
  - Catálogo de especialidades médicas disponibles

- **Especialistas Médicos** (`oh.medical.specialist`)
  - Registro de médicos especialistas vinculados a usuarios de Odoo
  - Gestión de múltiples especialidades por especialista
  - Registro de especialidad principal y número de colegiatura
  - Integración con sistema de usuarios para autenticación y firma digital

- **Líneas de Especialista** (`oh.medical.specialist.line`)
  - Detalle de especialidades y registros profesionales por especialista

- **Diagnósticos (CIE-11)** (`oh.diagnosis`)
  - Catálogo de diagnósticos basado en la Clasificación Internacional de Enfermedades versión 11
  - Códigos CIE-11 únicos
  - Marcador de diagnósticos notificables (vigilancia epidemiológica)
  - Clasificación por categorías funcionales

- **Categorías de Diagnóstico** (`oh.diagnosis.category`)
  - Clasificación funcional de diagnósticos para agrupación y reportes

- **Exámenes Médicos** (`oh.exam`)
  - Catálogo de exámenes médicos (Laboratorio, Imagenología, Funcional, Otros)
  - Códigos internos únicos
  - Marcador para exámenes requeridos en protocolo de Pre-Ingreso
  - Costo estimado para presupuestos

- **Centros IVSS** (`oh.partner.ivss`)
  - Catálogo de centros del Instituto Venezolano de los Seguros Sociales

- **Aseguradoras** (`oh.partner.insurance`)
  - Catálogo de compañías de seguros médicos

#### 3. Maestros de Medicinas

Gestión de información farmacéutica y medicamentos:

- **Maestro Conceptual de Medicina** (`oh.medicine.master`)
  - Sustancias activas (principios activos)
  - Agrupación de productos farmacéuticos por sustancia activa
  - Clasificación por categoría terapéutica

- **Categorías Terapéuticas** (`oh.medicine.therapeutic.category`)
  - Clasificación terapéutica de medicamentos

- **Presentaciones de Medicina** (`oh.medicine.presentation`)
  - Formatos físicos de medicamentos (Ej: Ampolla, Tableta, Jarabe)

- **Marcas de Medicina** (`oh.medicine.brand`)
  - Marcas comerciales de productos farmacéuticos

- **Vías de Administración** (`oh.medicine.via`)
  - Rutas de administración de medicamentos (Oral, Intramuscular, etc.)

- **Frecuencias de Dosis** (`oh.dose.frequency`)
  - Maestro de frecuencias de administración (Ej: "Cada 8 Horas")
  - Factor de dosis por día para cálculos automáticos

- **Duración de Tratamiento** (`oh.treatment.duration`)
  - Períodos estándar de tratamiento médico

- **Extensión de Productos** (`product.template` extendido)
  - Extensión del modelo de productos de Odoo para medicamentos
  - Marcador `oh_is_medicine` para identificar productos farmacéuticos
  - Vinculación con sustancia activa, presentación, marca y vías de administración
  - Integración con el módulo de inventario (`stock`) de Odoo

## Dependencias

Este módulo requiere los siguientes módulos de Odoo:

- `base` - Core de Odoo (obligatorio)
- `hr` - Gestión de Recursos Humanos
- `hr_recruitment` - Reclutamiento y selección de personal
- `stock` - Gestión de Inventario
- `product` - Gestión de Productos
- `uom` - Unidades de Medida

## Estructura del Proyecto

```
ohs_management/
├── __init__.py                 # Inicialización del módulo
├── __manifest__.py             # Manifesto del módulo (metadatos)
├── LICENSE                     # Licencia LGPL-3
├── README.md                   # Este archivo
│
├── models/                     # Modelos de datos
│   ├── __init__.py
│   ├── clinical_masters/       # Maestros clínicos
│   │   ├── oh_diagnosis_category.py
│   │   ├── oh_diagnosis.py
│   │   ├── oh_exam.py
│   │   ├── oh_medical_specialist.py
│   │   ├── oh_medical_specialist_line.py
│   │   └── oh_specialty.py
│   ├── medicines/              # Maestros de medicinas
│   │   ├── oh_dose_frequency.py
│   │   ├── oh_medicine_brand.py
│   │   ├── oh_medicine_master.py
│   │   ├── oh_medicine_presentation.py
│   │   ├── oh_medicine_therapeutic_category.py
│   │   ├── oh_medicine_via.py
│   │   ├── oh_product_extension.py
│   │   └── oh_treatment_duration.py
│   └── occupational_masters/   # Maestros ocupacionales
│       ├── oh_aptitude_recommendation.py
│       ├── oh_limitation.py
│       ├── oh_origin.py
│       └── oh_relocation_result.py
│
├── views/                      # Vistas XML de Odoo
│   ├── menu_configuration_view.xml
│   ├── clinical_masters/
│   ├── medicines/
│   └── occupational_masters/
│
├── data/                       # Datos por defecto (XML)
│   ├── clinical_masters/
│   ├── medicines/
│   └── occupational_masters/
│
├── security/                   # Configuración de seguridad
│   └── ir.model.access.csv     # Permisos de acceso
│
└── static/                     # Archivos estáticos
    └── description/
        └── icon.png            # Icono del módulo
```

## Instalación

### Requisitos Previos

- Odoo v17.0 instalado y configurado
- Python 3.10 o superior
- Acceso a la carpeta de módulos de Odoo

### Pasos de Instalación

1. **Copiar el módulo**
   ```bash
   # Copiar el directorio ohs_management a la carpeta de módulos de Odoo
   # Por ejemplo: /path/to/odoo/addons/ohs_management
   ```

2. **Actualizar la lista de aplicaciones**
   - Iniciar sesión en Odoo como administrador
   - Ir a **Aplicaciones** → **Actualizar lista de aplicaciones**

3. **Instalar el módulo**
   - Buscar "Gestión de Salud Ocupacional" o "OHS Management"
   - Hacer clic en **Instalar**

4. **Verificar la instalación**
   - El menú "Salud Ocupacional" debería aparecer en el menú principal
   - Verificar que los maestros de datos se hayan cargado correctamente

## Modo de Desarrollo

### Configuración del Entorno

Este módulo está diseñado para desarrollarse en un entorno Odoo estándar. Para desarrollo local:

1. **Entorno Virtual (Recomendado)**
   ```bash
   # Crear entorno virtual (si no existe)
   python -m venv venv
   
   # Activar entorno virtual
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

2. **Configuración de Odoo**
   - Configurar el archivo `odoo.conf` para apuntar a la carpeta de módulos
   - Asegurar que el módulo esté en la ruta de búsqueda de módulos

3. **Modo Desarrollo en Odoo**
   - Activar el **Modo Desarrollador** en Odoo:
     - Ir a **Configuración** → **Activar modo desarrollador**
   - Esto permite:
     - Recargar módulos sin reiniciar el servidor
     - Ver registros técnicos
     - Acceder a vistas de desarrollo

### Actualización de Módulo Durante Desarrollo

```bash
# Opción 1: Desde la interfaz de Odoo
# Aplicaciones → Buscar módulo → Actualizar

# Opción 2: Desde línea de comandos (si se usa odoo-bin)
odoo-bin -u ohs_management -d nombre_base_datos
```

### Estructura de Datos por Defecto

El módulo incluye datos maestros predefinidos en formato XML ubicados en la carpeta `data/`:

- **Datos Ocupacionales**: Recomendaciones, limitaciones, resultados de reubicación, orígenes
- **Datos Clínicos**: Especialidades, diagnósticos CIE-11, categorías, centros IVSS, aseguradoras
- **Datos de Medicinas**: Sustancias activas, presentaciones, marcas, vías de administración, frecuencias, duraciones

Estos datos se cargan automáticamente durante la instalación del módulo.

### Convenciones de Código

- **Nomenclatura de Modelos**: Prefijo `oh.` (Occupational Health)
- **Nomenclatura de Campos**: Prefijo `oh_` para campos personalizados en modelos heredados
- **Ordenamiento**: Los modelos incluyen `_order` para definir orden por defecto
- **Validaciones**: Uso de `_sql_constraints` para validaciones a nivel de base de datos
- **Campos Computados**: Uso de `@api.depends` y métodos `_compute_*` para campos calculados

### Próximas Funcionalidades (En Desarrollo)

Según los comentarios en el código, las siguientes funcionalidades están planificadas:

- `ohs_employee` - Gestión de registros médicos de empleados
- `ohs_certification` - Certificados de aptitud laboral
- `ohs_pharmacy` - Control de inventario farmacéutico por sucursal

## Notas para Desarrolladores

### Extensibilidad

Este módulo está diseñado para ser extensible y personalizable según las necesidades específicas de cada organización. Se recomienda:

1. **Revisar los modelos** antes de realizar personalizaciones
2. **Mantener la nomenclatura** al crear nuevos modelos relacionados
3. **Respetar las relaciones** entre maestros al agregar nuevos campos
4. **Documentar cambios** en modelos personalizados

### Integración con Otros Módulos

El módulo está preparado para integrarse con:

- **Módulo HR**: Para vinculación con empleados
- **Módulo HR Recruitment**: Para evaluaciones pre-empleo
- **Módulo Stock**: Para gestión de inventario farmacéutico
- **Módulo Product**: Para extensión de productos farmacéuticos

### Seguridad

Los permisos de acceso están definidos en `security/ir.model.access.csv`. Asegúrese de revisar y ajustar los permisos según las políticas de seguridad de su organización.

## Autores

- **Ricardo Marín**

## Licencia

Este módulo está bajo la licencia **LGPL-3**.

---

**Nota**: Este módulo está en desarrollo activo. Las funcionalidades operativas (gestión de empleados, certificados, etc.) se implementarán en fases posteriores sobre la base de los maestros de datos actuales.
