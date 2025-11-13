# Guía de Contribución

## Estructura de Ramas

El desarrollo del proyecto se organiza en **tres ramas principales** que siguen un flujo de trabajo estructurado:

### 1. `dev` (Desarrollo)
- **Propósito**: Rama principal de desarrollo activo
- **Uso**: Aquí se realizan todas las nuevas funcionalidades, correcciones y mejoras
- **Estado**: Puede contener código en desarrollo que aún no está completamente probado
- **Flujo**: Los desarrolladores crean ramas feature desde `dev` y hacen merge de vuelta a `dev`

### 2. `qa` (Quality Assurance)
- **Propósito**: Rama de pruebas y control de calidad
- **Uso**: Código que ha pasado la revisión inicial y está listo para pruebas exhaustivas
- **Estado**: Debe ser estable y funcional, pero aún no está listo para producción
- **Flujo**: Se hace merge desde `dev` cuando una funcionalidad está completa y revisada

### 3. `main` (Producción)
- **Propósito**: Rama de producción estable
- **Uso**: Contiene únicamente código probado, estable y listo para uso en producción
- **Estado**: Debe ser siempre estable y funcional
- **Flujo**: Se hace merge desde `qa` después de que todas las pruebas han pasado exitosamente

## Flujo de Trabajo

```
[Feature Branch] → dev → qa → main
```

### Proceso de Desarrollo

1. **Crear una rama feature desde `dev`**
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/nombre-de-la-funcionalidad
   ```

2. **Desarrollar y hacer commit**
   ```bash
   # Realizar cambios
   git add .
   git commit -m "Descripción clara de los cambios"
   ```

3. **Hacer merge a `dev`**
   ```bash
   git checkout dev
   git merge feature/nombre-de-la-funcionalidad
   git push origin dev
   ```

4. **Promover a `qa`** (cuando la funcionalidad esté completa)
   ```bash
   git checkout qa
   git pull origin qa
   git merge dev
   git push origin qa
   ```

5. **Promover a `main`** (después de pruebas exitosas)
   ```bash
   git checkout main
   git pull origin main
   git merge qa
   git push origin main
   ```

## Convenciones de Código

### Nomenclatura

- **Modelos**: Prefijo `oh.` (ej: `oh.diagnosis`, `oh.medicine.master`)
- **Campos personalizados**: Prefijo `oh_` en modelos heredados (ej: `oh_is_medicine`)
- **Ramas**: 
  - `feature/nombre-descriptivo` para nuevas funcionalidades
  - `fix/nombre-descriptivo` para correcciones de bugs
  - `refactor/nombre-descriptivo` para refactorizaciones

### Estilo de Código

- Seguir las convenciones de Python (PEP 8)
- Usar docstrings en español para documentar modelos y métodos
- Mantener comentarios claros y descriptivos
- Usar nombres descriptivos para variables y funciones

### Commits

- Mensajes de commit claros y descriptivos en español
- Preferir commits atómicos (un cambio lógico por commit)
- Formato sugerido: `tipo(subtipo): Descripción breve`

Ejemplos:
- `feat(certificados): Agregar modelo de certificados de aptitud`
- `fix(diagnosticos): Corregir validación de código CIE-11`
- `refactor(maestro_clinico): Reorganizar estructura de maestros clínicos`
