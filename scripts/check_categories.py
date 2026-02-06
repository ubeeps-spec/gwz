
import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import Category, Product
from django.db.models import Count, Q

print("Checking Categories...")
categories = Category.objects.all()
print(f"Total Categories: {categories.count()}")

for cat in categories:
    product_count = Product.objects.filter(categories=cat, is_active=True).count()
    print(f"Category: {cat.name}, Active Products: {product_count}")

print("\nChecking View Logic Query...")
view_categories = Category.objects.annotate(
    count=Count('products', filter=Q(products__is_active=True))
).filter(count__gt=0).order_by('name')

print(f"Categories returned by view query: {view_categories.count()}")
for cat in view_categories:
    print(f" - {cat.name} ({cat.count})")
