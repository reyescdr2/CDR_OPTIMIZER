# type: ignore
def get_tweaks_fr():
    return {
        'cat_system': [
            {
                'id': 'svc_diagtrack',
                'name': 'Désactiver la télémétrie',
                'help': 'Désactive DiagTrack. Libère les processus en arrière-plan.',
                'default': False
            },
            {
                'id': 'svc_sysmain',
                'name': 'Désactiver SysMain',
                'help': 'Précharge les applications en RAM. Désactiver si vous utilisez un SSD.',
                'default': False
            },
            {
                'id': 'svc_wsearch',
                'name': 'Désactiver Windows Search',
                'help': "Empêche l'indexation constante. TRÈS RECOMMANDÉ pour les SSD.",
                'default': False
            },
            {
                'id': 'svc_wuauserv_manual',
                'name': 'Windows Update Manuel',
                'help': 'Empêche les téléchargements de mises à jour pendant le jeu.',
                'default': False
            },
            {
                'id': 'ai_copilot',
                'name': 'Bloquer Windows Copilot',
                'help': "Désactive l'IA Copilot au niveau des GPO.",
                'default': False
            },
            {
                'id': 'ai_recall',
                'name': 'Désactiver Windows Recall',
                'help': 'Désactive les captures constantes de Windows Recall (IA).',
                'default': False
            },
            {
                'id': 'svc_bcastdvr',
                'name': 'Désactiver Game DVR',
                'help': "Empêche l'enregistrement d'écran en arrière-plan. Améliore les FPS.",
                'default': False
            },
            {
                'id': 'svc_wer',
                'name': "Désactiver le rapport d'erreurs Windows",
                'help': 'Système de collecte d\'erreurs Microsoft.',
                'default': False
            },
            {
                'id': 'svc_dps',
                'name': "Désactiver l'exécution des diagnostics",
                'help': 'Consomme des ressources pour diagnostiquer les défaillances silencieuses.',
                'default': False
            },
            {
                'id': 'svc_pcasvc',
                'name': "Désactiver l'Asst. de compatibilité PC",
                'help': "Moniteur d'applications héritées qui cause des micro-saccades.",
                'default': False
            },
            {
                'id': 'svc_remoteregistry',
                'name': 'Désactiver le Registre à distance',
                'help': 'Empêche les utilisateurs distants de modifier votre registre.',
                'default': False
            },
            {
                'id': 'svc_tabletinputservice',
                'name': 'Désactiver le clavier tactile',
                'help': "Désactiver si vous n'utilisez pas d'écran tactile.",
                'default': False
            },
            {
                'id': 'svc_wbio_srvc',
                'name': 'Désactiver la biométrie',
                'help': "Désactiver si vous n'utilisez pas d'empreinte digitale ou Face ID.",
                'default': False
            },
            {
                'id': 'svc_bits',
                'name': 'Désactiver BITS',
                'help': 'Transferts en arrière-plan pour Update/Store.',
                'default': False
            },
            {
                'id': 'svc_defrag_svc',
                'name': 'Désactiver la défragmentation auto',
                'help': 'Désactive la défragmentation automatique pour contrôler manuellement le trim SSD.',
                'default': False
            }
        ],
        'cat_clean': [
            {
                'id': 'clean_ram',
                'name': 'Optimiser la RAM (Clear Working Sets)',
                'help': 'Force la réduction du cache et des applications en arrière-plan pour libérer de la RAM instantanément.',
                'default': False
            },
            {
                'id': 'clean_temp',
                'name': 'Nettoyer le dossier Temp',
                'help': 'Supprime les fichiers temporaires des applications.',
                'default': False
            },
            {
                'id': 'clean_prefetch',
                'name': 'Nettoyer Prefetch',
                'help': 'Supprime les fichiers prefetch.',
                'default': False
            },
            {
                'id': 'clean_winupdate',
                'name': 'Nettoyer le cache Windows Update',
                'help': 'Efface les installateurs résiduels des anciennes mises à jour.',
                'default': False
            },
            {
                'id': 'clean_recycle',
                'name': 'Vider la corbeille',
                'help': 'Force le vidage de toutes les corbeilles sur tous les lecteurs.',
                'default': False
            },
            {
                'id': 'clean_dns',
                'name': 'Vider le cache DNS',
                'help': 'Répare les connexions lentes en renouvelant les routes réseau.',
                'default': False
            },
            {
                'id': 'clean_eventlog',
                'name': "Effacer l'observateur d'événements",
                'help': 'Supprime tous les journaux d\'événements Windows.',
                'default': False
            },
            {
                'id': 'clean_thumbcache',
                'name': 'Nettoyer le cache des miniatures',
                'help': 'Répare les icônes d\'images/vidéos corrompues.',
                'default': False
            },
            {
                'id': 'clean_fontcache',
                'name': 'Nettoyer le cache des polices',
                'help': 'Utile si le texte semble flou ou mal rendu.',
                'default': False
            },
            {
                'id': 'clean_iconcache',
                'name': 'Nettoyer le cache des icônes',
                'help': 'Efface et redémarre le cache des icônes du système.',
                'default': False
            },
            {
                'id': 'clean_crashdumps',
                'name': 'Supprimer les dumps de crash BSOD',
                'help': 'Supprime les fichiers massifs créés lors d\'un écran bleu.',
                'default': False
            },
            {
                'id': 'clean_chkdsk',
                'name': 'Supprimer les fragments CheckDisk',
                'help': 'Supprime les fichiers .chk orphelins après une récupération de disque.',
                'default': False
            },
            {
                'id': 'clean_onedrive_temp',
                'name': 'Nettoyer le cache OneDrive',
                'help': 'Efface les journaux et les résidus de OneDrive.',
                'default': False
            },
            {
                'id': 'clean_chrome_cache',
                'name': 'Nettoyer le cache Chrome',
                'help': 'Efface le cache de Google Chrome (sans supprimer les mots de passe).',
                'default': False
            },
            {
                'id': 'clean_edge_cache',
                'name': 'Nettoyer le cache Edge',
                'help': 'Efface le cache de Microsoft Edge.',
                'default': False
            },
            {
                'id': 'clean_firefox_cache',
                'name': 'Nettoyer le cache Firefox',
                'help': 'Efface le cache de Mozilla Firefox.',
                'default': False
            },
            {
                'id': 'clean_discord_cache',
                'name': 'Nettoyer le cache Discord',
                'help': 'Discord accumule beaucoup de cache avec le temps.',
                'default': False
            },
            {
                'id': 'clean_steam_cache',
                'name': 'Nettoyer le cache Steam',
                'help': 'Le navigateur Steam accumule des déchets qui le ralentissent.',
                'default': False
            },
            {
                'id': 'clean_epic_cache',
                'name': 'Nettoyer le cache Epic Games',
                'help': 'Aide le lanceur Epic Games à s\'ouvrir plus rapidement.',
                'default': False
            },
            {
                'id': 'clean_spotify_cache',
                'name': 'Nettoyer le cache Spotify',
                'help': 'Spotify stocke temporairement des gigaoctets de musique et de pochettes.',
                'default': False
            },
            {
                'id': 'clean_vcredist',
                'name': 'Nettoyer les VCRedist Steam',
                'help': 'Supprime les installateurs laissés par les jeux Steam.',
                'default': False
            },
            {
                'id': 'clean_usrdoc_temp',
                'name': 'Nettoyer les documents Temp',
                'help': 'Supprime les fichiers temporaires dans les dossiers de profil.',
                'default': False
            },
            {
                'id': 'clean_system_logs',
                'name': 'Supprimer les journaux d\'installation',
                'help': 'Supprime les journaux dans C:\\Windows.',
                'default': False
            },
            {
                'id': 'clean_crypt_svc',
                'name': 'Réinitialiser le cache Crypto',
                'help': 'Répare les signatures dans la base de données du système.',
                'default': False
            },
            {
                'id': 'clean_bits_queue',
                'name': 'Nettoyer la file d\'attente BITS',
                'help': 'Efface les tâches de téléchargement en arrière-plan.',
                'default': False
            }
        ],
        'cat_privacy': [
            {
                'id': 'priv_telemetry_level',
                'name': 'Niveau de télémétrie 0',
                'help': 'Bloque presque toute transmission de données de diagnostic.',
                'default': False
            },
            {
                'id': 'priv_etw_disable',
                'name': 'Blocage profond de la télémétrie ETW',
                'help': 'Désactive les sessions AutoLogger au niveau du noyau.',
                'default': False
            },
            {
                'id': 'priv_cortana',
                'name': 'Désactiver Cortana',
                'help': 'Libère de la RAM et les processus d\'écoute constante.',
                'default': False
            },
            {
                'id': 'priv_start_web',
                'name': 'Désactiver la recherche Web du menu Démarrer',
                'help': 'Recherche locale uniquement. Menu Démarrer ultra-rapide.',
                'default': False
            },
            {
                'id': 'priv_news',
                'name': 'Désactiver Actualités et centres d\'intérêt',
                'help': 'Supprime le widget météo et actualités de la barre des tâches.',
                'default': False
            },
            {
                'id': 'priv_location',
                'name': 'Désactiver la localisation',
                'help': 'Empêche Windows et les applications d\'accéder à votre position.',
                'default': False
            },
            {
                'id': 'priv_mic',
                'name': 'Désactiver les suggestions de frappe',
                'help': 'Désactive les prédictions qui envoient vos habitudes de frappe.',
                'default': False
            },
            {
                'id': 'priv_feedback',
                'name': 'Fréquence de feedback : Jamais',
                'help': 'Empêche Windows de demander constamment des avis.',
                'default': False
            },
            {
                'id': 'priv_activity',
                'name': "Désactiver l'historique d'activité",
                'help': "Empêche Windows d'enregistrer l'historique des applications et des fichiers.",
                'default': False
            },
            {
                'id': 'priv_sync',
                'name': 'Désactiver la synchronisation des paramètres',
                'help': 'Empêche l\'arrière-plan et les paramètres de se synchroniser sur le cloud.',
                'default': False
            },
            {
                'id': 'priv_advertising',
                'name': "Désactiver l'ID de publicité",
                'help': 'Empêche les publicités personnalisées via l\'ID de publicité.',
                'default': False
            },
            {
                'id': 'priv_appdiag',
                'name': 'Bloquer les diagnostics d\'application',
                'help': 'Empêche les applications d\'accéder aux diagnostics d\'autres applications.',
                'default': False
            },
            {
                'id': 'priv_tailored',
                'name': 'Désactiver les expériences personnalisées',
                'help': 'Empêche MS d\'utiliser les données de diagnostic pour du contenu personnel.',
                'default': False
            },
            {
                'id': 'priv_ceip',
                'name': 'Quitter le CEIP',
                'help': 'Quitte le programme d\'amélioration de Microsoft.',
                'default': False
            },
            {
                'id': 'priv_handwriting',
                'name': "Désactiver l'apprentissage de l'écriture manuscrite",
                'help': "Empêche la collecte de données du stylet.",
                'default': False
            },
            {
                'id': 'priv_defender_samples',
                'name': 'Ne pas envoyer d\'échantillons Defender',
                'help': 'Empêche Defender de télécharger des fichiers sur ses serveurs.',
                'default': False
            },
            {
                'id': 'priv_onedrive',
                'name': 'Désactiver OneDrive au démarrage',
                'help': 'Empêche OneDrive de démarrer avec le système.',
                'default': False
            },
            {
                'id': 'priv_meetnow',
                'name': 'Masquer "Réunion immédiate"',
                'help': 'Supprime l\'icône de caméra de la barre des tâches.',
                'default': False
            },
            {
                'id': 'priv_app_suggestions',
                'name': 'Désactiver les suggestions d\'applications',
                'help': 'Empêche Windows de suggérer des applications dans le menu Démarrer.',
                'default': False
            },
            {
                'id': 'priv_smartscreen',
                'name': 'Désactiver SmartScreen',
                'help': 'Réduit la protection contre les logiciels malveillants. ATTENTION.',
                'default': False
            }
        ],
        'cat_ui': [
            {
                'id': 'ui_animation',
                'name': 'Désactiver les animations de fenêtres',
                'help': 'Les fenêtres s\'ouvrent et se ferment instantanément.',
                'default': False
            },
            {
                'id': 'ui_transparency',
                'name': 'Désactiver la transparence',
                'help': 'Supprime les effets Mica/Acrylique. Libère le GPU.',
                'default': False
            },
            {
                'id': 'ui_shadows',
                'name': 'Supprimer les ombres',
                'help': 'Élimine les ombres des fenêtres et du curseur.',
                'default': False
            },
            {
                'id': 'ui_show_ext',
                'name': 'Afficher les extensions de fichiers',
                'help': 'Affiche .exe .jpg etc. Utile pour la sécurité.',
                'default': False
            },
            {
                'id': 'ui_show_hidden',
                'name': 'Afficher les fichiers cachés',
                'help': 'Affiche AppData et les dossiers cachés.',
                'default': False
            },
            {
                'id': 'ui_classic_menu',
                'name': 'Menu contextuel classique (Win11)',
                'help': 'Affiche le menu complet sans clics supplémentaires sous Win11.',
                'default': False
            },
            {
                'id': 'ui_darkmode',
                'name': 'Forcer le mode sombre',
                'help': 'Applique le mode sombre global aux applications et au système.',
                'default': False
            },
            {
                'id': 'ui_startup_delay',
                'name': 'Supprimer le délai de démarrage',
                'help': 'Élimine le délai de 10s imposé par Windows lors du chargement des applications.',
                'default': False
            },
            {
                'id': 'ui_taskbar_search',
                'name': 'Masquer la barre de recherche',
                'help': 'Supprime ou minimise la barre de recherche.',
                'default': False
            },
            {
                'id': 'ui_edge_tabs',
                'name': 'Masquer les onglets Edge dans Alt+Tab',
                'help': 'Évite l\'encombrement d\'Alt+Tab avec les onglets Edge.',
                'default': False
            },
            {
                'id': 'ui_lockscreen',
                'name': 'Désactiver l\'écran de verrouillage',
                'help': 'Va directement au mot de passe sans glisser.',
                'default': False
            },
            {
                'id': 'ui_blur_lock',
                'name': 'Supprimer le flou de connexion',
                'help': 'Supprime l\'effet de flou sur l\'écran de connexion.',
                'default': False
            },
            {
                'id': 'ui_actioncenter',
                'name': 'Désactiver le centre de notifications',
                'help': 'Supprime le panneau de notifications latéral.',
                'default': False
            },
            {
                'id': 'ui_snap',
                'name': "Désactiver l'assistant d'ancrage",
                'help': 'Empêche les suggestions lors du déplacement des fenêtres.',
                'default': False
            },
            {
                'id': 'ui_shake',
                'name': 'Désactiver Aero Shake',
                'help': 'Empêche de minimiser les fenêtres lors de l\'agitation d\'une.',
                'default': False
            },
            {
                'id': 'ui_balloon',
                'name': 'Désactiver les bulles d\'aide',
                'help': 'Désactive les info-bulles jaunes intrusives.',
                'default': False
            },
            {
                'id': 'ui_taskbar_animations',
                'name': 'Désactiver les animations de la barre des tâches',
                'help': 'Mouvements d\'icônes instantanés.',
                'default': False
            },
            {
                'id': 'ui_cursor_shadow',
                'name': 'Désactiver l\'ombre du curseur',
                'help': 'Supprime l\'ombre subtile sous le pointeur.',
                'default': False
            }
        ],
        'cat_net': [
            {
                'id': 'net_extreme_tcp',
                'name': 'Optimiseur TCP extrême (BBR)',
                'help': 'Algorithmes BBR/CUBIC modernes et désactivation de la modération des interruptions.',
                'default': False
            },
            {
                'id': 'net_autotuning',
                'name': 'Auto-Tuning TCP Normal',
                'help': 'Optimise la gestion des paquets par Windows. Améliore la latence.',
                'default': False
            },
            {
                'id': 'net_nagles',
                'name': "Désactiver l'algorithme de Nagle",
                'help': 'Envoie les paquets plus rapidement. Réduit la latence dans les MMO.',
                'default': False
            },
            {
                'id': 'net_rss',
                'name': 'Activer Receive-Side Scaling',
                'help': 'Distribue le traitement réseau sur plusieurs cœurs.',
                'default': False
            },
            {
                'id': 'net_qos',
                'name': 'Supprimer la limite de bande passante QoS',
                'help': 'Libère les 20% d\'internet réservés par Windows.',
                'default': False
            },
            {
                'id': 'net_deliveryopt',
                'name': "Désactiver l'optimisation de livraison P2P",
                'help': "Empêche Windows de télécharger des mises à jour sur Internet.",
                'default': False
            },
            {
                'id': 'net_wifi_power',
                'name': "Désactiver l'économie d'énergie WiFi",
                'help': "Empêche les déconnexions temporaires sur les ordinateurs portables.",
                'default': False
            },
            {
                'id': 'net_ecn',
                'name': 'Désactiver ECN',
                'help': 'L\'ECN cause parfois du lag dans les jeux. Le désactiver stabilise le ping.',
                'default': False
            },
            {
                'id': 'net_heuristics',
                'name': 'Désactiver les heuristiques TCP',
                'help': 'Empêche Windows de limiter la fenêtre TCP.',
                'default': False
            },
            {
                'id': 'net_lso',
                'name': 'Désactiver Large Send Offload',
                'help': 'LSO cause des pics de ping sur les cartes Intel/Realtek.',
                'default': False
            },
            {
                'id': 'net_chimney',
                'name': 'Désactiver TCP Chimney',
                'help': 'Peut causer une instabilité sur les routeurs modernes.',
                'default': False
            },
            {
                'id': 'net_ipv6',
                'name': 'Désactiver IPv6',
                'help': 'Cause parfois du lag local. Utiliser avec précaution.',
                'default': False
            },
            {
                'id': 'net_dnscache',
                'name': 'Éviter le cache DNS négatif',
                'help': 'Empêche l\'enregistrement des échecs de connexion temporaires.',
                'default': False
            },
            {
                'id': 'net_smb',
                'name': 'Désactiver SMBv1',
                'help': 'Protocole non sécurisé (WannaCry). Ferme une faille géante.',
                'default': False
            },
            {
                'id': 'net_teredo',
                'name': 'Désactiver le tunneling Teredo',
                'help': 'Transition IPv6 qui cause une surcharge.',
                'default': False
            },
            {
                'id': 'net_isatap',
                'name': 'Désactiver ISATAP',
                'help': 'Autre tunnel IPv6-IPv4 avec surcharge de ping.',
                'default': False
            },
            {
                'id': 'net_netbios',
                'name': 'Désactiver NetBIOS sur TCP',
                'help': 'Ne pas utiliser si vous partagez des imprimantes sur le réseau local.',
                'default': False
            },
            {
                'id': 'net_wpad',
                'name': 'Désactiver l\'auto-découverte WPAD',
                'help': 'Accélère le DNS et bloque un vecteur d\'attaque.',
                'default': False
            },
            {
                'id': 'net_tcp_1323',
                'name': 'Activer les horodatages RFC 1323',
                'help': 'Améliore la fiabilité lors des transferts volumineux.',
                'default': False
            },
            {
                'id': 'net_max_conn',
                'name': 'Max connexions 10 (HTTP 1.0)',
                'help': 'Accélère les chargements de pages web simultanés.',
                'default': False
            },
            {
                'id': 'net_max_conn11',
                'name': 'Max connexions 10 (HTTP 1.1)',
                'help': 'Accélère les chargements web HTTP 1.1.',
                'default': False
            },
            {
                'id': 'net_dns_cloudflare',
                'name': 'Définir DNS Cloudflare (1.1.1.1)',
                'help': 'Configure le DNS le plus rapide au monde par Cloudflare.',
                'default': False
            },
            {
                'id': 'net_dns_google',
                'name': 'Définir DNS Google (8.8.8.8)',
                'help': 'Configure le DNS de Google, rapide et fiable.',
                'default': False
            }
        ],
        'cat_gaming': [
            {
                'id': 'game_mode',
                'name': 'Activer le mode jeu Windows',
                'help': 'Priorise l\'accès du jeu au CPU/GPU.',
                'default': False
            },
            {
                'id': 'game_process_priority',
                'name': 'Élévation automatique de priorité (Booster)',
                'help': "Force une priorité 'Haute' en temps réel pour les processus de shooters compétitifs.",
                'default': False
            },
            {
                'id': 'game_process_lasso',
                'name': 'Game Booster actif',
                'help': 'Émule Process Lasso. Augmente la priorité du CPU à l\'ouverture des jeux.',
                'default': False
            },
            {
                'id': 'game_timer_res',
                'name': 'Résolution du timer 0.5ms',
                'help': 'Ajuste BCDEDIT pour un tickrate Windows haute précision.',
                'default': False
            },
            {
                'id': 'game_mouse_accel',
                'name': "Désactiver l'accélération de la souris",
                'help': 'Entrée 1:1 réelle. Essentiel pour les shooters compétitifs.',
                'default': False
            },
            {
                'id': 'game_ultimate_power',
                'name': 'Activer les performances ultimes',
                'help': 'Débloque le plan d\'alimentation Windows caché.',
                'default': False
            },
            {
                'id': 'game_msi_mode',
                'name': 'Hardware Latency Killer (MSI)',
                'help': 'Force le GPU/Réseau/USB à utiliser les interruptions MSI.',
                'default': False
            },
            {
                'id': 'game_hags',
                'name': 'Activer la planification de GPU à accélération matérielle',
                'help': 'Boost de FPS sous DX12. Nécessite un redémarrage.',
                'default': False
            },
            {
                'id': 'game_mmcss',
                'name': 'Optimiser MMCSS',
                'help': 'Redirige NetworkThrottlingIndex et le GPU vers le jeu.',
                'default': False
            },
            {
                'id': 'game_fullscreen_opt',
                'name': 'Désactiver les optimisations plein écran',
                'help': 'Évite le faux plein écran avec input lag.',
                'default': False
            },
            {
                'id': 'game_edge_bg',
                'name': 'Tuer Edge en arrière-plan',
                'help': 'Tue les processus msedge.exe qui consomment 500 Mo de RAM.',
                'default': False
            },
            {
                'id': 'game_chrome_bg',
                'name': 'Tuer Chrome en arrière-plan',
                'help': 'Élimine le flag pour les applications Chrome en arrière-plan.',
                'default': False
            },
            {
                'id': 'game_steam_hardware',
                'name': "Désactiver l'accélération matérielle Steam",
                'help': "Empêche Steam de consommer du GPU en arrière-plan.",
                'default': False
            },
            {
                'id': 'game_discord_hw',
                'name': "Désactiver l'accélération matérielle Discord",
                'help': "Si le GPU est à 99%, le désactiver évite les saccades.",
                'default': False
            },
            {
                'id': 'game_vr',
                'name': 'Réactivité du système (VR/Gaming)',
                'help': 'Règle SystemResponsiveness sur 0. Plus de cycles CPU pour le jeu.',
                'default': False
            },
            {
                'id': 'game_fth',
                'name': 'Désactiver Fault Tolerant Heap',
                'help': 'Empêche la dégradation du jeu lorsqu\'il crashe.',
                'default': False
            },
            {
                'id': 'game_hpet',
                'name': 'Désactiver HPET',
                'help': 'Réduit l\'input lag massif sur les anciens CPU ou Ryzen gen1.',
                'default': False
            },
            {
                'id': 'game_xbox_dvr',
                'name': 'Supprimer les clés de registre Xbox DVR',
                'help': 'Supprime les captures cachées. Augmente les FPS minimum sous DX12.',
                'default': False
            },
            {
                'id': 'game_core_parking',
                'name': 'Désactiver le Core Parking',
                'help': 'Empêche Windows d\'éteindre les cœurs du CPU.',
                'default': False
            },
            {
                'id': 'game_vbs',
                'name': 'Désactiver VBS',
                'help': '10% de surcharge en jeu. Uniquement si votre but est 100% gaming.',
                'default': False
            },
            {
                'id': 'perf_win32_priority',
                'name': 'Win32PrioritySeparation 26',
                'help': 'Optimise la priorité CPU pour les fenêtres actives (JEUX).',
                'default': False
            },
            {
                'id': 'perf_large_cache',
                'name': 'Large System Cache',
                'help': 'Améliore les performances des fichiers en utilisant plus de RAM.',
                'default': False
            },
            {
                'id': 'perf_io_limit',
                'name': 'Augmenter la limite de verrouillage de page IO',
                'help': 'Accélère les transferts de fichiers lourds.',
                'default': False
            },
            {
                'id': 'perf_wait_kill',
                'name': 'Tuer les services rapidement (2s)',
                'help': 'Réduit le temps d\'attente avant de tuer les services.',
                'default': False
            },
            {
                'id': 'perf_auto_end',
                'name': 'Fermeture auto des applications bloquées à l\'arrêt',
                'help': 'Force la fermeture des processus bloqués lors de l\'extinction.',
                'default': False
            },
            {
                'id': 'perf_menu_delay',
                'name': 'Délai d\'affichage des menus à zéro',
                'help': 'Les menus apparaissent instantanément.',
                'default': False
            },
            {
                'id': 'perf_startup_delay',
                'name': 'Supprimer le délai total de démarrage',
                'help': 'Lance les applications d\'arrière-plan sans temps d\'attente artificiel.',
                'default': False
            }
        ],
        'cat_power': [
            {
                'id': 'pwr_ultimate',
                'name': 'Forcer les performances ultimes',
                'help': 'Niveau de puissance maximal. Désactive toute économie de CPU.',
                'default': False
            },
            {
                'id': 'pwr_min_cpu',
                'name': 'CPU Minimum 100%',
                'help': 'Empêche le processeur de baisser de fréquence.',
                'default': False
            },
            {
                'id': 'pwr_throttling',
                'name': "Désactiver la limitation d'énergie",
                'help': "Empêche Windows de limiter Discord et les applications d'arrière-plan.",
                'default': False
            },
            {
                'id': 'pwr_cpu_boost',
                'name': 'Toujours activer le CPU Turbo Boost',
                'help': 'Maintient le turbo boost actif même sur batterie.',
                'default': False
            },
            {
                'id': 'pwr_pci_link',
                'name': 'Désactiver PCIe Link State Power Mgmt',
                'help': 'Empêche le GPU d\'entrer dans des états de faible consommation.',
                'default': False
            },
            {
                'id': 'pwr_hibernation',
                'name': 'Désactiver l\'hibernation',
                'help': 'Libère des gigaoctets sur C: et réduit l\'usure du SSD.',
                'default': False
            },
            {
                'id': 'pwr_disk_timeout',
                'name': 'Désactiver le délai d\'extinction du HDD',
                'help': 'Empêche les HDD de s\'éteindre causant des saccades.',
                'default': False
            },
            {
                'id': 'pwr_adaptive_brightness',
                'name': 'Désactiver la luminosité adaptative',
                'help': 'Empêche le capteur d\'ajuster automatiquement la luminosité.',
                'default': False
            },
            {
                'id': 'pwr_usb_hub_suspend',
                'name': 'Désactiver la suspension sélective du concentrateur USB',
                'help': 'Complément à la suspension USB Gaming. Plus stable.',
                'default': False
            }
        ],
        'cat_gpu': [
            {
                'id': 'gpu_hags',
                'name': 'Activer HAGS (Planification GPU matérielle)',
                'help': 'Déplace la file d\'attente des frames du CPU vers le GPU. Améliore les FPS en DX12/Vulkan.',
                'default': False
            },
            {
                'id': 'gpu_mpo',
                'name': 'Désactiver l\'MPO',
                'help': 'L\'MPO cause des écrans noirs et des saccades. Nvidia recommande de le désactiver.',
                'default': False
            },
            {
                'id': 'gpu_preemption',
                'name': 'Désactiver la préemption GPU',
                'help': 'Empêche les interruptions en milieu de frame. Élimine les micro-saccades.',
                'default': False
            },
            {
                'id': 'gpu_reduce_dpc',
                'name': 'Réduire la latence DPC du GPU',
                'help': 'Ajuste les interruptions du pilote GPU pour minimiser la latence DPC.',
                'default': False
            },
            {
                'id': 'gpu_dwm_priority',
                'name': 'Priorité haute DWM',
                'help': 'Augmente la priorité de dwm.exe pour un rendu plus fluide.',
                'default': False
            },
            {
                'id': 'gpu_gpu_priority',
                'name': 'Priorité GPU 8 (MMCSS)',
                'help': 'Ajuste GpuPriority pour une priorité plus élevée au processus de jeu.',
                'default': False
            },
            {
                'id': 'gpu_perf_registry',
                'name': 'Optimiser le registre GPU MMCSS',
                'help': 'Ajuste NetworkThrottlingIndex et SystemResponsiveness pour le GPU.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_power',
                'name': 'NVIDIA : Performances maximales',
                'help': 'Force les performances maximales dans le panneau NVIDIA via le registre.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_telemetry',
                'name': 'Désactiver la télémétrie NVIDIA',
                'help': 'Arrête les tâches de télémétrie NVIDIA en arrière-plan.',
                'default': False
            },
            {
                'id': 'gpu_amd_power',
                'name': 'AMD : Pas d\'économie d\'énergie GPU',
                'help': 'Empêche le GPU AMD d\'entrer dans des états de basse fréquence.',
                'default': False
            },
            {
                'id': 'gpu_amd_telemetry',
                'name': 'Désactiver la télémétrie AMD',
                'help': 'Arrête les services de télémétrie AMD en arrière-plan.',
                'default': False
            },
            {
                'id': 'gpu_pci_express_max',
                'name': 'Mode maximum PCIe GPU',
                'help': 'Désactive le Link State Power Management spécifiquement pour le GPU.',
                'default': False
            },
            {
                'id': 'gpu_disable_fullscreen_opt',
                'name': 'Désactiver les optimisations plein écran globales',
                'help': 'Force le plein écran exclusif réel dans tous les jeux.',
                'default': False
            },
            {
                'id': 'gpu_freesync_vsync_off',
                'name': 'Désactiver la V-Sync globale',
                'help': 'Désactive la V-Sync par défaut dans toutes les applications via le registre.',
                'default': False
            },
            {
                'id': 'gpu_cache_clean',
                'name': 'Nettoyer le cache des shaders GPU',
                'help': 'Efface le cache des shaders accumulé. Utile si saccades en entrant dans des zones.',
                'default': False
            },
            {
                'id': 'gpu_vram_paging',
                'name': 'Optimiser la pagination VRAM',
                'help': 'Utilise la RAM système comme extension pour les GPU avec peu de VRAM.',
                'default': False
            },
            {
                'id': 'gpu_shader_cache',
                'name': 'Rediriger le cache des shaders vers SSD rapide',
                'help': 'Configure le cache des shaders pour une lecture rapide sur NVMe.',
                'default': False
            },
            {
                'id': 'gpu_disable_mpv',
                'name': 'Désactiver la précompilation arrière-plan DX12/Vulkan',
                'help': 'Empêche la précompilation des shaders pendant que vous jouez.',
                'default': False
            },
            {
                'id': 'gpu_gsync_compat',
                'name': 'G-Sync sur moniteurs FreeSync',
                'help': 'Force la compatibilité G-Sync sur les moniteurs AMD avec GPU Nvidia.',
                'default': False
            },
            {
                'id': 'gpu_night_light_off',
                'name': "Désactiver l'éclairage nocturne",
                'help': "Empêche Windows d'altérer l'étalonnage des couleurs du moniteur.",
                'default': False
            }
        ],
        'cat_kernel': [
            {
                'id': 'ext_57_processes',
                'name': 'Consolidation des services système (processus minimaux)',
                'help': 'Redirige svchost et désactive les services non critiques pour réduire le nombre total de processus actifs au minimum opérationnel.',
                'default': False
            },
            {
                'id': 'kern_registry_size',
                'name': 'Augmenter la taille max du registre',
                'help': 'Prévient les erreurs de limite de registre sur les systèmes personnalisés.',
                'default': False
            },
            {
                'id': 'kern_bcdedit_inc',
                'name': 'Fréquence d\'interruption BCDEDIT',
                'help': 'Augmente la précision de l\'horloge via BCDEDIT. Clé pour un timer < 1ms.',
                'default': False
            },
            {
                'id': 'kern_memory_comp',
                'name': "Désactiver la compression de mémoire (MMAgent)",
                'help': "Empêche le CPU de gaspiller des cycles à compresser les pages RAM, priorisant la latence.",
                'default': False
            },
            {
                'id': 'kern_system_resp',
                'name': 'SystemResponsiveness à 0% (Temps Réel)',
                'help': 'Supprime la réserve de ressources d\'arrière-plan de Windows pour dédier 100% au processus focalisé.',
                'default': False
            },
            {
                'id': 'kernel_mitigations',
                'name': 'Désactiver les atténuations CPU',
                'help': 'Désactive Spectre/Meltdown. +5-15% CPU pur. Réduit la sécurité.',
                'default': False
            },
            {
                'id': 'kern_large_pages',
                'name': 'Activer les Large Pages (Mémoire virtuelle)',
                'help': 'Réduit les défauts de page (TLB misses) dans les applications gourmandes en mémoire.',
                'default': False
            },
            {
                'id': 'kern_iot_core',
                'name': 'Config de profil embarqué minimaliste',
                'help': 'Ajuste les paramètres internes du système pour se comporter comme un profil Windows IoT à faibles ressources.',
                'default': False
            },
            {
                'id': 'kern_process_isolation',
                'name': "Désactiver l'isolement des processus principaux",
                'help': "Réduit la surcharge de virtualisation du noyau pour maximiser la vitesse des threads.",
                'default': False
            }
        ],
        'cat_extreme': [
            {
                'id': 'ext_super_nuclear',
                'name': 'Nettoyage massif des services système',
                'help': 'Désactive tous les services réseau, d\'impression et visuels non essentiels. Irréversible sans restauration.',
                'default': False
            },
            {
                'id': 'ext_minimalist',
                'name': 'Profil Shell réduit haute performance',
                'help': 'Désactive les effets visuels du Shell Windows pour libérer totalement les cycles CPU et GPU.',
                'default': False
            },
            {
                'id': 'ext_defender_kill',
                'name': 'Désactivation permanente de Windows Defender',
                'help': 'Supprime le moteur d\'analyse et les services de sécurité natifs via registre/GPO.',
                'default': False
            },
            {
                'id': 'ext_uwp_kill_all',
                'name': 'Suppression complète des applications UWP intégrées',
                'help': 'Désinstalle toutes les applications UWP pré-installées pour tous les utilisateurs du système.',
                'default': False
            },
            {
                'id': 'ext_firewall_off',
                'name': 'Désactiver le pare-feu Windows (Stack Bypass)',
                'help': 'Désactive le filtrage de paquets natif pour minimiser la latence réseau.',
                'default': False
            },
            {
                'id': 'ext_update_dead',
                'name': 'Blocage de Windows Update (Politique LTSC)',
                'help': 'Empêche toute tentative de mise à jour ou de téléchargement de pilote par le système d\'exploitation.',
                'default': False
            }
        ],
        'cat_util': [
            {
                'id': 'util_dotnet',
                'name': 'Installer les runtimes .NET',
                'help': 'Assure la compatibilité avec toutes les versions des frameworks d\'application.',
                'default': False
            },
            {
                'id': 'util_vc_redist',
                'name': 'Installer les Redistribuables C++',
                'help': 'Installe toutes les bibliothèques nécessaires aux jeux et logiciels.',
                'default': False
            },
            {
                'id': 'util_directx',
                'name': 'Mettre à jour les runtimes DirectX',
                'help': 'Installe les composants DirectX hérités pour les anciens jeux.',
                'default': False
            },
            {
                'id': 'util_powershell_7',
                'name': 'Installer PowerShell 7',
                'help': 'Installe la version moderne et plus rapide du moteur de script Windows.',
                'default': False
            },
            {
                'id': 'util_driver_updates',
                'name': 'Exclure les mises à jour de pilotes',
                'help': 'Empêche Windows d\'écraser vos pilotes personnalisés avec des versions génériques.',
                'default': False
            },
            {
                'id': 'util_ps_telemetry',
                'name': 'Désactiver la télémétrie PowerShell',
                'help': 'Supprime le rapport d\'utilisation dans le terminal Windows moderne.',
                'default': False
            },
            {
                'id': 'util_end_task_rc',
                'name': 'Fin de tâche sur la barre des tâches',
                'help': 'Ajoute l\'option de fermer les processus directement depuis un clic droit sur la barre des tâches.',
                'default': False
            },
            {
                'id': 'util_start_recommendations',
                'name': 'Supprimer les recommandations de Démarrer',
                'help': 'Efface la section des fichiers récents et des applications suggérées dans Démarrer.',
                'default': False
            },
            {
                'id': 'util_sticky_keys',
                'name': 'Désactiver les touches rémanentes',
                'help': 'Empêche le système de poser des questions sur les touches rémanentes après avoir appuyé plusieurs fois sur Maj.',
                'default': False
            },
            {
                'id': 'util_taskbar_center',
                'name': 'Barre des tâches : Aligner à gauche',
                'help': 'Rétablit la position classique des icônes sur le bureau Windows 11.',
                'default': False
            },
            {
                'id': 'util_settings_home',
                'name': 'Supprimer la page d\'accueil des paramètres',
                'help': "Supprime l'écran 'Accueil' inutile lors de l'ouverture des paramètres Windows.",
                'default': False
            },
            {
                'id': 'util_new_outlook',
                'name': 'Bloquer le nouvel Outlook',
                'help': 'Empêche Windows de remplacer le client de messagerie classique par la version web-app.',
                'default': False
            },
            {
                'id': 'util_cross_device',
                'name': 'Désactiver les expériences multi-appareils',
                'help': 'Désactive la synchronisation des tâches inachevées avec d\'autres PC ou mobiles.',
                'default': False
            },
            {
                'id': 'util_task_view',
                'name': 'Masquer la vue des tâches',
                'help': 'Nettoie la barre des tâches en supprimant l\'icône des bureaux virtuels.',
                'default': False
            },
            {
                'id': 'util_folder_discovery',
                'name': "Désactiver la découverte automatique de dossiers",
                'help': "Empêche l'Explorateur de changer le type de vue lors de l'ouverture de dossiers contenant des images ou de la musique.",
                'default': False
            },
            {
                'id': 'util_bsod_detail',
                'name': 'BSOD avec informations détaillées',
                'help': 'Affiche les paramètres complets et les codes d\'erreur sur l\'écran bleu de la mort.',
                'default': False
            },
            {
                'id': 'util_numlock',
                'name': 'Activer Verr. Num au démarrage',
                'help': 'Active automatiquement Verr. Num lors de la connexion à Windows.',
                'default': False
            },
            {
                'id': 'util_verbose_logon',
                'name': 'Messages de connexion détaillés',
                'help': 'Affiche l\'état de chaque service pendant la connexion et la déconnexion.',
                'default': False
            },
            {
                'id': 'util_consumer_features',
                'name': 'Désactiver les suggestions du Store',
                'help': 'Empêche l\'installation silencieuse d\'applications promotionnelles de Microsoft.',
                'default': False
            },
            {
                'id': 'util_wpbt',
                'name': 'Bloquer l\'injection de bloatware (WPBT)',
                'help': 'Empêche les fabricants d\'installer des logiciels via le BIOS lors du démarrage de Windows.',
                'default': False
            },
            {
                'id': 'util_widgets_remove',
                'name': 'Supprimer les widgets Windows 11',
                'help': 'Désinstalle le panneau des widgets et des actualités de la barre des tâches.',
                'default': False
            },
            {
                'id': 'uwp_xbox',
                'name': 'Supprimer les applications Xbox',
                'help': 'Supprime toutes les applications Xbox (GameBar, TCUI). NE PAS UTILISER SI VOUS JOUEZ SUR LE PC GAME PASS.',
                'default': False
            },
            {
                'id': 'uwp_bloatware',
                'name': 'Supprimer les bloatwares natifs',
                'help': 'Supprime les applications inutiles : Zune, BingNews, GetHelp, Solitaire, People...',
                'default': False
            },
            {
                'id': 'uwp_onedrive',
                'name': 'Désinstaller OneDrive',
                'help': 'Désinstalle profondément Microsoft OneDrive du système.',
                'default': False
            },
            {
                'id': 'uwp_edge',
                'name': 'Supprimer Edge (Avancé)',
                'help': 'Tente de supprimer Microsoft Edge avec PowerShell. Ayez un autre navigateur prêt.',
                'default': False
            },
            {
                'id': 'uwp_3dbuilder',
                'name': 'Supprimer 3D Builder',
                'help': 'Désinstalle l\'application de modélisation 3D de Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_alarms',
                'name': 'Supprimer Alarmes et horloge',
                'help': 'Désinstalle l\'application d\'alarmes et de chronomètre.',
                'default': False
            },
            {
                'id': 'uwp_camera',
                'name': 'Supprimer Caméra',
                'help': 'Désinstalle l\'application caméra du Store.',
                'default': False
            },
            {
                'id': 'uwp_communications',
                'name': 'Supprimer Courrier et Calendrier',
                'help': 'Désinstalle les applications de courrier et de calendrier intégrées.',
                'default': False
            },
            {
                'id': 'uwp_feedback',
                'name': 'Supprimer Hub de commentaires',
                'help': 'Désinstalle l\'application de feedback de Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_gethelp',
                'name': 'Supprimer Obtenir de l\'aide',
                'help': 'Désinstalle l\'application de support technique de Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_maps',
                'name': 'Supprimer Cartes',
                'help': 'Désinstalle l\'application de cartes intégrée.',
                'default': False
            },
            {
                'id': 'uwp_mixedreality',
                'name': 'Supprimer Portail de réalité mixte',
                'help': 'Désinstalle le portail de réalité mixte.',
                'default': False
            },
            {
                'id': 'uwp_people',
                'name': 'Supprimer Contacts (People)',
                'help': 'Désinstalle l\'application de contacts intégrée.',
                'default': False
            },
            {
                'id': 'uwp_photos',
                'name': 'Supprimer Photos',
                'help': 'Désinstalle l\'application Photos moderne (remplaçable par la visionneuse classique).',
                'default': False
            },
            {
                'id': 'uwp_skype',
                'name': 'Supprimer Skype',
                'help': 'Désinstalle l\'application Skype pré-installée.',
                'default': False
            },
            {
                'id': 'uwp_solitaire',
                'name': 'Supprimer Solitaire',
                'help': 'Désinstalle les jeux de solitaire pré-installés.',
                'default': False
            },
            {
                'id': 'uwp_soundrecorder',
                'name': 'Supprimer Enregistreur vocal',
                'help': 'Désinstalle l\'application d\'enregistrement audio.',
                'default': False
            },
            {
                'id': 'uwp_stickynotes',
                'name': 'Supprimer Sticky Notes',
                'help': 'Désinstalle l\'application de notes adhésives.',
                'default': False
            },
            {
                'id': 'uwp_weather',
                'name': 'Supprimer Météo',
                'help': 'Désinstalle l\'application météo.',
                'default': False
            },
            {
                'id': 'uwp_yourphone',
                'name': 'Supprimer Votre téléphone',
                'help': 'Désinstalle l\'application de liaison avec le téléphone.',
                'default': False
            }
        ],
        'cat_pro': [
            {
                'id': 'util_context_compact',
                'name': 'Activer les menus contextuels compacts',
                'help': 'Réduit le padding et l\'espacement entre les options des menus clic droit.',
                'default': False
            },
            {
                'id': 'util_legacy_photo',
                'name': 'Restaurer la visionneuse de photos classique (Win7)',
                'help': 'Active la visionneuse d\'images ultra-rapide et légère des versions précédentes.',
                'default': False
            },
            {
                'id': 'util_legacy_calc',
                'name': 'Restaurer la calculatrice classique Win32',
                'help': 'Remplace la version UWP lente par la version exécutable traditionnelle.',
                'default': False
            },
            {
                'id': 'util_god_mode',
                'name': 'Accès unifié au Panneau de configuration',
                'help': 'Crée un raccourci vers tous les paramètres administratifs du système dans une seule fenêtre.',
                'default': False
            },
            {
                'id': 'util_verbose_boot',
                'name': 'Activer l\'historique de démarrage détaillé',
                'help': 'Affiche les pilotes et services chargés pendant le démarrage sur l\'écran.',
                'default': False
            },
            {
                'id': 'util_desktop_labels',
                'name': 'Supprimer les flèches de raccourci',
                'help': 'Nettoie les icônes du bureau en supprimant la flèche de raccourci.',
                'default': False
            },
            {
                'id': 'util_explorer_pc',
                'name': "Ouvrir l'Explorateur sur 'Ce PC'",
                'help': 'Configure l\'explorateur pour ignorer la vue des fichiers récents par défaut.',
                'default': False
            }
        ],
        'cat_help': []
    }
