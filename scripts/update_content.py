import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import SiteSettings, Category, Page

def update_content():
    print("Updating GWZ content to Traditional Chinese...")
    
    # 1. Update Categories (Translate to Chinese)
    category_map = {
        "featured": "精選",
        "blog": "最新消息",  # Mapped to Latest News
        "recipes": "食譜",
        "food-review": "食評",
        "lifestyle": "生活風格",
        "products": "產品",
    }
    
    for slug, name in category_map.items():
        cat, created = Category.objects.get_or_create(slug=slug)
        cat.name = name
        cat.save()
        print(f"Category updated: {slug} -> {name}")

    # 2. Create About Us Page
    about_page, created = Page.objects.get_or_create(slug='about-us')
    about_page.title = "關於我們"
    about_page.content = """
    <h2>關於 GWZ</h2>
    <p>GWZ 致力於為您帶來最優質的烹飪體驗。</p>
    <p>George 的烹飪旅程充滿了對美食的熱情與探索。我們不僅提供食譜，更分享一種生活態度。</p>
    """
    about_page.is_active = True
    about_page.save()
    print("Page 'About Us' created/updated.")

    # 3. Update Site Settings (Optional, mainly for backup)
    site_settings, created = SiteSettings.objects.get_or_create(id=1)
    site_settings.site_name = "GWZ"
    site_settings.save()
    print("Site Settings updated.")

if __name__ == "__main__":
    update_content()
