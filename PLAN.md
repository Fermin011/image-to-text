# OCR Images to PDF - Plan de Desarrollo

## Descripción
Aplicación de escritorio (PyQt6) que convierte imágenes (1-500) en un PDF
con texto seleccionable/copiable usando OCR.

## Stack Tecnológico
- **GUI**: PyQt6
- **OCR**: pytesseract + Tesseract OCR
- **PDF**: reportlab + PyPDF2
- **Imágenes**: Pillow
- **Arquitectura**: MVC

## Estructura del Proyecto
```
OCR-IMAGENES PDF/
├── main.py                  # Entry point
├── requirements.txt
├── PLAN.md
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── ocr_engine.py   # Lógica OCR con pytesseract
│   │   └── pdf_builder.py  # Generación del PDF final
│   ├── views/
│   │   ├── __init__.py
│   │   ├── main_window.py  # Ventana principal
│   │   ├── image_list.py   # Widget lista de imágenes
│   │   └── styles.py       # QSS y paleta de colores
│   └── controllers/
│       ├── __init__.py
│       └── app_controller.py  # Coordinación vista-modelo
```

## Paleta de Colores
- Fondo principal: #1a1025 (violeta muy oscuro)
- Fondo secundario: #2d1b4e (violeta oscuro)
- Acento primario: #f5c518 (amarillo)
- Acento secundario: #d4a017 (amarillo oscuro)
- Texto principal: #e8e0f0 (lavanda claro)
- Texto secundario: #9b8fb0 (gris violeta)
- Bordes: #3d2a5c (violeta medio)

## Etapas y Commits

### Etapa 1 - Scaffolding
**Commit**: "init: estructura base del proyecto"
- Crear estructura de carpetas
- requirements.txt con dependencias
- main.py vacío con entry point
- __init__.py en todos los paquetes

### Etapa 2 - Vista: Ventana base con tema
**Commit**: "feat: ventana principal con tema violeta-amarillo"
- main_window.py con layout base
- styles.py con QSS completo
- Ventana con título, tamaño mínimo, tema aplicado

### Etapa 3 - Vista: Zona de carga y lista de imágenes
**Commit**: "feat: zona de carga drag-and-drop y lista de imagenes"
- Botón para cargar imágenes (file dialog)
- Drag and drop de archivos
- Lista visual de imágenes cargadas con nombre y tamaño
- Botones para eliminar/reordenar imágenes

### Etapa 4 - Vista: Controles de acción y barra de progreso
**Commit**: "feat: barra de progreso y controles de exportacion"
- Botón "Convertir a PDF"
- Barra de progreso con porcentaje
- Selector de idioma OCR (español/inglés)
- Estado de la operación (label)

### Etapa 5 - Modelo: Motor OCR
**Commit**: "feat: motor OCR con pytesseract"
- ocr_engine.py con clase OcrEngine
- Procesamiento de imagen individual
- Soporte multi-idioma
- Worker thread para no bloquear UI

### Etapa 6 - Modelo: Generador de PDF
**Commit**: "feat: generador de PDF con texto seleccionable"
- pdf_builder.py con clase PdfBuilder
- Crear PDF searchable (imagen + capa de texto invisible)
- Merge de múltiples páginas en un solo PDF

### Etapa 7 - Controlador: Carga de imágenes
**Commit**: "feat: controlador de carga y gestion de imagenes"
- app_controller.py conectando vista con modelo
- Validación de archivos (formatos, cantidad)
- Gestión del estado de la lista de imágenes

### Etapa 8 - Controlador: Procesamiento y exportación
**Commit**: "feat: flujo completo de conversion OCR a PDF"
- Proceso batch de imágenes
- Actualización de progreso en tiempo real
- Diálogo de guardado del PDF resultante
- Manejo de errores durante conversión

### Etapa 9 - Pulido final
**Commit**: "fix: ajustes finales y validaciones"
- Validación de Tesseract instalado
- Mensajes de error amigables
- Deshabilitar controles durante procesamiento
- Pruebas de flujo completo

## Dependencias (requirements.txt)
```
PyQt6>=6.5
Pillow>=10.0
pytesseract>=0.3.10
reportlab>=4.0
PyPDF2>=3.0
```

## Requisito Externo
- Tesseract OCR debe estar instalado en el sistema
- Windows: https://github.com/UB-Mannheim/tesseract/wiki
- Paquetes de idioma: eng + spa
