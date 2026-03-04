# type: ignore
def get_tweaks_it():
    return {
        'cat_system': [
            {
                'id': 'svc_diagtrack',
                'name': 'Disabilita Telemetria',
                'help': 'Disabilita DiagTrack. Libera i processi in background.',
                'default': False
            },
            {
                'id': 'svc_sysmain',
                'name': 'Disabilita SysMain',
                'help': 'Precarica le app nella RAM. Disabilita se usi un SSD.',
                'default': False
            },
            {
                'id': 'svc_wsearch',
                'name': 'Disabilita Windows Search',
                'help': "Impedisce l'indicizzazione costante. ALTAMENTE RACCOMANDATO per gli SSD.",
                'default': False
            },
            {
                'id': 'svc_wuauserv_manual',
                'name': 'Windows Update Manuale',
                'help': 'Impedisce il download degli aggiornamenti durante il gioco.',
                'default': False
            },
            {
                'id': 'ai_copilot',
                'name': 'Blocca Windows Copilot',
                'help': "Disabilita l'IA Copilot a livello di GPO.",
                'default': False
            },
            {
                'id': 'ai_recall',
                'name': 'Disabilita Windows Recall',
                'help': 'Disabilita gli screenshot costanti di Windows Recall (IA).',
                'default': False
            },
            {
                'id': 'svc_bcastdvr',
                'name': 'Disabilita Game DVR',
                'help': "Impedisce la registrazione dello schermo in background. Migliora gli FPS.",
                'default': False
            },
            {
                'id': 'svc_wer',
                'name': 'Disabilita Segnalazione errori Windows',
                'help': 'Sistema di raccolta errori Microsoft.',
                'default': False
            },
            {
                'id': 'svc_dps',
                'name': "Disabilita Esecuzione diagnostica",
                'help': 'Consuma risorse per diagnosticare guasti silenziosi.',
                'default': False
            },
            {
                'id': 'svc_pcasvc',
                'name': "Disabilita Assistente compatibilità PC",
                'help': "Monitoraggio delle app legacy che causa micro-scatti.",
                'default': False
            },
            {
                'id': 'svc_remoteregistry',
                'name': 'Disabilita Registro remoto',
                'help': 'Impedisce agli utenti remoti di modificare il registro.',
                'default': False
            },
            {
                'id': 'svc_tabletinputservice',
                'name': 'Disabilita tastiera touch',
                'help': "Disabilita se non usi un touch screen.",
                'default': False
            },
            {
                'id': 'svc_wbio_srvc',
                'name': 'Disabilita Biometria',
                'help': "Disabilita se non usi impronte digitali o Face ID.",
                'default': False
            },
            {
                'id': 'svc_bits',
                'name': 'Disabilita BITS',
                'help': 'Trasferimenti in background per Update/Store.',
                'default': False
            },
            {
                'id': 'svc_defrag_svc',
                'name': 'Disabilita deframmentazione auto',
                'help': 'Disabilita la deframmentazione automatica per controllare manualmente il trim SSD.',
                'default': False
            }
        ],
        'cat_clean': [
            {
                'id': 'clean_ram',
                'name': 'Ottimizza RAM (Clear Working Sets)',
                'help': 'Forza la riduzione della cache e delle app in background per liberare RAM istantaneamente.',
                'default': False
            },
            {
                'id': 'clean_temp',
                'name': 'Pulisci cartella temporanea',
                'help': 'Elimina i file temporanei delle applicazioni.',
                'default': False
            },
            {
                'id': 'clean_prefetch',
                'name': 'Pulisci Prefetch',
                'help': 'Elimina i file di pre-caricamento (prefetch).',
                'default': False
            },
            {
                'id': 'clean_winupdate',
                'name': 'Pulisci cache Windows Update',
                'help': 'Elimina i file di installazione residui dei vecchi aggiornamenti.',
                'default': False
            },
            {
                'id': 'clean_recycle',
                'name': 'Svuota Cestino',
                'help': 'Forza lo svuotamento di tutti i cestini su tutti i dischi.',
                'default': False
            },
            {
                'id': 'clean_dns',
                'name': 'Svuota cache DNS',
                'help': 'Risolve connessioni lente rinnovando i percorsi di rete.',
                'default': False
            },
            {
                'id': 'clean_eventlog',
                'name': 'Cancella Visualizzatore eventi',
                'help': 'Elimina tutti i log degli eventi di Windows.',
                'default': False
            },
            {
                'id': 'clean_thumbcache',
                'name': 'Pulisci cache miniature',
                'help': 'Ripristina le icone di immagini/video corrotte.',
                'default': False
            },
            {
                'id': 'clean_fontcache',
                'name': 'Pulisci cache font',
                'help': 'Utile se il testo appare sfocato o reso male.',
                'default': False
            },
            {
                'id': 'clean_iconcache',
                'name': 'Pulisci cache icone',
                'help': 'Elimina e riavvia la cache delle icone di sistema.',
                'default': False
            },
            {
                'id': 'clean_crashdumps',
                'name': 'Elimina dump crash BSOD',
                'help': 'Elimina file enormi creati durante una schermata blu.',
                'default': False
            },
            {
                'id': 'clean_chkdsk',
                'name': 'Elimina frammenti CheckDisk',
                'help': 'Elimina i file .chk rimasti dopo un ripristino del disco.',
                'default': False
            },
            {
                'id': 'clean_onedrive_temp',
                'name': 'Pulisci cache OneDrive',
                'help': 'Elimina log e residui di OneDrive.',
                'default': False
            },
            {
                'id': 'clean_chrome_cache',
                'name': 'Pulisci cache Chrome',
                'help': 'Elimina la cache di Google Chrome (senza cancellare le password).',
                'default': False
            },
            {
                'id': 'clean_edge_cache',
                'name': 'Pulisci cache Edge',
                'help': 'Elimina la cache di Microsoft Edge.',
                'default': False
            },
            {
                'id': 'clean_firefox_cache',
                'name': 'Pulisci cache Firefox',
                'help': 'Elimina la cache di Mozilla Firefox.',
                'default': False
            },
            {
                'id': 'clean_discord_cache',
                'name': 'Pulisci cache Discord',
                'help': 'Discord accumula molta cache nel tempo.',
                'default': False
            },
            {
                'id': 'clean_steam_cache',
                'name': 'Pulisci cache Steam',
                'help': 'Il browser di Steam accumula spazzatura che lo rallenta.',
                'default': False
            },
            {
                'id': 'clean_epic_cache',
                'name': 'Pulisci cache Epic Games',
                'help': "Aiuta l'Epic Games Launcher ad aprirsi più velocemente.",
                'default': False
            },
            {
                'id': 'clean_spotify_cache',
                'name': 'Pulisci cache Spotify',
                'help': 'Spotify memorizza temporaneamente gigabyte di musica e copertine.',
                'default': False
            },
            {
                'id': 'clean_vcredist',
                'name': 'Pulisci VCRedist Steam',
                'help': 'Elimina i file di installazione lasciati dai giochi Steam.',
                'default': False
            },
            {
                'id': 'clean_usrdoc_temp',
                'name': 'Pulisci documenti temporanei',
                'help': 'Elimina i file temporanei nelle cartelle del profilo.',
                'default': False
            },
            {
                'id': 'clean_system_logs',
                'name': "Elimina log d'installazione",
                'help': "Elimina i log in C:\\Windows.",
                'default': False
            },
            {
                'id': 'clean_crypt_svc',
                'name': 'Ripristina cache Crypto',
                'help': 'Ripristina le firme nel database di sistema.',
                'default': False
            },
            {
                'id': 'clean_bits_queue',
                'name': 'Pulisci coda BITS',
                'help': 'Elimina le attività di download in background.',
                'default': False
            }
        ],
        'cat_privacy': [
            {
                'id': 'priv_telemetry_level',
                'name': 'Livello telemetria 0',
                'help': 'Blocca quasi tutta la trasmissione di dati diagnostici.',
                'default': False
            },
            {
                'id': 'priv_etw_disable',
                'name': 'Blocco telemetria ETW profondo',
                'help': 'Disabilita le sessioni AutoLogger a livello kernel.',
                'default': False
            },
            {
                'id': 'priv_cortana',
                'name': 'Disabilita Cortana',
                'help': 'Libera RAM e processi di ascolto costante.',
                'default': False
            },
            {
                'id': 'priv_start_web',
                'name': 'Disabilita ricerca Web nel menu Start',
                'help': 'Solo ricerca locale. Menu Start ultra veloce.',
                'default': False
            },
            {
                'id': 'priv_news',
                'name': 'Disabilita Notizie e interessi',
                'help': 'Rimuove il widget meteo e notizie dalla barra delle applicazioni.',
                'default': False
            },
            {
                'id': 'priv_location',
                'name': 'Disabilita posizione',
                'help': 'Impedisce a Windows e alle app di accedere alla tua posizione.',
                'default': False
            },
            {
                'id': 'priv_mic',
                'name': 'Disabilita suggerimenti digitazione',
                'help': 'Disabilita le previsioni che inviano i modelli di digitazione.',
                'default': False
            },
            {
                'id': 'priv_feedback',
                'name': 'Frequenza feedback: Mai',
                'help': 'Impedisce a Windows di chiedere costantemente opinioni.',
                'default': False
            },
            {
                'id': 'priv_activity',
                'name': "Disabilita cronologia attività",
                'help': "Impedisce a Windows di salvare la cronologia delle app e dei file.",
                'default': False
            },
            {
                'id': 'priv_sync',
                'name': 'Disabilita sincronizzazione impostazioni',
                'help': "Impedisce a sfondo e impostazioni di caricarsi sul cloud.",
                'default': False
            },
            {
                'id': 'priv_advertising',
                'name': "Disabilita ID pubblicità",
                'help': "Impedisce annunci personalizzati tramite l'ID pubblicità.",
                'default': False
            },
            {
                'id': 'priv_appdiag',
                'name': "Blocca diagnostica app",
                'help': "Impedisce alle app di accedere alla diagnostica di altre app.",
                'default': False
            },
            {
                'id': 'priv_tailored',
                'name': 'Disabilita esperienze personalizzate',
                'help': "Impedisce a MS di usare dati diagnostici per contenuti personali.",
                'default': False
            },
            {
                'id': 'priv_ceip',
                'name': 'Lascia CEIP',
                'help': "Esce dal programma di miglioramento Microsoft.",
                'default': False
            },
            {
                'id': 'priv_handwriting',
                'name': "Disabilita apprendimento scrittura a mano",
                'help': "Impedisce la raccolta dei dati della penna stilo.",
                'default': False
            },
            {
                'id': 'priv_defender_samples',
                'name': "Non inviare campioni Defender",
                'help': "Impedisce a Defender di caricare file sui suoi server.",
                'default': False
            },
            {
                'id': 'priv_onedrive',
                'name': 'Disabilita OneDrive all\'avvio',
                'help': 'Impedisce a OneDrive di avviarsi con il sistema.',
                'default': False
            },
            {
                'id': 'priv_meetnow',
                'name': 'Nascondi "Riunione immediata"',
                'help': 'Rimuove l\'icona della fotocamera dalla barra delle applicazioni.',
                'default': False
            },
            {
                'id': 'priv_app_suggestions',
                'name': 'Disabilita suggerimenti app',
                'help': 'Impedisce a Windows di suggerire app nel menu Start.',
                'default': False
            },
            {
                'id': 'priv_smartscreen',
                'name': 'Disabilita SmartScreen',
                'help': 'Riduce la protezione malware. ATTENZIONE.',
                'default': False
            }
        ],
        'cat_ui': [
            {
                'id': 'ui_animation',
                'name': 'Disabilita animazioni finestre',
                'help': 'Le finestre si aprono e chiudono istantaneamente.',
                'default': False
            },
            {
                'id': 'ui_transparency',
                'name': 'Disabilita trasparenza',
                'help': 'Rimuove gli effetti Mica/Acrylic. Libera la GPU.',
                'default': False
            },
            {
                'id': 'ui_shadows',
                'name': 'Rimuovi ombre',
                'help': 'Elimina le ombre dalle finestre e dal cursore.',
                'default': False
            },
            {
                'id': 'ui_show_ext',
                'name': 'Mostra estensioni file',
                'help': 'Mostra .exe .jpg ecc. Utile per la sicurezza.',
                'default': False
            },
            {
                'id': 'ui_show_hidden',
                'name': 'Mostra file nascosti',
                'help': 'Mostra AppData e le cartelle nascoste.',
                'default': False
            },
            {
                'id': 'ui_classic_menu',
                'name': 'Menu contestuale classico (Win11)',
                'help': 'Mostra il menu completo senza clic extra in Win11.',
                'default': False
            },
            {
                'id': 'ui_darkmode',
                'name': 'Forza Modalità Scura',
                'help': 'Applica la modalità scura globale alle app e al sistema.',
                'default': False
            },
            {
                'id': 'ui_startup_delay',
                'name': 'Rimuovi ritardo di avvio',
                'help': 'Elimina il ritardo di 10s imposto da Windows al caricamento delle app.',
                'default': False
            },
            {
                'id': 'ui_taskbar_search',
                'name': 'Nascondi barra di ricerca',
                'help': 'Rimuove o riduce al minimo la barra di ricerca.',
                'default': False
            },
            {
                'id': 'ui_edge_tabs',
                'name': 'Nascondi schede Edge in Alt+Tab',
                'help': 'Evita il disordine di Alt+Tab con le schede di Edge.',
                'default': False
            },
            {
                'id': 'ui_lockscreen',
                'name': 'Disabilita schermata di blocco',
                'help': 'Va direttamente alla password senza scorrere.',
                'default': False
            },
            {
                'id': 'ui_blur_lock',
                'name': 'Rimuovi sfocatura login',
                'help': 'Rimuove l\'effetto sfocatura nella schermata di login.',
                'default': False
            },
            {
                'id': 'ui_actioncenter',
                'name': 'Disabilita Centro notifiche',
                'help': 'Rimuove il pannello delle notifiche laterale.',
                'default': False
            },
            {
                'id': 'ui_snap',
                'name': "Disabilita Assistente di ancoraggio",
                'help': 'Impedisce i suggerimenti durante il trascinamento delle finestre.',
                'default': False
            },
            {
                'id': 'ui_shake',
                'name': 'Disabilita Aero Shake',
                'help': 'Impedisce di ridurre a icona le finestre scuotendone una.',
                'default': False
            },
            {
                'id': 'ui_balloon',
                'name': 'Disabilita fumetti d\'aiuto',
                'help': 'Disabilita i pop-up gialli intrusivi.',
                'default': False
            },
            {
                'id': 'ui_taskbar_animations',
                'name': 'Disabilita animazioni barra applicazioni',
                'help': 'Movimenti delle icone istantanei.',
                'default': False
            },
            {
                'id': 'ui_cursor_shadow',
                'name': 'Disabilita ombra cursore',
                'help': 'Rimuove la sottile ombra sotto il puntatore.',
                'default': False
            }
        ],
        'cat_net': [
            {
                'id': 'net_extreme_tcp',
                'name': 'Ottimizzatore TCP estremo (BBR)',
                'help': 'Algoritmi moderni BBR/CUBIC e disabilita la moderazione delle interruzioni.',
                'default': False
            },
            {
                'id': 'net_autotuning',
                'name': 'Auto-Tuning TCP Normale',
                'help': 'Ottimizza il modo in cui Windows gestisce i pacchetti. Migliora la latenza.',
                'default': False
            },
            {
                'id': 'net_nagles',
                'name': "Disabilita algoritmo di Nagle",
                'help': 'Invia i pacchetti più velocemente. Riduce la latenza nei MMO.',
                'default': False
            },
            {
                'id': 'net_rss',
                'name': 'Abilita Receive-Side Scaling',
                'help': 'Distribuisce l\'elaborazione di rete su più core.',
                'default': False
            },
            {
                'id': 'net_qos',
                'name': 'Rimuovi limite larghezza di banda QoS',
                'help': 'Libera il 20% di internet riservato da Windows.',
                'default': False
            },
            {
                'id': 'net_deliveryopt',
                'name': "Disabilita ottimizzazione recapito P2P",
                'help': "Impedisce a Windows di caricare aggiornamenti su Internet.",
                'default': False
            },
            {
                'id': 'net_wifi_power',
                'name': "Disabilita risparmio energetico WiFi",
                'help': "Impedisce disconnessioni temporanee sui laptop.",
                'default': False
            },
            {
                'id': 'net_ecn',
                'name': 'Disabilita ECN',
                'help': "L'ECN a volte causa lag nei giochi. Disabilitarlo stabilizza il ping.",
                'default': False
            },
            {
                'id': 'net_heuristics',
                'name': 'Disabilita euristiche TCP',
                'help': 'Impedisce a Windows di limitare la finestra TCP.',
                'default': False
            },
            {
                'id': 'net_lso',
                'name': 'Disabilita Large Send Offload',
                'help': 'LSO causa picchi di ping su schede Intel/Realtek.',
                'default': False
            },
            {
                'id': 'net_chimney',
                'name': 'Disabilita TCP Chimney',
                'help': 'Può causare instabilità sui router moderni.',
                'default': False
            },
            {
                'id': 'net_ipv6',
                'name': 'Disabilita IPv6',
                'help': 'A volte causa lag locale. Usa con cautela.',
                'default': False
            },
            {
                'id': 'net_dnscache',
                'name': 'Evita cache DNS negativa',
                'help': 'Impedisce di salvare i fallimenti temporanei di connessione.',
                'default': False
            },
            {
                'id': 'net_smb',
                'name': 'Disabilita SMBv1',
                'help': 'Protocollo non sicuro (WannaCry). Chiude una falla enorme.',
                'default': False
            },
            {
                'id': 'net_teredo',
                'name': 'Disabilita tunneling Teredo',
                'help': 'Transizione IPv6 che causa overhead (sovraccarico).',
                'default': False
            },
            {
                'id': 'net_isatap',
                'name': 'Disabilita ISATAP',
                'help': 'Un altro tunnel IPv6-IPv4 con overhead di ping.',
                'default': False
            },
            {
                'id': 'net_netbios',
                'name': 'Disabilita NetBIOS su TCP',
                'help': 'Non usare se condividi stampanti sulla rete locale.',
                'default': False
            },
            {
                'id': 'net_wpad',
                'name': 'Disabilita auto-scoperta WPAD',
                'help': 'Accelera il DNS e ferma un vettore d\'attacco.',
                'default': False
            },
            {
                'id': 'net_tcp_1323',
                'name': 'Abilita timestamp RFC 1323',
                'help': 'Migliora l\'affidabilità nei trasferimenti di grandi dimensioni.',
                'default': False
            },
            {
                'id': 'net_max_conn',
                'name': 'Max connessioni 10 (HTTP 1.0)',
                'help': 'Accelera il caricamento simultaneo di pagine web.',
                'default': False
            },
            {
                'id': 'net_max_conn11',
                'name': 'Max connessioni 10 (HTTP 1.1)',
                'help': 'Accelera i caricamenti web HTTP 1.1.',
                'default': False
            },
            {
                'id': 'net_dns_cloudflare',
                'name': 'Imposta DNS Cloudflare (1.1.1.1)',
                'help': 'Configura il DNS più veloce al mondo da Cloudflare.',
                'default': False
            },
            {
                'id': 'net_dns_google',
                'name': 'Imposta DNS Google (8.8.8.8)',
                'help': 'Configura i DNS di Google, veloci e affidabili.',
                'default': False
            }
        ],
        'cat_gaming': [
            {
                'id': 'game_mode',
                'name': 'Abilita Modalità gioco Windows',
                'help': "Assegna priorità d'uso di CPU/GPU al gioco.",
                'default': False
            },
            {
                'id': 'game_process_priority',
                'name': 'Elevazione automatica priorità (Booster)',
                'help': "Forza la priorità 'Alta' in tempo reale per i processi dei shooter competitivi.",
                'default': False
            },
            {
                'id': 'game_process_lasso',
                'name': 'Game Booster attivo',
                'help': "Simula Process Lasso. Alza la priorità della CPU quando s'aprono i giochi.",
                'default': False
            },
            {
                'id': 'game_timer_res',
                'name': 'Risoluzione timer 0.5ms',
                'help': 'Regola BCDEDIT per un tickrate Windows di alta precisione.',
                'default': False
            },
            {
                'id': 'game_mouse_accel',
                'name': "Disabilita accelerazione mouse",
                'help': 'Input reale 1:1. Essenziale per i shooter competitivi.',
                'default': False
            },
            {
                'id': 'game_ultimate_power',
                'name': 'Attiva Prestazioni Eccellenti',
                'help': "Sblocca il piano d'alimentazione nascosto di Windows.",
                'default': False
            },
            {
                'id': 'game_msi_mode',
                'name': 'Hardware Latency Killer (MSI)',
                'help': 'Forza GPU/Rete/USB a usare gli interrupt MSI.',
                'default': False
            },
            {
                'id': 'game_hags',
                'name': 'Abilita Pianificazione GPU con accelerazione hardware',
                'help': 'Boost degli FPS in DX12. Richiede il riavvio.',
                'default': False
            },
            {
                'id': 'game_mmcss',
                'name': 'Ottimizza MMCSS',
                'help': 'Indirizza NetworkThrottlingIndex e la GPU verso il gioco.',
                'default': False
            },
            {
                'id': 'game_fullscreen_opt',
                'name': 'Disabilita ottimizzazioni schermo intero',
                'help': 'Evita il falso schermo intero con input lag.',
                'default': False
            },
            {
                'id': 'game_edge_bg',
                'name': 'Chiudi Edge in background',
                'help': 'Chiude i processi msedge.exe che divorano 500 MB di RAM.',
                'default': False
            },
            {
                'id': 'game_chrome_bg',
                'name': 'Chiudi Chrome in background',
                'help': 'Elimina il flag per le app Chrome in background.',
                'default': False
            },
            {
                'id': 'game_steam_hardware',
                'name': "Disabilita accelerazione HW Steam",
                'help': "Impedisce a Steam di consumare GPU in background.",
                'default': False
            },
            {
                'id': 'game_discord_hw',
                'name': "Disabilita accelerazione HW Discord",
                'help': "Se la GPU è al 99%, disabilitarlo evita scatti.",
                'default': False
            },
            {
                'id': 'game_vr',
                'name': 'Reattività del sistema (VR/Gaming)',
                'help': 'Imposta SystemResponsiveness a 0. Più cicli CPU al gioco.',
                'default': False
            },
            {
                'id': 'game_fth',
                'name': 'Disabilita Fault Tolerant Heap',
                'help': 'Evita il degrado del gioco quando crasha.',
                'default': False
            },
            {
                'id': 'game_hpet',
                'name': 'Disabilita HPET',
                'help': 'Riduce l\'enorme input lag sui vecchi CPU o Ryzen gen1.',
                'default': False
            },
            {
                'id': 'game_xbox_dvr',
                'name': 'Elimina chiavi registro Xbox DVR',
                'help': 'Elimina catture nascoste. Alza gli FPS minimi in DX12.',
                'default': False
            },
            {
                'id': 'game_core_parking',
                'name': 'Disabilita Core Parking',
                'help': 'Impedisce a Windows di spegnere i core della CPU.',
                'default': False
            },
            {
                'id': 'game_vbs',
                'name': 'Disabilita VBS',
                'help': 'Overhead del 10% nei giochi. Solo se il tuo obiettivo è il 100% gioco.',
                'default': False
            },
            {
                'id': 'perf_win32_priority',
                'name': 'Win32PrioritySeparation 26',
                'help': 'Ottimizza la priorità CPU per le finestre attive (GIOCHI).',
                'default': False
            },
            {
                'id': 'perf_large_cache',
                'name': 'Large System Cache',
                'help': 'Migliora le prestazioni dei file usando più RAM.',
                'default': False
            },
            {
                'id': 'perf_io_limit',
                'name': 'Alza il limite blocco pagine IO',
                'help': 'Accelera i trasferimenti di file pesanti.',
                'default': False
            },
            {
                'id': 'perf_wait_kill',
                'name': 'Chiudi i servizi velocemente (2s)',
                'help': 'Riduce i tempi d\'attesa prima di chiudere i servizi.',
                'default': False
            },
            {
                'id': 'perf_auto_end',
                'name': "Chiusura auto app bloccate all'arresto",
                'help': "Sforza la chiusura dei processi bloccati all'arresto.",
                'default': False
            },
            {
                'id': 'perf_menu_delay',
                'name': 'Ritardo visualizzazione menu a zero',
                'help': 'I menu appaiono istantaneamente.',
                'default': False
            },
            {
                'id': 'perf_startup_delay',
                'name': 'Rimuovi ritardo totale di avvio',
                'help': 'Avvia le app in background senza tempi d\'attesa artificiali.',
                'default': False
            }
        ],
        'cat_power': [
            {
                'id': 'pwr_ultimate',
                'name': 'Forza Prestazioni Eccellenti',
                'help': 'Massimo livello di energia. Disabilita ogni risparmio CPU.',
                'default': False
            },
            {
                'id': 'pwr_min_cpu',
                'name': 'CPU Minimo 100%',
                'help': 'Impedisce al processore di abbassare la frequenza.',
                'default': False
            },
            {
                'id': 'pwr_throttling',
                'name': "Disabilita Power Throttling",
                'help': "Impedisce a Windows di limitare Discord e le app in background.",
                'default': False
            },
            {
                'id': 'pwr_cpu_boost',
                'name': 'Abilita sempre Turbo Boost CPU',
                'help': 'Mantiene il turbo boost attivo anche a batteria.',
                'default': False
            },
            {
                'id': 'pwr_pci_link',
                'name': 'Disabilita PCIe Link State Power Mgmt',
                'help': 'Impedisce alla GPU di entrare in stati di basso consumo.',
                'default': False
            },
            {
                'id': 'pwr_hibernation',
                'name': 'Disabilita Ibernazione',
                'help': 'Libera gigabyte su C: e riduce l\'usura dell\'SSD.',
                'default': False
            },
            {
                'id': 'pwr_disk_timeout',
                'name': 'Disabilita timeout HDD',
                'help': 'Impedisce agli HDD di spegnersi causando scatti.',
                'default': False
            },
            {
                'id': 'pwr_adaptive_brightness',
                'name': 'Disabilita luminosità adattiva',
                'help': "Impedisce al sensore di regolare la luminosità automaticamente.",
                'default': False
            },
            {
                'id': 'pwr_usb_hub_suspend',
                'name': 'Disabilita sospensione selettiva hub USB',
                'help': 'Complemento a Gaming USB Suspend. Più stabile.',
                'default': False
            }
        ],
        'cat_gpu': [
            {
                'id': 'gpu_hags',
                'name': 'Abilita HAGS (Pianificazione GPU hw)',
                'help': 'Sposta la coda dei frame dalla CPU alla GPU. Migliora gli FPS in DX12/Vulkan.',
                'default': False
            },
            {
                'id': 'gpu_mpo',
                'name': 'Disabilita MPO',
                'help': 'L\'MPO causa schermi neri e scatti. Nvidia consiglia di disabilitarlo.',
                'default': False
            },
            {
                'id': 'gpu_preemption',
                'name': 'Disabilita preemption GPU',
                'help': 'Impedisce le interruzioni a metà frame. Elimina i micro-scatti.',
                'default': False
            },
            {
                'id': 'gpu_reduce_dpc',
                'name': 'Riduci latenza DPC GPU',
                'help': 'Regola le interruzioni del driver GPU per ridurre la latenza DPC.',
                'default': False
            },
            {
                'id': 'gpu_dwm_priority',
                'name': 'Priorità DWM Alta',
                'help': 'Alza la priorità di dwm.exe per un rendering più fluido.',
                'default': False
            },
            {
                'id': 'gpu_gpu_priority',
                'name': 'Priorità GPU 8 (MMCSS)',
                'help': 'Regola GpuPriority per dare maggiore priorità al processo gaming.',
                'default': False
            },
            {
                'id': 'gpu_perf_registry',
                'name': 'Ottimizza registro GPU MMCSS',
                'help': 'Regola NetworkThrottlingIndex e SystemResponsiveness per la GPU.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_power',
                'name': 'NVIDIA: Prestazioni massime',
                'help': 'Forza le Prestazioni Massime nel pannello NVIDIA tramite registro.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_telemetry',
                'name': 'Disabilita telemetria NVIDIA',
                'help': 'Ferma le attività di telemetria NVIDIA in background.',
                'default': False
            },
            {
                'id': 'gpu_amd_power',
                'name': 'AMD: No risparmio energetico GPU',
                'help': 'Impedisce alla GPU AMD di entrare in stati di bassa frequenza.',
                'default': False
            },
            {
                'id': 'gpu_amd_telemetry',
                'name': 'Disabilita telemetria AMD',
                'help': 'Ferma i servizi di telemetria AMD in background.',
                'default': False
            },
            {
                'id': 'gpu_pci_express_max',
                'name': 'Modalità PCIe GPU massima',
                'help': 'Disabilita Link State Power Management specificamente per la GPU.',
                'default': False
            },
            {
                'id': 'gpu_disable_fullscreen_opt',
                'name': 'Disabilita ottimizzazioni schermo intero globali',
                'help': 'Forza il vero schermo intero esclusivo in tutti i giochi.',
                'default': False
            },
            {
                'id': 'gpu_freesync_vsync_off',
                'name': 'Disabilita V-Sync globale',
                'help': 'Disabilita il V-Sync per impostazione predefinita in tutte le app.',
                'default': False
            },
            {
                'id': 'gpu_cache_clean',
                'name': 'Pulisci cache shader GPU',
                'help': 'Elimina la cache degli shader accumulata. Utile se scatta entrando in zone.',
                'default': False
            },
            {
                'id': 'gpu_vram_paging',
                'name': 'Ottimizza paginazione VRAM',
                'help': 'Usa la RAM di sistema come estensione per GPU con poca VRAM.',
                'default': False
            },
            {
                'id': 'gpu_shader_cache',
                'name': 'Reindirizza cache shader su SSD rapido',
                'help': 'Configura la cache degli shader per una lettura rapida su NVMe.',
                'default': False
            },
            {
                'id': 'gpu_disable_mpv',
                'name': 'Disabilita precompilazione background DX12/Vulkan',
                'help': 'Impedisce la precompilazione degli shader mentre giochi.',
                'default': False
            },
            {
                'id': 'gpu_gsync_compat',
                'name': 'G-Sync su monitor FreeSync',
                'help': 'Forza la compatibilità G-Sync su monitor AMD con GPU Nvidia.',
                'default': False
            },
            {
                'id': 'gpu_night_light_off',
                'name': 'Disabilita Luce notturna',
                'help': 'Impedisce a Windows di alterare la calibrazione del colore del monitor.',
                'default': False
            }
        ],
        'cat_kernel': [
            {
                'id': 'ext_57_processes',
                'name': 'Consolidamento servizi di sistema (processi minimi)',
                'help': 'Reindirizza svchost e disabilita i servizi non critici per ridurre il totale dei processi attivi al minimo operativo.',
                'default': False
            },
            {
                'id': 'kern_registry_size',
                'name': 'Aumenta dimensione max registro',
                'help': 'Previene errori di limite del registro su sistemi personalizzati.',
                'default': False
            },
            {
                'id': 'kern_bcdedit_inc',
                'name': 'Frequenza interrupt BCDEDIT',
                'help': 'Aumenta la precisione dell\'orologio tramite BCDEDIT. Chiave per timer < 1ms.',
                'default': False
            },
            {
                'id': 'kern_memory_comp',
                'name': "Disabilita compressione memoria (MMAgent)",
                'help': "Impedisce alla CPU di sprecare cicli comprimendo le pagine RAM, dando priorità alla latenza.",
                'default': False
            },
            {
                'id': 'kern_system_resp',
                'name': 'SystemResponsiveness a 0% (Tempo Reale)',
                'help': 'Rimuove la riserva di risorse in background di Windows per dedicare il 100% al processo in primo piano.',
                'default': False
            },
            {
                'id': 'kernel_mitigations',
                'name': 'Disabilita Mitigazioni CPU',
                'help': 'Disabilita Spectre/Meltdown. +5-15% CPU pura. Riduce la sicurezza.',
                'default': False
            },
            {
                'id': 'kern_large_pages',
                'name': 'Abilita Large Pages (Memoria virtuale)',
                'help': 'Riduce i page fault (TLB miss) nelle applicazioni ad alto carico di memoria.',
                'default': False
            },
            {
                'id': 'kern_iot_core',
                'name': 'Config profilo embedded minimalista',
                'help': 'Regola i parametri interni del sistema per comportarsi come un profilo Windows IoT a basso consumo di risorse.',
                'default': False
            },
            {
                'id': 'kern_process_isolation',
                'name': "Disabilita isolamento processi core",
                'help': "Riduce l'overhead di virtualizzazione del kernel per massimizzare la velocità dei thread.",
                'default': False
            }
        ],
        'cat_extreme': [
            {
                'id': 'ext_super_nuclear',
                'name': 'Pulizia massiccia servizi di sistema',
                'help': 'Disabilita tutti i servizi non essenziali di rete, stampa e visuali. Irreversibile senza ripristino.',
                'default': False
            },
            {
                'id': 'ext_minimalist',
                'name': 'Profilo Shell ridotto ad alte prestazioni',
                'help': 'Disabilita gli effetti visivi della Shell di Windows per liberare totalmente cicli CPU e GPU.',
                'default': False
            },
            {
                'id': 'ext_defender_kill',
                'name': 'Disattivazione permanente Windows Defender',
                'help': 'Rimuove il motore di scansione e i servizi di sicurezza nativi tramite registro/GPO.',
                'default': False
            },
            {
                'id': 'ext_uwp_kill_all',
                'name': 'Rimozione completa app UWP integrate',
                'help': 'Disinstalla tutte le app UWP preinstallate per tutti gli utenti del sistema.',
                'default': False
            },
            {
                'id': 'ext_firewall_off',
                'name': 'Disabilita Windows Firewall (Stack Bypass)',
                'help': 'Disabilita il filtraggio pacchetti nativo per ridurre al minimo la latenza di rete.',
                'default': False
            },
            {
                'id': 'ext_update_dead',
                'name': 'Blocco Windows Update (Politica LTSC)',
                'help': 'Impedisce ogni tentativo di aggiornamento o download di driver dal sistema operativo.',
                'default': False
            }
        ],
        'cat_util': [
            {
                'id': 'util_dotnet',
                'name': 'Installa runtime .NET',
                'help': 'Garantisce la compatibilità con tutte le versioni dei framework applicativi.',
                'default': False
            },
            {
                'id': 'util_vc_redist',
                'name': 'Installa Redistribuibili C++',
                'help': 'Installa tutte le librerie necessarie per l\'esecuzione di giochi e software.',
                'default': False
            },
            {
                'id': 'util_directx',
                'name': 'Aggiorna runtime DirectX',
                'help': 'Installa i componenti DirectX legacy per i giochi vecchi.',
                'default': False
            },
            {
                'id': 'util_powershell_7',
                'name': 'Installa PowerShell 7',
                'help': 'Installa la versione moderna e più veloce del motore di script di Windows.',
                'default': False
            },
            {
                'id': 'util_driver_updates',
                'name': 'Escludi aggiornamenti driver',
                'help': 'Impedisce a Windows di sovrascrivere i driver personalizzati con versioni generiche.',
                'default': False
            },
            {
                'id': 'util_ps_telemetry',
                'name': 'Disabilita telemetria PowerShell',
                'help': 'Rimuove i report di utilizzo nel terminale moderno di Windows.',
                'default': False
            },
            {
                'id': 'util_end_task_rc',
                'name': 'Termina attività su barra applicazioni',
                'help': 'Aggiunge l\'opzione per chiudere i processi direttamente dal tasto destro sulla barra delle applicazioni.',
                'default': False
            },
            {
                'id': 'util_start_recommendations',
                'name': 'Rimuovi consigli in Start',
                'help': 'Svuota la sezione dei file recenti e delle app suggerite in Start.',
                'default': False
            },
            {
                'id': 'util_sticky_keys',
                'name': 'Disabilita Tasti permanenti',
                'help': 'Impedisce al sistema di chiedere dei tasti permanenti dopo aver premuto più volte Shift.',
                'default': False
            },
            {
                'id': 'util_taskbar_center',
                'name': 'Barra applicazioni: Allinea a sinistra',
                'help': 'Ripristina la posizione classica delle icone sul desktop di Windows 11.',
                'default': False
            },
            {
                'id': 'util_settings_home',
                'name': "Rimuovi home page Impostazioni",
                'help': "Rimuove l'inutile schermata 'Home' all'apertura delle impostazioni di Windows.",
                'default': False
            },
            {
                'id': 'util_new_outlook',
                'name': 'Blocca nuovo Outlook',
                'help': 'Impedisce a Windows di sostituire il client mail classico con la versione web-app.',
                'default': False
            },
            {
                'id': 'util_cross_device',
                'name': 'Disabilita esperienze multi-dispositivo',
                'help': 'Disabilita la sincronizzazione delle attività non finite con altri PC o cellulari.',
                'default': False
            },
            {
                'id': 'util_task_view',
                'name': 'Nascondi Visualizzazione attività',
                'help': 'Pulisce la barra delle applicazioni rimuovendo l\'icona dei desktop virtuali.',
                'default': False
            },
            {
                'id': 'util_folder_discovery',
                'name': 'Disattiva scoperta cartelle auto',
                'help': 'Impedisce a Esplora file di cambiare il tipo di visualizzazione aprendo cartelle con immagini o musica.',
                'default': False
            },
            {
                'id': 'util_bsod_detail',
                'name': 'BSOD con informazioni dettagliate',
                'help': 'Mostra parametri completi e codici d\'errore nella schermata blu della morte.',
                'default': False
            },
            {
                'id': 'util_numlock',
                'name': "Attiva Bloc Num all'avvio",
                'help': "Attiva automaticamente il Bloc Num all'accesso a Windows.",
                'default': False
            },
            {
                'id': 'util_verbose_logon',
                'name': 'Messaggi di login dettagliati',
                'help': "Mostra lo stato di ciascun servizio durante l'accesso e l'uscita.",
                'default': False
            },
            {
                'id': 'util_consumer_features',
                'name': 'Disabilita suggerimenti app Store',
                'help': "Impedisce l'installazione silenziosa di app promozionali da Microsoft.",
                'default': False
            },
            {
                'id': 'util_wpbt',
                'name': "Blocca iniezione bloatware (WPBT)",
                'help': "Impedisce ai produttori di installare software via BIOS all'avvio di Windows.",
                'default': False
            },
            {
                'id': 'util_widgets_remove',
                'name': 'Rimuovi Widget Windows 11',
                'help': 'Disinstalla il pannello dei widget e delle notizie dalla barra delle applicazioni.',
                'default': False
            },
            {
                'id': 'uwp_xbox',
                'name': 'Rimuovi app Xbox',
                'help': 'Elimina tutte le app Xbox (GameBar, TCUI). NON USARE SE GIOCHI CON IL PC GAME PASS.',
                'default': False
            },
            {
                'id': 'uwp_bloatware',
                'name': 'Rimuovi bloatware nativo',
                'help': 'Elimina le app spazzatura: Zune, BingNews, GetHelp, Solitaire, People...',
                'default': False
            },
            {
                'id': 'uwp_onedrive',
                'name': 'Disinstalla OneDrive',
                'help': 'Disinstalla profondamente Microsoft OneDrive dal sistema.',
                'default': False
            },
            {
                'id': 'uwp_edge',
                'name': 'Rimuovi Edge (Avanzato)',
                'help': 'Tenta di rimuovere Microsoft Edge con PowerShell. Tieni pronto un altro browser.',
                'default': False
            },
            {
                'id': 'uwp_3dbuilder',
                'name': 'Rimuovi 3D Builder',
                'help': 'Disinstalla l\'app di modellazione 3D di Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_alarms',
                'name': 'Rimuovi Alarmi e orologio',
                'help': 'Disinstalla l\'app di sveglie e cronometro.',
                'default': False
            },
            {
                'id': 'uwp_camera',
                'name': 'Rimuovi Fotocamera',
                'help': 'Disinstalla l\'app fotocamera dallo Store.',
                'default': False
            },
            {
                'id': 'uwp_communications',
                'name': 'Rimuovi Posta e Calendario',
                'help': 'Disinstalla le app integrate di posta e calendario.',
                'default': False
            },
            {
                'id': 'uwp_feedback',
                'name': 'Rimuovi Hub di feedback',
                'help': 'Disinstalla l\'app di feedback di Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_gethelp',
                'name': "Rimuovi Richiesta di assistenza",
                'help': "Disinstalla l'app di supporto tecnico di Microsoft.",
                'default': False
            },
            {
                'id': 'uwp_maps',
                'name': 'Rimuovi Mappe',
                'help': "Disinstalla l'app mappe integrata.",
                'default': False
            },
            {
                'id': 'uwp_mixedreality',
                'name': 'Rimuovi Portale realtà mista',
                'help': 'Disinstalla il portale di realtà mista.',
                'default': False
            },
            {
                'id': 'uwp_people',
                'name': 'Rimuovi Contatti (People)',
                'help': 'Disinstalla l\'app contatti integrata.',
                'default': False
            },
            {
                'id': 'uwp_photos',
                'name': 'Rimuovi Foto',
                'help': 'Disinstalla l\'app Foto moderna (sostituibile col visualizzatore classico).',
                'default': False
            },
            {
                'id': 'uwp_skype',
                'name': 'Rimuovi Skype',
                'help': 'Disinstalla l\'app Skype preinstallata.',
                'default': False
            },
            {
                'id': 'uwp_solitaire',
                'name': 'Rimuovi Solitario',
                'help': 'Disinstalla i giochi di solitario preinstallati.',
                'default': False
            },
            {
                'id': 'uwp_soundrecorder',
                'name': 'Rimuovi Registratore vocale',
                'help': 'Disinstalla l\'app di registrazione audio.',
                'default': False
            },
            {
                'id': 'uwp_stickynotes',
                'name': 'Rimuovi Sticky Notes',
                'help': 'Disinstalla l\'app di note adesive.',
                'default': False
            },
            {
                'id': 'uwp_weather',
                'name': 'Rimuovi Meteo',
                'help': "Disinstalla l'app meteo.",
                'default': False
            },
            {
                'id': 'uwp_yourphone',
                'name': 'Rimuovi Il tuo telefono',
                'help': 'Disinstalla l\'app di collegamento con lo smartphone.',
                'default': False
            }
        ],
        'cat_pro': [
            {
                'id': 'util_context_compact',
                'name': 'Abilita menu contestuali compatti',
                'help': 'Riduce il padding e lo spazio tra le opzioni dei menu del tasto destro.',
                'default': False
            },
            {
                'id': 'util_legacy_photo',
                'name': 'Ripristina Visualizzatore foto classico (Win7)',
                'help': 'Abilita il visualizzatore immagini ultra rapido e leggero delle vecchie versioni.',
                'default': False
            },
            {
                'id': 'util_legacy_calc',
                'name': 'Ripristina Calcolatrice classica Win32',
                'help': 'Sostituisce la versione UWP lenta con la versione eseguibile tradizionale.',
                'default': False
            },
            {
                'id': 'util_god_mode',
                'name': 'Accesso unificato al Pannello di controllo',
                'help': 'Crea un collegamento a tutte le impostazioni amministrative del sistema in un\'unica finestra.',
                'default': False
            },
            {
                'id': 'util_verbose_boot',
                'name': "Abilita cronologia d'avvio dettagliata",
                'help': "Mostra i driver e i servizi caricati durante l'avvio sullo schermo.",
                'default': False
            },
            {
                'id': 'util_desktop_labels',
                'name': 'Rimuovi frecce dai collegamenti',
                'help': 'Pulisce le icone del desktop eliminando la freccia di scelta rapida.',
                'default': False
            },
            {
                'id': 'util_explorer_pc',
                'name': "Apri Esplora file su 'Questo PC'",
                'help': "Configura l'esplora risorse per saltare la vista dei file recenti per impostazione predefinita.",
                'default': False
            }
        ],
        'cat_help': []
    }
