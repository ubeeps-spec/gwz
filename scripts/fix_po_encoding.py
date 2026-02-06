import os

def fix_po_encoding():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    po_path = os.path.join(base_dir, 'locale', 'zh_Hant', 'LC_MESSAGES', 'django.po')
    
    print(f"Reading {po_path}...")
    
    content = b""
    try:
        with open(po_path, 'rb') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Try decoding with utf-8, if fails, try cp950 (Big5) or cp1252
    decoded_content = ""
    try:
        decoded_content = content.decode('utf-8')
        print("Successfully decoded as UTF-8")
    except UnicodeDecodeError:
        print("UTF-8 decode failed, trying CP950 (Big5)...")
        try:
            decoded_content = content.decode('cp950')
            print("Successfully decoded as CP950")
        except UnicodeDecodeError:
            print("CP950 decode failed, trying latin-1...")
            decoded_content = content.decode('latin-1')
            print("Fallback to latin-1")

    # Ensure no duplicates of the appended part if run multiple times
    # (Simple check: if "Featured Products" appears twice, remove the second one)
    # Actually, let's just write it back as UTF-8 first.
    
    try:
        with open(po_path, 'w', encoding='utf-8') as f:
            f.write(decoded_content)
        print("Successfully wrote back as UTF-8")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    fix_po_encoding()
