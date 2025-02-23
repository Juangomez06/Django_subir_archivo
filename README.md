# 📂 Subir y Validar Archivos TXT en Django  

Este proyecto es una aplicación web desarrollada en Django que permite a los usuarios subir archivos TXT, validar su contenido según reglas específicas y almacenarlos en la base de datos. Además, los usuarios pueden ver la lista de archivos subidos y descargarlos.  

## ✨ Características  

- 📤 **Subida de Archivos TXT**: Los usuarios pueden cargar archivos a través de un formulario web.  
- ✅ **Validación de Contenido**: El sistema valida el contenido de los archivos según reglas predefinidas.  
- 💾 **Almacenamiento en Base de Datos**: Los archivos válidos se guardan para su posterior consulta.  
- 📜 **Gestión de Archivos**: Los usuarios pueden ver la lista de archivos subidos y descargarlos.  

## 📋 Requisitos  

Asegúrate de contar con los siguientes requisitos antes de ejecutar el proyecto:  

- Python 3.8 o superior  
- Django 4.2 o superior  

## 🚀 Instalación y Configuración  

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.  

### 1️⃣ Clonar el Repositorio  

```bash
git clone https://github.com/Juangomez06/django_subir_archivo.git
cd django_subir_archivo_txt
```

### 2️⃣ Crear y Activar un Entorno Virtual  

#### En Windows:  

```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS/Linux:  

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependencias  

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar la Base de Datos  

Este proyecto usa SQLite por defecto. Si deseas usar otra base de datos, modifica la configuración en `settings.py`. Luego, aplica las migraciones:  

```bash
python manage.py migrate
```

### 5️⃣ Ejecutar el Servidor de Desarrollo  

```bash
python manage.py runserver
```

### 6️⃣ Acceder a la Aplicación  

Abre tu navegador y visita:  

🔗 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
