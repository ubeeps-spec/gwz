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
    # The user said "Directory is corresponding to product categories"
    # We will rename existing categories to Chinese
    category_map = {
        "featured": "精選",
        "blog": "博客",
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
    # User asked for "About Us" (關於我們)
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
    
    # 3. Create core content pages for feature cards
    pages_data = [
        {
            'slug': 'featured',
            'title': '精選博客',
            'content': """
            <h2>精選博客</h2>
            <p>從王子的食譜與烹飪影片中獲得靈感，發現他對食材、火候與風味的獨到見解。</p>
            <p>在這裡，我們會不定期分享精選文章，包含烹飪技巧、節慶料理、以及廚房好物推薦。</p>
            """,
        },
        {
            'slug': 'blog',
            'title': '博客',
            'content': """
            <h2>博客</h2>
            <p>與王子一起探索家庭美食與烹飪祕方，記錄生活中的美好餐桌時光。</p>
            """,
        },
        {
            'slug': 'food-review',
            'title': '美食評論',
            'content': """
            <h2>美食評論</h2>
            <p>王子熱愛嘗試新鮮美食，帶您走訪各地餐廳與市集，分享真實的味覺體驗。</p>
            """,
        },
        {
            'slug': 'recipes',
            'title': '新鮮食譜',
            'content': """
            <h2>新鮮食譜</h2>
            <p>從入門到進階，王子以簡單步驟帶你掌握家常料理的核心技法。</p>
            """,
        },
        {
            'slug': 'products',
            'title': '特色產品',
            'content': """
            <h2>特色產品</h2>
            <p>王子自製了豐富多樣的調味料，讓你的家常菜也能充滿層次與驚喜。</p>
            """,
        },
        {
            'slug': 'lifestyle',
            'title': '生活方式與文化',
            'content': """
            <h2>生活方式與文化</h2>
            <p>透過王子的視角，看見更廣袤的世界：旅行、購物、文化、與美食交織的生活風景。</p>
            """,
        },
        {
            'slug': 'terms',
            'title': '條款與細則',
            'content': """
            <h2>條款與細則</h2>
            <p>歡迎來到 GWZ 網上商店。在使用本網站之前，請仔細閱讀以下條款與細則。</p>
            
            <h3>1. 一般條款</h3>
            <p>本網站由 GWZ 營運。在整個網站中，「我們」是指 GWZ。GWZ 向您（使用者）提供本網站，包括本網站提供的所有資訊、工具和服務，條件是您接受此處所述的所有條款、細則、政策和聲明。</p>
            
            <h3>2. 線上商店條款</h3>
            <p>同意這些服務條款，即表示您在您居住的州或省至少已達到成年年齡。</p>
            <p>您不得將我們的產品用於任何非法或未經授權的目的，也不得在使用服務時違反您所在司法管轄區的任何法律（包括但不限於版權法）。</p>
            
            <h3>3. 產品與服務</h3>
            <p>我們已盡一切努力盡可能準確地顯示商店中出現的產品的顏色和圖像。我們不能保證您的電腦顯示器顯示的任何顏色都是準確的。</p>
            <p>我們保留限制向任何人、地理區域或司法管轄區銷售我們的產品或服務的權利。我們可能視情況行使此權利。</p>
            
            <h3>4. 價格與付款</h3>
            <p>產品價格如有更改，恕不另行通知。我們保留隨時修改或終止服務（或其任何部分或內容）的權利，恕不另行通知。</p>
            
            <h3>5. 退換貨政策</h3>
            <p>請參閱我們的退換貨政策頁面以獲取詳細資訊。</p>
            
            <h3>6. 個人資訊</h3>
            <p>您透過商店提交的個人資訊受我們的隱私權政策管轄。</p>
            
            <h3>7. 聯絡資訊</h3>
            <p>有關服務條款的問題應發送至我們的聯絡電子郵件。</p>
            """,
        },
        {
            'slug': 'privacy',
            'title': '隱私權政策',
            'content': """
            <h2>隱私權政策</h2>
            <p>GWZ 尊重您的隱私權並致力於保護您的個人資料。</p>
            
            <h3>我們收集的資訊</h3>
            <p>當您訪問本網站時，我們會自動收集有關您設備的某些資訊，包括有關您的網頁瀏覽器、IP 地址、時區以及安裝在您設備上的一些 Cookie 的資訊。</p>
            <p>此外，當您進行購買或嘗試透過本網站進行購買時，我們會收集您的某些資訊，包括您的姓名、帳單地址、送貨地址、付款資訊（包括信用卡號碼）、電子郵件地址和電話號碼。</p>
            
            <h3>我們如何使用您的資訊</h3>
            <p>我們通常使用我們收集的訂單資訊來完成透過本網站下的任何訂單（包括處理您的付款資訊、安排運輸以及向您提供發票和/或訂單確認）。</p>
            <p>此外，我們使用此訂單資訊來：</p>
            <ul>
                <li>與您溝通；</li>
                <li>篩選我們的訂單是否存在潛在風險或欺詐；以及</li>
                <li>根據您與我們分享的偏好，向您提供與我們的產品或服務相關的資訊或廣告。</li>
            </ul>
            
            <h3>資料保留</h3>
            <p>當您透過本網站下訂單時，除非您要求我們刪除此資訊，否則我們將保留您的訂單資訊作為我們的記錄。</p>
            """,
        },
    ]
    
    for pd in pages_data:
        page, created = Page.objects.get_or_create(slug=pd['slug'])
        page.title = pd['title']
        page.content = pd['content']
        page.is_active = True
        page.save()
        print(f"Page '{pd['slug']}' created/updated.")

if __name__ == "__main__":
    update_content()
