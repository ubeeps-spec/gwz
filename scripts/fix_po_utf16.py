import os

def fix_po_utf16_corruption():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    po_path = os.path.join(base_dir, 'locale', 'zh_Hant', 'LC_MESSAGES', 'django.po')
    
    print(f"Reading {po_path}...")
    
    with open(po_path, 'rb') as f:
        content = f.read()

    # The corrupted part starts with UTF-16LE encoded "msgid"
    # m\x00s\x00g\x00i\x00d\x00
    corrupt_start_pattern = b'm\x00s\x00g\x00i\x00d\x00'
    
    idx = content.find(corrupt_start_pattern)
    
    if idx != -1:
        print(f"Found corruption start at byte {idx}. Truncating...")
        # Backtrack to remove any preceding null bytes or newlines that might be part of the corruption
        # But we want to keep the last valid newline if possible.
        # Let's just truncate at idx.
        valid_content = content[:idx]
        
        # Strip trailing nulls if any
        while valid_content and valid_content[-1] == 0:
            valid_content = valid_content[:-1]
            
        # Ensure it ends with a newline
        if not valid_content.endswith(b'\n'):
            valid_content += b'\n'
            
        # Append the new translations (UTF-8)
        new_translations = """
msgid "Featured Products"
msgstr "精選產品"

msgid "Prince has created a variety of seasonings to make your dishes flavorful."
msgstr "王子創造了各種調味料，讓您的菜餚更加美味。"

msgid "Learn More"
msgstr "了解更多"

msgid "Lifestyle & Culture"
msgstr "生活與文化"

msgid "See the wider world through Prince's eyes..."
msgstr "透過王子的眼睛看更廣闊的世界..."

msgid "Discover More"
msgstr "發現更多"

msgid "Beyond cooking, we invite you to see the world through George's eyes, sharing his experiences in travel, shopping, and different cultures."
msgstr "除了烹飪，我們邀請您透過 George 的眼睛看世界，分享他在旅行、購物和不同文化中的經歷。"

msgid "Shop"
msgstr "商店"

msgid "Show per page:"
msgstr "每頁顯示："

msgid "Price: Low to High"
msgstr "價格：低到高"

msgid "Price: High to Low"
msgstr "價格：高到低"

msgid "Default Sorting"
msgstr "預設排序"

msgid "All Products"
msgstr "所有產品"
"""
        final_content = valid_content + new_translations.encode('utf-8')
        
        with open(po_path, 'wb') as f:
            f.write(final_content)
        print("Successfully repaired django.po")
        
    else:
        print("Could not find the expected corruption pattern. Please check the file manually.")

if __name__ == "__main__":
    fix_po_utf16_corruption()
