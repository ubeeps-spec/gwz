
import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from django.contrib.auth.models import User

try:
    if User.objects.filter(username='admin').exists():
        user = User.objects.get(username='admin')
        user.set_password('admin123')
        user.save()
        print("Superuser 'admin' password reset to 'admin123'.")
    else:
        User.objects.create_superuser('admin', 'admin@gwz.one', 'admin123')
        print("Superuser 'admin' created with password 'admin123'.")
except Exception as e:
    print(f"Error: {e}")
