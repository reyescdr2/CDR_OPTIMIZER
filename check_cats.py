import sys, os

# Define paths
base_path = r'c:\Users\Administrator\Desktop\CDR'
i18n_path = os.path.join(base_path, 'i18n_data')
sys.path.append(i18n_path)

def check_categories():
    # Find all translation files
    files = [f for f in os.listdir(i18n_path) if f.startswith('tweaks_') and f.endswith('.py')]
    
    # Use Spanish as the reference (usually the most updated)
    reference_file = 'tweaks_es.py'
    if reference_file not in files:
        print(f"Error: {reference_file} not found. Cannot compare.")
        return

    import importlib
    try:
        ref_mod = importlib.import_module(reference_file[:-3])
        ref_data = getattr(ref_mod, 'get_tweaks_es')()
        ref_keys = set(ref_data.keys())
        print(f"Reference ({reference_file}) keys: {sorted(ref_keys)}\n")
    except Exception as e:
        print(f"Error loading reference {reference_file}: {e}")
        return

    # Compare other files
    for f in sorted(files):
        if f == reference_file: continue
        
        try:
            mod_name = f[:-3] # type: ignore
            mod = importlib.import_module(mod_name)
            func = getattr(mod, 'get_' + mod_name)
            data = func()
            keys = set(data.keys())
            
            missing = ref_keys - keys
            extra = keys - ref_keys
            
            if missing or extra:
                print(f"--- {f} ---")
                if missing: print(f"  MISSING: {missing}")
                if extra: print(f"  EXTRA: {extra}")
            else:
                print(f"OK: {f} matches reference.")
                
        except Exception as e:
            print(f"Error loading {f}: {e}")

if __name__ == "__main__":
    check_categories()
