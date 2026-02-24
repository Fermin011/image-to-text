# OCR Images to PDF

Aplicacion de escritorio que convierte imagenes en un archivo PDF con texto seleccionable y copiable.
Utiliza reconocimiento optico de caracteres (OCR) para extraer el texto de las imagenes y genera un PDF
donde cada pagina conserva la imagen original con una capa de texto invisible por encima, permitiendo
buscar, seleccionar y copiar el contenido.

Soporta entre 1 y 500 imagenes por conversion, con procesamiento en segundo plano y barra de progreso
en tiempo real.

---

## Requisitos previos

### Python 3.10+

Descargar desde [python.org](https://www.python.org/downloads/).
Durante la instalacion marcar la opcion **"Add Python to PATH"**.

### Tesseract OCR

El motor de reconocimiento de texto debe estar instalado por separado.

1. Descargar el instalador desde [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Ejecutar el instalador y en la seccion **"Choose Components"** marcar los paquetes de idioma:
   - `Spanish` (obligatorio si se quiere OCR en espanol)
   - `English` (viene marcado por defecto)
3. Instalar en la ruta por defecto: `C:\Program Files\Tesseract-OCR\`

> Si se instala en otra ruta, la aplicacion buscara automaticamente en las ubicaciones comunes de Windows.
> En caso de que no lo detecte, se mostrara un mensaje de advertencia al abrir el programa.

---

## Instalacion

### 1. Clonar el repositorio

```bash
git clone https://github.com/Fermin011/image-to-text.git
cd image-to-text
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows (CMD):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Uso

Con el entorno virtual activado:

```bash
python main.py
```

### Flujo de trabajo

1. **Cargar imagenes**: Arrastrar archivos a la zona de carga o usar el boton "Seleccionar archivos"
2. **Ordenar**: Usar los botones "Subir" y "Bajar" para reordenar las imagenes
3. **Seleccionar idiomas**: Marcar Espanol, Ingles o ambos segun el contenido de las imagenes
4. **Convertir**: Presionar "Convertir a PDF" y elegir donde guardar el archivo
5. **Resultado**: Se genera un PDF con todas las imagenes en orden, con texto seleccionable

### Formatos de imagen soportados

- PNG
- JPG / JPEG
- BMP
- TIFF / TIF
- WEBP

---

## Estructura del proyecto

```
image-to-text/
├── main.py                      # Punto de entrada
├── requirements.txt             # Dependencias Python
├── src/
│   ├── controllers/
│   │   └── app_controller.py    # Logica de coordinacion entre vista y modelo
│   ├── models/
│   │   ├── ocr_engine.py        # Motor OCR con pytesseract (worker thread)
│   │   └── pdf_builder.py       # Generacion y merge de paginas PDF
│   └── views/
│       ├── main_window.py       # Ventana principal
│       ├── image_list.py        # Widget de carga y lista de imagenes
│       └── styles.py            # Tema visual (QSS)
```

La aplicacion sigue el patron **MVC** (Modelo-Vista-Controlador):

- **Modelo**: `ocr_engine.py` ejecuta el OCR en un hilo separado. `pdf_builder.py` ensambla el PDF final.
- **Vista**: `main_window.py` y `image_list.py` definen la interfaz. `styles.py` contiene el tema visual.
- **Controlador**: `app_controller.py` conecta la vista con los modelos y gestiona el flujo de la aplicacion.

---

## Dependencias

| Paquete | Uso |
|---|---|
| PyQt6 | Interfaz grafica |
| Pillow | Carga y manipulacion de imagenes |
| pytesseract | Wrapper de Tesseract OCR para Python |
| reportlab | Generacion de documentos PDF |
| PyPDF2 | Merge de multiples paginas PDF |

---

## Solucion de problemas

**"Tesseract OCR no detectado"**
Verificar que Tesseract esta instalado en `C:\Program Files\Tesseract-OCR\` y que el ejecutable
`tesseract.exe` existe en esa carpeta.

**Error con idioma `spa.traineddata`**
El paquete de idioma espanol no fue instalado con Tesseract. Se puede descargar manualmente desde
[tessdata](https://github.com/tesseract-ocr/tessdata) y copiar el archivo `spa.traineddata` a la
carpeta `C:\Program Files\Tesseract-OCR\tessdata\`.

**La barra de progreso no avanza**
El OCR puede tardar varios segundos por imagen dependiendo del tamano y la complejidad.
Con 500 imagenes el proceso puede llevar varios minutos.
