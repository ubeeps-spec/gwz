
import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import Category, Product
from django.db.models import Count, Q

print("--- DIAGNOSTIC SCRIPT START ---")

print("\n1. All Categories in DB:")
all_cats = Category.objects.all()
if not all_cats.exists():
    print("NO CATEGORIES FOUND!")
else:
    for c in all_cats:
        print(f" - ID: {c.id}, Name: {c.name}, Slug: {c.slug}")

print("\n2. All Products in DB:")
all_prods = Product.objects.all()
if not all_prods.exists():
    print("NO PRODUCTS FOUND!")
else:
    for p in all_prods:
        cats = ", ".join([c.name for c in p.categories.all()])
        print(f" - ID: {p.id}, Name: {p.name}, Active: {p.is_active}, Categories: [{cats}]")

print("\n3. View Query Simulation:")
view_categories = Category.objects.annotate(
    count=Count('products', filter=Q(products__is_active=True))
).filter(count__gt=0).order_by('name')

print(f"View Query Result Count: {view_categories.count()}")
for c in view_categories:
    print(f" - Name: {c.name}, Count: {c.count}")

print("\n--- DIAGNOSTIC SCRIPT END ---")
