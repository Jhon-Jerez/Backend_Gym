#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt

# CREAR OBJETO GYM Y ASIGNAR EL OWNER (LÓGICA IF EXPLÍCITA)
python manage.py shell -c "from django.contrib.auth import get_user_model; from gyms.models import Gym; User = get_user_model(); owner = User.objects.get(email='owner@gimnasio.com'); if not Gym.objects.filter(owner=owner).exists(): Gym.objects.create(name='Gimnasio Principal', owner=owner)"

python manage.py collectstatic --no-input
python manage.py migrate