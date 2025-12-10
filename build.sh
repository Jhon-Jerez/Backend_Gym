#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt # Primero, instala TODO.

python manage.py migrate core

# 2. Luego aplica todas las demás migraciones, usando --fake-initial para evitar que Django
# entre en conflicto con las dependencias de 'auth'.
python manage.py migrate --fake-initial