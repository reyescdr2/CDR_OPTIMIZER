# type: ignore
import typing
import subprocess
import os
import shutil
import time
import typing
import importlib
import ctypes
import sys



import winreg
import wmi # type: ignore
import psutil # type: ignore

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

# --- C++ ENGINE INTEGRATION ---
try:
    engine_path = resource_path("cdr_engine.dll")
    cdr_engine = ctypes.CDLL(engine_path)
    
    cdr_engine.OptimizeMemory_CPP.argtypes = []
    cdr_engine.OptimizeMemory_CPP.restype = ctypes.c_int
    
    cdr_engine.ApplyRegistryDWORD_CPP.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong]
    cdr_engine.ApplyRegistryDWORD_CPP.restype = ctypes.c_int

    cdr_engine.ApplyRegistryString_CPP.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    cdr_engine.ApplyRegistryString_CPP.restype = ctypes.c_int
    
    cdr_engine.FlushStandbyList_CPP.argtypes = []
    cdr_engine.FlushStandbyList_CPP.restype = ctypes.c_int

    cdr_engine.SetHighPriority_CPP.argtypes = [ctypes.c_ulong]
    cdr_engine.SetHighPriority_CPP.restype = ctypes.c_int

    # ── New high-speed functions ──────────────────────────────────────────
    try:
        cdr_engine.ApplyRegistryCU_DWORD.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong]
        cdr_engine.ApplyRegistryCU_DWORD.restype = ctypes.c_int
    except AttributeError: pass

    try:
        cdr_engine.ApplyRegistryCU_String.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        cdr_engine.ApplyRegistryCU_String.restype = ctypes.c_int
    except AttributeError: pass

    try:
        cdr_engine.DisableService.argtypes = [ctypes.c_char_p]
        cdr_engine.DisableService.restype = ctypes.c_int
    except AttributeError: pass

    try:
        cdr_engine.BatchDisableServices.argtypes = [ctypes.c_char_p]
        cdr_engine.BatchDisableServices.restype = ctypes.c_int
    except AttributeError: pass

    try:
        cdr_engine.RunHidden.argtypes = [ctypes.c_char_p]
        cdr_engine.RunHidden.restype = ctypes.c_int
    except AttributeError: pass

    HAS_CPP_ENGINE = True
except Exception as e:
    HAS_CPP_ENGINE = False
    print(f"CDR Engine DLL could not be loaded: {e}")
# ------------------------------

def disable_services_cpp(service_names: list) -> int:
    """Disable a list of Windows services using the C++ engine (much faster than sc.exe).
    Falls back to subprocess if the DLL is not available."""
    if HAS_CPP_ENGINE:
        batch = ";".join(service_names)
        return cdr_engine.BatchDisableServices(batch.encode())
    else:
        count = 0
        for svc in service_names:
            run_cmd(f'sc stop "{svc}"')
            run_cmd(f'sc config "{svc}" start= disabled')
            run_cmd(f'sc failure "{svc}" reset= 0 actions= ""')
            count += 1
        return count

def disable_critical_tasks():
    """Disable Windows scheduled tasks used for telemetry and maintenance."""
    tasks = [
        r"\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
        r"\Microsoft\Windows\Application Experience\ProgramDataUpdater",
        r"\Microsoft\Windows\Application Experience\StartupAppScan",
        r"\Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
        r"\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip",
        r"\Microsoft\Windows\Autochk\Proxy",
        r"\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector",
        r"\Microsoft\Windows\Feedback\Siuf\DmClient",
        r"\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload"
    ]
    for task in tasks:
        run_cmd(f'schtasks /change /tn "{task}" /disable')

def reg_lm(subkey: str, value: str, data) -> None:
    """Write a DWORD or string to HKLM using C++ (no subprocess).
    Falls back to subprocess reg.exe if DLL not available."""
    if HAS_CPP_ENGINE:
        if isinstance(data, int):
            cdr_engine.ApplyRegistryDWORD_CPP(subkey.encode(), value.encode(), data)
        else:
            cdr_engine.ApplyRegistryString_CPP(subkey.encode(), value.encode(), str(data).encode())
    else:
        if isinstance(data, int):
            run_cmd(f'reg add "HKLM\\{subkey}" /v {value} /t REG_DWORD /d {data} /f')
        else:
            run_cmd(f'reg add "HKLM\\{subkey}" /v {value} /t REG_SZ /d "{data}" /f')

def reg_cu(subkey: str, value: str, data) -> None:
    """Write a DWORD or string to HKCU using C++ (no subprocess)."""
    if HAS_CPP_ENGINE:
        if isinstance(data, int):
            cdr_engine.ApplyRegistryCU_DWORD(subkey.encode(), value.encode(), data)
        else:
            cdr_engine.ApplyRegistryCU_String(subkey.encode(), value.encode(), str(data).encode())
    else:
        if isinstance(data, int):
            run_cmd(f'reg add "HKCU\\{subkey}" /v {value} /t REG_DWORD /d {data} /f')
        else:
            run_cmd(f'reg add "HKCU\\{subkey}" /v {value} /t REG_SZ /d "{data}" /f')

def run_cmd(command):
    try:
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=0x08000000)
    except Exception as e:
        print(f"Error executing: {command} - {e}")

def run_ps(command):
    import tempfile, os
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
            f.write(command)
            tmp_path = f.name
        subprocess.run(
            ['powershell', '-ExecutionPolicy', 'Bypass', '-NonInteractive', '-NoProfile', '-File', tmp_path],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=0x08000000
        )
    except Exception as e:
        print(f"Error running PS script: {e}")
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass

def is_laptop():
    try:
        c = wmi.WMI() # type: ignore
        return len(c.Win32_Battery()) > 0 # type: ignore
    except:
        return False

def check_drivers():
    try:
        c = wmi.WMI() # type: ignore
        bad_devices = c.query("SELECT Name, DeviceID, ConfigManagerErrorCode FROM Win32_PnPEntity WHERE ConfigManagerErrorCode != 0") # type: ignore
        return bad_devices # type: ignore
    except:
        return []

def fix_drivers(bad_devices):
    for dev in bad_devices:
        try:
            dev_id = dev.DeviceID
            run_ps(f"Disable-PnpDevice -InstanceId '{dev_id}' -Confirm:$false")
            time.sleep(1)
            run_ps(f"Enable-PnpDevice -InstanceId '{dev_id}' -Confirm:$false")
        except:
            pass
            
    run_cmd("pnputil /scan-devices")

def get_registry_value(hkey, sub_key, value_name):
    try:
        registry_key = winreg.OpenKey(hkey, sub_key, 0, winreg.KEY_READ) # type: ignore
        value, regtype = winreg.QueryValueEx(registry_key, value_name) # type: ignore
        winreg.CloseKey(registry_key) # type: ignore
        return value
    except Exception:
        return None

try:
    import game_booster # type: ignore
except ImportError:
    game_booster = None

