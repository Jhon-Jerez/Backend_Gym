#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt

# 3. CREAR OBJETO GYM Y ASIGNAR EL OWNER
python manage.py shell -c "from django.contrib.auth import get_user_model; from gyms.models import Gym; User = get_user_model(); owner = User.objects.get(email='owner@gimnasio.com'); Gym.objects.filter(name='SpartanosGym').exists() or Gym.objects.create(name='SpartanosGym', owner=owner)"

python manage.py collectstatic --no-input
python manage.py migrate