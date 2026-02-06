import os
import django
import sys
from django.core.files import File
from django.conf import settings

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import SiteSettings, Category, Product, HeroSlide

def import_content():
    print("Importing GWZ content...")
    
    # 1. Update Site Settings
    site_settings, created = SiteSettings.objects.get_or_create(id=1)
    site_settings.site_name = "GWZ"
    site_settings.hero_title = "Become a home cook with George"
    site_settings.hero_subtitle = "Join George on his culinary journey and enjoy the finer things in life!"
    site_settings.hero_button_text = "Explore Recipes"
    site_settings.hero_link = "/shop/"
    site_settings.footer_about = "Beyond cooking, we invite you to see the world through George’s eyes as he shares his experience in travel, shopping and different cultures."
    site_settings.navbar_items = "Featured, Blog, Recipes, Products, Lifestyle, About"
    
    # Colors (Ensure they are set)
    site_settings.top_bar_bg_color = "#5D2E86"
    site_settings.navbar_bg_color = "#5D2E86"
    site_settings.product_label_bg_color = "#FFD700"
    site_settings.product_label_text_color = "#000000"
    
    site_settings.save()
    print("Site Settings updated.")

    # 2. Create Categories
    categories = [
        ("Featured", "featured"),
        ("Blog", "blog"),
        ("Recipes", "recipes"),
        ("Food Review", "food-review"),
        ("Lifestyle", "lifestyle"),
        ("Products", "products"),
    ]
    
    for name, slug in categories:
        cat, created = Category.objects.get_or_create(slug=slug, defaults={'name': name})
        if created:
            print(f"Category created: {name}")
        else:
            print(f"Category exists: {name}")

    # 3. Create/Update Hero Slide
    # Remove existing slides to avoid clutter or duplicates if running multiple times
    HeroSlide.objects.all().delete()
    
    HeroSlide.objects.create(
        title="Become a home cook with George",
        subtitle="Join George on his culinary journey and enjoy the finer things in life!",
        link="/shop/",
        sort_order=1
    )
    print("Hero Slide created.")
    
    # 4. Create Sample Products/Content
    # We use Product model to simulate content for now
    
    # Featured Blog Item
    cat_featured = Category.objects.get(slug="featured")
    Product.objects.get_or_create(
        name="George's Cooking Videos",
        defaults={
            'slug': 'georges-cooking-videos',
            'sku': 'BLOG-001',
            'price': 0,
            'description': "Get inspiration from George’s recipes and cooking videos.",
            'stock': 1,
            'is_active': True
        }
    )[0].categories.add(cat_featured)

    # Blog Item
    cat_blog = Category.objects.get(slug="blog")
    Product.objects.get_or_create(
        name="Secret Recipes",
        defaults={
            'slug': 'secret-recipes',
            'sku': 'BLOG-002',
            'price': 0,
            'description': "Follow George’s home cook journey and secret recipes.",
            'stock': 1,
            'is_active': True
        }
    )[0].categories.add(cat_blog)
    
    # Food Review
    cat_review = Category.objects.get(slug="food-review")
    Product.objects.get_or_create(
        name="Fine Dining Experience",
        defaults={
            'slug': 'fine-dining-experience',
            'sku': 'REVIEW-001',
            'price': 0,
            'description': "Like every other foodie, George loves to try new food and visit good restaurants. Join George as he experience a range of fine dining and local gems.",
            'stock': 1,
            'is_active': True
        }
    )[0].categories.add(cat_review)
    
    # Products (Sauces)
    cat_products = Category.objects.get(slug="products")
    Product.objects.get_or_create(
        name="GWZ Signature Sauce",
        defaults={
            'slug': 'gwz-signature-sauce',
            'sku': 'PROD-001',
            'price': 128.00,
            'description': "To help you elevate your culinary skills, George has also designed a range of sauces that will spice up your home cooked dishes. GWZ sauces also make great presents during festive seasons.",
            'stock': 100,
            'is_active': True
        }
    )[0].categories.add(cat_products)

    print("Sample content created.")

if __name__ == "__main__":
    import_content()
