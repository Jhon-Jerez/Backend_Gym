#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt # Primero, instala TODO.

python manage.py collectstatic --no-input # Luego, recoge estáticos.
python manage.py migrate # Finalmente, migra la base de datos.