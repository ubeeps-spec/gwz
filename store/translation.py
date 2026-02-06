from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Page, HeroSlide, SiteSettings, PaymentMethod, Coupon

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'specs')

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(HeroSlide)
class HeroSlideTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_text')

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = (
        'site_name', 
        'hero_title', 
        'hero_subtitle', 
        'hero_button_text', 
        'feature_title',
        'feature_subtitle',
        'founder_name',
        'founder_intro_title',
        'founder_intro_text',
        'footer_about', 
        'footer_copyright',
        'menu_home_text',
        'menu_store_text',
        'menu_about_text',
        'menu_blog_text',
        'menu_contact_text',
        'menu_tutorial_text',
        'contact_address',
        'contact_opening_hours',
        'navbar_items'
    )