def check_state(tweak_id):
    try:
        if tweak_id == "svc_diagtrack":
            val = get_registry_value(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\DiagTrack", "Start") # type: ignore
            return val == 4
        elif tweak_id == "svc_sysmain":
            val = get_registry_value(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\SysMain", "Start") # type: ignore
            return val == 4
        elif tweak_id == "priv_advertising":
            val = get_registry_value(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo", "Enabled") # type: ignore
            return val == 0
        elif tweak_id == "game_mode":
            val = get_registry_value(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar", "AllowAutoGameMode") # type: ignore
            return val == 1
        return None
    except:
        return None

def execute_tweaks(config_dict, progress_callback=None):
    total = len(config_dict)
    count = 0
    for t_id, is_active in config_dict.items():
        count += 1
        if t_id == "game_process_lasso":
            if is_active:
                if game_booster and not game_booster.booster_instance.running:
                    game_booster.booster_instance.start()
            else:
                if game_booster and game_booster.booster_instance.running:
                    game_booster.booster_instance.stop()

        elif t_id == "game_msi_mode":
            if is_active:
                # Script PowerShell para forzar Message Signaled Interrupts en todos los dispositivos compatibles (Red, GPU, USB)
                # Esto es una optimización extrema que requiere iterar el registro HKLM\SYSTEM\CurrentControlSet\Enum
                msi_script = """
                $regPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Enum"
                Get-ChildItem -Path $regPath -Recurse -ErrorAction SilentlyContinue | 
                Where-Object { $_.GetSubKeyNames() -contains "Device Parameters" } | 
                ForEach-Object {
                    $devParam = Join-Path $_.PSPath "Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties"
                    if (Test-Path $devParam) {
                        Set-ItemProperty -Path $devParam -Name "MSISupported" -Value 1 -Type DWord -Force -ErrorAction SilentlyContinue
                    }
                }
                """
                run_ps(msi_script)

        elif t_id == "net_extreme_tcp":
            if is_active:
                run_cmd('netsh int tcp set global rss=enabled')
                run_cmd('netsh int tcp set global autotuninglevel=normal')
                run_cmd('netsh int tcp set supplemental template=custom icw=10')
                run_cmd('netsh int tcp set supplemental template=internet congestionprovider=bbr2') # O bbr si es Win 10
                run_cmd('netsh int tcp set supplemental template=internet congestionprovider=cubic') # Backup
                
                # Deshabilitar Green Ethernet e Interrupt Moderation en adaptadores físicos
                run_ps('Get-NetAdapterAdvancedProperty | Where-Object {$_.DisplayName -match "Energy Efficient Ethernet" -or $_.DisplayName -match "Green Ethernet"} | Set-NetAdapterAdvancedProperty -RegistryValue "0" -ErrorAction SilentlyContinue')
                run_ps('Disable-NetAdapterChecksumOffload -Name "*" -TcpIPv4 -UdpIPv4 -IpIPv4 -ErrorAction SilentlyContinue')
                run_ps('Disable-NetAdapterLso -Name "*" -IPv4 -IPv6 -ErrorAction SilentlyContinue')
                run_ps('Get-NetAdapterAdvancedProperty | Where-Object {$_.DisplayName -match "Interrupt Moderation"} | Set-NetAdapterAdvancedProperty -RegistryValue "0" -ErrorAction SilentlyContinue')

        elif t_id == "priv_etw_disable":
            if is_active:
                # Bloqueo Profundo de AutoLoggers (Telemetría de Kernel)
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\AutoLogger-Diagtrack-Listener" /v Start /t REG_DWORD /d 0 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\SQMLogger" /v Start /t REG_DWORD /d 0 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\AITEventLog" /v Start /t REG_DWORD /d 0 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\AppHost" /v Start /t REG_DWORD /d 0 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\AppModel" /v Start /t REG_DWORD /d 0 /f')

        elif t_id == "game_iso_build":
            if is_active:
                # Just open the folder for now where we would put ISO tools, or launch an external tool
                run_cmd("start https://www.ntlite.com/download/")

        elif t_id == "svc_diagtrack":
            if is_active:
                run_cmd('sc stop "DiagTrack"')
                run_cmd('sc config "DiagTrack" start= disabled')
                run_cmd('sc failure "DiagTrack" reset= 0 actions= ""')
                run_cmd('sc stop "dmwappushservice"')
                run_cmd('sc config "dmwappushservice" start= disabled')
                run_cmd('sc failure "dmwappushservice" reset= 0 actions= ""')
                # Persistent Policy
                run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
                disable_critical_tasks()
            else:
                run_cmd('sc config "DiagTrack" start= auto')
                run_cmd('sc start "DiagTrack"')
                run_cmd('sc config "dmwappushservice" start= demand')

        elif t_id == "svc_wsearch":
            if is_active:
                run_cmd('sc stop "WSearch"')
                run_cmd('sc config "WSearch" start= disabled')
                run_cmd('sc failure "WSearch" reset= 0 actions= ""')
            else:
                run_cmd('sc config "WSearch" start= delayed-auto')
                run_cmd('sc start "WSearch"')

        elif t_id == "svc_sysmain":
            if is_active:
                run_cmd('sc stop "SysMain"')
                run_cmd('sc config "SysMain" start= disabled')
                run_cmd('sc failure "SysMain" reset= 0 actions= ""')
            else:
                run_cmd('sc config "SysMain" start= auto')
                run_cmd('sc start "SysMain"')

        elif t_id == "svc_wuauserv_manual":
            if is_active:
                run_cmd('sc config "wuauserv" start= demand')
            else:
                run_cmd('sc config "wuauserv" start= auto')

        elif t_id == "svc_bcastdvr":
            if is_active:
                run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR" /v AllowGameDVR /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR" /v AllowGameDVR /t REG_DWORD /d 1 /f')

        elif t_id == "svc_maps":
            if is_active:
                run_cmd('sc config "MapsBroker" start= disabled')
                run_cmd('sc failure "MapsBroker" reset= 0 actions= ""')
            else: run_cmd('sc config "MapsBroker" start= auto')

        elif t_id == "svc_fax":
            if is_active:
                run_cmd('sc config "Fax" start= disabled')
                run_cmd('sc failure "Fax" reset= 0 actions= ""')
            else: run_cmd('sc config "Fax" start= demand')

        elif t_id == "svc_print":
            if is_active:
                run_cmd('sc config "Spooler" start= disabled')
                run_cmd('sc failure "Spooler" reset= 0 actions= ""')
            else: run_cmd('sc config "Spooler" start= auto')

        elif t_id == "svc_xboxgip":
            if is_active:
                run_cmd('sc config "XboxGipSvc" start= disabled')
                run_cmd('sc failure "XboxGipSvc" reset= 0 actions= ""')
            else: run_cmd('sc config "XboxGipSvc" start= demand')

        elif t_id.startswith("svc_xbl"):
            svc_map = {"svc_xblauth": "XblAuthManager", "svc_xblgamesave": "XblGameSave", "svc_xboxnetapi": "XboxNetApiSvc"}
            svc_name = svc_map.get(t_id)
            if svc_name:
                if is_active:
                    run_cmd(f'sc config "{svc_name}" start= disabled')
                    run_cmd(f'sc failure "{svc_name}" reset= 0 actions= ""')
                else: run_cmd(f'sc config "{svc_name}" start= demand')

        elif t_id in ["svc_wer", "svc_wercplsupport"]:
            svc_name = "WerSvc" if t_id == "svc_wer" else "wercplsupport"
            if is_active:
                run_cmd(f'sc config "{svc_name}" start= disabled')
                run_cmd(f'sc failure "{svc_name}" reset= 0 actions= ""')
            else: run_cmd(f'sc config "{svc_name}" start= demand')

        elif t_id in ["svc_diagsvc", "svc_dps", "svc_diagtrack"]:
            svc_name = {"svc_diagsvc": "WdiServiceHost", "svc_dps": "DPS", "svc_diagtrack": "DiagTrack"}.get(t_id)
            if svc_name:
                if is_active: 
                    run_cmd(f'sc stop "{svc_name}"')
                    run_cmd(f'sc config "{svc_name}" start= disabled')
                    run_cmd(f'sc failure "{svc_name}" reset= 0 actions= ""')
                else:
                    run_cmd(f'sc config "{svc_name}" start= auto')

        elif t_id == "svc_pcasvc":
            if is_active:
                run_cmd('sc config "PcaSvc" start= disabled')
                run_cmd('sc failure "PcaSvc" reset= 0 actions= ""')
            else: run_cmd('sc config "PcaSvc" start= auto')

        elif t_id == "svc_sensors":
            if is_active:
                run_cmd('sc config "SensorService" start= disabled')
                run_cmd('sc failure "SensorService" reset= 0 actions= ""')
            else: run_cmd('sc config "SensorService" start= demand')

        elif t_id == "svc_smartcard":
            if is_active:
                run_cmd('sc config "SCardSvr" start= disabled')
                run_cmd('sc failure "SCardSvr" reset= 0 actions= ""')
            else: run_cmd('sc config "SCardSvr" start= demand')

        elif t_id == "svc_wallet":
            if is_active:
                run_cmd('sc config "WalletService" start= disabled')
                run_cmd('sc failure "WalletService" reset= 0 actions= ""')
            else: run_cmd('sc config "WalletService" start= demand')

        elif t_id.startswith("svc_"):
            generic_services = {
                "svc_bthserv": "bthserv", "svc_bthhfsrv": "bthhfsrv", "svc_camsvc": "FrameServer",
                "svc_iphlpsvc": "iphlpsvc", "svc_lltdsvc": "lltdsvc", "svc_luafv": "luafv",
                "svc_netman": "netman", "svc_netprofm": "netprofm", "svc_nsi": "nsi",
                "svc_p2psvc": "p2psvc", "svc_p2pimsvc": "p2pimsvc", "svc_pnrpsvc": "pnrpsvc",
                "svc_pnrp_peer_dist_pub": "pnrp_peer_dist_pub", "svc_policyagent": "PolicyAgent",
                "svc_rasman": "RasMan", "svc_remoteaccess": "RemoteAccess", "svc_remoteregistry": "RemoteRegistry",
                "svc_seclogon": "seclogon", "svc_sdrsvc": "SDRSVC", "svc_shellhwdetection": "ShellHWDetection",
                "svc_ssdpsrv": "SSDPSRV", "svc_stisvc": "stisvc", "svc_tabletinputservice": "TabletInputService",
                "svc_upnphost": "upnphost", "svc_vds": "vds", "svc_vss": "vss",
                "svc_wbio_srvc": "WbioSrvc", "svc_wcncsvc": "wcncsvc", "svc_wisvc": "wisvc",
                "svc_wmiapsrv": "wmiapsrv", "svc_wpmsvc": "WpnService", "svc_wscsvc": "wscsvc",
                "svc_wudf_svc": "WUDFsvc", "svc_workfolderssvc": "WorkfoldersSvc", "svc_one_sync_svc": "OneSyncSvc",
                "svc_aj_router": "AJRouter", "svc_app_v_client": "AppVClient", "svc_bits": "BITS",
                "svc_app_info": "Appinfo", "svc_app_mgmt": "AppMgmt", "svc_app_readiness": "AppReadiness",
                "svc_auto_time": "AutoTimeSvc", "svc_crypt_svc": "CryptSvc", "svc_defrag_svc": "defragsvc",
                "svc_disp_broker": "DispBrokerDesktopSvc", "svc_ds_role": "DsRoleSvc", "svc_fd_phost": "FDResPub",
                "svc_fh_svc": "fhsvc", "svc_game_svc": "GamingServices", "svc_hid_serv": "hidserv",
                "svc_key_iso": "KeyIso", "svc_license_manager": "LicenseManager", "svc_mp_svc": "WinDefend",
                "svc_net_data_usage": "NDU", "svc_per_mon": "perfmon", "svc_power": "Power",
                "svc_print_workflow": "PrintWorkflowUserSvc", "svc_push_to_install": "PushToInstall",
                "svc_security_health": "SecurityHealthService", "svc_sms_router": "SmsRouter",
                "svc_sys_main": "SysMain", "svc_themes": "Themes", "svc_time_broker": "TimeBrokerSvc",
                "svc_touch_keyboard": "TabletInputService", "svc_uac": "luafv", "svc_vmic_shutdown": "vmicshutdown",
                "svc_vmic_guest_interface": "vmicguestinterface", "svc_vmic_heartbeat": "vmicheartbeat",
                "svc_vmic_kvp": "vmickvp", "svc_vmic_rdv": "vmicrdv", "svc_vmic_vss": "vmicvss"
            }
            if svc_name:
                if is_active:
                    run_cmd(f'sc stop "{svc_name}"')
                    run_cmd(f'sc config "{svc_name}" start= disabled')
                    run_cmd(f'sc failure "{svc_name}" reset= 0 actions= ""')
                else:
                    run_cmd(f'sc config "{svc_name}" start= demand')

        elif t_id == "clean_temp" and is_active:
            temp_dirs = [os.environ.get('TEMP'), os.environ.get('TMP'), r"C:\Windows\Temp"]
            for temp in temp_dirs:
                if temp and os.path.exists(temp):
                    run_cmd(f'del /q /f /s "{temp}\\*"')
                    run_cmd(f'rmdir /q /s "{temp}\\"')
        elif t_id == "clean_prefetch" and is_active:
            run_cmd(r'del /q /f /s "C:\Windows\Prefetch\*"')
        elif t_id == "clean_winupdate" and is_active:
            run_cmd('net stop wuauserv')
            run_cmd(r'del /q /f /s "C:\Windows\SoftwareDistribution\Download\*"')
            run_cmd('net start wuauserv')
        elif t_id == "clean_recycle" and is_active:
            run_ps('Clear-RecycleBin -Force')
        elif t_id == "clean_dns" and is_active:
            run_cmd('ipconfig /flushdns')
        elif t_id == "clean_discord_cache" and is_active:
            discord_cachedir = os.path.expandvars(r"%appdata%\discord\Cache")
            if os.path.exists(discord_cachedir):
                run_cmd(f'del /q /f /s "{discord_cachedir}\\*"')
        elif t_id == "clean_steam_cache" and is_active:
            steam_dir_x86 = r"C:\\Program Files (x86)\\Steam\\appcache\\httpcache"
            steam_dir_user = os.path.expandvars(r"%localappdata%\\Steam\\htmlcache")
            if os.path.exists(steam_dir_x86): run_cmd(f'del /q /f /s "{steam_dir_x86}\\*"')
            if os.path.exists(steam_dir_user): run_cmd(f'del /q /f /s "{steam_dir_user}\\*"')
        
        elif t_id == "clean_eventlog" and is_active:
            run_ps('wevtutil el | Foreach-Object {wevtutil cl "$_"}')
            
        elif t_id == "clean_chrome_cache" and is_active:
            chrome_cache = os.path.expandvars(r"%localappdata%\\Google\\Chrome\\User Data\\Default\\Cache")
            if os.path.exists(chrome_cache): run_cmd(f'del /q /f /s "{chrome_cache}\\*"')

        elif t_id == "clean_edge_cache" and is_active:
            edge_cache = os.path.expandvars(r"%localappdata%\\Microsoft\\Edge\\User Data\\Default\\Cache")
            if os.path.exists(edge_cache): run_cmd(f'del /q /f /s "{edge_cache}\\*"')

        elif t_id == "clean_crashdumps" and is_active:
            run_cmd(r'del /q /f /s "C:\\Windows\\Minidump\\*"')
            run_cmd(r'del /q /f /s "C:\\Windows\\MEMORY.DMP"')

        elif t_id == "clean_epic_cache" and is_active:
            epic_cache = os.path.expandvars(r"%localappdata%\\EpicGamesLauncher\\Saved\\webcache")
            if os.path.exists(epic_cache): run_cmd(f'del /q /f /s "{epic_cache}\\*"')

        elif t_id == "clean_spotify_cache" and is_active:
            spotify_cache = os.path.expandvars(r"%localappdata%\Spotify\Browser\Cache")
            if os.path.exists(spotify_cache): run_cmd(f'del /q /f /s "{spotify_cache}\\*"')

        elif t_id == "clean_usrdoc_temp" and is_active:
            run_cmd(r'del /q /f /s "%USERPROFILE%\Documents\*.tmp"')
        
        elif t_id == "clean_system_logs" and is_active:
            run_cmd(r'del /q /f /s "C:\Windows\*.log"')

        elif t_id == "clean_crypt_svc" and is_active:
            run_cmd('net stop cryptsvc')
            run_cmd(r'del /q /f /s "C:\Windows\System32\catroot2\*"')
            run_cmd('net start cryptsvc')

        elif t_id == "clean_bits_queue" and is_active:
            run_cmd('net stop bits')
            run_cmd(r'del /q /f /s "C:\ProgramData\Microsoft\Network\Downloader\*"')
            run_cmd('net start bits')

        elif t_id == "clean_thumbcache" and is_active:
            thumbcache_dir = os.path.expandvars(r"%localappdata%\Microsoft\Windows\Explorer")
            run_cmd(f'del /q /f "{thumbcache_dir}\\thumbcache_*.db"')

        elif t_id == "clean_fontcache" and is_active:
            run_cmd('net stop FontCache')
            run_cmd(r'del /q /f /s "C:\Windows\ServiceProfiles\LocalService\AppData\Local\FontCache\*"')
            run_cmd(r'del /q /f "C:\Windows\System32\FNTCACHE.DAT"')
            run_cmd('net start FontCache')

        elif t_id == "clean_iconcache" and is_active:
            iconcache = os.path.expandvars(r"%localappdata%\Microsoft\Windows\Explorer")
            run_cmd(f'del /q /f /a:h "{iconcache}\\iconcache_*.db"')
            run_cmd('ie4uinit.exe -show')

        elif t_id == "clean_chkdsk" and is_active:
            for drive_letter in ['C', 'D', 'E', 'F']:
                chk_path = f"{drive_letter}:\\"
                if os.path.exists(chk_path):
                    run_cmd(f'del /q /f /s "{chk_path}*.chk"')

        elif t_id == "clean_onedrive_temp" and is_active:
            onedrive_log = os.path.expandvars(r"%localappdata%\Microsoft\OneDrive\logs")
            onedrive_temp = os.path.expandvars(r"%localappdata%\Microsoft\OneDrive\setup\temp")
            if os.path.exists(onedrive_log): run_cmd(f'del /q /f /s "{onedrive_log}\\*"')
            if os.path.exists(onedrive_temp): run_cmd(f'del /q /f /s "{onedrive_temp}\\*"')

        elif t_id == "clean_firefox_cache" and is_active:
            ff_cache = os.path.expandvars(r"%localappdata%\Mozilla\Firefox\Profiles")
            if os.path.exists(ff_cache):
                run_cmd(f'for /d %p in ("{ff_cache}\\*.default*") do del /q /f /s "%p\\cache2\\*"')

        elif t_id == "clean_vcredist" and is_active:
            for steam_path in [r"C:\Program Files (x86)\Steam", r"C:\Program Files\Steam"]:
                redist = os.path.join(steam_path, "_CommonRedist")
                if os.path.exists(redist):
                    run_cmd(f'rmdir /s /q "{redist}"')

        elif t_id == "clean_ram" and is_active:
            if HAS_CPP_ENGINE:
                cdr_engine.OptimizeMemory_CPP()
                cdr_engine.FlushStandbyList_CPP()
            else:
                try:
                    for proc in psutil.process_iter(['pid']):
                        try:
                            handle = ctypes.windll.kernel32.OpenProcess(0x01F0FFF, False, proc.info['pid']) # type: ignore
                            if handle:
                                ctypes.windll.kernel32.SetProcessWorkingSetSize(handle, -1, -1) # type: ignore
                                ctypes.windll.kernel32.CloseHandle(handle) # type: ignore
                        except:
                            pass
                except:
                    pass

        elif t_id == "priv_advertising":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v Enabled /t REG_DWORD /d 1 /f')

        elif t_id == "priv_cortana":
            if is_active:
                run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f')
            else:
                run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 1 /f')

        elif t_id == "priv_appdiag":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy" /v LetAppsGetDiagnosticInfo /t REG_DWORD /d 2 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy" /v LetAppsGetDiagnosticInfo /f')

        elif t_id == "priv_location":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" /v Value /t REG_SZ /d Deny /f')
            else: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" /v Value /t REG_SZ /d Allow /f')

        elif t_id == "priv_camera":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /t REG_SZ /d Deny /f')
            else: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /t REG_SZ /d Allow /f')

        elif t_id == "priv_mic":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Input\Personalization\TrainedDataStore" /v HarvestContacts /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg delete "HKCU\Software\Microsoft\Input\Personalization\TrainedDataStore" /v HarvestContacts /f')

        elif t_id == "priv_activity":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v PublishUserActivities /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v PublishUserActivities /f')

        elif t_id == "priv_sync":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\SettingSync" /v DisableSettingSync /t REG_DWORD /d 2 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows\SettingSync" /v DisableSettingSync /f')

        elif t_id == "priv_smartscreen":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" /v SmartScreenEnabled /t REG_SZ /d Off /f')
            else: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" /v SmartScreenEnabled /t REG_SZ /d On /f')

        elif t_id == "priv_ceip":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\SQMClient\Windows" /v CEIPEnable /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\SQMClient\Windows" /v CEIPEnable /f')

        elif t_id == "priv_typing":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization" /v Enabled /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization" /v Enabled /t REG_DWORD /d 1 /f')

        elif t_id == "priv_wifi_sense":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config" /v AutoConnectAllowedOEM /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config" /v AutoConnectAllowedOEM /t REG_DWORD /d 1 /f')

        elif t_id == "priv_handwriting":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\InputPersonalization" /v RestrictImplicitTextCollection /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\InputPersonalization" /v RestrictImplicitTextCollection /t REG_DWORD /d 0 /f')

        elif t_id == "priv_defender_samples":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SubmitSamplesConsent /t REG_DWORD /d 2 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SubmitSamplesConsent /f')

        elif t_id == "priv_meetnow":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v HideSCAMeetNow /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v HideSCAMeetNow /f')

        elif t_id == "priv_start_web":
            if is_active:
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v BingSearchEnabled /t REG_DWORD /d 0 /f')
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v CortanaConsent /t REG_DWORD /d 0 /f')
            else:
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v BingSearchEnabled /t REG_DWORD /d 1 /f')

        elif t_id == "priv_feedback":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Siuf\Rules" /v PeriodInNanoSeconds /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Siuf\Rules" /v PeriodInNanoSeconds /t REG_DWORD /d 1 /f')

        elif t_id == "priv_tailored":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Privacy" /v TailoredExperiencesWithDiagnosticDataEnabled /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Privacy" /v TailoredExperiencesWithDiagnosticDataEnabled /t REG_DWORD /d 1 /f')

        elif t_id == "priv_news":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Feeds" /v ShellFeedsOnboardingMode /t REG_DWORD /d 2 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Feeds" /v ShellFeedsOnboardingMode /t REG_DWORD /d 0 /f')

        elif t_id == "priv_telemetry_level":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 3 /f')

        elif t_id == "priv_app_suggestions":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SilentInstalledAppsEnabled /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SilentInstalledAppsEnabled /t REG_DWORD /d 1 /f')

        elif t_id == "priv_onedrive":
            if is_active:
                run_cmd('taskkill /f /im OneDrive.exe')
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v OneDrive /t REG_SZ /d "" /f')

        elif t_id == "ui_animation":
            if is_active:
                run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f')
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 3 /f')
            else:
                run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9e3e078012000000 /f')
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 1 /f')
                
        elif t_id == "ui_classic_menu":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32" /f /ve')
            else:
                run_cmd('reg delete "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f')

        elif t_id == "ui_transparency":
            if is_active: run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v EnableTransparency /t REG_DWORD /d 0 /f')
            else: run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v EnableTransparency /t REG_DWORD /d 1 /f')

        elif t_id == "ui_darkmode":
            if is_active:
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 0 /f')
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 0 /f')
            else:
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 1 /f')

        elif t_id == "ui_shadows":
            if is_active: run_cmd(r'reg add "HKCU\Control Panel\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012028010000000 /f')
            else: run_cmd(r'reg add "HKCU\Control Panel\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9e3e078012000000 /f')

        elif t_id == "ui_show_ext":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v HideFileExt /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v HideFileExt /t REG_DWORD /d 1 /f')

        elif t_id == "ui_show_hidden":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 2 /f')

        elif t_id == "ui_taskbar_search":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v SearchboxTaskbarMode /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v SearchboxTaskbarMode /t REG_DWORD /d 1 /f')

        elif t_id == "ui_lockscreen":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Personalization" /v NoLockScreen /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows\Personalization" /v NoLockScreen /f')

        elif t_id == "ui_startup_delay":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /f')

        elif t_id == "net_autotuning":
            if is_active:
                run_cmd('netsh int tcp set global autotuninglevel=normal')
            else:
                run_cmd('netsh int tcp set global autotuninglevel=restricted')

        elif t_id == "net_nagles":
            if is_active:
                run_ps('$regPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces"; Get-ChildItem $regPath | ForEach-Object { $path = $_.PSPath; New-ItemProperty -Path $path -Name "TcpAckFrequency" -Value 1 -PropertyType DWord -Force -ErrorAction SilentlyContinue; New-ItemProperty -Path $path -Name "TCPNoDelay" -Value 1 -PropertyType DWord -Force -ErrorAction SilentlyContinue }')
            else:
                run_ps('$regPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces"; Get-ChildItem $regPath | ForEach-Object { $path = $_.PSPath; Remove-ItemProperty -Path $path -Name "TcpAckFrequency" -ErrorAction SilentlyContinue; Remove-ItemProperty -Path $path -Name "TCPNoDelay" -ErrorAction SilentlyContinue }')

        elif t_id == "net_rss":
            if is_active: run_cmd('netsh int tcp set global rss=enabled')
            else: run_cmd('netsh int tcp set global rss=default')

        elif t_id == "net_heuristics":
            if is_active: run_cmd('netsh int tcp set global heuristics=disabled')
            else: run_cmd('netsh int tcp set global heuristics=enabled')

        elif t_id == "net_smb":
            if is_active: run_cmd('sc config "LanmanWorkstation" start= disabled')
            else: run_cmd('sc config "LanmanWorkstation" start= auto')

        elif t_id == "net_ipv6":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters" /v DisabledComponents /t REG_DWORD /d 255 /f')
            else: run_cmd(r'reg delete "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters" /v DisabledComponents /f')

        elif t_id == "net_teredo":
            if is_active: run_cmd('netsh interface teredo set state disabled')
            else: run_cmd('netsh interface teredo set state default')

        elif t_id == "net_wifi_power":
            if is_active: run_ps('Get-NetAdapter | Where-Object {$_.MediaType -eq "Native 802.11"} | ForEach-Object { Disable-NetAdapterPowerManagement -Name $_.Name -ErrorAction SilentlyContinue }')

        elif t_id == "net_deliveryopt":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" /v DODownloadMode /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" /v DODownloadMode /f')

        elif t_id == "net_lso":
            if is_active: run_cmd('netsh int tcp set global lso=disabled')
            else: run_cmd('netsh int tcp set global lso=enabled')

        elif t_id == "net_qos":
            if is_active:
                run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched" /v NonBestEffortLimit /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg delete "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched" /v NonBestEffortLimit /f')

        elif t_id == "net_ecn":
            if is_active: run_cmd('netsh int tcp set global ecncapability=disabled')
            else: run_cmd('netsh int tcp set global ecncapability=enabled')

        elif t_id == "net_chimney":
            if is_active: run_cmd('netsh int tcp set global chimney=disabled')
            else: run_cmd('netsh int tcp set global chimney=enabled')

        elif t_id == "net_isatap":
            if is_active: run_cmd('netsh int ipv6 isatap set state disabled')
            else: run_cmd('netsh int ipv6 isatap set state default')

        elif t_id == "net_wpad":
            if is_active: run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Wpad" /v WpadDecision /t REG_DWORD /d 0 /f')
            else: run_cmd('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Wpad" /v WpadDecision /f')

        elif t_id == "net_dnscache":
            if is_active: run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters" /v MaxNegativeCacheTtl /t REG_DWORD /d 0 /f')
            else: run_cmd('reg delete "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters" /v MaxNegativeCacheTtl /f')

        elif t_id == "net_max_conn":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v MaxConnectionsPerServer /t REG_DWORD /d 10 /f')
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v MaxConnectionsPer1_0Server /t REG_DWORD /d 10 /f')
            else:
                run_cmd('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v MaxConnectionsPerServer /f')
                run_cmd('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v MaxConnectionsPer1_0Server /f')

        elif t_id == "game_mode":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\GameBar" /v AllowAutoGameMode /t REG_DWORD /d 1 /f')
            else:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\GameBar" /v AllowAutoGameMode /t REG_DWORD /d 0 /f')
                
        elif t_id == "game_ultimate_power":
            if is_active:
                run_cmd("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
                run_cmd("powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61")
            else:
                run_cmd("powercfg -setactive 381b4222-f694-41f0-9685-ff5bb260df2e")

        elif t_id == "game_hags":
            if is_active: run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 2 /f')
            else: run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 1 /f')

        elif t_id == "game_mmcss":
            if is_active:
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 0xFFFFFFFF /f')
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 10 /f')
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 20 /f')

        elif t_id == "game_vbs":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard" /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard" /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 1 /f')

        elif t_id == "game_mouse_accel":
            if is_active:
                run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v MouseSpeed /t REG_SZ /d 0 /f')
                run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v MouseThreshold1 /t REG_SZ /d 0 /f')
                run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v MouseThreshold2 /t REG_SZ /d 0 /f')
            else:
                run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v MouseSpeed /t REG_SZ /d 1 /f')

        elif t_id == "game_timer_res":
            if is_active:
                run_cmd('bcdedit /set disabledynamictick yes')
                run_cmd('bcdedit /set useplatformclock no')
            else:
                run_cmd('bcdedit /deletevalue disabledynamictick')
                run_cmd('bcdedit /deletevalue useplatformclock')

        elif t_id == "game_edge_bg":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Edge" /v BackgroundModeEnabled /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Edge" /v BackgroundModeEnabled /t REG_DWORD /d 1 /f')

        elif t_id == "game_fullscreen_opt":
            if is_active:
                run_cmd('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_FSEBehavior /t REG_DWORD /d 2 /f')
            else:
                run_cmd('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_FSEBehavior /t REG_DWORD /d 0 /f')

        elif t_id == "game_hpet":
            if is_active: run_cmd('bcdedit /set useplatformclock no')
            else: run_cmd('bcdedit /deletevalue useplatformclock')

        elif t_id == "game_fth":
            if is_active: run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\FTH" /v Enabled /t REG_DWORD /d 0 /f')
            else: run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\FTH" /v Enabled /t REG_DWORD /d 1 /f')

        elif t_id == "game_core_parking":
            if is_active: run_cmd('powercfg -setacvalueindex scheme_current sub_processor cpprob 100')
            else: run_cmd('powercfg -setacvalueindex scheme_current sub_processor cpprob 0')

        elif t_id == "game_steam_hardware":
            if is_active: run_cmd('reg add "HKCU\\Software\\Valve\\Steam" /v CEFRemoteDebuggingPort /t REG_DWORD /d 0 /f')
            else: run_cmd('reg delete "HKCU\\Software\\Valve\\Steam" /v CEFRemoteDebuggingPort /f')

        elif t_id == "game_discord_hw":
            if is_active: run_cmd('reg add "HKCU\\Software\\Discord" /v HardwareAcceleration /t REG_DWORD /d 0 /f')
            else: run_cmd('reg add "HKCU\\Software\\Discord" /v HardwareAcceleration /t REG_DWORD /d 1 /f')

        elif t_id == "game_sleep":
            if is_active:
                run_cmd('powercfg -x -standby-timeout-ac 0')
                run_cmd('powercfg -x -hibernate-timeout-ac 0')
            else:
                run_cmd('powercfg -x -standby-timeout-ac 30')

        elif t_id == "game_usb_suspend":
            if is_active: run_cmd('powercfg -setacvalueindex scheme_current 2a737441-1930-4402-8d77-b2bebba308a3 483a51dc-2701-4434-9005-14781555abd0 0')
            else: run_cmd('powercfg -setacvalueindex scheme_current 2a737441-1930-4402-8d77-b2bebba308a3 483a51dc-2701-4434-9005-14781555abd0 1')

        elif t_id == "game_xbox_dvr":
            if is_active:
                run_cmd('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f')
                run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR" /v AllowGameDVR /t REG_DWORD /d 0 /f')
            else:
                run_cmd('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 1 /f')

        elif t_id == "game_vr":
            if is_active: run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f')
            else: run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 20 /f')

        elif t_id == "game_discord_overlay":
            if is_active: run_cmd('reg add "HKCU\\Software\\Discord" /v OverlayEnabled /t REG_DWORD /d 0 /f')
            else: run_cmd('reg add "HKCU\\Software\\Discord" /v OverlayEnabled /t REG_DWORD /d 1 /f')

        elif t_id == "game_chrome_bg":
            if is_active: run_cmd('reg add "HKCU\\Software\\Policies\\Google\\Chrome" /v BackgroundModeEnabled /t REG_DWORD /d 0 /f')
            else: run_cmd('reg delete "HKCU\\Software\\Policies\\Google\\Chrome" /v BackgroundModeEnabled /f')

        elif t_id == "pwr_ultimate":
            if is_active:
                run_cmd("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
                run_cmd("powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61")
            else:
                run_cmd("powercfg -setactive 381b4222-f694-41f0-9685-ff5bb260df2e")

        elif t_id == "pwr_min_cpu":
            if is_active: run_cmd('powercfg -setacvalueindex scheme_current sub_processor PROCTHROTTLEMIN 100')
            else: run_cmd('powercfg -setacvalueindex scheme_current sub_processor PROCTHROTTLEMIN 5')
        
        elif t_id == "pwr_disk_timeout":
            if is_active: run_cmd('powercfg -x -disk-timeout-ac 0')
            else: run_cmd('powercfg -x -disk-timeout-ac 20')

        elif t_id == "pwr_pci_link":
            if is_active: run_cmd('powercfg -setacvalueindex scheme_current 2a737441-1930-4402-8d77-b2bebba308a3 ee12f458-a159-4ac9-a9a3-5c777286395e 0')
            else: run_cmd('powercfg -setacvalueindex scheme_current 2a737441-1930-4402-8d77-b2bebba308a3 ee12f458-a159-4ac9-a9a3-5c777286395e 1')

        elif t_id == "pwr_hibernation":
            if is_active: run_cmd('powercfg -h off')
            else: run_cmd('powercfg -h on')

        elif t_id == "pwr_throttling":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /v PowerThrottlingOff /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /f')

        elif t_id == "perf_win32_priority":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 38 /f')
            else: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 2 /f')

        elif t_id == "perf_large_cache":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v LargeSystemCache /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v LargeSystemCache /t REG_DWORD /d 0 /f')

        elif t_id == "perf_io_limit":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v IoPageLockLimit /t REG_DWORD /d 16777216 /f')
            else: run_cmd(r'reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v IoPageLockLimit /f')

        elif t_id == "perf_worker_threads":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Executive" /v AdditionalWorkerThreads /t REG_DWORD /d 16 /f')
            else: run_cmd(r'reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Executive" /v AdditionalWorkerThreads /f')

        elif t_id == "perf_wait_kill":
            if is_active: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v WaitToKillServiceTimeout /t REG_SZ /d 2000 /f')
            else: run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v WaitToKillServiceTimeout /t REG_SZ /d 5000 /f')

        elif t_id == "perf_auto_end":
            if is_active: run_cmd(r'reg add "HKCU\Control Panel\Desktop" /v AutoEndTasks /t REG_SZ /d 1 /f')
            else: run_cmd(r'reg add "HKCU\Control Panel\Desktop" /v AutoEndTasks /t REG_SZ /d 0 /f')

        elif t_id == "perf_menu_delay":
            if is_active: run_cmd(r'reg add "HKCU\Control Panel\Desktop" /v MenuShowDelay /t REG_SZ /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Control Panel\Desktop" /v MenuShowDelay /t REG_SZ /d 400 /f')

        elif t_id in ["perf_startup_delay", "ui_startup_delay"]:
            if is_active: 
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /f')
                run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /t REG_DWORD /d 0 /f')
            else:
                run_cmd(r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /f')

        elif t_id == "ui_taskbar_animations":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v TaskbarAnimations /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v TaskbarAnimations /t REG_DWORD /d 1 /f')

        elif t_id == "ui_shake_min":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v DisallowShaking /t REG_DWORD /d 1 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v DisallowShaking /t REG_DWORD /d 0 /f')

        elif t_id == "ui_snap_assist":
            if is_active: run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v SnapAssist /t REG_DWORD /d 0 /f')
            else: run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v SnapAssist /t REG_DWORD /d 1 /f')

        elif t_id == "priv_news":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Feeds" /v ShellFeedsOnboardingMode /t REG_DWORD /d 2 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Feeds" /v ShellFeedsOnboardingMode /t REG_DWORD /d 0 /f')

        elif t_id == "priv_telemetry_level":
            if is_active: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 3 /f')

        elif t_id == "priv_app_suggestions":
            if is_active: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SilentInstalledAppsEnabled /t REG_DWORD /d 0 /f')
            else: run_cmd(r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SilentInstalledAppsEnabled /t REG_DWORD /d 1 /f')


        elif t_id == "uwp_xbox" and is_active:
            # Remove for all users and remove provisioned package (system-wide)
            run_ps('Get-AppxPackage -AllUsers *Xbox* | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue')
            run_ps('Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like "*Xbox*"} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue')

        elif t_id == "uwp_bloatware" and is_active:
            # Expanded bloatware list for exhaustive removal
            bloat = ["*Zune*", "*BingNews*", "*GetHelp*", "*Solitaire*", "*People*", "*MixedReality*", "*3DBuilder*", "*SkypeApp*", "*YourPhone*", "*WindowsAlarms*", "*windowscalculator*", "*WindowsCamera*", "*windowscommunicationsapps*", "*WindowsFeedbackHub*", "*WindowsMaps*", "*SoundRecorder*", "*MicrosoftStickyNotes*", "*ZuneMusic*", "*ZuneVideo*", "*Cortana*", "*Microsoft.549981C3F5F10*", "*WebExperience*", "*Teams*", "*Getstarted*", "*OneConnect*", "*Microsoft.Wallet*", "*StorePurchaseApp*", "*PowerAutomateDesktop*", "*BingSearch*", "*Microsoft.Xbox.TCUI*", "*Microsoft.XboxGameOverlay*", "*Microsoft.XboxGamingOverlay*", "*Microsoft.XboxIdentityProvider*", "*Microsoft.XboxSpeechToTextOverlay*"]
            for b in bloat:
                run_ps(f'Get-AppxPackage -AllUsers "{b}" | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue')
                run_ps(f'Get-AppxProvisionedPackage -Online | Where-Object {{$_.DisplayName -like "{b}" -or $_.PackageName -like "{b}"}} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue')

        elif t_id == "uwp_onedrive" and is_active:
            run_cmd('taskkill /f /im OneDrive.exe')
            # Try system-level uninstaller
            run_cmd(r'%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall')
            run_cmd(r'%SystemRoot%\System32\OneDriveSetup.exe /uninstall')
            run_cmd(r'%LOCALAPPDATA%\Microsoft\OneDrive\OneDrive.exe /uninstall')
            # Deep Clean Folders
            run_cmd(r'rmdir /s /q "%LocalAppData%\Microsoft\OneDrive"')
            run_cmd(r'rmdir /s /q "%AppData%\Microsoft\OneDrive"')
            run_cmd(r'rmdir /s /q "C:\ProgramData\Microsoft OneDrive"')
            # Registry Clean (Clsid)
            run_cmd(r'reg delete "HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" /f')
            run_cmd(r'reg delete "HKEY_CLASSES_ROOT\Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" /f')

        elif t_id == "uwp_edge" and is_active:
            # Remove Edge Appx
            run_ps('Get-AppxPackage -AllUsers *MicrosoftEdge* | ForEach-Object { Remove-AppxPackage -Package $_.PackageFullName -AllUsers -ErrorAction SilentlyContinue }')
            # Aggressive Setup Uninstall
            edge_script = r"""
            $edgePath = "${env:ProgramFiles(x86)}\Microsoft\Edge\Application"
            if (Test-Path $edgePath) {
                $installer = Get-ChildItem -Path $edgePath -Filter "setup.exe" -Recurse | Select-Object -First 1
                if ($installer) {
                    Start-Process -FilePath $installer.FullName -ArgumentList "--uninstall", "--system-level", "--force-uninstall" -Wait
                }
            }
            # Remove remaining folders
            Remove-Item -Path "$env:ProgramFiles(x86)\Microsoft\Edge" -Recurse -Force -ErrorAction SilentlyContinue
            Remove-Item -Path "$env:ProgramFiles(x86)\Microsoft\EdgeUpdate" -Recurse -Force -ErrorAction SilentlyContinue
            """
            run_ps(edge_script)

        elif t_id == "kernel_mitigations":
            if is_active:
                run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v FeatureSettingsOverride /t REG_DWORD /d 3 /f')
                run_cmd(r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v FeatureSettingsOverrideMask /t REG_DWORD /d 3 /f')
            else:
                run_cmd(r'reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v FeatureSettingsOverride /f')
                run_cmd(r'reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v FeatureSettingsOverrideMask /f')

        elif t_id == "kernel_memory_comp":
            if is_active:
                run_ps("Disable-MMAgent -mc")
            else:
                run_ps("Enable-MMAgent -mc")

        elif t_id == "kernel_system_resp":
            if is_active:
                run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f')
            else:
                run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 20 /f')

        elif t_id == "ai_copilot":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\WindowsCopilot" /v TurnOffWindowsCopilot /t REG_DWORD /d 1 /f')
                run_cmd('reg add "HKLM\\Software\\Policies\\Microsoft\\Windows\\WindowsCopilot" /v TurnOffWindowsCopilot /t REG_DWORD /d 1 /f')
            else:
                run_cmd('reg delete "HKCU\\Software\\Policies\\Microsoft\\Windows\\WindowsCopilot" /v TurnOffWindowsCopilot /f')

        elif t_id == "ai_recall":
            if is_active:
                run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsAI" /v DisableRecallCapture /t REG_DWORD /d 1 /f')
            else:
                run_cmd('reg delete "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsAI" /v DisableRecallCapture /f')

        elif t_id == "telemetry_office_vs" and is_active:
            run_cmd(r'reg add "HKCU\Software\Microsoft\Office\Common\ClientTelemetry" /v DisableTelemetry /t REG_DWORD /d 1 /f')
            run_cmd(r'reg add "HKCU\Software\Microsoft\VisualStudio\Telemetry" /v TurnOffSwitch /t REG_DWORD /d 1 /f')
            
        elif t_id == "task_ceip" and is_active:
            tasks = [
                r"\Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
                r"\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask",
                r"\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip",
                r"\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
                r"\Microsoft\Windows\Application Experience\ProgramDataUpdater",
                r"\Microsoft\Windows\Application Experience\StartupAppTask",
                r"\Microsoft\Windows\Autochk\Proxy",
                r"\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector",
                r"\Microsoft\Windows\Feedback\Siuf\DmClient",
                r"\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload"
            ]
            for t in tasks:
                run_ps(f'Disable-ScheduledTask -TaskName "{t}" -ErrorAction SilentlyContinue')

        # ── GPU y Pantalla ────────────────────────────────────────────────────
        elif t_id == "gpu_hags":
            val = "1" if is_active else "0"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_nvidia_telemetry":
            if is_active:
                for svc in ["NvTelemetryContainer", "NvSvc"]:
                    run_cmd(f'sc config "{svc}" start= disabled')
                    run_cmd(f'sc stop "{svc}"')
                run_cmd('reg add "HKLM\\SOFTWARE\\NVIDIA Corporation\\NvControlPanel2\\Client" /v OptInOrOutPreference /t REG_DWORD /d 0 /f')
            else:
                run_cmd('sc config "NvTelemetryContainer" start= auto')

        elif t_id == "gpu_nvidia_power":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v PerfLevelSrc /t REG_DWORD /d 8738 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v PowerMizerEnable /t REG_DWORD /d 1 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v PowerMizerLevel /t REG_DWORD /d 1 /f')

        elif t_id == "gpu_amd_telemetry":
            if is_active:
                for svc in ["AMD Crash Defender Service", "AMD External Events Utility"]:
                    run_cmd(f'sc config "{svc}" start= disabled')

        elif t_id == "gpu_amd_power":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v EnableUlps /t REG_DWORD /d 0 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v PP_SclkDeepSleepDisable /t REG_DWORD /d 1 /f')

        elif t_id == "gpu_preemption":
            val = "0" if is_active else "2"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler" /v EnablePreemption /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_mpo":
            val = "0" if is_active else "2"
            run_cmd(f'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\Dwm" /v OverlayTestMode /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_dwm_priority":
            if is_active:
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\DisplayPostProcessing" /v Priority /t REG_DWORD /d 8 /f')
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\DisplayPostProcessing" /v "Scheduling Category" /t REG_SZ /d High /f')

        elif t_id == "gpu_disable_fullscreen_opt":
            val = "1" if is_active else "0"
            run_cmd(f'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 2 /f')
            run_cmd(f'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_HonorUserFSEBehaviorMode /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_freesync_vsync_off":
            if is_active:
                run_cmd('reg add "HKCU\\SOFTWARE\\Microsoft\\DirectX\\UserGpuPreferences" /v DirectXUserGlobalSettings /t REG_SZ /d SwapEffectUpgradeEnable=0;VRROptimizeEnable=1; /f')

        elif t_id == "gpu_gpu_priority":
            val = "8" if is_active else "2"
            run_cmd(f'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v GpuPriority /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_perf_registry":
            if is_active:
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f')
                run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f')

        elif t_id == "gpu_reduce_dpc":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v TdrDelay /t REG_DWORD /d 10 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v TdrDdiDelay /t REG_DWORD /d 10 /f')

        elif t_id == "gpu_pci_express_max":
            if is_active:
                run_ps('powercfg /setacvalueindex SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 ee12f906-d277-404b-b6da-e5fa1a576df5 0')
                run_ps('powercfg /setdcvalueindex SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 ee12f906-d277-404b-b6da-e5fa1a576df5 0')
                run_ps('powercfg /apply SCHEME_CURRENT')

        elif t_id == "gpu_cache_clean":
            if is_active:
                import tempfile
                nv_cache = os.path.expandvars(r"%localappdata%\NVIDIA\DXCache")
                amd_cache = os.path.expandvars(r"%localappdata%\AMD\DxCache")
                vk_cache = os.path.expandvars(r"%localappdata%\vulkan")
                for p in [nv_cache, amd_cache, vk_cache]:
                    if os.path.exists(p):
                        run_cmd(f'rmdir /s /q "{p}"')

        elif t_id == "gpu_night_light_off":
            if is_active:
                run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\CloudStore\\Store\\DefaultAccount\\Current\\default$windows.data.bluelightreduction.settings" /v Data /t REG_BINARY /d 4300000043000000 /f')

        elif t_id == "gpu_disable_mpv":
            val = "0" if is_active else "1"
            run_cmd(f'reg add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v D3D12_ENABLE_UNSAFE_COMMAND_BUFFER_REUSE /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_gsync_compat":
            val = "1" if is_active else "0"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v GsyncMode /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_vram_paging":
            val = "0" if is_active else "1"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm\\Global\\nvStraps" /v EnableGpuPagingSaving /t REG_DWORD /d {val} /f')

        elif t_id == "gpu_shader_cache":
            if is_active:
                run_cmd(r'reg add "HKLM\SOFTWARE\Microsoft\Direct3D" /v ShaderCachePath /t REG_SZ /d C:\ShaderCache /f')
                os.makedirs(r"C:\ShaderCache", exist_ok=True)

        # ── Kernel y Avanzado ─────────────────────────────────────────────────
        elif t_id == "kern_bcdedit_inc":
            if is_active:
                run_cmd('bcdedit /set useplatformclock true')
                run_cmd('bcdedit /set disabledynamictick yes')
            else:
                run_cmd('bcdedit /deletevalue useplatformclock')
                run_cmd('bcdedit /set disabledynamictick no')

        elif t_id == "kern_timer_resolution":
            if is_active:
                run_cmd('bcdedit /set tscsyncpolicy enhanced')
                run_cmd('bcdedit /set useplatformclock true')
                run_cmd('bcdedit /set disabledynamictick yes')
            else:
                run_cmd('bcdedit /deletevalue tscsyncpolicy')

        elif t_id == "kern_svc_host_split":
            if is_active:
                ram_bytes = psutil.virtual_memory().total # type: ignore
                run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v SvcHostSplitThresholdInKB /t REG_DWORD /d {ram_bytes // 1024} /f')
            else:
                run_cmd('reg delete "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v SvcHostSplitThresholdInKB /f')

        elif t_id == "kern_disable_ntfs_time":
            val = "1" if is_active else "0"
            run_cmd(f'fsutil behavior set DisableLastAccess {val}')

        elif t_id == "kern_mft_boost":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\FileSystem" /v NtfsMftZoneReservation /t REG_DWORD /d 2 /f')

        elif t_id == "kern_disable_8dot3":
            val = "1" if is_active else "0"
            run_cmd(f'fsutil behavior set disable8dot3 {val}')

        elif t_id == "kern_pcie_latency":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PnP" /v PciLatencyTimer /t REG_DWORD /d 32 /f')

        elif t_id == "kern_critical_worker":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Executive" /v AdditionalCriticalWorkerThreads /t REG_DWORD /d 2 /f')

        elif t_id == "kern_irq_priority_gpu":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v IRQ8Priority /t REG_DWORD /d 1 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v IRQ16Priority /t REG_DWORD /d 1 /f')

        elif t_id == "kern_prio_separation":
            val = "38" if is_active else "2"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d {val} /f')

        elif t_id == "kern_no_ntfs_compress":
            if is_active:
                run_cmd('compact /u /s /a /i /f C:\\Windows')

        elif t_id == "kern_disable_spectre":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v FeatureSettingsOverride /t REG_DWORD /d 3 /f')
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v FeatureSettingsOverrideMask /t REG_DWORD /d 3 /f')
            else:
                run_cmd('reg delete "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v FeatureSettingsOverride /f')
                run_cmd('reg delete "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v FeatureSettingsOverrideMask /f')

        elif t_id == "kern_idle_disable":
            val = "1" if is_active else "0"
            run_cmd(f'powercfg /setacvalueindex SCHEME_CURRENT SUB_PROCESSOR IDLEDISABLE {val}')
            run_cmd('powercfg /apply SCHEME_CURRENT')

        elif t_id == "kern_large_page":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v LargePageMinimum /t REG_DWORD /d 0 /f')

        elif t_id == "kern_lt_memory":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v LockPagesInMemory /t REG_DWORD /d 1 /f')
            else:
                run_cmd('reg delete "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v LockPagesInMemory /f')

        elif t_id == "kern_irpstack":
            val = "20" if is_active else "15"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters" /v IRPStackSize /t REG_DWORD /d {val} /f')

        elif t_id == "kern_pfn_list":
            if is_active:
                try:
                    ctypes.windll.ntdll.NtSetSystemInformation(18, ctypes.byref(ctypes.c_ulong(0)), ctypes.sizeof(ctypes.c_ulong)) # type: ignore
                except Exception:
                    pass

        elif t_id == "kern_affinity_interrupt":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v IRQ0Priority /t REG_DWORD /d 1 /f')

        elif t_id == "kern_disable_psr":
            val = "0" if is_active else "1"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e968-e325-11ce-bfc1-08002be10318}}\\0000" /v EnablePSR /t REG_DWORD /d {val} /f')

        elif t_id == "kern_registry_size":
            if is_active:
                run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v RegistrySizeLimit /t REG_DWORD /d 4294967295 /f')

        # ── Extra DNS ──────────────────────────────────────────────────────────
        elif t_id == "net_dns_cloudflare" and is_active:
            run_ps('Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | ForEach-Object { Set-DnsClientServerAddress -InterfaceIndex $_.InterfaceIndex -ServerAddresses "1.1.1.1","1.0.0.1" }')

        elif t_id == "net_dns_google" and is_active:
            run_ps('Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | ForEach-Object { Set-DnsClientServerAddress -InterfaceIndex $_.InterfaceIndex -ServerAddresses "8.8.8.8","8.8.4.4" }')

        # ── Extra Power ────────────────────────────────────────────────────────
        elif t_id == "pwr_cpu_boost":
            val = "2" if is_active else "0"
            run_cmd(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\be337238-0d82-4146-a960-4f3749d470c7" /v Attributes /t REG_DWORD /d 0 /f')
            run_cmd(f'powercfg /setacvalueindex SCHEME_CURRENT SUB_PROCESSOR PERFBOOSTMODE {val}')
            run_cmd('powercfg /apply SCHEME_CURRENT')

        elif t_id == "pwr_adaptive_brightness":
            val = "0" if is_active else "1"
            run_cmd(f'powercfg /setacvalueindex SCHEME_CURRENT SUB_VIDEO ADAPTBRIT {val}')
            run_cmd('powercfg /apply SCHEME_CURRENT')

        elif t_id == "pwr_usb_hub_suspend":
            val = "0" if is_active else "1"
            run_cmd(f'powercfg /setacvalueindex SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 0853a681-27c8-4100-a2fd-82013e970683 {val}')
            run_cmd('powercfg /apply SCHEME_CURRENT')

        # ── Individual UWP Apps Removal ───────────────────────────────────────
        elif t_id.startswith("uwp_") and is_active:
            uwp_map = {
                "uwp_3dbuilder": "*3DBuilder*", "uwp_alarms": "*WindowsAlarms*", "uwp_calculator": "*windowscalculator*",
                "uwp_camera": "*WindowsCamera*", "uwp_communications": "*windowscommunicationsapps*", "uwp_feedback": "*WindowsFeedbackHub*",
                "uwp_gethelp": "*GetHelp*", "uwp_maps": "*WindowsMaps*", "uwp_mixedreality": "*MixedReality.Portal*",
                "uwp_people": "*People*", "uwp_photos": "*Photos*", "uwp_skype": "*SkypeApp*",
                "uwp_solitaire": "*SolitaireCollection*", "uwp_soundrecorder": "*SoundRecorder*", "uwp_stickynotes": "*MicrosoftStickyNotes*",
                "uwp_weather": "*BingWeather*", "uwp_yourphone": "*YourPhone*"
            }
            app_id = uwp_map.get(t_id)
            if app_id:
                run_ps(f'Get-AppxPackage -AllUsers "{app_id}" | ForEach-Object {{ Remove-AppxPackage -Package $_.PackageFullName -AllUsers -ErrorAction SilentlyContinue }}')
                run_ps(f'Get-AppxProvisionedPackage -Online | Where-Object {{$_.DisplayName -like "{app_id}" -or $_.PackageName -like "{app_id}"}} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue')

        # ── OPTIMIZACIONES EXTREMAS (Nuclear Mode) ────────────────────────────
        elif t_id == "ext_super_nuclear" and is_active:
            # 1. SVCHOST MERGING (The most effective for process count)
            # This forces all service instances into a single svchost process.
            run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v SvcHostSplitThresholdInKB /t REG_DWORD /d 4294967295 /f')
            
            # 2. MASSIVE SERVICE STRIPPING (Optimized for Gaming Stability)
            # Removed critical services: Appinfo (UAC), Schedule (Task Scheduler), 
            # NlaSvc/NetProfM (Internet connectivity awareness), and BrokerInfrastructure.
            super_svcs = [
                "DusmSvc", "WdNisSvc", "WinDefend", "SecurityHealthService", 
                "SDRSVC", "WbioSrvc", "FontCache", "Stisvc",
                "ShellHWDetection", "WSearch", "SysMain", "PcaSvc", 
                "DiagTrack", "DPS", "WdiServiceHost", "WdiSystemHost", 
                "WerSvc", "Spooler", "MapsBroker", "TabletInputService"
            ]
            for s in super_svcs:
                run_cmd(f'sc stop "{s}"')
                run_cmd(f'sc config "{s}" start= disabled')

            # 3. DISABLING BACKGROUND APPS (Essential for reducing process count)
            run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppPrivacy" /v LetAppsRunInBackground /t REG_DWORD /d 2 /f')

            # 4. MASSIVE SCHEDULED TASKS DISABLING
            tasks_to_kill = [
                "Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser",
                "Microsoft\\Windows\\Application Experience\\ProgramDataUpdater",
                "Microsoft\\Windows\\Autochk\\Proxy",
                "Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator",
                "Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip",
                "Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector",
                "Microsoft\\Windows\\Maintenance\\WinSAT",
                "Microsoft\\Windows\\Power Efficiency Diagnostics\\AnalyzeSystem",
                "Microsoft\\Windows\\Shell\\FamilySafetyMonitor",
                "Microsoft\\Windows\\WindowsUpdate\\Scheduled Start",
                "Microsoft\\Windows\\UpdateOrchestrator\\Schedule Scan"
            ]
            for task in tasks_to_kill:
                run_cmd(f'schtasks /change /tn "{task}" /disable')

            # 5. COMPONENT TERMINATION
            killer_list = ["RuntimeBroker.exe", "BackgroundTransferHost.exe", "SmartScreen.exe", "SearchHost.exe", "StartMenuExperienceHost.exe"]
            for p in killer_list:
                run_cmd(f'taskkill /F /IM "{p}" /T')

        elif t_id == "ext_nuclear_services" and is_active:
            nuclear_svcs = [
                "AppReadiness", "AppvClient", "AssignedAccessManagerSvc", "AxInstSV", "BDESVC",
                "BthAvctpSvc", "bthserv", "CDPSvc", "CertPropSvc", "ClipSVC", "DialogBlockingService",
                "DispBrokerDesktopSvc", "Dot3svc", "DsRoleSvc", "EntAppStoreSvc", "fhsvc", "FileSyncSvc",
                "FrameServer", "GraphicsPerfSvc", "hidserv", "HvHost", "icssvc", "IpxlatCfgSvc",
                "LxssManager", "MapsBroker", "MessagingService", "NaturalAuthentication", "NcaSvc",
                "NetTcpPortSharing", "PhoneSvc", "PimIndexMaintenanceSvc", "PrintWorkflowUserSvc",
                "ProjectorSvc", "QWAVE", "RasAuto", "RasMan", "RemoteAccess", "RemoteRegistry",
                "RetailDemo", "SensorDataService", "SensorService", "SensrSvc", "SessionEnv",
                "SharedRealitySvc", "SharingService", "ShellHWDetection", "SmsRouter", "SNMPTRAP",
                "Spooler", "SSDPSRV", "StiSvc", "SysMain", "TabletInputService", "Telephony",
                "Themes", "TieringEngineService", "TimeBrokerSvc", "TrkWks", "UevAgentService",
                "upnphost", "VSS", "W32Time", "WalletService", "WbioSrvc",
                "WdiServiceHost", "WdiSystemHost", "Wecsvc", "WerSvc", "WFDSConMgrSvc",
                "WiaRpc", "wisvc", "WlanSvc", "WManSvc", "WpcMonSvc", "WpnService",
                "wuauserv", "WwanSvc", "XblAuthManager", "XblGameSave", "XboxGipSvc", "XboxNetApiSvc"
            ]
            for s in nuclear_svcs:
                run_cmd(f'sc stop "{s}"')
                run_cmd(f'sc config "{s}" start= disabled')

        elif t_id == "ext_minimalist" and is_active:
            run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f')
            run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f')
            run_cmd('reg add "HKCU\\Control Panel\\Desktop\\WindowMetrics" /v MinAnimate /t REG_SZ /d 0 /f')
            run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v TaskbarAnimations /t REG_DWORD /d 0 /f')
            run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\DWM" /v EnableAeroPeek /t REG_DWORD /d 0 /f')
            run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\DWM" /v AlwaysHibernateThumbnails /t REG_DWORD /d 0 /f')

        elif t_id == "ext_defender_kill" and is_active:
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f')
            run_cmd('sc config "WinDefend" start= disabled')
            run_cmd('sc config "SecurityHealthService" start= disabled')

        elif t_id == "ext_uwp_kill_all" and is_active:
            bloat_all = [
                "*Xbox*", "*BingNews*", "*BingWeather*", "*GetHelp*", "*Solitaire*",
                "*People*", "*MixedReality*", "*3DBuilder*", "*SkypeApp*", "*YourPhone*",
                "*WindowsAlarms*", "*windowscalculator*", "*WindowsCamera*",
                "*windowscommunicationsapps*", "*WindowsFeedbackHub*", "*WindowsMaps*",
                "*SoundRecorder*", "*MicrosoftStickyNotes*", "*ZuneMusic*", "*ZuneVideo*",
                "*Cortana*", "*Microsoft.549981C3F5F10*", "*WebExperience*", "*Teams*"
            ]
            for b in bloat_all:
                run_ps(f'Get-AppxPackage -AllUsers "{b}" | ForEach-Object {{ Remove-AppxPackage -Package $_.PackageFullName -AllUsers -ErrorAction SilentlyContinue }}')
                run_ps(f'Get-AppxProvisionedPackage -Online | Where-Object {{$_.DisplayName -like "{b}" -or $_.PackageName -like "{b}"}} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue')

        elif t_id == "ext_firewall_off" and is_active:
            run_cmd('netsh advfirewall set allprofiles state off')

        elif t_id == "ext_update_dead" and is_active:
            run_cmd('sc config "wuauserv" start= disabled')
            run_cmd('sc stop "wuauserv"')
            run_cmd('sc config "UsoSvc" start= disabled')
            run_cmd('sc stop "UsoSvc"')
            run_cmd('sc config "WaaSMedicSvc" start= disabled')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate" /v DisableWindowsUpdateAccess /t REG_DWORD /d 1 /f')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" /v NoAutoUpdate /t REG_DWORD /d 1 /f')
            run_cmd('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" /v AUOptions /t REG_DWORD /d 1 /f')

        if progress_callback:
            progress_callback(int((count / total) * 100))

    run_cmd('gpupdate /force')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() # type: ignore
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # type: ignore
