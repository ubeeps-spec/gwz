import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import SiteSettings, Category, Product, HeroSlide
from django.core.files import File

def setup_gwz():
    print("Setting up GWZ...")

    # 1. Update Site Settings
    settings, created = SiteSettings.objects.get_or_create(id=1)
    settings.site_name = "GWZ"
    settings.navbar_items = "Featured, Blog, Recipes, Products, Lifestyle, About"
    
    # Colors
    settings.top_bar_bg_color = "#2E1A47" # Purple
    settings.navbar_bg_color = "#2E1A47"  # Purple
    settings.navbar_text_color = "#ffffff"
    settings.product_label_bg_color = "#F4D03F" # Yellow
    settings.product_label_text_color = "#2E1A47" # Purple Text on Yellow

    # Footer
    settings.footer_about = "Beyond cooking, we invite you to see the world through George’s eyes as he shares his experience in travel, shopping and different cultures."
    settings.footer_copyright = "Copyright © 2026 GWZ. All rights reserved."
    
    settings.save()
    print("Site Settings Updated.")

    # 2. Create Categories
    categories = ["Sauces", "Recipes", "Lifestyle", "Featured"]
    cat_objs = {}
    for cat_name in categories:
        cat, created = Category.objects.get_or_create(name=cat_name, defaults={'slug': cat_name.lower()})
        cat_objs[cat_name] = cat
        print(f"Category '{cat_name}' created/found.")

    # 3. Create Sample Products
    # Product 1: GWZ Signature Sauce
    p1, created = Product.objects.get_or_create(
        name="GWZ Signature Sauce",
        defaults={
            'sku': 'GWZ-SAUCE-001',
            'price': 128.00,
            'description': "To help you elevate your culinary skills, George has also designed a range of sauces that will spice up your home cooked dishes. GWZ sauces also make great presents during festive seasons.",
            'stock': 100,
            'is_active': True
        }
    )
    if created:
        p1.categories.add(cat_objs['Sauces'], cat_objs['Featured'])
        print("Product 'GWZ Signature Sauce' created.")
    
    # Product 2: Premium Soy Sauce
    p2, created = Product.objects.get_or_create(
        name="GWZ Premium Soy Sauce",
        defaults={
            'sku': 'GWZ-SOY-002',
            'price': 88.00,
            'description': "Traditional recipe with a modern twist. Perfect for everyday cooking.",
            'stock': 100,
            'is_active': True
        }
    )
    if created:
        p2.categories.add(cat_objs['Sauces'])
        print("Product 'GWZ Premium Soy Sauce' created.")

    # 4. Create Hero Slide
    # Note: We don't have images yet, but we can set text.
    HeroSlide.objects.all().delete() # Clear existing
    HeroSlide.objects.create(
        title="Become a home cook with George",
        subtitle="Join George on his culinary journey and enjoy the finer things in life!",
        button_text="Explore Recipes",
        link="/products",
        sort_order=1,
        is_active=True
    )
    print("Hero Slide created.")

if __name__ == '__main__':
    setup_gwz()
