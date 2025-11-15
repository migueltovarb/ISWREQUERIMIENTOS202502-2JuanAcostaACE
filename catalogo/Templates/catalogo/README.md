# Catálogo de Autos - Juan Acosta

**Entrega final - ISW 2025-02**  
**Profesor:** Miguel Tobar

## Descripción
Catálogo de autos con Django (CRUD completo)

## Funcionalidades
- Listado público con imágenes
- Panel admin
- 5 autos de ejemplo

## Cómo ejecutar
```bash
cd Django_prueba
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # admin / 123
python manage.py runserver