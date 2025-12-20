import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') # Replace 'project' with your project folder name
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Get details from Environment Variables (set these in Render)
username = os.getenv("ADMIN_USERNAME", "ramelams")
email = os.getenv("ADMIN_EMAIL", "ramelams07@gmail.com")
password = os.getenv("ADMIN_PASSWORD", "ramelams")

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"Superuser {username} already exists.")