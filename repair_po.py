
import os

po_file = 'locale/zh_Hant/LC_MESSAGES/django.po'
fixed_po_file = 'locale/zh_Hant/LC_MESSAGES/django_fixed.po'

def fix_mojibake(text):
    try:
        # Try the most common mojibake pattern: UTF-8 interpreted as Latin-1/Windows-1252
        # We need to encode back to latin-1 to get the original utf-8 bytes, then decode as utf-8
        return text.encode('cp1252').decode('utf-8')
    except Exception as e:
        return text

def repair_file():
    if not os.path.exists(po_file):
        print(f"File not found: {po_file}")
        return

    with open(po_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if it looks damaged (simple heuristic: look for "Traditional Chinese" translation)
    # The corrupted one had: msgstr "ç¹é«ä¸­æ"
    # The correct one should have: msgstr "繁體中文"
    
    if "ç¹" in content or "Ã" in content:
        print("Detected Mojibake. Attempting repair...")
        fixed_content = fix_mojibake(content)
        
        # Verify repair
        if "繁體中文" in fixed_content:
            print("Repair successful!")
            with open(fixed_po_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Saved fixed content to {fixed_po_file}")
        else:
            print("Repair failed. Content might be damaged beyond simple reversal.")
            # Fallback: Write what we have but maybe it's not fixing it
            with open(fixed_po_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
    else:
        print("No obvious Mojibake detected. Content seems fine or issue is different.")
        print("First 200 chars:")
        print(content[:200])

if __name__ == "__main__":
    repair_file()
