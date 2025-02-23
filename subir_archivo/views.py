from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Document  # Importa el modelo
from django.core.validators import validate_email, ValidationError

def uploadFile(request):
    validation_results = []  # Almacenará los resultados de la validación
    documents = Document.objects.all()  # Obtener todos los archivos subidos

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if not file.name.endswith('.txt'):
                validation_results.append("Error: El archivo debe ser un TXT.")
            else:
                # Leer el archivo TXT
                decoded_file = file.read().decode('utf-8').splitlines()
                
                # Validar cada fila
                for row_number, line in enumerate(decoded_file, start=1):
                    row = line.strip().split(',')  # Dividir por comas
                    if len(row) != 5:
                        validation_results.append(f"Error en fila {row_number}: El archivo debe tener exactamente 5 columnas.")
                        continue
                    
                    # Validar columna 1: Números enteros entre 3 y 10 caracteres
                    if not row[0].isdigit() or len(row[0]) <= 3 or len(row[0]) > 10:
                        validation_results.append(f"Error en fila {row_number}, columna 1: Debe ser un número entero entre 3 y 10 caracteres.")
                    
                    # Validar columna 2: Correo electrónico
                    try:
                        validate_email(row[1])
                    except ValidationError:
                        validation_results.append(f"Error en fila {row_number}, columna 2: Correo electrónico no válido.")
                    
                    # Validar columna 3: Solo "CC" o "TI"
                    if row[2] not in ["CC", "TI"]:
                        validation_results.append(f"Error en fila {row_number}, columna 3: Solo se permiten los valores 'CC' o 'TI'.")
                    
                    # Validar columna 4: Números entre 500000 y 1500000
                    try:
                        value = int(row[3])
                        if value <= 100000 or value >= 1500000:
                            validation_results.append(f"Error en fila {row_number}, columna 4: El valor debe estar entre 500000 y 1500000.")
                    except ValueError:
                        validation_results.append(f"Error en fila {row_number}, columna 4: Debe ser un número entero.")
                
                # Si no hay errores de validación, guardar el archivo en la base de datos
                if not validation_results:
                    document = Document(uploadedFile=file)
                    document.save()
                    validation_results.append(f"¡Archivo '{file.name}' subido y validado correctamente!")
    else:
        form = UploadFileForm()
    
    return render(request, "subir_archivo/upload-file.html", {
        "form": form,
        "validation_results": validation_results,
        "documents": documents,  # Pasar los archivos subidos a la plantilla
    })