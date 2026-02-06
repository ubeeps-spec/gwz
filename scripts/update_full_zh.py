import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import SiteSettings, HeroSlide

def update_full_zh():
    print("Updating GWZ Hero Slides and Settings to Chinese...")
    
    # 1. Update Site Settings
    site_settings, created = SiteSettings.objects.get_or_create(id=1)
    site_settings.hero_title = "成爲像 George 一樣的家庭厨師"
    site_settings.hero_subtitle = "加入王子的美食之旅，享受生活中的美好事物！"
    site_settings.hero_button_text = "探索食譜"
    site_settings.footer_about = "除了烹飪，我們邀請您通過 George 的眼睛看世界，分享他在旅行、購物和不同文化中的體驗。"
    site_settings.save()
    print("Site Settings updated to Chinese.")
    
    # 2. Update Hero Slides
    HeroSlide.objects.all().delete()
    
    HeroSlide.objects.create(
        title="成爲像 George 一樣的家庭厨師",
        subtitle="加入王子的美食之旅，享受生活中的美好事物！",
        link="/shop/",
        sort_order=1
    )
    print("Hero Slides updated to Chinese.")

if __name__ == "__main__":
    update_full_zh()
