import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin'
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}'...")
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created. Password: '{password}'")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == "__main__":
    create_admin()
