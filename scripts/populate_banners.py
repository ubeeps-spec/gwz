
import os
import sys
import django
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import tempfile

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import HeroSlide

def populate_banners():
    print("Populating banners...")
    
    # 1. Clear existing slides
    HeroSlide.objects.all().delete()
    print("Cleared existing slides.")

    # 2. Define sample images
    banner_images = [
        {
            "url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1980&h=700&auto=format&fit=crop",
            "title": "加入王子的美食之旅",
            "subtitle": "享受生活中的美好事物！",
            "button_text": "立即加入",
            "link": "/shop/"
        },
        {
            "url": "https://images.unsplash.com/photo-1507048331197-7d4ac70811cf?q=80&w=1980&h=700&auto=format&fit=crop",
            "title": "成為像 George 一樣的家庭廚師",
            "subtitle": "探索獨家食譜與烹飪技巧",
            "button_text": "查看食譜",
            "link": "/shop/?category=食譜"
        },
        {
            "url": "https://images.unsplash.com/photo-1495521821757-a1efb6729352?q=80&w=1980&h=700&auto=format&fit=crop",
            "title": "精選優質食材",
            "subtitle": "為您的餐桌帶來最棒的風味",
            "button_text": "開始購物",
            "link": "/shop/"
        }
    ]
    
    # Fake user agent to avoid 403
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    for index, item in enumerate(banner_images):
        try:
            print(f"Downloading image {index + 1} from {item['url']}...")
            response = requests.get(item['url'], headers=headers)
            if response.status_code == 200:
                # Use standard tempfile instead of Django's wrapper if it causes issues on Windows
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as img_temp:
                    img_temp.write(response.content)
                    temp_path = img_temp.name
                
                slide = HeroSlide(
                    title=item['title'],
                    subtitle=item['subtitle'],
                    button_text=item['button_text'],
                    link=item['link'],
                    sort_order=index,
                    is_active=True
                )
                
                # Save image to the model
                with open(temp_path, 'rb') as f:
                    filename = f"banner_{index + 1}.jpg"
                    slide.image.save(filename, File(f), save=True)
                
                # Clean up temp file
                os.unlink(temp_path)
                
                print(f"Created slide: {item['title']}")
            else:
                print(f"Failed to download image {index + 1}: Status {response.status_code}")
        except Exception as e:
            print(f"Error processing slide {index + 1}: {e}")

    print("Banner population complete.")

if __name__ == '__main__':
    populate_banners()
