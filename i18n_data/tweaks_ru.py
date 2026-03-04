# type: ignore
def get_tweaks_ru():
    return {
        'cat_system': [
            {
                'id': 'svc_diagtrack',
                'name': 'Отключить телеметрию',
                'help': 'Отключает DiagTrack. Освобождает фоновые процессы.',
                'default': False
            },
            {
                'id': 'svc_sysmain',
                'name': 'Отключить SysMain',
                'help': 'Предварительная загрузка приложений в ОЗУ. Отключите, если используете SSD.',
                'default': False
            },
            {
                'id': 'svc_wsearch',
                'name': 'Отключить Windows Search',
                'help': 'Предотвращает постоянную индексацию. НАСТОЯТЕЛЬНО РЕКОМЕНДУЕТСЯ для SSD.',
                'default': False
            },
            {
                'id': 'svc_wuauserv_manual',
                'name': 'Ручное обновление Windows',
                'help': 'Предотвращает загрузку обновлений во время игры.',
                'default': False
            },
            {
                'id': 'ai_copilot',
                'name': 'Блокировать Windows Copilot',
                'help': 'Отключает ИИ Copilot на уровне GPO.',
                'default': False
            },
            {
                'id': 'ai_recall',
                'name': 'Отключить Windows Recall',
                'help': 'Отключает постоянные скриншоты Windows Recall (ИИ).',
                'default': False
            },
            {
                'id': 'svc_bcastdvr',
                'name': 'Отключить Game DVR',
                'help': 'Предотвращает запись экрана в фоновом режиме. Повышает FPS.',
                'default': False
            },
            {
                'id': 'svc_wer',
                'name': 'Отключить отчеты об ошибках',
                'help': 'Система сбора ошибок Microsoft.',
                'default': False
            },
            {
                'id': 'svc_dps',
                'name': 'Отключить выполнение диагностики',
                'help': 'Потребляет ресурсы для диагностики скрытых сбоев.',
                'default': False
            },
            {
                'id': 'svc_pcasvc',
                'name': 'Отключить пом. по совместимости',
                'help': 'Монитор устаревших приложений, вызывающий микро-фризы.',
                'default': False
            },
            {
                'id': 'svc_remoteregistry',
                'name': 'Отключить удаленный реестр',
                'help': 'Предотвращает изменение реестра удаленными пользователями.',
                'default': False
            },
            {
                'id': 'svc_tabletinputservice',
                'name': 'Отключить сенсорную клавиатуру',
                'help': 'Отключите, если не используете сенсорный экран.',
                'default': False
            },
            {
                'id': 'svc_wbio_srvc',
                'name': 'Отключить биометрию',
                'help': 'Отключите, если не используете отпечатки пальцев или Face ID.',
                'default': False
            },
            {
                'id': 'svc_bits',
                'name': 'Отключить BITS',
                'help': 'Фоновая передача для Update/Store.',
                'default': False
            },
            {
                'id': 'svc_defrag_svc',
                'name': 'Отключить авто-дефрагментацию',
                'help': 'Отключает автоматическую дефрагментацию для ручного управления trim SSD.',
                'default': False
            }
        ],
        'cat_clean': [
            {
                'id': 'clean_ram',
                'name': 'Оптимизировать ОЗУ (Clear Working Sets)',
                'help': 'Принудительно уменьшает кеш и фоновые приложения для мгновенного освобождения ОЗУ.',
                'default': False
            },
            {
                'id': 'clean_temp',
                'name': 'Очистить временную папку',
                'help': 'Удаляет временные файлы приложений.',
                'default': False
            },
            {
                'id': 'clean_prefetch',
                'name': 'Очистить Prefetch',
                'help': 'Удаляет файлы предварительной выборки (prefetch).',
                'default': False
            },
            {
                'id': 'clean_winupdate',
                'name': 'Очистить кеш обновлений Windows',
                'help': 'Удаляет остаточные установочные файлы старых обновлений.',
                'default': False
            },
            {
                'id': 'clean_recycle',
                'name': 'Очистить корзину',
                'help': 'Принудительно очищает все корзины на всех дисках.',
                'default': False
            },
            {
                'id': 'clean_dns',
                'name': 'Очистить кеш DNS',
                'help': 'Исправляет медленные соединения путем обновления сетевых маршрутов.',
                'default': False
            },
            {
                'id': 'clean_eventlog',
                'name': 'Очистить журнал событий',
                'help': 'Удаляет все журналы событий Windows.',
                'default': False
            },
            {
                'id': 'clean_thumbcache',
                'name': 'Очистить кеш эскизов',
                'help': 'Восстанавливает поврежденные иконки изображений/видео.',
                'default': False
            },
            {
                'id': 'clean_fontcache',
                'name': 'Очистить кеш шрифтов',
                'help': 'Полезно, если текст выглядит размытым или плохо отрисованным.',
                'default': False
            },
            {
                'id': 'clean_iconcache',
                'name': 'Очистить кеш иконок',
                'help': 'Удаляет и перезапускает системный кеш иконок.',
                'default': False
            },
            {
                'id': 'clean_crashdumps',
                'name': 'Удалить дампы памяти BSOD',
                'help': 'Удаляет огромные файлы, созданные при синем экране.',
                'default': False
            },
            {
                'id': 'clean_chkdsk',
                'name': 'Удалить фрагменты CheckDisk',
                'help': 'Удаляет файлы .chk, оставшиеся после восстановления диска.',
                'default': False
            },
            {
                'id': 'clean_onedrive_temp',
                'name': 'Очистить кеш OneDrive',
                'help': 'Удаляет логи и остатки OneDrive.',
                'default': False
            },
            {
                'id': 'clean_chrome_cache',
                'name': 'Очистить кеш Chrome',
                'help': 'Удаляет кеш Google Chrome (без удаления паролей).',
                'default': False
            },
            {
                'id': 'clean_edge_cache',
                'name': 'Очистить кеш Edge',
                'help': 'Удаляет кеш Microsoft Edge.',
                'default': False
            },
            {
                'id': 'clean_firefox_cache',
                'name': 'Очистить кеш Firefox',
                'help': 'Удаляет кеш Mozilla Firefox.',
                'default': False
            },
            {
                'id': 'clean_discord_cache',
                'name': 'Очистить кеш Discord',
                'help': 'Discord со временем накапливает много кеша.',
                'default': False
            },
            {
                'id': 'clean_steam_cache',
                'name': 'Очистить кеш Steam',
                'help': 'Браузер Steam накапливает мусор, который замедляет его.',
                'default': False
            },
            {
                'id': 'clean_epic_cache',
                'name': 'Очистить кеш Epic Games',
                'help': 'Помогает Epic Games Launcher открываться быстрее.',
                'default': False
            },
            {
                'id': 'clean_spotify_cache',
                'name': 'Очистить кеш Spotify',
                'help': 'Spotify временно хранит гигабайты музыки и обложек.',
                'default': False
            },
            {
                'id': 'clean_vcredist',
                'name': 'Очистить VCRedist Steam',
                'help': 'Удаляет установщики, оставленные играми Steam.',
                'default': False
            },
            {
                'id': 'clean_usrdoc_temp',
                'name': 'Очистить временные документы',
                'help': 'Удаляет временные файлы в папках профиля.',
                'default': False
            },
            {
                'id': 'clean_system_logs',
                'name': 'Удалить журналы установки',
                'help': 'Удаляет журналы в C:\\Windows.',
                'default': False
            },
            {
                'id': 'clean_crypt_svc',
                'name': 'Сбросить кеш Crypto',
                'help': 'Восстанавливает подписи в системной базе данных.',
                'default': False
            },
            {
                'id': 'clean_bits_queue',
                'name': 'Очистить очередь BITS',
                'help': 'Удаляет фоновые задачи загрузки.',
                'default': False
            }
        ],
        'cat_privacy': [
            {
                'id': 'priv_telemetry_level',
                'name': 'Уровень телеметрии 0',
                'help': 'Блокирует почти всю передачу диагностических данных.',
                'default': False
            },
            {
                'id': 'priv_etw_disable',
                'name': 'Глубокая блокировка телеметрии ETW',
                'help': 'Отключает сеансы AutoLogger на уровне ядра.',
                'default': False
            },
            {
                'id': 'priv_cortana',
                'name': 'Отключить Cortana',
                'help': 'Освобождает ОЗУ и процессы постоянного прослушивания.',
                'default': False
            },
            {
                'id': 'priv_start_web',
                'name': 'Отключить веб-поиск в меню Пуск',
                'help': 'Только локальный поиск. Ультра-быстрое меню Пуск.',
                'default': False
            },
            {
                'id': 'priv_news',
                'name': 'Отключить Новости и интересы',
                'help': 'Удаляет виджет погоды и новостей из панели задач.',
                'default': False
            },
            {
                'id': 'priv_location',
                'name': 'Отключить местоположение',
                'help': 'Предотвращает доступ Windows и приложений к вашему положению.',
                'default': False
            },
            {
                'id': 'priv_mic',
                'name': 'Отключить подсказки при наборе',
                'help': 'Отключает прогнозы, которые отправляют ваши шаблоны набора.',
                'default': False
            },
            {
                'id': 'priv_feedback',
                'name': 'Частота отзывов: Никогда',
                'help': 'Предотвращает постоянные запросы мнений от Windows.',
                'default': False
            },
            {
                'id': 'priv_activity',
                'name': 'Отключить журнал активности',
                'help': 'Предотвращает сохранение истории приложений и файлов Windows.',
                'default': False
            },
            {
                'id': 'priv_sync',
                'name': 'Отключить синхронизацию настроек',
                'help': 'Предотвращает загрузку фона и настроек в облако.',
                'default': False
            },
            {
                'id': 'priv_advertising',
                'name': 'Отключить рекламный ID',
                'help': 'Предотвращает персонализированную рекламу через рекламный ID.',
                'default': False
            },
            {
                'id': 'priv_appdiag',
                'name': 'Блокировать диагностику приложений',
                'help': 'Предотвращает доступ приложений к диагностике других приложений.',
                'default': False
            },
            {
                'id': 'priv_tailored',
                'name': 'Отключить персонализацию',
                'help': 'Предотвращает использование диагностических данных MS для личного контента.',
                'default': False
            },
            {
                'id': 'priv_ceip',
                'name': 'Выйти из CEIP',
                'help': 'Выход из программы улучшения Microsoft.',
                'default': False
            },
            {
                'id': 'priv_handwriting',
                'name': 'Отключить обучение рукописи',
                'help': 'Предотвращает сбор данных со стилуса.',
                'default': False
            },
            {
                'id': 'priv_defender_samples',
                'name': 'Не отправлять образцы Defender',
                'help': 'Предотвращает загрузку файлов Defender на свои серверы.',
                'default': False
            },
            {
                'id': 'priv_onedrive',
                'name': 'Отключить OneDrive при запуске',
                'help': 'Предотвращает запуск OneDrive вместе с системой.',
                'default': False
            },
            {
                'id': 'priv_meetnow',
                'name': 'Скрыть "Провести собрание"',
                'help': 'Удаляет иконку камеры из панели задач.',
                'default': False
            },
            {
                'id': 'priv_app_suggestions',
                'name': 'Отключить предложения приложений',
                'help': 'Предотвращает предложение приложений в меню Пуск.',
                'default': False
            },
            {
                'id': 'priv_smartscreen',
                'name': 'Отключить SmartScreen',
                'help': 'Снижает защиту от вредоносных программ. ВНИМАНИЕ.',
                'default': False
            }
        ],
        'cat_ui': [
            {
                'id': 'ui_animation',
                'name': 'Отключить анимацию окон',
                'help': 'Окна открываются и закрываются мгновенно.',
                'default': False
            },
            {
                'id': 'ui_transparency',
                'name': 'Отключить прозрачность',
                'help': 'Удаляет эффекты Mica/Acrylic. Освобождает GPU.',
                'default': False
            },
            {
                'id': 'ui_shadows',
                'name': 'Удалить тени',
                'help': 'Удаляет тени от окон и курсора.',
                'default': False
            },
            {
                'id': 'ui_show_ext',
                'name': 'Показывать расширения файлов',
                'help': 'Показывает .exe .jpg и т.д. Полезно для безопасности.',
                'default': False
            },
            {
                'id': 'ui_show_hidden',
                'name': 'Показывать скрытые файлы',
                'help': 'Показывает AppData и скрытые папки.',
                'default': False
            },
            {
                'id': 'ui_classic_menu',
                'name': 'Классическое контекстное меню (Win11)',
                'help': 'Показывает полное меню без лишних кликов в Win11.',
                'default': False
            },
            {
                'id': 'ui_darkmode',
                'name': 'Форсировать темную тему',
                'help': 'Применяет глобальную темную тему к приложениям и системе.',
                'default': False
            },
            {
                'id': 'ui_startup_delay',
                'name': 'Удалить задержку запуска',
                'help': 'Удаляет 10-секундную задержку Windows при загрузке приложений.',
                'default': False
            },
            {
                'id': 'ui_taskbar_search',
                'name': 'Скрыть панель поиска',
                'help': 'Удаляет или минимизирует панель поиска.',
                'default': False
            },
            {
                'id': 'ui_edge_tabs',
                'name': 'Скрыть вкладки Edge в Alt+Tab',
                'help': 'Избегает загромождения Alt+Tab вкладками Edge.',
                'default': False
            },
            {
                'id': 'ui_lockscreen',
                'name': 'Отключить экран блокировки',
                'help': 'Переход сразу к паролю без смахивания.',
                'default': False
            },
            {
                'id': 'ui_blur_lock',
                'name': 'Удалить размытие входа',
                'help': 'Удаляет эффект размытия на экране входа.',
                'default': False
            },
            {
                'id': 'ui_actioncenter',
                'name': 'Отключить центр уведомлений',
                'help': 'Удаляет боковую панель уведомлений.',
                'default': False
            },
            {
                'id': 'ui_snap',
                'name': 'Отключить привязку окон',
                'help': 'Предотвращает подсказки при перетаскивании окон.',
                'default': False
            },
            {
                'id': 'ui_shake',
                'name': 'Отключить Aero Shake',
                'help': 'Предотвращает сворачивание окон при встряхивании одного из них.',
                'default': False
            },
            {
                'id': 'ui_balloon',
                'name': 'Отключить всплывающие подсказки',
                'help': 'Отключает навязчивые желтые всплывающие окна.',
                'default': False
            },
            {
                'id': 'ui_taskbar_animations',
                'name': 'Отключить анимацию панели задач',
                'help': 'Мгновенное перемещение иконок.',
                'default': False
            },
            {
                'id': 'ui_cursor_shadow',
                'name': 'Отключить тень курсора',
                'help': 'Удаляет тонкую тень под указателем.',
                'default': False
            }
        ],
        'cat_net': [
            {
                'id': 'net_extreme_tcp',
                'name': 'Экстремальный оптимизатор TCP (BBR)',
                'help': 'Современные алгоритмы BBR/CUBIC и отключение модерации прерываний.',
                'default': False
            },
            {
                'id': 'net_autotuning',
                'name': 'Нормальный авто-тюнинг TCP',
                'help': 'Оптимизирует обработку пакетов Windows. Улучшает задержку.',
                'default': False
            },
            {
                'id': 'net_nagles',
                'name': 'Отключить алгоритм Нейгла',
                'help': 'Отправляет пакеты быстрее. Снижает задержку в MMO.',
                'default': False
            },
            {
                'id': 'net_rss',
                'name': 'Включить Receive-Side Scaling',
                'help': 'Распределяет сетевую обработку по нескольким ядрам.',
                'default': False
            },
            {
                'id': 'net_qos',
                'name': 'Снять лимит пропускной способности QoS',
                'help': 'Освобождает 20% интернета, зарезервированных Windows.',
                'default': False
            },
            {
                'id': 'net_deliveryopt',
                'name': 'Отключить оптимизацию доставки P2P',
                'help': 'Предотвращает загрузку обновлений Windows в Интернет.',
                'default': False
            },
            {
                'id': 'net_wifi_power',
                'name': 'Отключить экономию энергии WiFi',
                'help': 'Предотвращает временные разрывы связи на ноутбуках.',
                'default': False
            },
            {
                'id': 'net_ecn',
                'name': 'Отключить ECN',
                'help': 'ECN иногда вызывает лаги в играх. Отключение стабилизирует пинг.',
                'default': False
            },
            {
                'id': 'net_heuristics',
                'name': 'Отключить эвристику TCP',
                'help': 'Предотвращает ограничение окна TCP со стороны Windows.',
                'default': False
            },
            {
                'id': 'net_lso',
                'name': 'Отключить Large Send Offload',
                'help': 'LSO вызывает скачки пинга на картах Intel/Realtek.',
                'default': False
            },
            {
                'id': 'net_chimney',
                'name': 'Отключить TCP Chimney',
                'help': 'Может вызвать нестабильность на современных роутерах.',
                'default': False
            },
            {
                'id': 'net_ipv6',
                'name': 'Отключить IPv6',
                'help': 'Иногда вызывает локальные лаги. Используйте с осторожностью.',
                'default': False
            },
            {
                'id': 'net_dnscache',
                'name': 'Избегать негативного кеша DNS',
                'help': 'Предотвращает сохранение временных неудач соединения.',
                'default': False
            },
            {
                'id': 'net_smb',
                'name': 'Отключить SMBv1',
                'help': 'Небезопасный протокол (WannaCry). Закрывает гигантскую брешь.',
                'default': False
            },
            {
                'id': 'net_teredo',
                'name': 'Отключить туннелирование Teredo',
                'help': 'Переход IPv6, вызывающий задержки.',
                'default': False
            },
            {
                'id': 'net_isatap',
                'name': 'Отключить ISATAP',
                'help': 'Еще один туннель IPv6-IPv4 с задержками пинга.',
                'default': False
            },
            {
                'id': 'net_netbios',
                'name': 'Отключить NetBIOS через TCP',
                'help': 'Не используйте, если вы делитесь принтерами в локальной сети.',
                'default': False
            },
            {
                'id': 'net_wpad',
                'name': 'Отключить авто-обнаружение WPAD',
                'help': 'Ускоряет DNS и блокирует вектор атаки.',
                'default': False
            },
            {
                'id': 'net_tcp_1323',
                'name': 'Включить временные метки RFC 1323',
                'help': 'Улучшает надежность при передаче больших объемов данных.',
                'default': False
            },
            {
                'id': 'net_max_conn',
                'name': 'Макс. соединений 10 (HTTP 1.0)',
                'help': 'Ускоряет одновременную загрузку веб-страниц.',
                'default': False
            },
            {
                'id': 'net_max_conn11',
                'name': 'Макс. соединений 10 (HTTP 1.1)',
                'help': 'Ускоряет веб-загрузку HTTP 1.1.',
                'default': False
            },
            {
                'id': 'net_dns_cloudflare',
                'name': 'Установить DNS Cloudflare (1.1.1.1)',
                'help': 'Настраивает самый быстрый DNS в мире от Cloudflare.',
                'default': False
            },
            {
                'id': 'net_dns_google',
                'name': 'Установить DNS Google (8.8.8.8)',
                'help': 'Настраивает DNS от Google, быстрый и надежный.',
                'default': False
            }
        ],
        'cat_gaming': [
            {
                'id': 'game_mode',
                'name': 'Включить игровой режим Windows',
                'help': 'Приоритизирует доступ игры к CPU/GPU.',
                'default': False
            },
            {
                'id': 'game_process_priority',
                'name': 'Авто-повышение приоритета (Booster)',
                'help': 'Форсирует "Высокий" приоритет в реальном времени для соревновательных шутеров.',
                'default': False
            },
            {
                'id': 'game_process_lasso',
                'name': 'Активный Game Booster',
                'help': 'Эмулирует Process Lasso. Повышает приоритет CPU при открытии игр.',
                'default': False
            },
            {
                'id': 'game_timer_res',
                'name': 'Разрешение таймера 0.5мс',
                'help': 'Настраивает BCDEDIT для высокоточного тикрейта Windows.',
                'default': False
            },
            {
                'id': 'game_mouse_accel',
                'name': 'Отключить акселерацию мыши',
                'help': 'Реальный ввод 1:1. Важно для соревновательных шутеров.',
                'default': False
            },
            {
                'id': 'game_ultimate_power',
                'name': 'Включить макс. производительность',
                'help': 'Разблокирует скрытый план электропитания Windows.',
                'default': False
            },
            {
                'id': 'game_msi_mode',
                'name': 'Hardware Latency Killer (MSI)',
                'help': 'Принуждает GPU/Сеть/USB использовать прерывания MSI.',
                'default': False
            },
            {
                'id': 'game_hags',
                'name': 'Включить план. GPU с аппаратным уск.',
                'help': 'Буст FPS в DX12. Требуется перезагрузка.',
                'default': False
            },
            {
                'id': 'game_mmcss',
                'name': 'Оптимизировать MMCSS',
                'help': 'Направляет NetworkThrottlingIndex и GPU на игру.',
                'default': False
            },
            {
                'id': 'game_fullscreen_opt',
                'name': 'Отключить оптимизацию во весь экран',
                'help': 'Избегает фальшивого полноэкранного режима с задержкой ввода.',
                'default': False
            },
            {
                'id': 'game_edge_bg',
                'name': 'Убить Edge в фоне',
                'help': 'Убивает процессы msedge.exe, которые пожирают 500 МБ ОЗУ.',
                'default': False
            },
            {
                'id': 'game_chrome_bg',
                'name': 'Убить Chrome в фоне',
                'help': 'Устраняет флаг для приложений Chrome в фоновом режиме.',
                'default': False
            },
            {
                'id': 'game_steam_hardware',
                'name': 'Отключить аппаратное уск. Steam',
                'help': 'Предотвращает потребление ресурсов GPU Steam-ом в фоне.',
                'default': False
            },
            {
                'id': 'game_discord_hw',
                'name': 'Отключить аппаратное уск. Discord',
                'help': 'Если GPU загружен на 99%, отключение поможет избежать лагов.',
                'default': False
            },
            {
                'id': 'game_vr',
                'name': 'Отклик системы (VR/Гейминг)',
                'help': 'Устанавливает SystemResponsiveness на 0. Больше циклов CPU для игры.',
                'default': False
            },
            {
                'id': 'game_fth',
                'name': 'Отключить Fault Tolerant Heap',
                'help': 'Предотвращает деградацию игры при вылетах.',
                'default': False
            },
            {
                'id': 'game_hpet',
                'name': 'Отключить HPET',
                'help': 'Снижает огромную задержку ввода на старых CPU или Ryzen gen1.',
                'default': False
            },
            {
                'id': 'game_xbox_dvr',
                'name': 'Удалить записи реестра Xbox DVR',
                'help': 'Удаляет скрытые записи. Повышает минимальный FPS в DX12.',
                'default': False
            },
            {
                'id': 'game_core_parking',
                'name': 'Отключить Core Parking',
                'help': 'Предотвращает отключение ядер процессора со стороны Windows.',
                'default': False
            },
            {
                'id': 'game_vbs',
                'name': 'Отключить VBS',
                'help': '10% задержек в играх. Только если ваша цель — 100% гейминг.',
                'default': False
            },
            {
                'id': 'perf_win32_priority',
                'name': 'Win32PrioritySeparation 26',
                'help': 'Оптимизирует приоритет CPU для активных окон (ИГРЫ).',
                'default': False
            },
            {
                'id': 'perf_large_cache',
                'name': 'Large System Cache',
                'help': 'Улучшает производительность файлов, используя больше ОЗУ.',
                'default': False
            },
            {
                'id': 'perf_io_limit',
                'name': 'Поднять лимит блокировки страниц ввода-вывода',
                'help': 'Ускоряет передачу тяжелых файлов.',
                'default': False
            },
            {
                'id': 'perf_wait_kill',
                'name': 'Быстро убивать службы (2с)',
                'help': 'Снижает время ожидания перед завершением служб.',
                'default': False
            },
            {
                'id': 'perf_auto_end',
                'name': 'Авто-завершение зависших приложений',
                'help': 'Принудительно завершает зависшие процессы при выключении.',
                'default': False
            },
            {
                'id': 'perf_menu_delay',
                'name': 'Задержка меню на ноль',
                'help': 'Меню появляются мгновенно.',
                'default': False
            },
            {
                'id': 'perf_startup_delay',
                'name': 'Удалить полную задержку запуска',
                'help': 'Запускает фоновые приложения без искусственного ожидания.',
                'default': False
            }
        ],
        'cat_power': [
            {
                'id': 'pwr_ultimate',
                'name': 'Форсировать макс. производительность',
                'help': 'Максимальный уровень мощности. Отключает любую экономию CPU.',
                'default': False
            },
            {
                'id': 'pwr_min_cpu',
                'name': 'Мин. нагрузка CPU 100%',
                'help': 'Предотвращает снижение частоты процессора.',
                'default': False
            },
            {
                'id': 'pwr_throttling',
                'name': 'Отключить Power Throttling',
                'help': 'Предотвращает ограничение Discord и фоновых приложений.',
                'default': False
            },
            {
                'id': 'pwr_cpu_boost',
                'name': 'Всегда включать CPU Turbo Boost',
                'help': 'Держит турбо-буст активным даже при работе от батареи.',
                'default': False
            },
            {
                'id': 'pwr_pci_link',
                'name': 'Отключить PCIe Link State Power Mgmt',
                'help': 'Предотвращает переход GPU в состояния низкого энергопотребления.',
                'default': False
            },
            {
                'id': 'pwr_hibernation',
                'name': 'Отключить гибернацию',
                'help': 'Освобождает гигабайты на C: и снижает износ SSD.',
                'default': False
            },
            {
                'id': 'pwr_disk_timeout',
                'name': 'Отключить тайм-аут HDD',
                'help': 'Предотвращает отключение HDD, вызывающее фризы.',
                'default': False
            },
            {
                'id': 'pwr_adaptive_brightness',
                'name': 'Отключить адаптивную яркость',
                'help': 'Предотвращает автоматическую регулировку яркости датчиком.',
                'default': False
            },
            {
                'id': 'pwr_usb_hub_suspend',
                'name': 'Отключить выборочную приостановку USB-концентратора',
                'help': 'Дополнение к Gaming USB Suspend. Более стабильно.',
                'default': False
            }
        ],
        'cat_gpu': [
            {
                'id': 'gpu_hags',
                'name': 'Включить HAGS (Апп. планирование)',
                'help': 'Переносит очередь кадров с CPU на GPU. Повышает FPS в DX12/Vulkan.',
                'default': False
            },
            {
                'id': 'gpu_mpo',
                'name': 'Отключить MPO',
                'help': 'MPO вызывает черные экраны и лаги. Nvidia рекомендует отключать.',
                'default': False
            },
            {
                'id': 'gpu_preemption',
                'name': 'Отключить приоритезацию GPU',
                'help': 'Предотвращает прерывания в середине кадра. Устраняет микро-фризы.',
                'default': False
            },
            {
                'id': 'gpu_reduce_dpc',
                'name': 'Снизить задержку DPC GPU',
                'help': 'Настраивает прерывания драйвера GPU для минимизации задержки DPC.',
                'default': False
            },
            {
                'id': 'gpu_dwm_priority',
                'name': 'Высокий приоритет DWM',
                'help': 'Повышает приоритет dwm.exe для более плавного рендеринга.',
                'default': False
            },
            {
                'id': 'gpu_gpu_priority',
                'name': 'Приоритет GPU 8 (MMCSS)',
                'help': 'Настраивает GpuPriority для повышения приоритета игрового процесса.',
                'default': False
            },
            {
                'id': 'gpu_perf_registry',
                'name': 'Оптимизировать реестр GPU MMCSS',
                'help': 'Настраивает NetworkThrottlingIndex и SystemResponsiveness для GPU.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_power',
                'name': 'NVIDIA: Макс. производительность',
                'help': 'Форсирует максимальную производительность в панели NVIDIA через реестр.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_telemetry',
                'name': 'Отключить телеметрию NVIDIA',
                'help': 'Останавливает задачи телеметрии NVIDIA в фоновом режиме.',
                'default': False
            },
            {
                'id': 'gpu_amd_power',
                'name': 'AMD: Без экономии энергии GPU',
                'help': 'Предотвращает переход GPU AMD в состояния низкой частоты.',
                'default': False
            },
            {
                'id': 'gpu_amd_telemetry',
                'name': 'Отключить телеметрию AMD',
                'help': 'Останавливает службы телеметрии AMD в фоновом режиме.',
                'default': False
            },
            {
                'id': 'gpu_pci_express_max',
                'name': 'Максимальный режим PCIe GPU',
                'help': 'Отключает Link State Power Management специально для GPU.',
                'default': False
            },
            {
                'id': 'gpu_disable_fullscreen_opt',
                'name': 'Отключить глоб.оптимизацию во весь экран',
                'help': 'Форсирует реальный эксклюзивный полноэкранный режим во всех играх.',
                'default': False
            },
            {
                'id': 'gpu_freesync_vsync_off',
                'name': 'Отключить глоб. V-Sync',
                'help': 'Отключает V-Sync по умолчанию во всех приложениях через реестр.',
                'default': False
            },
            {
                'id': 'gpu_cache_clean',
                'name': 'Очистить кеш шейдеров GPU',
                'help': 'Удаляет накопленный кеш шейдеров. Полезно, если лагает при входе в локации.',
                'default': False
            },
            {
                'id': 'gpu_vram_paging',
                'name': 'Оптимизировать пагинацию VRAM',
                'help': 'Использует системную ОЗУ как расширение для GPU с малым объемом VRAM.',
                'default': False
            },
            {
                'id': 'gpu_shader_cache',
                'name': 'Перенаправить кеш шейдеров на быстрый SSD',
                'help': 'Настраивает кеш шейдеров для быстрого чтения на NVMe.',
                'default': False
            },
            {
                'id': 'gpu_disable_mpv',
                'name': 'Отключить фоновую прекомпиляцию DX12/Vulkan',
                'help': 'Предотвращает прекомпиляцию шейдеров во время игры.',
                'default': False
            },
            {
                'id': 'gpu_gsync_compat',
                'name': 'G-Sync на мониторах FreeSync',
                'help': 'Принудительно включает совместимость G-Sync на мониторах AMD с GPU Nvidia.',
                'default': False
            },
            {
                'id': 'gpu_night_light_off',
                'name': 'Отключить ночной свет',
                'help': 'Предотвращает изменение калибровки цвета монитора со стороны Windows.',
                'default': False
            }
        ],
        'cat_kernel': [
            {
                'id': 'ext_57_processes',
                'name': 'Консолидация системных служб (минимум процессов)',
                'help': 'Перенаправляет svchost и отключает некритичные службы для снижения общего числа активных процессов до рабочего минимума.',
                'default': False
            },
            {
                'id': 'kern_registry_size',
                'name': 'Увеличить макс. размер реестра',
                'help': 'Предотвращает ошибки лимита реестра на кастомных системах.',
                'default': False
            },
            {
                'id': 'kern_bcdedit_inc',
                'name': 'Частота прерываний BCDEDIT',
                'help': 'Повышает точность часов через BCDEDIT. Ключ для таймера < 1мс.',
                'default': False
            },
            {
                'id': 'kern_memory_comp',
                'name': 'Отключить сжатие памяти (MMAgent)',
                'help': 'Предотвращает потерю циклов CPU на сжатие страниц ОЗУ, приоритизируя задержку.',
                'default': False
            },
            {
                'id': 'kern_system_resp',
                'name': 'SystemResponsiveness на 0% (Real Time)',
                'help': 'Удаляет фоновый резерв ресурсов Windows, посвящая 100% сфокусированному процессу.',
                'default': False
            },
            {
                'id': 'kernel_mitigations',
                'name': 'Отключить защиты CPU',
                'help': 'Отключает Spectre/Meltdown. +5-15% чистой мощи CPU. Снижает безопасность.',
                'default': False
            },
            {
                'id': 'kern_large_pages',
                'name': 'Включить Large Pages (Вирт. память)',
                'help': 'Снижает ошибки страниц (TLB misses) в приложениях с высокой нагрузкой на память.',
                'default': False
            },
            {
                'id': 'kern_iot_core',
                'name': 'Конфиг минималистичного профиля Embedded',
                'help': 'Настраивает внутренние параметры системы так, чтобы она вела себя как профиль Windows IoT с низким потреблением ресурсов.',
                'default': False
            },
            {
                'id': 'kern_process_isolation',
                'name': 'Отключить изоляцию процессов ядра',
                'help': 'Снижает нагрузку виртуализации ядра для максимизации скорости потоков.',
                'default': False
            }
        ],
        'cat_extreme': [
            {
                'id': 'ext_super_nuclear',
                'name': 'Масштабная чистка системных служб',
                'help': 'Отключает все второстепенные сетевые, печатные и визуальные службы. Необратимо без восстановления.',
                'default': False
            },
            {
                'id': 'ext_minimalist',
                'name': 'Профиль Shell со сниженной нагрузкой',
                'help': 'Отключает визуальные эффекты Windows Shell для полного освобождения циклов CPU и GPU.',
                'default': False
            },
            {
                'id': 'ext_defender_kill',
                'name': 'Перманентное отключение Windows Defender',
                'help': 'Удаляет движок сканирования и нативные службы безопасности через реестр/GPO.',
                'default': False
            },
            {
                'id': 'ext_uwp_kill_all',
                'name': 'Полное удаление встроенных UWP-приложений',
                'help': 'Удаляет все предустановленные UWP-приложения для всех пользователей системы.',
                'default': False
            },
            {
                'id': 'ext_firewall_off',
                'name': 'Отключить брандмауэр Windows (Stack Bypass)',
                'help': 'Отключает нативную фильтрацию пакетов для минимизации сетевой задержки.',
                'default': False
            },
            {
                'id': 'ext_update_dead',
                'name': 'Блокировка обновлений Windows (LTSC Policy)',
                'help': 'Предотвращает любую попытку обновления или загрузки драйверов со стороны ОС.',
                'default': False
            }
        ],
        'cat_util': [
            {
                'id': 'util_dotnet',
                'name': 'Установить рантаймы .NET',
                'help': 'Обеспечивает совместимость со всеми версиями фреймворков приложений.',
                'default': False
            },
            {
                'id': 'util_vc_redist',
                'name': 'Установить C++ Redistributables',
                'help': 'Устанавливает все библиотеки, необходимые для запуска игр и программ.',
                'default': False
            },
            {
                'id': 'util_directx',
                'name': 'Обновить рантаймы DirectX',
                'help': 'Устанавливает устаревшие компоненты DirectX для старых игр.',
                'default': False
            },
            {
                'id': 'util_powershell_7',
                'name': 'Установить PowerShell 7',
                'help': 'Устанавливает современную и более быструю версию движка скриптов Windows.',
                'default': False
            },
            {
                'id': 'util_driver_updates',
                'name': 'Исключить обновления драйверов',
                'help': 'Предотвращает перезапись ваших кастомных драйверов базовыми версиями от Windows.',
                'default': False
            },
            {
                'id': 'util_ps_telemetry',
                'name': 'Отключить телеметрию PowerShell',
                'help': 'Удаляет отчеты об использовании в современном терминале Windows.',
                'default': False
            },
            {
                'id': 'util_end_task_rc',
                'name': 'Завершение задачи на панели задач',
                'help': 'Добавляет опцию закрытия процессов прямо правым кликом по панели задач.',
                'default': False
            },
            {
                'id': 'util_start_recommendations',
                'name': 'Удалить рекомендации в Пуск',
                'help': 'Очищает секцию недавних файлов и предложенных приложений в Пуск.',
                'default': False
            },
            {
                'id': 'util_sticky_keys',
                'name': 'Отключить залипание клавиш',
                'help': 'Предотвращает вопросы системы о залипании клавиш после частого нажатия Shift.',
                'default': False
            },
            {
                'id': 'util_taskbar_center',
                'name': 'Панель задач: выравнивание слева',
                'help': 'Восстанавливает классическое положение иконок на рабочем столе Windows 11.',
                'default': False
            },
            {
                'id': 'util_settings_home',
                'name': 'Удалить главную страницу параметров',
                'help': 'Удаляет бесполезный экран "Главная" при открытии настроек Windows.',
                'default': False
            },
            {
                'id': 'util_new_outlook',
                'name': 'Блокировать новый Outlook',
                'help': 'Предотвращает замену классического почтового клиента на веб-версию со стороны Windows.',
                'default': False
            },
            {
                'id': 'util_cross_device',
                'name': 'Отключить кросс-девайс функции',
                'help': 'Отключает синхронизацию незавершенных задач с другими ПК или мобильными.',
                'default': False
            },
            {
                'id': 'util_task_view',
                'name': 'Скрыть представление задач',
                'help': 'Очищает панель задач, удаляя иконку виртуальных рабочих столов.',
                'default': False
            },
            {
                'id': 'util_folder_discovery',
                'name': 'Выключить авто-определение папок',
                'help': 'Предотвращает смену вида Проводника при открытии папок с фото или музыкой.',
                'default': False
            },
            {
                'id': 'util_bsod_detail',
                'name': 'BSOD с детальной инфо',
                'help': 'Показывает полные параметры и коды ошибок на синем экране смерти.',
                'default': False
            },
            {
                'id': 'util_numlock',
                'name': 'Включить NumLock при запуске',
                'help': 'Автоматически активирует NumLock при входе в Windows.',
                'default': False
            },
            {
                'id': 'util_verbose_logon',
                'name': 'Детальные сообщения входа',
                'help': 'Показывает статус каждой службы во время входа и выхода.',
                'default': False
            },
            {
                'id': 'util_consumer_features',
                'name': 'Отключить предложения Store',
                'help': 'Предотвращает тихую установку рекламных приложений от Microsoft.',
                'default': False
            },
            {
                'id': 'util_wpbt',
                'name': 'Блокировать инъекцию Bloatware (WPBT)',
                'help': 'Предотвращает установку софта производителями через BIOS при запуске Windows.',
                'default': False
            },
            {
                'id': 'util_widgets_remove',
                'name': 'Удалить виджеты Windows 11',
                'help': 'Деинсталлирует панель виджетов и новостей из панели задач.',
                'default': False
            },
            {
                'id': 'uwp_xbox',
                'name': 'Удалить Xbox-приложения',
                'help': 'Удаляет все приложения Xbox (GameBar, TCUI). НЕ ИСПОЛЬЗУЙТЕ, ЕСЛИ ИГРАЕТЕ ЧЕРЕЗ PC GAME PASS.',
                'default': False
            },
            {
                'id': 'uwp_bloatware',
                'name': 'Удалить нативный мусор (Bloatware)',
                'help': 'Удаляет мусорные приложения: Zune, BingNews, GetHelp, Solitaire, People...',
                'default': False
            },
            {
                'id': 'uwp_onedrive',
                'name': 'Деинсталлировать OneDrive',
                'help': 'Глубоко удаляет Microsoft OneDrive из системы.',
                'default': False
            },
            {
                'id': 'uwp_edge',
                'name': 'Удалить Edge (продвинуто)',
                'help': 'Пытается удалить Microsoft Edge через PowerShell. Имейте запасной браузер.',
                'default': False
            },
            {
                'id': 'uwp_3dbuilder',
                'name': 'Удалить 3D Builder',
                'help': 'Удаляет приложение Microsoft для 3D-моделирования.',
                'default': False
            },
            {
                'id': 'uwp_alarms',
                'name': 'Удалить Будильники и часы',
                'help': 'Удаляет приложение будильника и секундомера.',
                'default': False
            },
            {
                'id': 'uwp_camera',
                'name': 'Удалить Камеру',
                'help': 'Удаляет приложение камеры из Store.',
                'default': False
            },
            {
                'id': 'uwp_communications',
                'name': 'Удалить Почту и Календарь',
                'help': 'Удаляет встроенные приложения почты и календаря.',
                'default': False
            },
            {
                'id': 'uwp_feedback',
                'name': 'Удалить Центр отзывов',
                'help': 'Удаляет приложение Microsoft для фидбека.',
                'default': False
            },
            {
                'id': 'uwp_gethelp',
                'name': 'Удалить Help',
                'help': 'Удаляет приложение техподдержки Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_maps',
                'name': 'Удалить Карты',
                'help': 'Удаляет встроенное приложение карт.',
                'default': False
            },
            {
                'id': 'uwp_mixedreality',
                'name': 'Удалить Портал смешанной реальности',
                'help': 'Удаляет портал смешанной реальности.',
                'default': False
            },
            {
                'id': 'uwp_people',
                'name': 'Удалить Люди (People)',
                'help': 'Удаляет встроенное приложение контактов.',
                'default': False
            },
            {
                'id': 'uwp_photos',
                'name': 'Удалить Фотографии',
                'help': 'Удаляет современное приложение Фото (заменяется классическим просмотрщиком).',
                'default': False
            },
            {
                'id': 'uwp_skype',
                'name': 'Удалить Skype',
                'help': 'Удаляет предустановленное приложение Skype.',
                'default': False
            },
            {
                'id': 'uwp_solitaire',
                'name': 'Удалить Солитер',
                'help': 'Удаляет предустановленные игры пасьянса.',
                'default': False
            },
            {
                'id': 'uwp_soundrecorder',
                'name': 'Удалить Запись голоса',
                'help': 'Удаляет приложение для записи аудио.',
                'default': False
            },
            {
                'id': 'uwp_stickynotes',
                'name': 'Удалить Sticky Notes',
                'help': 'Удаляет приложение липких заметок.',
                'default': False
            },
            {
                'id': 'uwp_weather',
                'name': 'Удалить Погоду',
                'help': 'Удаляет приложение погоды.',
                'default': False
            },
            {
                'id': 'uwp_yourphone',
                'name': 'Удалить Ваш телефон',
                'help': 'Удаляет приложение для связи со смартфоном.',
                'default': False
            }
        ],
        'cat_pro': [
            {
                'id': 'util_context_compact',
                'name': 'Включить компактные меню',
                'help': 'Уменьшает отступы и расстояние между опциями меню правого клика.',
                'default': False
            },
            {
                'id': 'util_legacy_photo',
                'name': 'Вернуть классический просмотрщик фото (Win7)',
                'help': 'Включает ультра-быстрый и легкий просмотрщик картинок из предыдущих версий.',
                'default': False
            },
            {
                'id': 'util_legacy_calc',
                'name': 'Вернуть классический калькулятор Win32',
                'help': 'Заменяет медленную UWP-версию традиционным исполняемым файлом.',
                'default': False
            },
            {
                'id': 'util_god_mode',
                'name': 'Единый доступ к Панели управления',
                'help': 'Создает ярлык ко всем административным настройкам системы в одном окне.',
                'default': False
            },
            {
                'id': 'util_verbose_boot',
                'name': 'Включить детальный отчет загрузки',
                'help': 'Отображает загружаемые драйверы и службы во время бута на экране.',
                'default': False
            },
            {
                'id': 'util_desktop_labels',
                'name': 'Удалить стрелки ярлыков',
                'help': 'Очищает иконки рабочего стола, удаляя стрелку быстрого доступа.',
                'default': False
            },
            {
                'id': 'util_explorer_pc',
                'name': "Открыть проводник на 'Этот ПК'",
                'help': 'Настраивает проводник так, чтобы он пропускал вид недавних файлов по умолчанию.',
                'default': False
            }
        ],
        'cat_help': []
    }
