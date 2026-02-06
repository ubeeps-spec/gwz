import os

def remove_null_bytes():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    po_path = os.path.join(base_dir, 'locale', 'zh_Hant', 'LC_MESSAGES', 'django.po')
    
    print(f"Cleaning {po_path}...")
    
    with open(po_path, 'rb') as f:
        content = f.read()
    
    # Remove all null bytes
    cleaned_content = content.replace(b'\x00', b'')
    
    with open(po_path, 'wb') as f:
        f.write(cleaned_content)
        
    print("Successfully removed null bytes.")

if __name__ == "__main__":
    remove_null_bytes()
