# create_admin.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Change these to your desired superuser credentials
USERNAME = 'ramelams'
EMAIL = 'ramelams07@gmail.com'
PASSWORD = 'ramelams'

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created!")
else:
    print("Superuser already exists.")
