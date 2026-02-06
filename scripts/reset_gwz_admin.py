
import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from django.contrib.auth.models import User
from axes.models import AccessAttempt, AccessLog

def reset_gwz_admin():
    new_username = 'gwzadmin'
    old_username = 'admin'
    password = 'gwzadmin123'
    
    try:
        # 1. Clear Axes Lockouts (IP bans/attempts)
        count_attempts = AccessAttempt.objects.all().count()
        AccessAttempt.objects.all().delete()
        # AccessLog.objects.all().delete() # Optional: keep logs for history, but attempts cause lockouts
        print(f"Cleared {count_attempts} failed login attempts/lockouts.")

        # 2. Rename or Create User
        if User.objects.filter(username=old_username).exists():
            user = User.objects.get(username=old_username)
            user.username = new_username
            user.set_password(password)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print(f"Successfully renamed user '{old_username}' to '{new_username}' and reset password.")
        
        elif User.objects.filter(username=new_username).exists():
            user = User.objects.get(username=new_username)
            user.set_password(password)
            user.is_active = True
            user.save()
            print(f"User '{new_username}' already exists. Password reset successfully.")
            
        else:
            User.objects.create_superuser(new_username, 'admin@gwz.one', password)
            print(f"Created new superuser '{new_username}'.")
            
        print(f"\nLogin Details:\nUsername: {new_username}\nPassword: {password}")
        
    except Exception as e:
        print(f"Error during reset: {e}")

if __name__ == '__main__':
    reset_gwz_admin()
