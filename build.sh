#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt

# CREAR OBJETO GYM USANDO get_or_create()
python manage.py shell -c "from django.contrib.auth import get_user_model; from gyms.models import Gym; User = get_user_model(); owner = User.objects.get(email='owner@gimnasio.com'); Gym.objects.get_or_create(owner=owner, defaults={'name': 'SpartaGym', 'address': '123 Fitness St', 'city': 'Fitville', 'state': 'CA', 'zip_code': '90001'})"

python manage.py collectstatic --no-input
python manage.py migrate