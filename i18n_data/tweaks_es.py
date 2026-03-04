# type: ignore
def get_tweaks_es():
    return {       'cat_system': [       {       'id': 'svc_diagtrack',
                                                              'name': 'Bloqueo de Telemetría (DiagTrack)',
                                                              'help': 'Desactiva el servicio de rastreo de diagnóstico '
                                                                      'para liberar hilos del kernel.',
                                                              'default': False},
                                                      {       'id': 'svc_sysmain',
                                                              'name': 'Inhabilitar SysMain (Superfetch)',
                                                              'help': 'Evita la precarga constante en RAM, mejorando '
                                                                      'la latencia en unidades SSD.',
                                                              'default': False},
                                                      {       'id': 'svc_wsearch',
                                                              'name': 'Inhabilitar Windows Search Indexer',
                                                              'help': 'Detiene la indexación de archivos en segundo '
                                                                      'plano para reducir el I/O del disco.',
                                                              'default': False},
                                                      {       'id': 'svc_wuauserv_manual',
                                                              'name': 'Windows Update: Modo Manual/Demanda',
                                                              'help': 'Impide que las descargas automáticas '
                                                                      'interrumpan sesiones de baja latencia.',
                                                              'default': False},
                                                      {       'id': 'ai_copilot',
                                                              'name': 'Bloqueo de GPO para Windows Copilot',
                                                              'help': 'Desactiva la integración de IA en la barra de '
                                                                      'tareas y búsqueda.',
                                                              'default': False},
                                                      {       'id': 'ai_recall',
                                                              'name': 'Inhabilitar Windows Recall (Snapshot IA)',
                                                              'help': 'Evita la captura constante de pantalla y '
                                                                      'actividad por el motor de IA.',
                                                              'default': False},
                                                      {       'id': 'svc_bcastdvr',
                                                              'name': 'Inhabilitar Game DVR (Captura de Fondo)',
                                                              'help': 'Elimina la grabación invisible que consume '
                                                                      'recursos de la GPU.',
                                                              'default': False},
                                                      {       'id': 'svc_wer',
                                                              'name': 'Inhabilitar Windows Error Reporting',
                                                              'help': 'Evita el envío de volcados de memoria tras '
                                                                      'fallos de aplicaciones.',
                                                              'default': False},
                                                      {       'id': 'svc_dps',
                                                              'name': 'Inhabilitar Diagnostic Policy Service',
                                                              'help': 'Detiene la ejecución de políticas de '
                                                                      'diagnóstico automático.',
                                                              'default': False},
                                                      {       'id': 'svc_pcasvc',
                                                              'name': 'Inhabilitar Program Compatibility Assistant',
                                                              'help': 'Elimina micro-pausas causadas por el monitor de '
                                                                      'compatibilidad.',
                                                              'default': False},
                                                      {       'id': 'svc_remoteregistry',
                                                              'name': 'Inhabilitar Acceso a Registro Remoto',
                                                              'help': 'Cierra un vector de seguridad y ahorra memoria '
                                                                      'en servicios de red.',
                                                              'default': False},
                                                      {       'id': 'svc_tabletinputservice',
                                                              'name': 'Inhabilitar Panel de Escritura / Táctil',
                                                              'help': 'Libera recursos dedicados a digitalizadores y '
                                                                      'teclados virtuales.',
                                                              'default': False},
                                                      {       'id': 'svc_wbio_srvc',
                                                              'name': 'Inhabilitar Subsistema de Biometría',
                                                              'help': 'Desactiva el soporte para huella digital y '
                                                                      'reconocimiento facial.',
                                                              'default': False},
                                                      {       'id': 'svc_bits',
                                                              'name': 'Inhabilitar Background Intelligent Transfer',
                                                              'help': 'Detiene descargas silenciosas de la Store y '
                                                                      'actualizaciones.',
                                                              'default': False},
                                                      {       'id': 'svc_defrag_svc',
                                                              'name': 'Optimizar Programador de Desfragmentación',
                                                              'help': 'Desactiva el mantenimiento automático para '
                                                                      'control manual de TRIM/SSD.',
                                                              'default': False}],
        'cat_clean': [       {       'id': 'clean_ram',
                                                 'name': 'Liberación de Working Sets (Memoria)',
                                                 'help': 'Fuerza la limpieza del conjunto de trabajo del sistema y '
                                                         'standby list.',
                                                 'default': False},
                                         {       'id': 'clean_temp',
                                                 'name': 'Depuración de Archivos Temporales (%TEMP%)',
                                                 'help': 'Elimina caché residual de aplicaciones de usuario.',
                                                 'default': False},
                                         {       'id': 'clean_prefetch',
                                                 'name': 'Purga de Prefetch (Runtime Cache)',
                                                 'help': 'Elimina datos de precarga para regenerar caché limpio.',
                                                 'default': False},
                                         {       'id': 'clean_winupdate',
                                                 'name': 'Limpieza de Repositorio Windows Update',
                                                 'help': 'Borra el catálogo de actualizaciones distribuidas y '
                                                         'residuales.',
                                                 'default': False},
                                         {       'id': 'clean_recycle',
                                                 'name': 'Vaciado Forzado de Papelera',
                                                 'help': 'Ejecuta un vaciado completo en todas las unidades logicas.',
                                                 'default': False},
                                         {       'id': 'clean_dns',
                                                 'name': 'Flush de Resolución DNS',
                                                 'help': 'Reinicia el caché de resolución de nombres de red.',
                                                 'default': False},
                                         {       'id': 'clean_eventlog',
                                                 'name': 'Purga de Registros de Eventos (EventView)',
                                                 'help': 'Elimina el historial de auditoría y errores del sistema.',
                                                 'default': False},
                                         {       'id': 'clean_thumbcache',
                                                 'name': 'Reiniciar Caché de Miniaturas',
                                                 'help': 'Reconstruye la base de datos de iconos de archivos '
                                                         'multimedia.',
                                                 'default': False},
                                         {       'id': 'clean_fontcache',
                                                 'name': 'Reiniciar Caché de Fuentes',
                                                 'help': 'Soluciona anomalías en el renderizado de tipografías.',
                                                 'default': False},
                                         {       'id': 'clean_iconcache',
                                                 'name': 'Reiniciar Explorador de Iconos',
                                                 'help': 'Elimina el caché de iconos del Shell de Windows.',
                                                 'default': False},
                                         {       'id': 'clean_crashdumps',
                                                 'name': 'Remover Volcados de Memoria (Minidumps)',
                                                 'help': 'Elimina archivos de diagnóstico de errores críticos.',
                                                 'default': False},
                                         {       'id': 'clean_chkdsk',
                                                 'name': 'Remover Fragmentos Recuperados (CHK)',
                                                 'help': 'Elimina archivos huerfanos detectados por CheckDisk.',
                                                 'default': False},
                                         {       'id': 'clean_onedrive_temp',
                                                 'name': 'Depuración de Caché de OneDrive',
                                                 'help': 'Elimina logs y metadatos de sincronización.',
                                                 'default': False},
                                         {       'id': 'clean_chrome_cache',
                                                 'name': 'Depuración de Caché Google Chrome',
                                                 'help': 'Limpia el almacenamiento temporal del motor Chromium.',
                                                 'default': False},
                                         {       'id': 'clean_edge_cache',
                                                 'name': 'Depuración de Caché Microsoft Edge',
                                                 'help': 'Limpia el almacenamiento temporal de Edge WebView.',
                                                 'default': False},
                                         {       'id': 'clean_firefox_cache',
                                                 'name': 'Depuración de Caché Mozilla Firefox',
                                                 'help': 'Limpia el motor Gecko de datos temporales.',
                                                 'default': False},
                                         {       'id': 'clean_discord_cache',
                                                 'name': 'Depuración de Caché Discord (Electrón)',
                                                 'help': 'Elimina archivos de medios y assets temporales de Discord.',
                                                 'default': False},
                                         {       'id': 'clean_steam_cache',
                                                 'name': 'Depuración de Caché Steam Browser',
                                                 'help': 'Limpia el caché del WebHelper de Steam.',
                                                 'default': False},
                                         {       'id': 'clean_epic_cache',
                                                 'name': 'Depuración de Caché Epic Games Engine',
                                                 'help': 'Limpia datos temporales del launcher de Epic.',
                                                 'default': False},
                                         {       'id': 'clean_spotify_cache',
                                                 'name': 'Depuración de Caché Spotify Streaming',
                                                 'help': 'Elimina fragmentos de audio e imágenes cacheadas.',
                                                 'default': False},
                                         {       'id': 'clean_vcredist',
                                                 'name': 'Eliminar Instaladores Redist (Steam)',
                                                 'help': 'Remueve paquetes de instalación de VCRedist y DirectX '
                                                         'huérfanos.',
                                                 'default': False},
                                         {       'id': 'clean_usrdoc_temp',
                                                 'name': 'Limpieza de Directorios de Perfil',
                                                 'help': 'Borra temporales en carpetas de documentos de usuario.',
                                                 'default': False},
                                         {       'id': 'clean_system_logs',
                                                 'name': 'Purga de Logs de Sistema (WinDir)',
                                                 'help': 'Elimina registros de instalación en el directorio raíz.',
                                                 'default': False},
                                         {       'id': 'clean_crypt_svc',
                                                 'name': 'Reset de Base de Datos Criptografica',
                                                 'help': 'Reinicia el catalogo de firmas de servicios de cifrado.',
                                                 'default': False},
                                         {       'id': 'clean_bits_queue',
                                                 'name': 'Reset de Cola de Transferencia (BITS)',
                                                 'help': 'Limpia la cola de trabajos en segundo plano.',
                                                 'default': False}],
        'cat_privacy': [       {       'id': 'priv_telemetry_level',
                                                            'name': 'Nivel de Telemetría: Seguridad (Nivel 0)',
                                                            'help': 'Bloquea toda transmisión de datos de diagnóstico '
                                                                    'no vital al mínimo legal.',
                                                            'default': False},
                                                    {       'id': 'priv_etw_disable',
                                                            'name': 'Bloqueo Profundo de Trazado de Eventos (ETW)',
                                                            'help': 'Desactiva sesiones AutoLogger a nivel de Kernel '
                                                                    'para evitar I/O constante.',
                                                            'default': False},
                                                    {       'id': 'priv_cortana',
                                                            'name': 'Remover Asistente Cortana (Procesos en BG)',
                                                            'help': 'Elimina el motor de búsqueda por voz y sus '
                                                                    'servicios asociados.',
                                                            'default': False},
                                                    {       'id': 'priv_start_web',
                                                            'name': 'Búsqueda de Inicio: Solo Resultados Locales',
                                                            'help': 'Desactiva la integración de Bing en el Menú '
                                                                    'Inicio para mejorar la latencia.',
                                                            'default': False},
                                                    {       'id': 'priv_news',
                                                            'name': 'Inhabilitar Shell News & Interests (Widgets)',
                                                            'help': 'Elimina el feed de noticias y clima de la barra '
                                                                    'de tareas.',
                                                            'default': False},
                                                    {       'id': 'priv_location',
                                                            'name': 'Restricción de Servicios de Geolocalización',
                                                            'help': 'Impide que el sistema y aplicaciones accedan a la '
                                                                    'ubicación física.',
                                                            'default': False},
                                                    {       'id': 'priv_mic',
                                                            'name': 'Inhabilitar Telemetría de Entrada (Escritura)',
                                                            'help': 'Desactiva la recolección de patrones de escritura '
                                                                    'enviados a la nube.',
                                                            'default': False},
                                                    {       'id': 'priv_feedback',
                                                            'name': 'Frecuencia de Feedback del Sistema: Nunca',
                                                            'help': 'Configura la política de solicitudes de opinión '
                                                                    'de Microsoft a deshabilitado.',
                                                            'default': False},
                                                    {       'id': 'priv_activity',
                                                            'name': 'Depurar Historial de Actividad (Timeline)',
                                                            'help': 'Evita que Windows registre el uso de archivos y '
                                                                    'aplicaciones localmente.',
                                                            'default': False},
                                                    {       'id': 'priv_sync',
                                                            'name': 'Suspender Sincronización con Entorno Cloud',
                                                            'help': 'Evita la subida de preferencias y configuraciones '
                                                                    'a la cuenta Microsoft.',
                                                            'default': False},
                                                    {       'id': 'priv_advertising',
                                                            'name': 'Inhabilitar ID de Publicidad Personalizada',
                                                            'help': 'Evita la creación de un perfil de consumidor '
                                                                    'basado en el uso de apps.',
                                                            'default': False},
                                                    {       'id': 'priv_appdiag',
                                                            'name': 'Restricción de Diagnóstico de Aplicaciones',
                                                            'help': 'Impide que aplicaciones de terceros lean '
                                                                    'metadatos de diagnóstico de otras apps.',
                                                            'default': False},
                                                    {       'id': 'priv_tailored',
                                                            'name': 'Inhabilitar Experiencias Basadas en Datos',
                                                            'help': 'Evita que Microsoft use diagnósticos para ofrecer '
                                                                    'contenido personalizado.',
                                                            'default': False},
                                                    {       'id': 'priv_ceip',
                                                            'name': 'Opt-out del Programa de Mejora del Consumidor',
                                                            'help': 'Cancela la participación en el programa de '
                                                                    'recolección de datos CEIP.',
                                                            'default': False},
                                                    {       'id': 'priv_handwriting',
                                                            'name': 'Inhabilitar Aprendizaje de Tinta y Escritura',
                                                            'help': 'Evita que el sistema aprenda de la escritura '
                                                                    'manual para telemetría.',
                                                            'default': False},
                                                    {       'id': 'priv_defender_samples',
                                                            'name': 'Restricción de Envío de Muestras a Defender',
                                                            'help': 'Evita que archivos sospechosos se envíen '
                                                                    'automáticamente a servidores MS.',
                                                            'default': False},
                                                    {       'id': 'priv_onedrive',
                                                            'name': 'Impedir Ejecución Automática de OneDrive',
                                                            'help': 'Desactiva el inicio de sesión automático de '
                                                                    'OneDrive tras el arranque.',
                                                            'default': False},
                                                    {       'id': 'priv_meetnow',
                                                            'name': "Remover Interfaz de 'Meet Now' (Skype)",
                                                            'help': 'Elimina el acceso directo de reuniones de la '
                                                                    'bandeja del sistema.',
                                                            'default': False},
                                                    {       'id': 'priv_app_suggestions',
                                                            'name': 'Remover Sugerencias de Aplicaciones en Shell',
                                                            'help': 'Elimina la publicidad de apps recomendadas en el '
                                                                    'Menú Inicio.',
                                                            'default': False},
                                                    {       'id': 'priv_smartscreen',
                                                            'name': 'Inhabilitar Filtro SmartScreen (Análisis I/O)',
                                                            'help': 'Desactiva el escaneo en tiempo real de archivos '
                                                                    'descargados. USA CON CUIDADO.',
                                                            'default': False}],
        'cat_ui': [       {       'id': 'ui_animation',
                                                                    'name': 'Optimizar Latencia de Ventanas (No Anim)',
                                                                    'help': 'Elimina los tiempos de transición al '
                                                                            'abrir/cerrar ventanas.',
                                                                    'default': False},
                                                            {       'id': 'ui_transparency',
                                                                    'name': 'Deshabilitar Efectos de Transparencia',
                                                                    'help': 'Remueve efectos Mica/Acrílico para '
                                                                            'reducir carga en la GPU.',
                                                                    'default': False},
                                                            {       'id': 'ui_shadows',
                                                                    'name': 'Remover Renderizado de Sombras (UI)',
                                                                    'help': 'Elimina sombras en ventanas y cursor para '
                                                                            'una UI más limpia.',
                                                                    'default': False},
                                                            {       'id': 'ui_show_ext',
                                                                    'name': 'Habilitar Visualización de Extensiones',
                                                                    'help': 'Obliga a mostrar extensiones de archivo '
                                                                            '(.exe, .pkg) por seguridad.',
                                                                    'default': False},
                                                            {       'id': 'ui_show_hidden',
                                                                    'name': 'Habilitar Archivos y Carpetas Ocultas',
                                                                    'help': 'Muestra directorios de sistema como '
                                                                            'AppData y ProgramData.',
                                                                    'default': False},
                                                            {       'id': 'ui_classic_menu',
                                                                    'name': 'Restaurar Menú Contextual Clásico',
                                                                    'help': 'Habilita el menú de click derecho '
                                                                            'completo en Windows 11.',
                                                                    'default': False},
                                                            {       'id': 'ui_darkmode',
                                                                    'name': 'Forzar Modo Oscuro Global (System wide)',
                                                                    'help': 'Aplica el perfil de color oscuro a todas '
                                                                            'las aplicaciones compatibles.',
                                                                    'default': False},
                                                            {       'id': 'ui_startup_delay',
                                                                    'name': 'Remover Retraso de Inicio Artificial',
                                                                    'help': 'Elimina el delay impuesto por Windows '
                                                                            'antes de cargar apps de inicio.',
                                                                    'default': False},
                                                            {       'id': 'ui_taskbar_search',
                                                                    'name': 'Depurar Interfaz de Búsqueda (Barra)',
                                                                    'help': 'Reduce o elimina el cuadro de búsqueda de '
                                                                            'la barra de tareas.',
                                                                    'default': False},
                                                            {       'id': 'ui_edge_tabs',
                                                                    'name': 'Excluir Pestañas de Edge en Alt+Tab',
                                                                    'help': 'Limpia el selector de tareas (Alt+Tab) de '
                                                                            'pestañas individuales de Edge.',
                                                                    'default': False},
                                                            {       'id': 'ui_lockscreen',
                                                                    'name': 'Omitir Pantalla de Bloqueo (Lockscreen)',
                                                                    'help': 'Accede directamente al prompt de '
                                                                            'contraseña sin transición de imagen.',
                                                                    'default': False},
                                                            {       'id': 'ui_blur_lock',
                                                                    'name': 'Quitar Desenfoque en Inicio de Sesión',
                                                                    'help': 'Elimina el efecto blur en el fondo de la '
                                                                            'pantalla de login.',
                                                                    'default': False},
                                                            {       'id': 'ui_actioncenter',
                                                                    'name': 'Inhabilitar Centro de Notificaciones',
                                                                    'help': 'Elimina el panel lateral de alertas para '
                                                                            'evitar interrupciones.',
                                                                    'default': False},
                                                            {       'id': 'ui_snap',
                                                                    'name': 'Inhabilitar Asistente de Snap Layouts',
                                                                    'help': 'Evita sugerencias de posicionamiento al '
                                                                            'arrastrar ventanas.',
                                                                    'default': False},
                                                            {       'id': 'ui_shake',
                                                                    'name': "Inhabilitar 'Aero Shake' (Minimizar)",
                                                                    'help': 'Evita minimizar ventanas al agitar la '
                                                                            'ventana activa.',
                                                                    'default': False},
                                                            {       'id': 'ui_balloon',
                                                                    'name': "Supresión de Notificaciones 'Balloon'",
                                                                    'help': 'Desactiva los avisos informativos '
                                                                            'antiguos del sistema.',
                                                                    'default': False},
                                                            {       'id': 'ui_taskbar_animations',
                                                                    'name': 'Inhabilitar Animaciones de Barra de '
                                                                            'Tareas',
                                                                    'help': 'Movimiento instantáneo de iconos tras la '
                                                                            'interacción.',
                                                                    'default': False},
                                                            {       'id': 'ui_cursor_shadow',
                                                                    'name': 'Remover Sombra del Puntero',
                                                                    'help': 'Elimina el efecto de profundidad bajo el '
                                                                            'cursor del mouse.',
                                                                    'default': False}],
        'cat_net': [       {       'id': 'net_extreme_tcp',
                                                             'name': 'TCP Extreme Optimizer (BBR/CUBIC)',
                                                             'help': 'Implementa algoritmos de control de congestión '
                                                                     'modernos para reducir la latencia.',
                                                             'default': False},
                                                     {       'id': 'net_autotuning',
                                                             'name': 'TCP Window Auto-Tuning: Normal',
                                                             'help': 'Optimiza el escalado de la ventana de recepción '
                                                                     'para conexiones de alta velocidad.',
                                                             'default': False},
                                                     {       'id': 'net_nagles',
                                                             'name': 'Inhabilitar Algoritmo de Nagle (No-Delay)',
                                                             'help': 'Reduce el overhead de empaquetado para mejorar '
                                                                     'el tiempo de respuesta en juegos.',
                                                             'default': False},
                                                     {       'id': 'net_rss',
                                                             'name': 'Habilitar Receive-Side Scaling (RSS)',
                                                             'help': 'Distribuye la carga de procesamiento de red de '
                                                                     'forma balanceada entre los núcleos del CPU.',
                                                             'default': False},
                                                     {       'id': 'net_qos',
                                                             'name': 'Remover Reserva de Ancho de Banda (QoS)',
                                                             'help': 'Libera el 20% del tráfico que Windows reserva '
                                                                     'para el sistema por defecto.',
                                                             'default': False},
                                                     {       'id': 'net_deliveryopt',
                                                             'name': 'Inhabilitar Optimización de Entrega (P2P)',
                                                             'help': 'Evita que Windows use tu ancho de banda para '
                                                                     'distribuir actualizaciones a otros.',
                                                             'default': False},
                                                     {       'id': 'net_wifi_power',
                                                             'name': 'Inhabilitar Ahorro de Energía en Adaptadores '
                                                                     'WiFi',
                                                             'help': 'Evita micro-desconexiones y picos de lag por '
                                                                     'estados de bajo consumo en red inalámbrica.',
                                                             'default': False},
                                                     {       'id': 'net_ecn',
                                                             'name': 'Inhabilitar Explicit Congestion Notification '
                                                                     '(ECN)',
                                                             'help': 'Evita el descarte preventivo de paquetes en '
                                                                     'routers que no lo soportan bien.',
                                                             'default': False},
                                                     {       'id': 'net_heuristics',
                                                             'name': 'Inhabilitar TCP Window Heuristics',
                                                             'help': 'Impide que Windows limite dinámicamente el stack '
                                                                     'TCP basándose en heurísticas.',
                                                             'default': False},
                                                     {       'id': 'net_lso',
                                                             'name': 'Inhabilitar Large Send Offload (LSO)',
                                                             'help': 'Evita ráfagas de paquetes que pueden saturar el '
                                                                     'buffer de la tarjeta de red.',
                                                             'default': False},
                                                     {       'id': 'net_chimney',
                                                             'name': 'Inhabilitar TCP Chimney Offload',
                                                             'help': 'Evita la transferencia de carga TCP al hardware '
                                                                     'si causa inestabilidad de ping.',
                                                             'default': False},
                                                     {       'id': 'net_ipv6',
                                                             'name': 'Inhabilitar Protocolo IPv6 (Dual Stack)',
                                                             'help': 'Desactiva IPv6 para priorizar el tráfico IPv4 y '
                                                                     'reducir overhead de resolución.',
                                                             'default': False},
                                                     {       'id': 'net_dnscache',
                                                             'name': 'Prevenir Almacenamiento de DNS Negativo',
                                                             'help': 'Evita que el sistema guarde fallos temporales de '
                                                                     'resolución de nombres.',
                                                             'default': False},
                                                     {       'id': 'net_smb',
                                                             'name': 'Inhabilitar Protocolo Legado SMBv1',
                                                             'help': 'Cierra una vulnerabilidad crítica de seguridad y '
                                                                     'reduce procesos huérfanos.',
                                                             'default': False},
                                                     {       'id': 'net_teredo',
                                                             'name': 'Inhabilitar Interfaz de Tunelizado Teredo',
                                                             'help': 'Remueve el adaptador virtual de transición IPv6 '
                                                                     'para ahorrar ciclos.',
                                                             'default': False},
                                                     {       'id': 'net_isatap',
                                                             'name': 'Inhabilitar Protocolo ISATAP',
                                                             'help': 'Elimina el tunelizado intra-sitio de paquetes '
                                                                     'IPv6.',
                                                             'default': False},
                                                     {       'id': 'net_netbios',
                                                             'name': 'Inhabilitar NetBIOS sobre TCP/IP',
                                                             'help': 'Desactiva la resolución de nombres antigua para '
                                                                     'redes locales.',
                                                             'default': False},
                                                     {       'id': 'net_wpad',
                                                             'name': 'Inhabilitar Auto-Descubrimiento WPAD',
                                                             'help': 'Acelera el inicio de la navegación web al omitir '
                                                                     'la búsqueda de proxy.',
                                                             'default': False},
                                                     {       'id': 'net_tcp_1323',
                                                             'name': 'Habilitar RFC 1323 (TCP Extensions)',
                                                             'help': 'Mejora la fiabilidad de las transmisiones en '
                                                                     'redes de alta latencia.',
                                                             'default': False},
                                                     {       'id': 'net_max_conn',
                                                             'name': 'Aumentar Conexiones Simultáneas (HTTP 1.0)',
                                                             'help': 'Eleva el límite de conexiones a 10 para acelerar '
                                                                     'la carga de webs antiguas.',
                                                             'default': False},
                                                     {       'id': 'net_max_conn11',
                                                             'name': 'Aumentar Conexiones Simultáneas (HTTP 1.1)',
                                                             'help': 'Eleva el límite de conexiones a 10 para acelerar '
                                                                     'la carga de sitios modernos.',
                                                             'default': False},
                                                     {       'id': 'net_dns_cloudflare',
                                                             'name': 'Establecer DNS Cloudflare (1.1.1.1)',
                                                             'help': 'Utiliza la infraestructura DNS más rápida y '
                                                                     'privada disponible globalmente.',
                                                             'default': False},
                                                     {       'id': 'net_dns_google',
                                                             'name': 'Establecer DNS Google (8.8.8.8)',
                                                             'help': 'Utiliza los servidores DNS de Google para una '
                                                                     'resolución confiable.',
                                                             'default': False}],
        'cat_gaming': [       {       'id': 'game_mode',
                                                                    'name': 'Habilitar Modo de Juego (Priorización de '
                                                                            'Recursos)',
                                                                    'help': 'Prioriza hilos de ejecución de juegos '
                                                                            'sobre procesos de background.',
                                                                    'default': False},
                                                            {       'id': 'game_process_priority',
                                                                    'name': 'Elevación Automática de Prioridad '
                                                                            '(Booster)',
                                                                    'help': "Fuerza prioridad 'Alta' en tiempo real "
                                                                            'para procesos de shooters competitivos.',
                                                                    'default': False},
                                                            {       'id': 'game_process_lasso',
                                                                    'name': 'Gestión Dinámica de Procesos (Lasso '
                                                                            'Emulation)',
                                                                    'help': 'Asegura que el juego tenga acceso '
                                                                            'exclusivo a los núcleos físicos del CPU.',
                                                                    'default': False},
                                                            {       'id': 'game_timer_res',
                                                                    'name': 'Fijar Resolución de Timer a 0.5ms (RTC)',
                                                                    'help': 'Reduce el jitter de entrada y mejora la '
                                                                            'suavidad del motor gráfico.',
                                                                    'default': False},
                                                            {       'id': 'game_mouse_accel',
                                                                    'name': 'Inhabilitar Aceleración de Mouse (Raw '
                                                                            'Input)',
                                                                    'help': 'Proporciona una relación 1:1 real entre '
                                                                            'el movimiento físico y el puntero.',
                                                                    'default': False},
                                                            {       'id': 'game_ultimate_power',
                                                                    'name': "Habilitar Plan 'Ultimate Performance'",
                                                                    'help': 'Desbloquea el perfil energético de máxima '
                                                                            'latencia cero de Windows.',
                                                                    'default': False},
                                                            {       'id': 'game_msi_mode',
                                                                    'name': 'Habilitar Modo MSI (Message Signaled '
                                                                            'Interrupts)',
                                                                    'help': 'Reduce la latencia de interrupción de '
                                                                            'hardware para GPU y adaptadores de red.',
                                                                    'default': False},
                                                            {       'id': 'game_hags',
                                                                    'name': 'Habilitar Hardware GPU Scheduling (HAGS)',
                                                                    'help': 'Reduce la sobrecarga del CPU al delegar '
                                                                            'la gestión de memoria a la GPU.',
                                                                    'default': False},
                                                            {       'id': 'game_mmcss',
                                                                    'name': 'Optimizar Servicio MMCSS (Multimedia '
                                                                            'Class Scheduler)',
                                                                    'help': 'Prioriza el tráfico multimedia y de '
                                                                            'juegos en el kernel de Windows.',
                                                                    'default': False},
                                                            {       'id': 'game_fullscreen_opt',
                                                                    'name': 'Inhabilitar Optimización de Pantalla '
                                                                            'Completa',
                                                                    'help': 'Evita el modo borderless forzado que '
                                                                            'introduce latencia de entrada.',
                                                                    'default': False},
                                                            {       'id': 'game_edge_bg',
                                                                    'name': 'Suspender Procesos de Edge en Background',
                                                                    'help': 'Libera memoria RAM ocupada por procesos '
                                                                            'inactivos del navegador.',
                                                                    'default': False},
                                                            {       'id': 'game_chrome_bg',
                                                                    'name': 'Suspender Procesos de Chrome en '
                                                                            'Background',
                                                                    'help': 'Evita que las extensiones de Chrome '
                                                                            'consuman ciclos de CPU durante el juego.',
                                                                    'default': False},
                                                            {       'id': 'game_steam_hardware',
                                                                    'name': 'Inhabilitar Aceleración de HW en Steam',
                                                                    'help': 'Evita el uso innecesario de la GPU por '
                                                                            'parte de la interfaz de Steam.',
                                                                    'default': False},
                                                            {       'id': 'game_discord_hw',
                                                                    'name': 'Inhabilitar Aceleración de HW en Discord',
                                                                    'help': 'Libera recursos de visualización de la '
                                                                            'GPU durante sesiones de juego.',
                                                                    'default': False},
                                                            {       'id': 'game_vr',
                                                                    'name': 'Responsividad del Sistema (Gaming/VR '
                                                                            'Mode)',
                                                                    'help': 'Ajusta el perfil de respuesta para '
                                                                            'minimizar micro-stutters.',
                                                                    'default': False},
                                                            {       'id': 'game_fth',
                                                                    'name': 'Inhabilitar Fault Tolerant Heap (FTH)',
                                                                    'help': 'Evita la degradación del rendimiento tras '
                                                                            'cierres inesperados de aplicaciones.',
                                                                    'default': False},
                                                            {       'id': 'game_hpet',
                                                                    'name': 'Inhabilitar High Precision Event Timer '
                                                                            '(HPET)',
                                                                    'help': 'Elimina una fuente común de stutters en '
                                                                            'arquitecturas modernas.',
                                                                    'default': False},
                                                            {       'id': 'game_xbox_dvr',
                                                                    'name': 'Eliminar Registros de Captura (Game DVR)',
                                                                    'help': 'Remueve llaves de registro que activan la '
                                                                            'grabación de fondo invisible.',
                                                                    'default': False},
                                                            {       'id': 'game_core_parking',
                                                                    'name': 'Inhabilitar Core Parking (Estado de '
                                                                            'Núcleos)',
                                                                    'help': 'Mantiene todos los núcleos del CPU '
                                                                            'activos para evitar latencia de '
                                                                            'despertar.',
                                                                    'default': False},
                                                            {       'id': 'game_vbs',
                                                                    'name': 'Inhabilitar Virtualization-Based Security '
                                                                            '(VBS)',
                                                                    'help': 'Desactivar aislamiento de núcleo para '
                                                                            'mejorar FPS. SÓLO GAMING EXTREMO.',
                                                                    'default': False},
                                                            {       'id': 'perf_win32_priority',
                                                                    'name': 'Optimizar Separación de Prioridad Win32',
                                                                    'help': 'Ajusta la distribución de tiempo del '
                                                                            'procesador para la app activa.',
                                                                    'default': False},
                                                            {       'id': 'perf_large_cache',
                                                                    'name': 'Habilitar Cache de Sistema Extendido',
                                                                    'help': 'Mejora el rendimiento de archivos pesados '
                                                                            'residiendo mas tiempo en RAM.',
                                                                    'default': False},
                                                            {       'id': 'perf_io_limit',
                                                                    'name': 'Elevar Límite de Bloqueo de Páginas I/O',
                                                                    'help': 'Aumenta el throughput de transferencia de '
                                                                            'datos en disco.',
                                                                    'default': False},
                                                            {       'id': 'perf_wait_kill',
                                                                    'name': 'Reducir Tiempo de Cierre de Servicios',
                                                                    'help': 'Acelera el apagado del sistema al '
                                                                            'terminar procesos en 2 segundos.',
                                                                    'default': False},
                                                            {       'id': 'perf_auto_end',
                                                                    'name': 'Cierre Forzado de Apps al Apagar',
                                                                    'help': 'Termina automáticamente procesos que '
                                                                            'impidan el apagado del equipo.',
                                                                    'default': False},
                                                            {       'id': 'perf_menu_delay',
                                                                    'name': 'Eliminar Retraso de Visualización de '
                                                                            'Menús',
                                                                    'help': 'Configura el delay de menús a 0ms para '
                                                                            'una respuesta instantánea.',
                                                                    'default': False},
                                                            {       'id': 'perf_startup_delay',
                                                                    'name': 'Eliminar Retraso de Carga en el Arranque',
                                                                    'help': 'Optimiza la secuencia de inicio de '
                                                                            'aplicaciones post-logon.',
                                                                    'default': False}],
        'cat_power': [       {       'id': 'pwr_ultimate',
                                                                   'name': "Forzar Perfil 'Ultimate Performance' "
                                                                           '(PowerCfg)',
                                                                   'help': 'Elimina cualquier restricción energética '
                                                                           'para maximizar el clock del CPU.',
                                                                   'default': False},
                                                           {       'id': 'pwr_min_cpu',
                                                                   'name': 'Estado Mínimo del Procesador: 100%',
                                                                   'help': 'Evita que la frecuencia del CPU fluctúe, '
                                                                           'manteniendo un rendimiento constante.',
                                                                   'default': False},
                                                           {       'id': 'pwr_throttling',
                                                                   'name': 'Inhabilitar Power Throttling del Sistema',
                                                                   'help': 'Impide que Windows limite recursos a '
                                                                           'aplicaciones en segundo plano como '
                                                                           'Discord.',
                                                                   'default': False},
                                                           {       'id': 'pwr_cpu_boost',
                                                                   'name': 'Mantener CPU Turbo Boost (Always On)',
                                                                   'help': 'Fuerza el uso de frecuencias Turbo incluso '
                                                                           'bajo condiciones de batería.',
                                                                   'default': False},
                                                           {       'id': 'pwr_pci_link',
                                                                   'name': 'Inhabilitar PCIe Link State Power '
                                                                           'Management',
                                                                   'help': 'Evita latencia al despertar la GPU desde '
                                                                           'estados de ahorro energético.',
                                                                   'default': False},
                                                           {       'id': 'pwr_hibernation',
                                                                   'name': 'Inhabilitar Hibernación (Hibernet.sys)',
                                                                   'help': 'Elimina el archivo de hibernación para '
                                                                           'ahorrar espacio y reducir I/O en SSD.',
                                                                   'default': False},
                                                           {       'id': 'pwr_disk_timeout',
                                                                   'name': 'Inhabilitar Reposo de Unidades de Disco '
                                                                           '(HDD)',
                                                                   'help': 'Evita el spin-down de discos mecánicos que '
                                                                           'causa micro-stutters.',
                                                                   'default': False},
                                                           {       'id': 'pwr_adaptive_brightness',
                                                                   'name': 'Inhabilitar Control de Brillo Adaptativo',
                                                                   'help': 'Desactiva el ajuste automático basado en '
                                                                           'sensores de luz ambiental.',
                                                                   'default': False},
                                                           {       'id': 'pwr_usb_hub_suspend',
                                                                   'name': 'Inhabilitar Suspensión Selectiva de Hubs '
                                                                           'USB',
                                                                   'help': 'Garantiza que los puertos USB no entren en '
                                                                           'reposo, evitando lag de periféricos.',
                                                                   'default': False}],
        'cat_gpu': [       {       'id': 'gpu_hags',
                                                                     'name': 'Habilitar Hardware Accelerated GPU '
                                                                             'Scheduling',
                                                                     'help': 'Reduce la latencia de cuadros al delegar '
                                                                             'la gestión de memoria a la propia GPU.',
                                                                     'default': False},
                                                             {       'id': 'gpu_mpo',
                                                                     'name': 'Inhabilitar Multi-Plane Overlay (MPO '
                                                                             'Bypass)',
                                                                     'help': 'Soluciona parpadeos y stutters en '
                                                                             'configuraciones multi-monitor o '
                                                                             'navegadores integrados.',
                                                                     'default': False},
                                                             {       'id': 'gpu_preemption',
                                                                     'name': 'Inhabilitar GPU Preemption (Priority '
                                                                             'Interrupt)',
                                                                     'help': 'Evita pausas en el renderizado al '
                                                                             'impedir que el sistema interrumpa la '
                                                                             'GPU.',
                                                                     'default': False},
                                                             {       'id': 'gpu_reduce_dpc',
                                                                     'name': 'Minimizar Latencia DPC del Driver '
                                                                             'Gráfico',
                                                                     'help': 'Ajusta parámetros de interrupción para '
                                                                             'priorizar el tiempo real en el '
                                                                             'procesamiento de video.',
                                                                     'default': False},
                                                             {       'id': 'gpu_dwm_priority',
                                                                     'name': 'Prioridad de Proceso Crítica para '
                                                                             'DWM.exe',
                                                                     'help': 'Asegura un refresco de escritorio fluido '
                                                                             'al elevar la prioridad del gestor de '
                                                                             'ventanas.',
                                                                     'default': False},
                                                             {       'id': 'gpu_gpu_priority',
                                                                     'name': 'Prioridad GPU a Nivel 8 (MMCSS Context)',
                                                                     'help': 'Eleva la jerarquía de ejecución del '
                                                                             'driver gráfico durante el gaming.',
                                                                     'default': False},
                                                             {       'id': 'gpu_perf_registry',
                                                                     'name': 'Optimización de Registro MMCSS para GPU',
                                                                     'help': 'Ajusta NetworkThrottling y '
                                                                             'SystemResponsiveness para flujos de '
                                                                             'video.',
                                                                     'default': False},
                                                             {       'id': 'gpu_nvidia_power',
                                                                     'name': 'NVIDIA: Forzar Modo de Rendimiento '
                                                                             'Máximo',
                                                                     'help': 'Configura el panel NVIDIA para ignorar '
                                                                             'el ahorro de energía vía registro.',
                                                                     'default': False},
                                                             {       'id': 'gpu_nvidia_telemetry',
                                                                     'name': 'Inhabilitar Telemetría de Driver NVIDIA',
                                                                     'help': 'Remueve servicios de recolección de '
                                                                             'datos de uso de NVIDIA.',
                                                                     'default': False},
                                                             {       'id': 'gpu_amd_power',
                                                                     'name': 'AMD: Desactivar PowerPlay / Low Power '
                                                                             'State',
                                                                     'help': 'Mantiene las frecuencias de reloj de la '
                                                                             'GPU AMD estables.',
                                                                     'default': False},
                                                             {       'id': 'gpu_amd_telemetry',
                                                                     'name': 'Inhabilitar Telemetría de Driver AMD '
                                                                             '(User Exp)',
                                                                     'help': 'Remueve servicios de background de '
                                                                             'reporte de errores de AMD.',
                                                                     'default': False},
                                                             {       'id': 'gpu_pci_express_max',
                                                                     'name': 'PCIe Link State: Deshabilitado (Nivel '
                                                                             'GPU)',
                                                                     'help': 'Ajuste específico de registro para el '
                                                                             'bus PCIe del adaptador gráfico.',
                                                                     'default': False},
                                                             {       'id': 'gpu_disable_fullscreen_opt',
                                                                     'name': 'Forzar Modo de Pantalla Completa '
                                                                             'Exclusiva',
                                                                     'help': 'Desactiva las optimizaciones de shell '
                                                                             'que emulan pantalla completa.',
                                                                     'default': False},
                                                             {       'id': 'gpu_freesync_vsync_off',
                                                                     'name': 'Inhabilitar V-Sync Global (Forzado)',
                                                                     'help': 'Desactiva la sincronización vertical a '
                                                                             'nivel de sistema para eliminar input '
                                                                             'lag.',
                                                                     'default': False},
                                                             {       'id': 'gpu_cache_clean',
                                                                     'name': 'Purga de Shader Cache (DirectX/Vulkan)',
                                                                     'help': 'Elimina el caché de sombreadores para '
                                                                             'solucionar stutters tras updates.',
                                                                     'default': False},
                                                             {       'id': 'gpu_vram_paging',
                                                                     'name': 'Optimizar Paginación de Memoria de Video '
                                                                             '(VRAM)',
                                                                     'help': 'Ajusta como Windows gestiona el '
                                                                             'intercambio de texturas entre RAM y '
                                                                             'VRAM.',
                                                                     'default': False},
                                                             {       'id': 'gpu_shader_cache',
                                                                     'name': 'Redireccionar Shader Cache a NVMe '
                                                                             '(Rápido)',
                                                                     'help': 'Asegura que los shaders se carguen desde '
                                                                             'la unidad de disco más veloz.',
                                                                     'default': False},
                                                             {       'id': 'gpu_disable_mpv',
                                                                     'name': 'Inhabilitar Precompilación de Shaders en '
                                                                             'BG',
                                                                     'help': 'Evita el uso intensivo de CPU/GPU '
                                                                             'mientras juegas por tareas de fondo.',
                                                                     'default': False},
                                                             {       'id': 'gpu_gsync_compat',
                                                                     'name': 'Habilitar Compatibilidad G-Sync '
                                                                             '(FreeSync Mode)',
                                                                     'help': 'Fuerza el refresco variable en monitores '
                                                                             'compatibles vía registro.',
                                                                     'default': False},
                                                             {       'id': 'gpu_night_light_off',
                                                                     'name': 'Inhabilitar Filtro de Luz Nocturna '
                                                                             '(Color Mapping)',
                                                                     'help': 'Evita alteraciones en la tabla de '
                                                                             'colores del monitor que introducen lag.',
                                                                     'default': False}],
        'cat_kernel': [       {       'id': 'ext_57_processes',
                                                                         'name': 'Consolidación de Servicios del '
                                                                                 'Sistema (mínimo de procesos)',
                                                                         'help': 'Redirige svchost y desactiva '
                                                                                 'servicios no críticos para reducir '
                                                                                 'la cantidad total de procesos '
                                                                                 'activos al mínimo operativo.',
                                                                         'default': False},
                                                                 {       'id': 'kern_registry_size',
                                                                         'name': 'Aumentar Límite del Registro (System '
                                                                                 'Hive)',
                                                                         'help': 'Previene errores de cuota de memoria '
                                                                                 'en el registro para sistemas '
                                                                                 'altamente personalizados.',
                                                                         'default': False},
                                                                 {       'id': 'kern_bcdedit_inc',
                                                                         'name': 'Frecuencia de Interrupciones BCDEDIT '
                                                                                 '(Ticks)',
                                                                         'help': "Ajusta 'useplatformtick' y "
                                                                                 "'disabledynamictick' para una base "
                                                                                 'de tiempo ultra precisa.',
                                                                         'default': False},
                                                                 {       'id': 'kern_memory_comp',
                                                                         'name': 'Deshabilitar Compresión de Memoria '
                                                                                 '(MMAgent)',
                                                                         'help': 'Evita que la CPU gaste ciclos '
                                                                                 'comprimiendo páginas de RAM, '
                                                                                 'priorizando la latencia.',
                                                                         'default': False},
                                                                 {       'id': 'kern_system_resp',
                                                                         'name': 'Ajuste de SystemResponsiveness al 0% '
                                                                                 '(Real-Time)',
                                                                         'help': 'Elimina la reserva de recursos de '
                                                                                 'background de Windows para dedicar '
                                                                                 'el 100% al proceso foco.',
                                                                         'default': False},
                                                                 {       'id': 'kernel_mitigations',
                                                                         'name': 'Inhabilitar Mitigaciones de '
                                                                                 'Seguridad del CPU',
                                                                         'help': 'Desactiva '
                                                                                 'Spectre/Meltdown/Speculative '
                                                                                 'Execution. +15% rendimiento, reduce '
                                                                                 'seguridad.',
                                                                         'default': False},
                                                                 {       'id': 'kern_large_pages',
                                                                         'name': 'Habilitar Large Pages (Memoria '
                                                                                 'Virtual)',
                                                                         'help': 'Reduce las faltas de página (TLB '
                                                                                 'misses) en aplicaciones con alta '
                                                                                 'carga de memoria.',
                                                                         'default': False},
                                                                 {       'id': 'kern_iot_core',
                                                                         'name': 'Configuración de Perfil Embebido '
                                                                                 'Minimalista',
                                                                         'help': 'Ajusta parámetros internos del '
                                                                                 'sistema para comportarse como un '
                                                                                 'perfil Windows IoT de bajo consumo '
                                                                                 'de recursos.',
                                                                         'default': False},
                                                                 {       'id': 'kern_process_isolation',
                                                                         'name': 'Deshabilitar Aislamiento de Procesos '
                                                                                 'Core',
                                                                         'help': 'Reduce el overhead de virtualización '
                                                                                 'del kernel para maximizar la '
                                                                                 'velocidad de hilos.',
                                                                         'default': False}],
        'cat_extreme': [       {       'id': 'ext_super_nuclear',
                                                                       'name': 'Perfil de Consolidación de Servicios (Máximo Rendimiento)',
                                                                       'help': 'Optimización avanzada que agrupa procesos del sistema para reducir el conteo a ~50. Mantiene compatibilidad total con juegos e Internet.',
                                                                       'default': False},
                                                               {       'id': 'ext_minimalist',
                                                                       'name': 'Perfil Shell Reducido de Alto '
                                                                               'Rendimiento',
                                                                       'help': 'Desactiva efectos visuales del Shell '
                                                                               'de Windows para liberar ciclos de CPU '
                                                                               'y GPU en su totalidad.',
                                                                       'default': False},
                                                               {       'id': 'ext_defender_kill',
                                                                       'name': 'Desactivación Permanente de Windows '
                                                                               'Defender',
                                                                       'help': 'Remueve el motor de escaneo y '
                                                                               'servicios de seguridad nativos vía '
                                                                               'registro/GPO.',
                                                                       'default': False},
                                                               {       'id': 'ext_uwp_kill_all',
                                                                       'name': 'Eliminación Completa de Aplicaciones '
                                                                               'UWP Integradas',
                                                                       'help': 'Desinstala todas las aplicaciones UWP '
                                                                               'preinstaladas para todos los usuarios '
                                                                               'del sistema.',
                                                                       'default': False},
                                                               {       'id': 'ext_firewall_off',
                                                                       'name': 'Inhabilitar Windows Firewall (Stack '
                                                                               'Bypass)',
                                                                       'help': 'Desactiva el filtrado de paquetes '
                                                                               'nativo para reducir latencia de red al '
                                                                               'mínimo.',
                                                                       'default': False},
                                                               {       'id': 'ext_update_dead',
                                                                       'name': 'Bloqueo de Windows Update (Política '
                                                                               'LTSC)',
                                                                       'help': 'Impide cualquier intento de '
                                                                               'actualización o descarga de drivers '
                                                                               'por parte del sistema operativo.',
                                                                       'default': False}],
        'cat_util': [       {       'id': 'util_dotnet',
                                                                  'name': 'Instalar .NET Runtimes',
                                                                  'help': 'Asegura la compatibilidad con todas las '
                                                                          'versiones de frameworks de aplicaciones.',
                                                                  'default': False},
                                                          {       'id': 'util_vc_redist',
                                                                  'name': 'Instalar C++ Redistributables',
                                                                  'help': 'Instala todas las librerías necesarias para '
                                                                          'la ejecución de juegos y software.',
                                                                  'default': False},
                                                          {       'id': 'util_directx',
                                                                  'name': 'Actualizar DirectX Runtimes',
                                                                  'help': 'Instala componentes legados de DirectX para '
                                                                          'juegos antiguos.',
                                                                  'default': False},
                                                          {       'id': 'util_powershell_7',
                                                                  'name': 'Instalar PowerShell 7',
                                                                  'help': 'Instala la versión moderna y más rápida del '
                                                                          'motor de scripts de Windows.',
                                                                  'default': False},
                                                          {       'id': 'util_driver_updates',
                                                                  'name': 'Excluir Drivers de Windows Update',
                                                                  'help': 'Evita que Windows sobreescriba tus drivers '
                                                                          'personalizados con versiones genéricas.',
                                                                  'default': False},
                                                          {       'id': 'util_ps_telemetry',
                                                                  'name': 'Deshabilitar Telemetría PowerShell',
                                                                  'help': 'Elimina el reporte de uso en la terminal '
                                                                          'moderna de Windows.',
                                                                  'default': False},
                                                          {       'id': 'util_end_task_rc',
                                                                  'name': 'Finalizar Tarea en Taskbar',
                                                                  'help': 'Agrega la opción de cerrar procesos '
                                                                          'directamente del click derecho en el '
                                                                          'taskbar.',
                                                                  'default': False},
                                                          {       'id': 'util_start_recommendations',
                                                                  'name': 'Quitar Recomendaciones del Inicio',
                                                                  'help': 'Limpia la sección de archivos recientes y '
                                                                          'apps sugeridas en el Inicio.',
                                                                  'default': False},
                                                          {       'id': 'util_sticky_keys',
                                                                  'name': 'Desactivar Sticky Keys',
                                                                  'help': 'Evita que el sistema pregunte por Sticky '
                                                                          'Keys tras pulsar Shift repetidamente.',
                                                                  'default': False},
                                                          {       'id': 'util_taskbar_center',
                                                                  'name': 'Taskbar: Alinear a la Izquierda',
                                                                  'help': 'Restaura la posición clásica de los iconos '
                                                                          'en el escritorio de Windows 11.',
                                                                  'default': False},
                                                          {       'id': 'util_settings_home',
                                                                  'name': 'Quitar Página Inicio de Ajustes',
                                                                  'help': "Elimina la pantalla de 'Inicio' innecesaria "
                                                                          'al abrir los ajustes de Windows.',
                                                                  'default': False},
                                                          {       'id': 'util_new_outlook',
                                                                  'name': 'Bloquear Nuevo Outlook',
                                                                  'help': 'Evita que Windows reemplace el cliente de '
                                                                          'correo clásico por la versión web-app.',
                                                                  'default': False},
                                                          {       'id': 'util_cross_device',
                                                                  'name': 'Desactivar Experiencias Multi-Dispositivo',
                                                                  'help': 'Desactiva la sincronización de tareas '
                                                                          'inacabadas con otros PCs o móviles.',
                                                                  'default': False},
                                                          {       'id': 'util_task_view',
                                                                  'name': 'Ocultar Vista de Tareas',
                                                                  'help': 'Limpia la barra de tareas eliminando el '
                                                                          'icono de escritorios virtuales.',
                                                                  'default': False},
                                                          {       'id': 'util_folder_discovery',
                                                                  'name': 'Desact. Descubrimiento Auto de Carpetas',
                                                                  'help': 'Evita que el Explorador cambie el tipo de '
                                                                          'vista al abrir carpetas con imágenes o '
                                                                          'música.',
                                                                  'default': False},
                                                          {       'id': 'util_bsod_detail',
                                                                  'name': 'BSOD con Información Detallada',
                                                                  'help': 'Muestra parámetros y códigos de error '
                                                                          'completos en la pantalla azul de la muerte.',
                                                                  'default': False},
                                                          {       'id': 'util_numlock',
                                                                  'name': 'Activar NumLock al Inicio',
                                                                  'help': 'Enciende NumLock automáticamente al iniciar '
                                                                          'sesión en Windows.',
                                                                  'default': False},
                                                          {       'id': 'util_verbose_logon',
                                                                  'name': 'Mensajes Detallados en Login',
                                                                  'help': 'Muestra el estado de cada servicio durante '
                                                                          'el inicio y cierre de sesión.',
                                                                  'default': False},
                                                          {       'id': 'util_consumer_features',
                                                                  'name': 'Desactivar Apps Sugeridas MS Store',
                                                                  'help': 'Evita la instalación silenciosa de apps '
                                                                          'promocionales de Microsoft.',
                                                                  'default': False},
                                                          {       'id': 'util_wpbt',
                                                                  'name': 'Bloquear Inyección de Bloatware (WPBT)',
                                                                  'help': 'Impide que fabricantes instalen software '
                                                                          'vía BIOS al iniciar Windows.',
                                                                  'default': False},
                                                          {       'id': 'util_widgets_remove',
                                                                  'name': 'Eliminar Widgets de Windows 11',
                                                                  'help': 'Desinstala el panel de widgets y noticias '
                                                                          'de la barra de tareas.',
                                                                  'default': False},
                                                          {       'id': 'uwp_xbox',
                                                                  'name': '[BORRAR] Apps Xbox & GameBar',
                                                                  'help': 'Desinstala COMPLETAMENTE todos los paquetes '
                                                                          'UWP de Xbox. IRREVERSIBLE.',
                                                                  'default': False},
                                                           {       'id': 'uwp_bloatware',
                                                                   'name': '[BORRAR] Bloatware General (Exhaustivo)',
                                                                   'help': 'Elimina Zune, BingNews, Solitaire, People, SkypeApp, YourPhone, Teams, PowerAutomate y 20+ apps más. IRREVERSIBLE.',
                                                                   'default': False},
                                                          {       'id': 'uwp_onedrive',
                                                                  'name': '[BORRAR] OneDrive',
                                                                  'help': 'Desinstala completamente OneDrive del '
                                                                          'sistema. IRREVERSIBLE.',
                                                                  'default': False},
                                                          {       'id': 'uwp_edge',
                                                                  'name': '[BORRAR] Microsoft Edge',
                                                                  'help': 'Elimina Edge del sistema. IRREVERSIBLE. '
                                                                          'Solo para entornos sin necesidad de Edge.',
                                                                  'default': False},
                                                          {       'id': 'uwp_3dbuilder',
                                                                  'name': '[BORRAR] 3D Builder',
                                                                  'help': 'Desinstala la app de modelado 3D de '
                                                                          'Microsoft.',
                                                                  'default': False},
                                                          {       'id': 'uwp_alarms',
                                                                  'name': '[BORRAR] Alarmas y Reloj',
                                                                  'help': 'Desinstala la aplicación de alarmas y '
                                                                          'cronómetro.',
                                                                  'default': False},
                                                          {       'id': 'uwp_camera',
                                                                  'name': '[BORRAR] Cámara de Windows',
                                                                  'help': 'Desinstala la app de cámara de la Store.',
                                                                  'default': False},
                                                          {       'id': 'uwp_communications',
                                                                  'name': '[BORRAR] Correo y Calendario',
                                                                  'help': 'Desinstala las apps de correo y calendario '
                                                                          'integradas.',
                                                                  'default': False},
                                                          {       'id': 'uwp_feedback',
                                                                  'name': '[BORRAR] Centro de Opiniones',
                                                                  'help': 'Desinstala la app de feedback de Microsoft.',
                                                                  'default': False},
                                                          {       'id': 'uwp_gethelp',
                                                                  'name': '[BORRAR] Obtener Ayuda',
                                                                  'help': 'Desinstala la app de soporte técnico de '
                                                                          'Microsoft.',
                                                                  'default': False},
                                                          {       'id': 'uwp_maps',
                                                                  'name': '[BORRAR] Mapas de Windows',
                                                                  'help': 'Desinstala la app de mapas integrada.',
                                                                  'default': False},
                                                          {       'id': 'uwp_mixedreality',
                                                                  'name': '[BORRAR] Mixed Reality Portal',
                                                                  'help': 'Desinstala el portal de realidad mixta.',
                                                                  'default': False},
                                                          {       'id': 'uwp_people',
                                                                  'name': '[BORRAR] Contactos (People)',
                                                                  'help': 'Desinstala la app de contactos integrada.',
                                                                  'default': False},
                                                          {       'id': 'uwp_photos',
                                                                  'name': '[BORRAR] Fotos de Microsoft',
                                                                  'help': 'Desinstala la app Fotos moderna '
                                                                          '(reemplazable por visor clásico).',
                                                                  'default': False},
                                                          {       'id': 'uwp_skype',
                                                                  'name': '[BORRAR] Skype',
                                                                  'help': 'Desinstala la app de Skype preinstalada.',
                                                                  'default': False},
                                                          {       'id': 'uwp_solitaire',
                                                                  'name': '[BORRAR] Solitario de Microsoft',
                                                                  'help': 'Desinstala los juegos de solitario '
                                                                          'preinstalados.',
                                                                  'default': False},
                                                          {       'id': 'uwp_soundrecorder',
                                                                  'name': '[BORRAR] Grabadora de Sonido',
                                                                  'help': 'Desinstala la app de grabación de audio.',
                                                                  'default': False},
                                                          {       'id': 'uwp_stickynotes',
                                                                  'name': '[BORRAR] Sticky Notes',
                                                                  'help': 'Desinstala la app de notas adhesivas.',
                                                                  'default': False},
                                                          {       'id': 'uwp_weather',
                                                                  'name': '[BORRAR] Bing Weather',
                                                                  'help': 'Desinstala la app del clima de Bing.',
                                                                  'default': False},
                                                          {       'id': 'uwp_yourphone',
                                                                  'name': '[BORRAR] Tu Teléfono (Link to Phone)',
                                                                  'help': 'Desinstala la app de vinculación con móvil.',
                                                                  'default': False}],
        'cat_pro': [       {       'id': 'util_context_compact',
                                                                'name': 'Habilitar Menús Contextuales Compactos',
                                                                'help': 'Reduce el padding y espacio entre opciones de '
                                                                        'los menús de click derecho.',
                                                                'default': False},
                                                        {       'id': 'util_legacy_photo',
                                                                'name': 'Restaurar Visor de Fotos Clásico (Win7)',
                                                                'help': 'Habilita el visor de imágenes ultra rápido y '
                                                                        'ligero de versiones anteriores.',
                                                                'default': False},
                                                        {       'id': 'util_legacy_calc',
                                                                'name': 'Restaurar Calculadora Clásica Win32',
                                                                'help': 'Reemplaza la versión UWP lenta por la versión '
                                                                        'ejecutable tradicional.',
                                                                'default': False},
                                                        {       'id': 'util_god_mode',
                                                                'name': 'Acceso Unificado al Panel de Control del '
                                                                        'Sistema',
                                                                'help': 'Crea un acceso directo a todos los ajustes '
                                                                        'administrativos del sistema en una sola '
                                                                        'ventana.',
                                                                'default': False},
                                                        {       'id': 'util_verbose_boot',
                                                                'name': 'Habilitar Historial de Arranque Detallado',
                                                                'help': 'Muestra los drivers y servicios cargándose '
                                                                        'durante el inicio en pantalla.',
                                                                'default': False},
                                                        {       'id': 'util_desktop_labels',
                                                                'name': 'Remover Flechas de Accesos Directos',
                                                                'help': 'Limpia los iconos del escritorio eliminando '
                                                                        'la flecha de shortcut.',
                                                                'default': False},
                                                        {       'id': 'util_explorer_pc',
                                                                'name': "Abrir Explorador en 'Este Equipo' (PC)",
                                                                'help': 'Configura el explorador para omitir la vista '
                                                                        'de archivos recientes por defecto.',
                                                                'default': False}],
        'cat_help': []}
