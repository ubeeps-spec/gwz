import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwz.settings')
django.setup()

from store.models import Page

def upsert_page(slug, title, content_html):
    page, _ = Page.objects.get_or_create(slug=slug, defaults={'title': title, 'content': content_html, 'is_active': True})
    page.title = title
    page.content = content_html
    page.is_active = True
    page.save()
    return page

def import_blog():
    index_html = """
    <div class="container">
      <h2 class="fw-bold mb-4">GWZ 博客</h2>
      <p class="lead">跟著 George 的家庭料理旅程，探索食譜、生活與美食心得。</p>
      <div class="row g-4 mt-3">
        <div class="col-md-4">
          <a href="/pages/blog-home-cook/" class="text-decoration-none">
            <div class="card h-100 shadow-sm">
              <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&h=600&auto=format&fit=crop" class="card-img-top" alt="家庭廚師的日常">
              <div class="card-body">
                <h5 class="card-title fw-bold">家庭廚師的日常</h5>
                <p class="card-text">如何在忙碌生活中，做出美味又健康的一餐。</p>
              </div>
            </div>
          </a>
        </div>
        <div class="col-md-4">
          <a href="/pages/blog-travel-food-notes/" class="text-decoration-none">
            <div class="card h-100 shadow-sm">
              <img src="https://images.unsplash.com/photo-1467003909585-2f8a72700288?q=80&w=800&h=600&auto=format&fit=crop" class="card-img-top" alt="旅行與美食筆記">
              <div class="card-body">
                <h5 class="card-title fw-bold">旅行與美食筆記</h5>
                <p class="card-text">從世界各地汲取靈感，帶回廚房中的風味故事。</p>
              </div>
            </div>
          </a>
        </div>
        <div class="col-md-4">
          <a href="/pages/blog-sauce-pairing/" class="text-decoration-none">
            <div class="card h-100 shadow-sm">
              <img src="https://images.unsplash.com/photo-1604908554028-618a4a692744?q=80&w=800&h=600&auto=format&fit=crop" class="card-img-top" alt="醬料的搭配技巧">
              <div class="card-body">
                <h5 class="card-title fw-bold">醬料的搭配技巧</h5>
                <p class="card-text">教你用簡單的醬料，快速提升家常菜的層次。</p>
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>
    """

    post1_html = """
    <p>身為家庭廚師，時間管理是關鍵。先準備好常用食材與醬料，能讓你在 20 分鐘內完成均衡的一餐。建議每週備料一次，像是切好的蔬菜、已腌好的肉類，以及一兩款萬用醬。</p>
    <ul>
      <li>備料清單：洋蔥、蒜頭、青蔥、當季蔬菜、雞腿肉、豆腐</li>
      <li>萬用醬：蒜香醬、辣椒油、芝麻醬</li>
    </ul>
    <p>把料理變簡單，是日常持續做飯的關鍵。</p>
    """

    post2_html = """
    <p>旅行讓我們認識食材的多樣性。無論是日本市場的新鮮魚貨，或是地中海的橄欖油，每一次品嚐都是新的靈感。回到家後，嘗試以在地食材重現記憶中的風味，是最有趣的挑戰。</p>
    <p>記錄：用三種橄欖油做沙拉的比較、以味噌入菜的家常做法、以及港式與台式的街頭美食差異。</p>
    """

    post3_html = """
    <p>醬料是家庭料理的靈魂。三種入門搭配：</p>
    <ol>
      <li>蒜香醬配烤蔬菜：提升香氣與層次。</li>
      <li>辣椒油配麵食：讓清淡的麵條瞬間有靈魂。</li>
      <li>芝麻醬配白切雞：滑順口感與堅果香，十分百搭。</li>
    </ol>
    <p>先少量嘗試，再依喜好微調比例，最能做出屬於自己的風味。</p>
    """

    upsert_page('blog', 'GWZ 博客', index_html)
    upsert_page('blog-home-cook', '家庭廚師的日常', post1_html)
    upsert_page('blog-travel-food-notes', '旅行與美食筆記', post2_html)
    upsert_page('blog-sauce-pairing', '醬料的搭配技巧', post3_html)

if __name__ == '__main__':
    import_blog()
