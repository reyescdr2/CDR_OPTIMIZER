# type: ignore
import typing
import psutil # type: ignore
import time
import threading
import ctypes
import os
import sys

# JUEGOS CONOCIDOS PARA OPTIMIZAR (Añadir más según necesidad)
KNOWN_GAMES = [
    "valorant-win64-shipping.exe",
    "cs2.exe",
    "fortniteclient-win64-shipping.exe",
    "cod.exe",
    "r5apex.exe",
    "gta5.exe",
    "overwatch.exe",
    "rainbowsix.exe",
    "dota2.exe",
    "league of legends.exe",
    "tarkov.exe",
    "robloxplayerbeta.exe",
    "minecraft.windows.exe",
    "bloodstrike.exe",
    "launcher.exe"
]

@typing.no_type_check
class ProcessLassoClone:
    thread: typing.Any = None
    active_game_pid: typing.Optional[int] = None
    
    def __init__(self):
        self.running = False
        self.thread = None
        self.active_game_pid = None
        
        # Guardaremos el ID real de la CPU para manipular afinidad.
        # CPU 0 es generalmente usada por Windows, queremos evitar que el juego la use 
        # para prevenir stuttering si es posible (en CPUs de más de 4 núcleos).
        self.cpu_count = psutil.cpu_count(logical=True) or 4
        self.isolate_cpu0 = self.cpu_count > 4
        
    def start(self):
        if self.running: return
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
        
    def stop(self):
        self.running = False
        if self.active_game_pid:
            self._restore_process(self.active_game_pid)
            
    def _purge_standby_list(self):
        """Usa llamadas de API no documentadas de Windows para purgar la RAM en espera"""
        try:
            # Recrea el comportamiento de EmptyStandbyList.exe
            # PS: Requiere privilegios de administrador que el Optimizador ya tiene.
            kernel32 = ctypes.windll.kernel32 # type: ignore
            psapi = ctypes.windll.psapi # type: ignore
            
            # Privilege escalation logic here for SeProfileSingleProcessPrivilege
            # (Simplified for this version - a real implementation needs deep Advapi32 calls)
            
            # Purge working sets of all apps
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['pid'] != 0 and proc.info['pid'] != 4:  # Skip System Idle and System
                    try:
                        handle = kernel32.OpenProcess(0x01F0FFF, False, proc.info['pid'])
                        if handle:
                            kernel32.SetProcessWorkingSetSize(handle, -1, -1)
                            kernel32.CloseHandle(handle)
                    except:
                        pass
        except Exception as e:
            print(f"[GameBooster] Error purging RAM: {e}")

    def _optimize_process(self, pid):
        try:
            proc = psutil.Process(pid)
            
            # 1. Prioridad ALTA (Evitar Tiempo Real, causa cuelgues de mouse/teclado)
            proc.nice(psutil.HIGH_PRIORITY_CLASS)
            
            # 2. Afinidad de CPU
            if self.isolate_cpu0:
                # Quitar CPU 0 (normalmente índice 0) para que el juego use el resto
                new_affinity = list(range(1, self.cpu_count))
                try:
                    proc.cpu_affinity(new_affinity)
                except Exception as e:
                    print(f"[GameBooster] Couldn't set affinity: {e}")
                    
            print(f"[GameBooster] Orquestado PID {pid} ({proc.name()}) para Máximo Rendimiento.")
            return True
        except Exception as e:
             print(f"[GameBooster] Error optimizando {pid}: {e}")
             return False

    def _restore_process(self, pid):
         try:
             proc = psutil.Process(pid)
             proc.nice(psutil.NORMAL_PRIORITY_CLASS)
             if self.isolate_cpu0:
                 proc.cpu_affinity(list(range(self.cpu_count)))
             print(f"[GameBooster] Restaurado PID {pid}.")
         except:
             pass

    def _monitor_loop(self):
        while self.running:
            try:
                # Buscar juegos corriendo
                game_found = False
                for proc in psutil.process_iter(['name', 'pid']):
                    name = proc.info['name']
                    if name and name.lower() in KNOWN_GAMES:
                        pid = proc.info['pid']
                        
                        if self.active_game_pid != pid:
                            # ¡Nuevo juego detectado!
                            print(f"[GameBooster] JUEGO DETECTADO: {name}")
                            
                            # Si había otro juego antes, restaurarlo
                            if self.active_game_pid:
                                self._restore_process(self.active_game_pid)
                            
                            # Purgar RAM al iniciar el juego
                            self._purge_standby_list()
                            
                            # Optimizar el nuevo juego
                            if self._optimize_process(pid):
                                self.active_game_pid = pid
                                
                        game_found = True
                        break # Solo optimizar un juego a la vez
                        
                if not game_found and self.active_game_pid:
                    # El juego se cerró
                    print("[GameBooster] Juego cerrado. Restaurando...")
                    self.active_game_pid = None
                    self._purge_standby_list() # Limpiar RAM tras jugar
                    
            except Exception as e:
                pass
                
            time.sleep(5) # Revisar cada 5 segundos

# Instancia global para ser usada por main.py / optimizer_core.py
booster_instance = ProcessLassoClone()
