#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt

# LIMPIA el build.sh para que solo contenga los comandos SEGUROS

# 1. Comando de creación del GYM (¡Asegúrate de que esta línea esté puesta ANTES de migrate!)
python manage.py shell -c "from django.contrib.auth import get_user_model; from gyms.models import Gym; User = get_user_model(); owner = User.objects.get(email='owner@gimnasio.com'); Gym.objects.filter(name='Gimnasio Principal').exists() or Gym.objects.create(name='Gimnasio Principal', owner=owner)"

python manage.py collectstatic --no-input
python manage.py migrate