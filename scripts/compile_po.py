import polib
import os

def compile_po(po_path, mo_path):
    print(f"Compiling {po_path} to {mo_path}...")
    try:
        po = polib.pofile(po_path)
        po.save_as_mofile(mo_path)
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    po_file = os.path.join(base_dir, 'locale', 'zh_Hant', 'LC_MESSAGES', 'django.po')
    mo_file = os.path.join(base_dir, 'locale', 'zh_Hant', 'LC_MESSAGES', 'django.mo')
    
    if os.path.exists(po_file):
        compile_po(po_file, mo_file)
    else:
        print(f"File not found: {po_file}")
