from .models import SiteSettings, Category
from decimal import Decimal

def site_settings(request):
    """
    Context processor to make SiteSettings and Categories available to all templates.
    """
    try:
        settings = SiteSettings.objects.first()
    except Exception:
        settings = None
        
    categories = Category.objects.all().order_by('name')
    return {
        'site_settings': settings,
        'categories': categories
    }

def cart_processor(request):
    """
    Context processor to make cart item count and details available to all templates.
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    cart_total_price = Decimal('0')
    cart_item_count = 0
    
    for pid, item in cart.items():
        # Create a copy to avoid modifying the session directly if mutable
        # and inject the ID which is the key in the cart dictionary
        item_data = item.copy()
        item_data['id'] = pid
        
        qty = int(item.get('qty', 0))
        try:
            price = Decimal(str(item.get('price', '0')))
        except:
            price = Decimal('0')
        
        cart_items.append(item_data)
        cart_item_count += qty
        cart_total_price += price * qty
        
    return {
        'cart_item_count': cart_item_count,
        'cart_items': cart_items,
        'cart_total_price': cart_total_price
    }
