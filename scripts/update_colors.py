import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import SiteSettings

def update_colors():
    print("Updating GWZ colors...")
    
    # Update Site Settings
    site_settings, created = SiteSettings.objects.get_or_create(id=1)
    
    # New Colors
    # Rich Purple: #5D2E86
    # Bright Yellow: #FFD700
    
    site_settings.top_bar_bg_color = "#5D2E86"
    site_settings.navbar_bg_color = "#5D2E86"
    site_settings.product_label_bg_color = "#FFD700"
    site_settings.product_label_text_color = "#000000"
    
    site_settings.save()
    print(f"Site Settings updated with new colors: Purple(#5D2E86) and Yellow(#FFD700)")

if __name__ == "__main__":
    update_colors()
