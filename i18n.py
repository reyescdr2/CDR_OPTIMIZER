# type: ignore
import typing
import ctypes
import os
import sys
from typing import Any, Dict, List

try:
    from i18n_data.tweaks_es import get_tweaks_es # type: ignore
except ImportError:
    get_tweaks_es = None
try:
    from i18n_data.tweaks_en import get_tweaks_en # type: ignore
except ImportError:
    get_tweaks_en = None
try:
    from i18n_data.tweaks_pt import get_tweaks_pt # type: ignore
except ImportError:
    get_tweaks_pt = None
try:
    from i18n_data.tweaks_fr import get_tweaks_fr # type: ignore
except ImportError:
    get_tweaks_fr = None
try:
    from i18n_data.tweaks_de import get_tweaks_de # type: ignore
except ImportError:
    get_tweaks_de = None
try:
    from i18n_data.tweaks_it import get_tweaks_it # type: ignore
except ImportError:
    get_tweaks_it = None
try:
    from i18n_data.tweaks_zh import get_tweaks_zh # type: ignore
except ImportError:
    get_tweaks_zh = None
try:
    from i18n_data.tweaks_ru import get_tweaks_ru # type: ignore
except ImportError:
    get_tweaks_ru = None

translations = {
    "es": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 Usuario:",
        "ram_label": "RAM:",
        "disk_label": "Disco C:",
        "cat_system": "SISTEMA",
        "cat_clean": "LIMPIEZA",
        "cat_privacy": "PRIVACIDAD",
        "cat_ui": "INTERFAZ",
        "cat_net": "RED",
        "cat_gaming": "GAMING",
        "cat_power": "ENERGÍA",
        "cat_gpu": "GRÁFICOS",
        "cat_kernel": "KERNEL",
        "cat_extreme": "EXTREMO",
        "cat_util": "HERRAMIENTAS",
        "cat_pro": "PERSONALIZAR",
        "cat_help": "AYUDA",
        "credits_main": """CRÉDITOS

Desarrollo y optimización: CDR Development
Motor del optimizador: CDR Core Engine
Interfaz y diseño: CustomTinker UI
Traducciones: Equipo Global CDR
Fondos animados: @spiderlilyedits (TikTok)""",
        "engine_title": "EJEMPLO DE FUNCIONAMIENTO",
        "engine_info": """CDR Optimizer incluye más de 220 opciones organizadas en 13 categorías.
Cada ajuste está diseñado para mejorar rendimiento, reducir latencia y optimizar el sistema de forma avanzada.

Aquí un resumen simplificado de algunas funciones clave:

⸻

⚙️ SISTEMA
    •    Desactiva servicios innecesarios y telemetría.
    •    Optimiza procesos del kernel.
    •    Reduce consumo de recursos en segundo plano.

🧹 LIMPIEZA
    •    Libera memoria RAM.
    •    Elimina caché y archivos temporales.
    •    Limpia registros y datos residuales.

🛡️ PRIVACIDAD
    •    Reduce envío de datos de diagnóstico.
    •    Desactiva rastreo en segundo plano.
    •    Limita servicios de ubicación.

🎨 INTERFAZ
    •    Reduce animaciones y retrasos.
    •    Mejora tiempos de respuesta.
    •    Aplica ajustes visuales optimizados.

🌐 RED
    •    Optimiza la pila TCP/IP.
    •    Reduce latencia en juegos online.
    •    Configura DNS de baja latencia.

🎮 GAMING
    •    Prioriza procesos de juegos.
    •    Reduce input lag.
    •    Optimiza temporizadores del sistema.""",
        "apply_btn": "🔥 APLICAR",
        "msg_success_title": "ÉXITO",
        "msg_success_body": "¡Configuración inyectada de forma inteligente al sistema!\nRecomendamos reiniciar la PC para que los cambios de registro y servicios surtan efecto completo.",
        "msg_confirm_title": "Confirmación de Cambios",
        "msg_confirm_body": "🔧 CDR OPTIMIZER aplicará su lógica inteligente:\n\nLos switches encendidos (ROJO) representarán opciones OPTIMIZADAS/DESACTIVADAS para mejorar el rendimiento.\nLos apagados (GRIS) se revertirán al estado NORMAL de Windows.\n\n¿Desea inyectar los cambios ahora?",
        "help_title": "INFO: Detalles de Optimización",
        "driver_btn": "🔍 DRIVERS",
        "driver_ok": "✅ Todos los drivers parecen estar funcionando correctamente según WMI.",
        "driver_err": "⚠️ Se encontraron dispositivos con códigos de error/advertencia:\n\n",
        "laptop_warn": "🔋 MODO LAPTOP DETECTADO:\nSe han ajustado las sugerencias y ocultado o mitigado configuraciones de energía que dañarían tu batería.",
        "driver_ask_fix": "¿Quieres que CDR Optimizer intente reparar e instalar estos controladores automáticamente reiniciándolos a bajo nivel?\nEsto tomará unos segundos.",
        "driver_fix_success": "Se ha enviado la orden de reparación PnP a Windows. Comprueba nuevamente si el error persiste.",
        "status_label": "ESTADO:",
        "status_ready": "LISTO",
        "status_working": "TRABAJANDO",
        "spider_credits": "@SPIDERLILYEDITS",
        "reyes_credits": "CDR by REYES",
        "btn_spider_tiktok": "tiktok 🎵",
        "btn_spider_youtube": "youtube ▶️",
        "btn_reyes_tiktok": "tiktok 🎵",
        "btn_reyes_ig": "instagram 📸",
        "admin_title": "Permisos de Administrador",
        "admin_body": "Por favor, ejecuta el Optimizador como Administrador.\nHaz clic derecho en el archivo y selecciona 'Ejecutar como administrador'."
    },
    "en": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 User:",
        "ram_label": "RAM:",
        "disk_label": "C: Drive:",
        "cat_system": "SYSTEM",
        "cat_clean": "CLEANUP",
        "cat_privacy": "PRIVACY",
        "cat_ui": "INTERFACE",
        "cat_net": "NETWORK",
        "cat_gaming": "GAMING",
        "cat_power": "POWER",
        "cat_gpu": "GRAPHICS",
        "cat_kernel": "KERNEL",
        "cat_extreme": "EXTREME",
        "cat_util": "TOOLS",
        "cat_pro": "CUSTOMIZE",
        "cat_help": "HELP",
        "credits_main": """Development & Optimization: CDR Development
Optimization Engine: CDR Core Engine
Interface & Design: CustomTinker UI
Translations: Global CDR Team""",
        "engine_title": "OPERATING EXAMPLE",
        "engine_info": """CDR Optimizer includes 220 technical options organized into 13 low-level categories, designed to maximize pure hardware performance.

System Capabilities:

• Aggressive telemetry blocking & unnecessary services.
• Deep hygiene of temporary files & volatile cache.
• TCP/IP stack tuning for ultra-low latency.
• Real-time execution profiles for gaming environments.
• Micro-parameter tuning in Kernel and Registry.""",
        "apply_btn": "🔥 APPLY",
        "msg_success_title": "SUCCESS",
        "msg_success_body": "Configuration smartly injected into the system!\nRestarting your PC is highly recommended for registry and service changes to take full effect.",
        "msg_confirm_title": "Confirm Changes",
        "msg_confirm_body": "🔧 CDR OPTIMIZER will apply its smart logic:\n\nSwitches turned ON (RED) represent OPTIMIZED/DISABLED features to boost performance.\nSwitches turned OFF (GREY) will revert to NORMAL Windows defaults.\n\nProceed to inject changes now?",
        "help_title": "INFO: Optimization Details",
        "driver_btn": "🔍 DRIVERS",
        "driver_ok": "✅ All drivers appear to be working correctly according to WMI.",
        "driver_err": "⚠️ Devices with error/warning codes were found:\n\n",
        "laptop_warn": "🔋 LAPTOP MODE DETECTED:\nSuggestions have been adjusted and power settings that could drain your battery have been hidden or mitigated.",
        "driver_ask_fix": "Would you like CDR Optimizer to attempt automatic repair by restarting these devices at a low level?\nThis will take a few seconds.",
        "driver_fix_success": "PnP repair command sent to Windows. Check again to see if the error persists.",
        "status_label": "STATUS:",
        "status_ready": "READY",
        "status_working": "WORKING",
        "spider_credits": "\n\nAnimated backgrounds: @spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "Administrator Permissions",
        "admin_body": "Please run the Optimizer as Administrator.\nRight-click the file and select 'Run as administrator'."
    },
    "pt": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 Usuário:",
        "ram_label": "RAM:",
        "disk_label": "Disco C:",
        "cat_system": "SISTEMA",
        "cat_clean": "LIMPEZA",
        "cat_privacy": "PRIVACIDADE",
        "cat_ui": "INTERFACE",
        "cat_net": "REDE",
        "cat_gaming": "GAMING",
        "cat_power": "ENERGIA",
        "cat_gpu": "GRÁFICOS",
        "cat_kernel": "KERNEL",
        "cat_extreme": "EXTREMO",
        "cat_util": "FERRAMENTAS",
        "cat_pro": "PERSONALIZAÇÃO",
        "cat_help": "AJUDA",
        "credits_main": """Desenvolvimento: CDR Development
Motor: CDR Core Engine
Design: CustomTinker UI
Traduções: Equipo Global de CDR""",
        "engine_title": "EXEMPLO OPERACIONAL",
        "engine_info": """CDR Optimizer inclui 220 opções organizadas em 13 categorias, projetadas para melhorar o desempenho do sistema.""",
        "apply_btn": "🔥 APLICAR",
        "msg_success_title": "SUCESSO",
        "msg_success_body": "Configuracao injetada de forma inteligente no sistema!\nRecomendamos reiniciar o PC para que as alteracoes tenham efeito total.",
        "msg_confirm_title": "Confirmar Alteracoes",
        "msg_confirm_body": "🔧 O CDR OPTIMIZER aplicara sua logica inteligente:\n\nSwitches ON (VERMELHO) sao recursos OTIMIZADOS/DESATIVADOS.\nSwitches OFF (CINZA) retornarao ao padrao do Windows.\n\nDeseja injetar as alteracoes agora?",
        "help_title": "INFO: Detalhes da Otimizacao",
        "driver_btn": "🔍 DRIVERS",
        "driver_ok": "✅ Todos os drivers parecem estar funcionando corretamente.",
        "driver_err": "⚠️ Dispositivos com erros foram encontrados:\n\n",
        "laptop_warn": "🔋 MODO LAPTOP DETECTADO:\nConfiguracoes de energia que poderiam descarregar sua bateria foram ajustadas.",
        "driver_ask_fix": "Gostaria de tentar reparar esses drivers automaticamente reiniciando os dispositivos?\nIsso levara alguns segundos.",
        "driver_fix_success": "O comando de reparacao PnP foi enviado para o Windows. Verifique novamente se o erro persiste.",
        "status_label": "STATUS:",
        "status_ready": "PRONTO",
        "status_working": "TRABALHANDO",
        "spider_credits": "\n\nFundos animados: @spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "Permissões de Administrador",
        "admin_body": "Por favor, execute o Otimizador como Administrador.\nClique com o botão direito no arquivo e selecione 'Executar como administrador'."
    },
    "fr": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 Utilisateur:",
        "ram_label": "RAM:",
        "disk_label": "Disque C:",
        "cat_system": "SYSTÈME",
        "cat_clean": "NETTOYAGE",
        "cat_privacy": "VIE PRIVÉE",
        "cat_ui": "INTERFACE",
        "cat_net": "RÉSEAU",
        "cat_gaming": "GAMING",
        "cat_power": "ÉNERGIE",
        "cat_gpu": "GRAPHIQUES",
        "cat_kernel": "KERNEL",
        "cat_extreme": "EXTRÊME",
        "cat_util": "OUTILS",
        "cat_pro": "PERSONNALISER",
        "cat_help": "AIDE",
        "credits_main": """Développement : CDR Development
Moteur d'optimisation : CDR Core Engine
Interface : CustomTinker UI
Traductions : Équipe Globale CDR""",
        "engine_title": "EXEMPLE DE FONCTIONNEMENT",
        "engine_info": """CDR Optimizer comprend 220 options techniques organisées en 13 catégories de bas niveau, conçues pour maximiser les performances pures du matériel.""",
        "apply_btn": "🔥 APPLIQUER",
        "msg_success_title": "SUCCES",
        "msg_success_body": "Configuration injectee avec succes dans le systeme!\nLe redemarrage du PC est recommande pour appliquer toutes les modifications.",
        "msg_confirm_title": "Confirmer les Modifications",
        "msg_confirm_body": "🔧 CDR OPTIMIZER appliquera sa logique intelligente:\n\nLes interrupteurs ON (ROUGE) representent des fonctionnalites OPTISEES/DESACTIVEES.\nLes interrupteurs OFF (GRIS) reviendront aux parametres par defaut de Windows.\n\nAppliquer les modifications maintenant?",
        "help_title": "INFO: Details d'Optimisation",
        "driver_btn": "🔍 PILOTES",
        "driver_ok": "✅ Tous les pilotes semblent fonctionner correctamente.",
        "driver_err": "⚠️ Des peripheriques avec des erreurs ont ete trouves:\n\n",
        "laptop_warn": "🔋 MODE PORTABLE DETECTE:\nLes parametres d'alimentation qui pourraient decharger votre batterie ont ete ajustes.",
        "driver_ask_fix": "Voulez-vous essayer de reparer automatiquement ces pilotes en redemarrant les peripheriques?\nCela prendra quelques secondes.",
        "driver_fix_success": "La commande de reparation PnP a ete envoyee a Windows. Verifiez a nouveau si l'error persiste.",
        "status_label": "STATUT:",
        "status_ready": "PRET",
        "status_working": "TRAVAIL",
        "spider_credits": "\n\nFonds animés : @spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "Autorisations d'Administrateur",
        "admin_body": "Veuillez exécuter l'Optimiseur en tant qu'administrateur.\nFaites un clic droit sur le fichier et sélectionnez 'Exécuter en tant qu'administrateur'."
    },
    "de": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 Benutzer:",
        "ram_label": "RAM:",
        "disk_label": "Laufwerk C:",
        "cat_system": "SYSTEM",
        "cat_clean": "CLEANUP",
        "cat_privacy": "PRIVACY",
        "cat_ui": "INTERFACE",
        "cat_net": "NETWORK",
        "cat_gaming": "GAMING",
        "cat_power": "POWER",
        "cat_gpu": "GRAPHICS",
        "cat_kernel": "KERNEL",
        "cat_extreme": "EXTREM",
        "cat_util": "TOOLS",
        "cat_pro": "PERSONALISIEREN",
        "cat_help": "HILFE",
        "credits_main": """Entwicklung: CDR Development
Optimierungs-Engine: CDR Core Engine
Interface: CustomTinker UI
Übersetzungen: Globales CDR-Team""",
        "engine_title": "BETRIEBSBEISPIEL",
        "engine_info": """CDR Optimizer enthält 220 technische Optionen, organisiert in 13 Low-Level-Kategorien, die auf maximale Hardwareleistung ausgelegt sind.""",
        "apply_btn": "🔥 ANWENDEN",
        "msg_success_title": "ERFOLG",
        "msg_success_body": "Konfiguration erfolgreich in das System injiziert!\nEin Neustart des PCs wird empfohlen, damit alle Änderungen wirksam werden.",
        "msg_confirm_title": "Änderungen bestatigen",
        "msg_confirm_body": "🔧 CDR OPTIMIZER wendet intelligente Logik an:\n\nEingeschaltete Schalter (ROT) stehen fur OPTIMIERTERE/DEAKTIVIERTE Funktionen.\nAusgeschaltete Schalter (GRAU) kehren zu den normalen Windows-Standardwerten zurück.\n\nJetzt anwenden?",
        "help_title": "INFO: Optimierungsdetails",
        "driver_btn": "🔍 TREIBER",
        "driver_ok": "✅ Alle Treiber scheinen ordnungsgemaß zu funktionieren.",
        "driver_err": "⚠️ Gerate mit Fehlern gefunden:\n\n",
        "laptop_warn": "🔋 LAPTOP-MODUS ERKANNT:\nEnergieeinstellungen, die den Akku belasten könnten, wurden angepasst.",
        "driver_ask_fix": "Möchten Sie versuchen, diese Treiber automatisch durch einen Neustart der Gerate zu reparieren?\nDies dauert nur wenige Sekunden.",
        "driver_fix_success": "Der PnP-Reparaturbefehl wurde an Windows gesendet. Überprüfen Sie erneut, ob der Fehler weiterhin besteht.",
        "status_label": "STATUS:",
        "status_ready": "BEREIT",
        "status_working": "ARBEITET",
        "spider_credits": "\n\nAnimierte Hintergründe: @spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "Administratorberechtigungen",
        "admin_body": "Bitte führen Sie den Optimizer als Administrator aus.\nKlicken Sie mit der rechten Maustaste auf die Datei und wählen Sie 'Als Administrator ausführen'."
    },
    "it": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 Utente:",
        "ram_label": "RAM:",
        "disk_label": "Disco C:",
        "cat_system": "SISTEMA",
        "cat_clean": "PULIZIA",
        "cat_privacy": "PRIVACY",
        "cat_ui": "INTERFACCIA",
        "cat_net": "RETE",
        "cat_gaming": "GAMING",
        "cat_power": "ENERGIA",
        "cat_gpu": "GRAFICA",
        "cat_kernel": "KERNEL",
        "cat_extreme": "ESTREMO",
        "cat_util": "STRUMENTI",
        "cat_pro": "PERSONALIZZA",
        "cat_help": "AIUTO",
        "credits_main": """Sviluppo: CDR Development
Motore: CDR Core Engine
Interfaccia: CustomTinker UI
Traduzioni: Team Globale CDR""",
        "engine_title": "ESEMPIO OPERATIVO",
        "engine_info": """CDR Optimizer include 220 opzioni tecniche organizzate in 13 categorie di basso livello, progettate per massimizzare le prestazioni pure dell'hardware.""",
        "apply_btn": "🔥 APPLICA",
        "msg_success_title": "SUCCESSO",
        "msg_success_body": "Configurazione iniettata con successo nel sistema!\nSi consiglia di riavviare il PC per applicare le modifiche del registro.",
        "msg_confirm_title": "Conferma Modifiche",
        "msg_confirm_body": "🔧 CDR OPTIMIZER applichera la sua logica intelligente:\n\nGli interruttori ON (ROSSO) rappresentano funzionalita OTTIMIZZATE/DISATTIVATE.\nGli interruttori OFF (GRIGIO) torneranno alle impostazioni predefinite di Windows.\n\nApplicare subito?",
        "help_title": "INFO: Dettagli Ottimizzazione",
        "driver_btn": "🔍 VERIFICA DRIVER",
        "driver_ok": "✅ Tutti i driver sembrano funzionare correttamente.",
        "driver_err": "⚠️ Trovati dispositivi con errori:\n\n",
        "laptop_warn": "🔋 MODALITA LAPTOP RILEVATA:\nLe impostazioni di alimentazione dannose per la batteria sono state modificate.",
        "driver_ask_fix": "Vuoi provare a riparare questi driver automaticamente riavviando i dispositivi?\nCi vorranno alcuni secondi.",
        "driver_fix_success": "Il comando di riparazione PnP è stato inviato a Windows. Controlla di nuovo se l'errore persiste.",
        "status_label": "STATO:",
        "status_ready": "PRONTO",
        "status_working": "LAVORANDO",
        "spider_credits": "\n\nSfondi animati: @spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "Autorizzazioni Amministratore",
        "admin_body": "Esegui l'Optimizer come amministratore.\nFai clic con il tasto destro sul file e seleziona 'Esegui come amministratore'."
    },
    "zh": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 用户:",
        "ram_label": "内存:",
        "disk_label": "C盘:",
        "cat_system": "系统",
        "cat_clean": "清理",
        "cat_privacy": "隐私",
        "cat_ui": "界面",
        "cat_net": "网络",
        "cat_gaming": "游戏",
        "cat_power": "电源",
        "cat_gpu": "显卡",
        "cat_kernel": "内核参数",
        "cat_extreme": "极致优化",
        "cat_util": "工具",
        "cat_pro": "个性化",
        "cat_help": "帮助",
        "credits_main": """开发与优化：CDR Development
优化引擎：CDR Core Engine
界面与设计：CustomTinker UI
翻译：全球 CDR 团队""",
        "engine_title": "运行示例",
        "engine_info": """CDR Optimizer 包含 220 个技术选项，分为 13 个低级类别，旨在最大限度地提高硬件性能。""",
        "apply_btn": "🔥 应用",
        "msg_success_title": "成功",
        "msg_success_body": "配置已成功注入系统！\n强烈建议重启电脑以使所有更改生效。",
        "msg_confirm_title": "确认更改",
        "msg_confirm_body": "🔧 CDR OPTIMIZER 将应用其智能逻辑：\n\n开启的开关（红色）代表已优化或已禁用的功能。\n关闭的开关（灰色）将恢复为正常的Windows默认值。\n\n现在应用更改吗？",
        "help_title": "信息：优化详情",
        "driver_btn": "🔍 驱动",
        "driver_ok": "✅ 根据系统信息，所有驱动程序工作正常。",
        "driver_err": "⚠️ 发现有硬件错误的设备:\n\n",
        "laptop_warn": "🔋 检测到笔记本模式：\n已调整可能会耗尽电池的电源设置。",
        "driver_ask_fix": "是否让优化器通过底层重启设备来自动修复这些驱动？\n这只需几秒钟。",
        "driver_fix_success": "PnP 修复命令已发送至 Windows。请再次检查错误是否仍然存在。",
        "status_label": "状态：",
        "status_ready": "就绪",
        "status_working": "处理中",
        "spider_credits": "\n\n动画背景：@spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "管理员权限",
        "admin_body": "请以管理员身份运行 Optimizer。\n右键单击该文件，然后选择“以管理员身份运行”。"
    },
    "ru": {
        "app_title": "CDR OPTIMIZER",
        "logo_title": "CDR",
        "user_prefix": "👤 Пользователь:",
        "ram_label": "ОЗУ:",
        "disk_label": "Диск C:",
        "cat_system": "СИСТЕМА",
        "cat_clean": "ОЧИСТКА",
        "cat_privacy": "ПРИВАТНОСТЬ",
        "cat_ui": "ИНТЕРФЕЙС",
        "cat_net": "СЕТЬ",
        "cat_gaming": "ИГРЫ",
        "cat_power": "ПИТАНИЕ",
        "cat_gpu": "ГРАФИКА",
        "cat_kernel": "ЯДРО",
        "cat_extreme": "ЭКСТРИМ",
        "cat_util": "УТИЛИТЫ",
        "cat_pro": "НАСТРОЙКА",
        "cat_help": "ПОМОЩЬ",
        "credits_main": """Разработка: CDR Development
Механизм: Основной механизм CDR
Интерфейс: CustomTinker UI
Переводы: Глобальная команда CDR""",
        "engine_title": "ПРИМЕР РАБОТЫ",
        "engine_info": """CDR Optimizer включает 220 опций, сгруппированных в 13 категорий, предназначенных для повышения производительности системы.""",
        "apply_btn": "🔥 ПРИМЕНИТЬ",
        "msg_success_title": "УСПЕШНО",
        "msg_success_body": "Конфигурация успешно применена к системе!\nРекомендуется перезагрузить ПК для вступления изменений в силу.",
        "msg_confirm_title": "Подтверждение изменений",
        "msg_confirm_body": "🔧 CDR ОПТИМИЗАТОР применит свою логику:\n\nВключенные переключатели (КРАСНЫЕ) — ОПТИМИЗИРОВАННЫЕ/ОТКЛЮЧЕННЫЕ функции.\nВыключенные (СЕРЫЕ) вернутся к стандартным настройкам Windows.\n\nПродолжить?",
        "help_title": "ИНФО: Детали оптимизации",
        "driver_btn": "🔍 ДРАЙВЕРЫ",
        "driver_ok": "✅ Все драйверы работают корректно.",
        "driver_err": "⚠️ Найдены устройства с ошибками:\n\n",
        "laptop_warn": "🔋 ОБНАРУЖЕН РЕЖИМ НОУТБУКА:\nНастройки питания, влияющие на батарею, были скорректированы.",
        "driver_ask_fix": "Хотите попробовать автоматически восстановить эти драйверы перезапуском устройств?\nЭто займет несколько секунд.",
        "driver_fix_success": "Команда восстановления PnP отправлена в Windows. Проверьте еще раз, сохраняется ли ошибка.",
        "status_label": "СТАТУС:",
        "status_ready": "ГОТОВ",
        "status_working": "РАБОТАЕТ",
        "spider_credits": "\n\nFondos animados: @spiderlilyedits (TikTok)",
        "btn_tiktok": "🎵 TikTok",
        "btn_youtube": "▶️ YouTube",
        "admin_title": "Права администратора",
        "admin_body": "Пожалуйста, запустите Optimizer от имени администратора.\nЩелкните файл правой кнопкой мыши и выберите «Запуск от имени администратора»."
    }
}

CURRENT_LANG = "es"

def set_lang(lang_code):
    global CURRENT_LANG
    if lang_code in translations:
        CURRENT_LANG = lang_code

def t(key):
    return translations.get(CURRENT_LANG, translations["en"]).get(key, f"[{key}]")

def get_tweaks_translated():
    if CURRENT_LANG == "es" and get_tweaks_es: return get_tweaks_es()
    if CURRENT_LANG == "pt" and get_tweaks_pt: return get_tweaks_pt()
    if CURRENT_LANG == "fr" and get_tweaks_fr: return get_tweaks_fr()
    if CURRENT_LANG == "de" and get_tweaks_de: return get_tweaks_de()
    if CURRENT_LANG == "it" and get_tweaks_it: return get_tweaks_it()
    if CURRENT_LANG == "zh" and get_tweaks_zh: return get_tweaks_zh()
    if CURRENT_LANG == "ru" and get_tweaks_ru: return get_tweaks_ru()
    
    if get_tweaks_en: return get_tweaks_en()
    return {}

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() # type: ignore
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # type: ignore
