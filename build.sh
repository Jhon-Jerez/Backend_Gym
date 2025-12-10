#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt

# 1. CREAR SUPERUSUARIO (Para acceder al /admin/)
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@gimnasio.com').exists() or User.objects.create_superuser(username='superadmin', email='admin@gimnasio.com', password='Jhon_Doe_123')"

# 2. CREAR USUARIO OWNER (Para el primer Gimnasio)
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='owner@gimnasio.com').exists() or User.objects.create_user(username='owner1', email='owner@gimnasio.com', password='Owner_Pass_123', is_staff=True)"

python manage.py collectstatic --no-input
python manage.py migrate