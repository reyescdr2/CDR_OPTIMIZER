import sys, os, pprint

sys.path.append(r'c:\Users\Administrator\Desktop\CDR\i18n_data')

category_mapping = {
    'Subsistemas y Servicios del Kernel': 'cat_system',
    'Mantenimiento y Purga': 'cat_clean',
    'Privacidad y Telemetría de Shell': 'cat_privacy',
    'Interfaz Gráfica y Optimización de Shell': 'cat_ui',
    'Optimización de Pila TCP/IP y Red': 'cat_net',
    'Aceleración de Procesos y Entorno Gaming': 'cat_gaming',
    'Gestión Energética y Eficiencia del CPU': 'cat_power',
    'Optimización de Video y Baja Latencia DPC': 'cat_gpu',
    'Parámetros de Kernel y Configuración Avanzada': 'cat_kernel',
    'Configuración de Alto Impacto en el Sistema': 'cat_extreme',
    'Herramientas de Utilidad (WinUtil/CDR)': 'cat_util',
    'Personalización Avanzada del Sistema': 'cat_pro',
    'Créditos': 'cat_help'
}

files = ['tweaks_fr.py', 'tweaks_it.py', 'tweaks_pt.py', 'tweaks_ru.py', 'tweaks_zh.py']

for f in files:
    try:
        mod_name = f[:-3]
        mod = __import__(mod_name)
        func = getattr(mod, 'get_' + mod_name)
        data = func()
        
        new_data = {}
        for old_key, val in data.items():
            new_key = category_mapping.get(old_key, old_key)
            new_data[new_key] = val
            
        file_path = os.path.join(r'c:\Users\Administrator\Desktop\CDR\i18n_data', f)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('# type: ignore\n')
            file.write(f'def get_{mod_name}():\n')
            file.write('    return ')
            pp = pprint.PrettyPrinter(indent=4, width=120)
            formatted = pp.pformat(new_data)
            # Indent all lines of formatted dict
            indented = '\n'.join('    ' + line if i > 0 else line for i, line in enumerate(formatted.splitlines()))
            file.write(indented + '\n')
        print(f"Standardized {f}")
    except Exception as e:
        print(f"Error standardizing {f}: {e}")
