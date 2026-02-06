
import os
import sys
import django

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from django.conf import settings
from store.models import SiteSettings

def replace_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
            return True
    except Exception as e:
        print(f"Error reading/writing {file_path}: {e}")
    return False

def main():
    # 1. Update SiteSettings in Database
    try:
        site_settings = SiteSettings.objects.first()
        if site_settings:
            changed = False
            if "PrintSmart" in site_settings.site_name:
                site_settings.site_name = site_settings.site_name.replace("PrintSmart", "GWZ")
                changed = True
            if "PrintSmart" in site_settings.footer_copyright:
                site_settings.footer_copyright = site_settings.footer_copyright.replace("PrintSmart.hk", "GWZ").replace("PrintSmart", "GWZ")
                changed = True
            
            # Also ensure logo is None if it was pointing to something old, but we already handled that in settings.py
            # But SiteSettings model has a logo field too.
            # If site_settings.logo is set, it overrides the default in base.html logic?
            # Let's check base.html logic:
            # {% if site_settings.logo %} ... {% else %} ... {% endif %}
            # So if site_settings.logo is set to something wrong, it will show.
            # But the user said "Upload logo black-512".
            # The user might have uploaded it via admin panel to SiteSettings?
            # If so, it should be fine.
            # But if the initial data had a "PrintSmart" logo path...
            # I'll just clear the logo field in SiteSettings if it looks like a default/placeholder, 
            # OR better, leave it alone if I can't verify.
            # But I should definitely fix the text fields.
            
            if changed:
                site_settings.save()
                print("Updated SiteSettings in database.")
            else:
                print("SiteSettings in database already clean or not found.")
        else:
            # Create default if not exists
            SiteSettings.objects.create(
                site_name="GWZ",
                footer_copyright="Copyright © 2026 GWZ"
            )
            print("Created new SiteSettings.")

    except Exception as e:
        print(f"Error updating database: {e}")

    # 2. Update Templates
    base_dir = settings.BASE_DIR
    templates_dir = os.path.join(base_dir, 'templates')
    
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, "PrintSmart.hk", "GWZ")
                replace_in_file(file_path, "PrintSmart", "GWZ")

    print("Branding update complete.")

if __name__ == '__main__':
    main()
