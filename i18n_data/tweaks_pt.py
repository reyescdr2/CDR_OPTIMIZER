# type: ignore
def get_tweaks_pt():
    return {
        'cat_system': [
            {
                'id': 'svc_diagtrack',
                'name': 'Desativar Telemetria',
                'help': 'Desativa o DiagTrack. Libera processos em segundo plano.',
                'default': False
            },
            {
                'id': 'svc_sysmain',
                'name': 'Desativar SysMain',
                'help': 'Pré-carrega aplicativos na RAM. Desativar se usar um SSD.',
                'default': False
            },
            {
                'id': 'svc_wsearch',
                'name': 'Desativar Windows Search',
                'help': 'Impede a indexação constante. MUITO RECOMENDADO para SSDs.',
                'default': False
            },
            {
                'id': 'svc_wuauserv_manual',
                'name': 'Windows Update Manual',
                'help': 'Impede downloads de atualizações durante o jogo.',
                'default': False
            },
            {
                'id': 'ai_copilot',
                'name': 'Bloquear Windows Copilot',
                'help': 'Desativa a IA Copilot ao nível de GPO.',
                'default': False
            },
            {
                'id': 'ai_recall',
                'name': 'Desativar Windows Recall',
                'help': 'Desativa as capturas constantes do Windows Recall (IA).',
                'default': False
            },
            {
                'id': 'svc_bcastdvr',
                'name': 'Desativar Game DVR',
                'help': 'Impede a gravação de tela em segundo plano. Melhora FPS.',
                'default': False
            },
            {
                'id': 'svc_wer',
                'name': 'Desativar Relatório de Erros do Windows',
                'help': 'Sistema de coleta de erros da Microsoft.',
                'default': False
            },
            {
                'id': 'svc_dps',
                'name': 'Desativar Execução de Diagnóstico',
                'help': 'Consome recursos para diagnosticar falhas silenciosas.',
                'default': False
            },
            {
                'id': 'svc_pcasvc',
                'name': 'Desativar Assist. de Compatibilidade de PC',
                'help': 'Monitor de aplicativos legados que causa micro-stutter.',
                'default': False
            },
            {
                'id': 'svc_remoteregistry',
                'name': 'Desativar Registro Remoto',
                'help': 'Impede que usuários remotos modifiquem o seu registro.',
                'default': False
            },
            {
                'id': 'svc_tabletinputservice',
                'name': 'Desativar Teclado Touch',
                'help': 'Desativar se não usar uma tela sensível ao toque.',
                'default': False
            },
            {
                'id': 'svc_wbio_srvc',
                'name': 'Desativar Biometria',
                'help': 'Desativar se não usar impressão digital ou Face ID.',
                'default': False
            },
            {
                'id': 'svc_bits',
                'name': 'Desativar BITS',
                'help': 'Transferências em segundo plano para Update/Store.',
                'default': False
            },
            {
                'id': 'svc_defrag_svc',
                'name': 'Desativar Desfragmentação Auto',
                'help': 'Desativa a desfragmentação automática para controlar manualmente o trim do SSD.',
                'default': False
            }
        ],
        'cat_clean': [
            {
                'id': 'clean_ram',
                'name': 'Otimizar RAM (Clear Working Sets)',
                'help': 'Força a redução do cache e aplicativos em segundo plano para liberar RAM instantaneamente.',
                'default': False
            },
            {
                'id': 'clean_temp',
                'name': 'Limpar Pasta Temporária',
                'help': 'Exclui os arquivos temporários dos aplicativos.',
                'default': False
            },
            {
                'id': 'clean_prefetch',
                'name': 'Limpar Prefetch',
                'help': 'Exclui os arquivos de pré-carregamento (prefetch).',
                'default': False
            },
            {
                'id': 'clean_winupdate',
                'name': 'Limpar Cache do Windows Update',
                'help': 'Exclui arquivos de instalação residuais de atualizações antigas.',
                'default': False
            },
            {
                'id': 'clean_recycle',
                'name': 'Esvaziar Lixeira',
                'help': 'Força o esvaziamento de todas as lixeiras em todos os discos.',
                'default': False
            },
            {
                'id': 'clean_dns',
                'name': 'Limpar Cache DNS',
                'help': 'Resolve conexões lentas renovando as rotas de rede.',
                'default': False
            },
            {
                'id': 'clean_eventlog',
                'name': 'Limpar Visualizador de Eventos',
                'help': 'Exclui todos os logs de eventos do Windows.',
                'default': False
            },
            {
                'id': 'clean_thumbcache',
                'name': 'Limpar Cache de Miniaturas',
                'help': 'Restaura ícones de imagens/vídeos corrompidos.',
                'default': False
            },
            {
                'id': 'clean_fontcache',
                'name': 'Limpar Cache de Fontes',
                'help': 'Útil se o texto parecer embaçado ou mal renderizado.',
                'default': False
            },
            {
                'id': 'clean_iconcache',
                'name': 'Limpar Cache de Ícones',
                'help': 'Exclui e reinicia o cache de ícones do sistema.',
                'default': False
            },
            {
                'id': 'clean_crashdumps',
                'name': 'Excluir Dumps de Crash BSOD',
                'help': 'Exclui arquivos enormes criados durante uma tela azul.',
                'default': False
            },
            {
                'id': 'clean_chkdsk',
                'name': 'Excluir Fragmentos CheckDisk',
                'help': 'Exclui arquivos .chk que sobraram de uma recuperação de disco.',
                'default': False
            },
            {
                'id': 'clean_onedrive_temp',
                'name': 'Limpar Cache do OneDrive',
                'help': 'Exclui logs e resíduos do OneDrive.',
                'default': False
            },
            {
                'id': 'clean_chrome_cache',
                'name': 'Limpar Cache do Chrome',
                'help': 'Exclui o cache do Google Chrome (sem apagar as senhas).',
                'default': False
            },
            {
                'id': 'clean_edge_cache',
                'name': 'Limpar Cache do Edge',
                'help': 'Exclui o cache do Microsoft Edge.',
                'default': False
            },
            {
                'id': 'clean_firefox_cache',
                'name': 'Limpar Cache do Firefox',
                'help': 'Exclui o cache do Mozilla Firefox.',
                'default': False
            },
            {
                'id': 'clean_discord_cache',
                'name': 'Limpar Cache do Discord',
                'help': 'O Discord acumula muito cache ao longo do tempo.',
                'default': False
            },
            {
                'id': 'clean_steam_cache',
                'name': 'Limpar Cache da Steam',
                'help': 'O navegador da Steam acumula lixo que o torna lento.',
                'default': False
            },
            {
                'id': 'clean_epic_cache',
                'name': 'Limpar Cache da Epic Games',
                'help': 'Ajuda o Epic Games Launcher a abrir mais rápido.',
                'default': False
            },
            {
                'id': 'clean_spotify_cache',
                'name': 'Limpar Cache do Spotify',
                'help': 'O Spotify armazena temporariamente gigabytes de música e capas.',
                'default': False
            },
            {
                'id': 'clean_vcredist',
                'name': 'Limpar VCRedist da Steam',
                'help': 'Exclui instaladores deixados pelos jogos da Steam.',
                'default': False
            },
            {
                'id': 'clean_usrdoc_temp',
                'name': 'Limpar Documentos Temp',
                'help': 'Exclui arquivos temporários nas pastas de perfil.',
                'default': False
            },
            {
                'id': 'clean_system_logs',
                'name': 'Excluir Logs de Instalação',
                'help': 'Exclui os logs em C:\\Windows.',
                'default': False
            },
            {
                'id': 'clean_crypt_svc',
                'name': 'Redefinir Cache de Cripto',
                'help': 'Restaura as assinaturas no banco de dados do sistema.',
                'default': False
            },
            {
                'id': 'clean_bits_queue',
                'name': 'Limpar Fila do BITS',
                'help': 'Exclui tarefas de download em segundo plano.',
                'default': False
            }
        ],
        'cat_privacy': [
            {
                'id': 'priv_telemetry_level',
                'name': 'Nível de Telemetria 0',
                'help': 'Bloqueia quase toda transmissão de dados de diagnóstico.',
                'default': False
            },
            {
                'id': 'priv_etw_disable',
                'name': 'Bloqueio de Telemetria ETW Profundo',
                'help': 'Desativa sessões de AutoLogger ao nível de kernel.',
                'default': False
            },
            {
                'id': 'priv_cortana',
                'name': 'Desativar Cortana',
                'help': 'Libera RAM e processos de escuta constante.',
                'default': False
            },
            {
                'id': 'priv_start_web',
                'name': 'Desativar Pesquisa Web no Menu Iniciar',
                'help': 'Somente pesquisa local. Menu Iniciar ultra rápido.',
                'default': False
            },
            {
                'id': 'priv_news',
                'name': 'Desativar Notícias e Interesses',
                'help': 'Remove o widget de clima e notícias da barra de tarefas.',
                'default': False
            },
            {
                'id': 'priv_location',
                'name': 'Desativar Localização',
                'help': 'Impede o Windows e os apps de acessarem sua posição.',
                'default': False
            },
            {
                'id': 'priv_mic',
                'name': 'Desativar Sugestões de Digitação',
                'help': 'Desativa previsões que enviam os seus padrões de digitação.',
                'default': False
            },
            {
                'id': 'priv_feedback',
                'name': 'Frequência de Feedback: Nunca',
                'help': 'Impede o Windows de pedir opiniões constantemente.',
                'default': False
            },
            {
                'id': 'priv_activity',
                'name': 'Desativar Histórico de Atividades',
                'help': 'Impede o Windows de salvar o histórico de apps e arquivos.',
                'default': False
            },
            {
                'id': 'priv_sync',
                'name': 'Desativar Sincronização de Ajustes',
                'help': 'Impede que o fundo e configurações subam para a nuvem.',
                'default': False
            },
            {
                'id': 'priv_advertising',
                'name': 'Desativar ID de Anúncio',
                'help': 'Impede anúncios personalizados através do ID de anúncio.',
                'default': False
            },
            {
                'id': 'priv_appdiag',
                'name': 'Bloquear Diagnóstico de Apps',
                'help': 'Impede apps de acessarem diagnósticos de outros apps.',
                'default': False
            },
            {
                'id': 'priv_tailored',
                'name': 'Desativar Experiências Personalizadas',
                'help': 'Impede a MS de usar dados de diagnóstico para conteúdo pessoal.',
                'default': False
            },
            {
                'id': 'priv_ceip',
                'name': 'Sair do CEIP',
                'help': 'Sai do programa de melhorias da Microsoft.',
                'default': False
            },
            {
                'id': 'priv_handwriting',
                'name': 'Desativar Aprendizado de Escrita',
                'help': 'Impede a coleta de dados da caneta stylus.',
                'default': False
            },
            {
                'id': 'priv_defender_samples',
                'name': 'Não Enviar Amostras do Defender',
                'help': 'Impede o Defender de fazer upload de arquivos para os seus servidores.',
                'default': False
            },
            {
                'id': 'priv_onedrive',
                'name': 'Desativar OneDrive ao Iniciar',
                'help': 'Impede o OneDrive de iniciar com o sistema.',
                'default': False
            },
            {
                'id': 'priv_meetnow',
                'name': 'Ocultar "Reunião Agora"',
                'help': 'Remove o ícone de câmera da barra de tarefas.',
                'default': False
            },
            {
                'id': 'priv_app_suggestions',
                'name': 'Desativar Sugestões de Apps',
                'help': 'Impede o Windows de sugerir apps no Menu Iniciar.',
                'default': False
            },
            {
                'id': 'priv_smartscreen',
                'name': 'Desativar SmartScreen',
                'help': 'Reduz a proteção contra malware. ATENÇÃO.',
                'default': False
            }
        ],
        'cat_ui': [
            {
                'id': 'ui_animation',
                'name': 'Desativar Animações de Janelas',
                'help': 'Janelas fecham e abrem instantaneamente.',
                'default': False
            },
            {
                'id': 'ui_transparency',
                'name': 'Desativar Transparência',
                'help': 'Remove efeitos Mica/Acrylic. Libera a GPU.',
                'default': False
            },
            {
                'id': 'ui_shadows',
                'name': 'Remover Sombras',
                'help': 'Elimina as sombras das janelas e do cursor.',
                'default': False
            },
            {
                'id': 'ui_show_ext',
                'name': 'Mostrar Extensões de Arquivos',
                'help': 'Mostra .exe .jpg etc. Útil para segurança.',
                'default': False
            },
            {
                'id': 'ui_show_hidden',
                'name': 'Mostrar Arquivos Ocultos',
                'help': 'Mostra AppData e pastas ocultas.',
                'default': False
            },
            {
                'id': 'ui_classic_menu',
                'name': 'Menu de Contexto Clássico (Win11)',
                'help': 'Mostra o menu completo sem cliques extras no Win11.',
                'default': False
            },
            {
                'id': 'ui_darkmode',
                'name': 'Forçar Modo Escuro',
                'help': 'Aplica modo escuro global aos aplicativos e ao sistema.',
                'default': False
            },
            {
                'id': 'ui_startup_delay',
                'name': 'Remover Atraso na Inicialização',
                'help': 'Elimina o atraso de 10s imposto pelo Windows ao carregar apps.',
                'default': False
            },
            {
                'id': 'ui_taskbar_search',
                'name': 'Ocultar Barra de Pesquisa',
                'help': 'Remove ou minimiza a barra de pesquisa.',
                'default': False
            },
            {
                'id': 'ui_edge_tabs',
                'name': 'Ocultar Abas do Edge no Alt+Tab',
                'help': 'Evita a desordem do Alt+Tab com as abas do Edge.',
                'default': False
            },
            {
                'id': 'ui_lockscreen',
                'name': 'Desativar Tela de Bloqueio',
                'help': 'Vai direto para a senha sem precisar deslizar.',
                'default': False
            },
            {
                'id': 'ui_blur_lock',
                'name': 'Remover Desfoque de Login',
                'help': 'Remover o efeito de desfoque na tela de login.',
                'default': False
            },
            {
                'id': 'ui_actioncenter',
                'name': 'Desativar Central de Notificações',
                'help': 'Remove o painel lateral de notificações.',
                'default': False
            },
            {
                'id': 'ui_snap',
                'name': 'Desativar Assistente de Ajuste',
                'help': 'Impede as sugestões ao arrastar janelas.',
                'default': False
            },
            {
                'id': 'ui_shake',
                'name': 'Desativar Aero Shake',
                'help': 'Impede de minimizar janelas ao sacudir uma.',
                'default': False
            },
            {
                'id': 'ui_balloon',
                'name': 'Desativar Balões de Ajuda',
                'help': 'Desativa pop-ups amarelos intrusivos.',
                'default': False
            },
            {
                'id': 'ui_taskbar_animations',
                'name': 'Desativar Animações da Barra de Tarefas',
                'help': 'Movimentos de ícones instantâneos.',
                'default': False
            },
            {
                'id': 'ui_cursor_shadow',
                'name': 'Desativar Sombra do Cursor',
                'help': 'Remove a sombra sutil sob o ponteiro.',
                'default': False
            }
        ],
        'cat_net': [
            {
                'id': 'net_extreme_tcp',
                'name': 'Otimizador TCP Extremo (BBR)',
                'help': 'Algoritmos modernos BBR/CUBIC e desativa moderação de interrupções.',
                'default': False
            },
            {
                'id': 'net_autotuning',
                'name': 'Auto-Tuning TCP Normal',
                'help': 'Otimiza como o Windows gerencia os pacotes. Melhora a latência.',
                'default': False
            },
            {
                'id': 'net_nagles',
                'name': 'Desativar Algoritmo de Nagle',
                'help': 'Envia os pacotes mais rápido. Reduz latência em MMOs.',
                'default': False
            },
            {
                'id': 'net_rss',
                'name': 'Ativar Receive-Side Scaling',
                'help': 'Distribui o processamento de rede por vários núcleos.',
                'default': False
            },
            {
                'id': 'net_qos',
                'name': 'Remover Limite de Banda QoS',
                'help': 'Libera os 20% de internet reservados pelo Windows.',
                'default': False
            },
            {
                'id': 'net_deliveryopt',
                'name': 'Desativar Otimização de Entrega P2P',
                'help': 'Impede o Windows de fazer upload de atualizações para a Internet.',
                'default': False
            },
            {
                'id': 'net_wifi_power',
                'name': 'Desativar Economia de Energia WiFi',
                'help': 'Impede desconexões temporárias em notebooks.',
                'default': False
            },
            {
                'id': 'net_ecn',
                'name': 'Desativar ECN',
                'help': 'O ECN às vezes causa lag em jogos. Desativar estabiliza o ping.',
                'default': False
            },
            {
                'id': 'net_heuristics',
                'name': 'Desativar Heurísticas TCP',
                'help': 'Impede o Windows de limitar a janela TCP.',
                'default': False
            },
            {
                'id': 'net_lso',
                'name': 'Desativar Large Send Offload',
                'help': 'O LSO causa picos de ping em placas Intel/Realtek.',
                'default': False
            },
            {
                'id': 'net_chimney',
                'name': 'Desativar TCP Chimney',
                'help': 'Pode causar instabilidade em roteadores modernos.',
                'default': False
            },
            {
                'id': 'net_ipv6',
                'name': 'Desativar IPv6',
                'help': 'Às vezes causa lag local. Use com precaução.',
                'default': False
            },
            {
                'id': 'net_dnscache',
                'name': 'Evitar Cache DNS Negativo',
                'help': 'Impede de salvar falhas temporárias de conexão.',
                'default': False
            },
            {
                'id': 'net_smb',
                'name': 'Desativar SMBv1',
                'help': 'Protocolo inseguro (WannaCry). Fecha uma brecha gigante.',
                'default': False
            },
            {
                'id': 'net_teredo',
                'name': 'Desativar Tunelamento Teredo',
                'help': 'Transição IPv6 que causa overhead.',
                'default': False
            },
            {
                'id': 'net_isatap',
                'name': 'Desativar ISATAP',
                'help': 'Outro túnel IPv6-IPv4 com overhead de ping.',
                'default': False
            },
            {
                'id': 'net_netbios',
                'name': 'Desativar NetBIOS sobre TCP',
                'help': 'Não use se você compartilha impressoras na rede local.',
                'default': False
            },
            {
                'id': 'net_wpad',
                'name': 'Desativar Autodescoberta WPAD',
                'help': 'Acelera o DNS e bloqueia um vetor de ataque.',
                'default': False
            },
            {
                'id': 'net_tcp_1323',
                'name': 'Ativar Timestamps RFC 1323',
                'help': 'Melhora a confiabilidade em transferências grandes.',
                'default': False
            },
            {
                'id': 'net_max_conn',
                'name': 'Conexões Máx 10 (HTTP 1.0)',
                'help': 'Acelera o carregamento simultâneo de páginas web.',
                'default': False
            },
            {
                'id': 'net_max_conn11',
                'name': 'Conexões Máx 10 (HTTP 1.1)',
                'help': 'Acelera carregamentos web HTTP 1.1.',
                'default': False
            },
            {
                'id': 'net_dns_cloudflare',
                'name': 'Definir DNS Cloudflare (1.1.1.1)',
                'help': 'Configura o DNS mais rápido do mundo pela Cloudflare.',
                'default': False
            },
            {
                'id': 'net_dns_google',
                'name': 'Definir DNS Google (8.8.8.8)',
                'help': 'Configura o DNS do Google, rápido e confiável.',
                'default': False
            }
        ],
        'cat_gaming': [
            {
                'id': 'game_mode',
                'name': 'Ativar Modo de Jogo Windows',
                'help': 'Prioriza o acesso do jogo à CPU/GPU.',
                'default': False
            },
            {
                'id': 'game_process_priority',
                'name': 'Elevação Automática de Prioridade (Booster)',
                'help': 'Força prioridade "Alta" em tempo real para os processos de shooters competitivos.',
                'default': False
            },
            {
                'id': 'game_process_lasso',
                'name': 'Game Booster Ativo',
                'help': 'Emula o Process Lasso. Aumenta a prioridade da CPU ao abrir jogos.',
                'default': False
            },
            {
                'id': 'game_timer_res',
                'name': 'Resolução do Timer 0.5ms',
                'help': 'Ajusta BCDEDIT para um tickrate Windows de alta precisão.',
                'default': False
            },
            {
                'id': 'game_mouse_accel',
                'name': 'Desativar Aceleração do Mouse',
                'help': 'Entrada real 1:1. Essencial para shooters competitivos.',
                'default': False
            },
            {
                'id': 'game_ultimate_power',
                'name': 'Ativar Desempenho Máximo',
                'help': 'Desbloqueia o plano de energia oculto do Windows.',
                'default': False
            },
            {
                'id': 'game_msi_mode',
                'name': 'Hardware Latency Killer (MSI)',
                'help': 'Força GPU/Rede/USB a usarem interrupções MSI.',
                'default': False
            },
            {
                'id': 'game_hags',
                'name': 'Ativar Agendamento de GPU Turbo HW',
                'help': 'Boost de FPS em DX12. Requer reinicialização.',
                'default': False
            },
            {
                'id': 'game_mmcss',
                'name': 'Otimizar MMCSS',
                'help': 'Direciona NetworkThrottlingIndex e a GPU para o jogo.',
                'default': False
            },
            {
                'id': 'game_fullscreen_opt',
                'name': 'Desativar Otimizações de Tela Inteira',
                'help': 'Evita a falsa tela cheia com input lag.',
                'default': False
            },
            {
                'id': 'game_edge_bg',
                'name': 'Matar Edge em Segundo Plano',
                'help': 'Mata os processos msedge.exe que devoram 500 MB de RAM.',
                'default': False
            },
            {
                'id': 'game_chrome_bg',
                'name': 'Matar Chrome em Segundo Plano',
                'help': 'Elimina a flag para aplicativos Chrome em segundo plano.',
                'default': False
            },
            {
                'id': 'game_steam_hardware',
                'name': 'Desativar Aceleração HW Steam',
                'help': 'Impede a Steam de consumir GPU em segundo plano.',
                'default': False
            },
            {
                'id': 'game_discord_hw',
                'name': 'Desativar Aceleração HW Discord',
                'help': 'Se o GPU estiver em 99%, desativar evita travamentos.',
                'default': False
            },
            {
                'id': 'game_vr',
                'name': 'Responsividade do Sistema (VR/Gaming)',
                'help': 'Define SystemResponsiveness para 0. Mais ciclos de CPU para o jogo.',
                'default': False
            },
            {
                'id': 'game_fth',
                'name': 'Desativar Fault Tolerant Heap',
                'help': 'Impede a degradação do jogo ao sofrer crash.',
                'default': False
            },
            {
                'id': 'game_hpet',
                'name': 'Desativar HPET',
                'help': 'Reduz o input lag massivo em CPUs antigas ou Ryzen gen1.',
                'default': False
            },
            {
                'id': 'game_xbox_dvr',
                'name': 'Eliminar Regitros do Xbox DVR',
                'help': 'Exclui capturas ocultas. Aumenta o FPS mínimo em DX12.',
                'default': False
            },
            {
                'id': 'game_core_parking',
                'name': 'Desativar Estacionamento de Núcleos',
                'help': 'Impede o Windows de desligar os núcleos da CPU.',
                'default': False
            },
            {
                'id': 'game_vbs',
                'name': 'Desativar VBS',
                'help': '10% de overhead em jogos. Somente se o seu foco for 100% jogos.',
                'default': False
            },
            {
                'id': 'perf_win32_priority',
                'name': 'Win32PrioritySeparation 26',
                'help': 'Otimiza a prioridade da CPU para janelas em foco (JOGOS).',
                'default': False
            },
            {
                'id': 'perf_large_cache',
                'name': 'Large System Cache',
                'help': 'Melhora o desempenho de arquivos usando mais RAM.',
                'default': False
            },
            {
                'id': 'perf_io_limit',
                'name': 'Subir Limite de Bloqueio de Páginas de IO',
                'help': 'Acelera as transferências de arquivos pesados.',
                'default': False
            },
            {
                'id': 'perf_wait_kill',
                'name': 'Matar Serviços Rápido (2s)',
                'help': 'Reduz o tempo de espera antes de encerrar serviços.',
                'default': False
            },
            {
                'id': 'perf_auto_end',
                'name': 'Fechamento Auto de Apps Bloqueados ao Sair',
                'help': 'Força o encerramento de processos travados ao desligar.',
                'default': False
            },
            {
                'id': 'perf_menu_delay',
                'name': 'Atraso de Exibição de Menu a Zero',
                'help': 'Os menus aparecem instantaneamente.',
                'default': False
            },
            {
                'id': 'perf_startup_delay',
                'name': 'Remover Atraso Total de Inicialização',
                'help': 'Lança os apps de fundo sem tempo de espera artificial.',
                'default': False
            }
        ],
        'cat_power': [
            {
                'id': 'pwr_ultimate',
                'name': 'Forçar Desempenho Máximo',
                'help': 'Nível máximo de energia. Desativa qualquer economia de CPU.',
                'default': False
            },
            {
                'id': 'pwr_min_cpu',
                'name': 'CPU Mínimo 100%',
                'help': 'Impede o processador de baixar a frequência.',
                'default': False
            },
            {
                'id': 'pwr_throttling',
                'name': 'Desativar Power Throttling',
                'help': 'Impede o Windows de limitar o Discord e aplicativos em segundo plano.',
                'default': False
            },
            {
                'id': 'pwr_cpu_boost',
                'name': 'Sempre Ativar Turbo Boost da CPU',
                'help': 'Mantém o turbo boost ativo mesmo na bateria.',
                'default': False
            },
            {
                'id': 'pwr_pci_link',
                'name': 'Desativar PCIe Link State Power Mgmt',
                'help': 'Impede a GPU de entrar em estados de baixo consumo.',
                'default': False
            },
            {
                'id': 'pwr_hibernation',
                'name': 'Desativar Hibernação',
                'help': 'Libera gigabytes em C: e reduz o desgaste do SSD.',
                'default': False
            },
            {
                'id': 'pwr_disk_timeout',
                'name': 'Desativar Timeout do HDD',
                'help': 'Impede que HDDs se desliguem causando travamentos.',
                'default': False
            },
            {
                'id': 'pwr_adaptive_brightness',
                'name': 'Desativar Brilho Adaptativo',
                'help': 'Impede o sensor de ajustar o brilho automaticamente.',
                'default': False
            },
            {
                'id': 'pwr_usb_hub_suspend',
                'name': 'Desativar Suspensão Seletiva de Hub USB',
                'help': 'Complemento ao Gaming USB Suspend. Mais estável.',
                'default': False
            }
        ],
        'cat_gpu': [
            {
                'id': 'gpu_hags',
                'name': 'Ativar HAGS (Agendamento GPU hw)',
                'help': 'Move a fila de frames da CPU para a GPU. Melhora FPS em DX12/Vulkan.',
                'default': False
            },
            {
                'id': 'gpu_mpo',
                'name': 'Desativar MPO',
                'help': 'O MPO causa telas pretas e travamentos. Nvidia recomenda desativar.',
                'default': False
            },
            {
                'id': 'gpu_preemption',
                'name': 'Desativar Preemptividade de GPU',
                'help': 'Impede interrupções no meio do frame. Elimina micro-travamentos.',
                'default': False
            },
            {
                'id': 'gpu_reduce_dpc',
                'name': 'Reduzir Latência DPC da GPU',
                'help': 'Ajusta interrupções do driver de GPU para minimizar latência DPC.',
                'default': False
            },
            {
                'id': 'gpu_dwm_priority',
                'name': 'Prioridade DWM Alta',
                'help': 'Aumenta prioridade do dwm.exe para renderização mais fluida.',
                'default': False
            },
            {
                'id': 'gpu_gpu_priority',
                'name': 'Prioridade GPU 8 (MMCSS)',
                'help': 'Ajusta GpuPriority para dar mais prioridade ao processo gamer.',
                'default': False
            },
            {
                'id': 'gpu_perf_registry',
                'name': 'Otimizar Registro GPU MMCSS',
                'help': 'Ajusta NetworkThrottlingIndex e SystemResponsiveness para a GPU.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_power',
                'name': 'NVIDIA: Desempenho Máximo',
                'help': 'Força Desempenho Máximo no painel NVIDIA via registro.',
                'default': False
            },
            {
                'id': 'gpu_nvidia_telemetry',
                'name': 'Desativar Telemetria NVIDIA',
                'help': 'Para tarefas de telemetria da NVIDIA em segundo plano.',
                'default': False
            },
            {
                'id': 'gpu_amd_power',
                'name': 'AMD: Sem Economia de Energia GPU',
                'help': 'Impede a GPU AMD de entrar em estados de baixa frequência.',
                'default': False
            },
            {
                'id': 'gpu_amd_telemetry',
                'name': 'Desativar Telemetria AMD',
                'help': 'Para os serviços de telemetria da AMD em segundo plano.',
                'default': False
            },
            {
                'id': 'gpu_pci_express_max',
                'name': 'Modo PCIe GPU Máximo',
                'help': 'Desativa Link State Power Management especificamente para a GPU.',
                'default': False
            },
            {
                'id': 'gpu_disable_fullscreen_opt',
                'name': 'Desativar Otimizações Tela Cheia Global',
                'help': 'Força tela cheia exclusiva real em todos os jogos.',
                'default': False
            },
            {
                'id': 'gpu_freesync_vsync_off',
                'name': 'Desativar V-Sync Global',
                'help': 'Desativa V-Sync por padrão em todos os apps via registro.',
                'default': False
            },
            {
                'id': 'gpu_cache_clean',
                'name': 'Limpar Cache de Shaders GPU',
                'help': 'Apaga cache de shaders acumulado. Útil se houver travas ao entrar em áreas.',
                'default': False
            },
            {
                'id': 'gpu_vram_paging',
                'name': 'Otimizar Paginação VRAM',
                'help': 'Usa RAM do sistema como extensão para GPUs com pouca VRAM.',
                'default': False
            },
            {
                'id': 'gpu_shader_cache',
                'name': 'Redirecionar Cache Shader p/ SSD Rápido',
                'help': 'Configura cache de shaders para leitura rápida em NVMe.',
                'default': False
            },
            {
                'id': 'gpu_disable_mpv',
                'name': 'Desativar Precomp. Background DX12/Vulkan',
                'help': 'Impede a pré-compilação de shaders enquanto você joga.',
                'default': False
            },
            {
                'id': 'gpu_gsync_compat',
                'name': 'G-Sync em Monitores FreeSync',
                'help': 'Força compatibilidade G-Sync em monitores AMD com GPU Nvidia.',
                'default': False
            },
            {
                'id': 'gpu_night_light_off',
                'name': 'Desativar Luz Noturna',
                'help': 'Impede o Windows de alterar a calibração de cor do monitor.',
                'default': False
            }
        ],
        'cat_kernel': [
            {
                'id': 'ext_57_processes',
                'name': 'Consolidação de Serviços do Sistema (Processos Mínimos)',
                'help': 'Redireciona svchost e desativa serviços não críticos para reduzir o total de processos ativos ao mínimo operacional.',
                'default': False
            },
            {
                'id': 'kern_registry_size',
                'name': 'Aumentar Tamanho Máx do Registro',
                'help': 'Previne erros de limite de registro em sistemas personalizados.',
                'default': False
            },
            {
                'id': 'kern_bcdedit_inc',
                'name': 'Frequência de Interrupção BCDEDIT',
                'help': 'Aumenta a precisão do relógio via BCDEDIT. Chave para timer < 1ms.',
                'default': False
            },
            {
                'id': 'kern_memory_comp',
                'name': 'Desativar Compressão de Memória (MMAgent)',
                'help': 'Impede a CPU de perder ciclos comprimindo páginas RAM, priorizando a latência.',
                'default': False
            },
            {
                'id': 'kern_system_resp',
                'name': 'SystemResponsiveness a 0% (Tempo Real)',
                'help': 'Remove a reserva de recursos de fundo do Windows para dedicar 100% ao processo focado.',
                'default': False
            },
            {
                'id': 'kernel_mitigations',
                'name': 'Desativar Mitigações de CPU',
                'help': 'Desativa Spectre/Meltdown. +5-15% CPU pura. Reduz segurança.',
                'default': False
            },
            {
                'id': 'kern_large_pages',
                'name': 'Ativar Large Pages (Memória Virtual)',
                'help': 'Reduz page faults (TLB misses) em aplicações com alta carga de memória.',
                'default': False
            },
            {
                'id': 'kern_iot_core',
                'name': 'Ajuste de Perfil Embedded Minimalista',
                'help': 'Ajusta parâmetros internos do sistema para se comportar como um perfil Windows IoT de baixos recursos.',
                'default': False
            },
            {
                'id': 'kern_process_isolation',
                'name': 'Desativar Isolamento de Processos Core',
                'help': 'Reduz o overhead de virtualização do kernel para maximizar a velocidade das threads.',
                'default': False
            }
        ],
        'cat_extreme': [
            {
                'id': 'ext_super_nuclear',
                'name': 'Limpeza Massiva de Serviços de Sistema',
                'help': 'Desativa todos os serviços não essenciais de rede, impressão e visuais. Irreversível sem restauração.',
                'default': False
            },
            {
                'id': 'ext_minimalist',
                'name': 'Perfil Shell Reduzido de Alta Performance',
                'help': 'Desativa os efeitos visuais do Shell do Windows para liberar totalmente os ciclos de CPU e GPU.',
                'default': False
            },
            {
                'id': 'ext_defender_kill',
                'name': 'Desativação Permanente Windows Defender',
                'help': 'Remove o motor de varredura e os serviços de segurança nativos via registro/GPO.',
                'default': False
            },
            {
                'id': 'ext_uwp_kill_all',
                'name': 'Remoção Completa de Apps UWP Integrados',
                'help': 'Desinstala todos os apps UWP pré-instalados para todos os usuários do sistema.',
                'default': False
            },
            {
                'id': 'ext_firewall_off',
                'name': 'Desativar Firewall Windows (Stack Bypass)',
                'help': 'Desativa a filtragem nativa de pacotes para minimizar a latência de rede.',
                'default': False
            },
            {
                'id': 'ext_update_dead',
                'name': 'Bloqueio do Windows Update (Política LTSC)',
                'help': 'Impede qualquer tentativa de atualização ou download de driver pelo sistema operacional.',
                'default': False
            }
        ],
        'cat_util': [
            {
                'id': 'util_dotnet',
                'name': 'Instalar Runtimes .NET',
                'help': 'Garante compatibilidade com todas as versões dos frameworks de aplicativos.',
                'default': False
            },
            {
                'id': 'util_vc_redist',
                'name': 'Instalar Redistribuíveis C++',
                'help': 'Instala todas as bibliotecas necessárias para rodar jogos e softwares.',
                'default': False
            },
            {
                'id': 'util_directx',
                'name': 'Atualizar Runtimes DirectX',
                'help': 'Instala componentes legados do DirectX para jogos antigos.',
                'default': False
            },
            {
                'id': 'util_powershell_7',
                'name': 'Instalar PowerShell 7',
                'help': 'Instala a versão moderna e mais rápida do motor de scripts do Windows.',
                'default': False
            },
            {
                'id': 'util_driver_updates',
                'name': 'Excluir Atualizações de Drivers',
                'help': 'Impede o Windows de sobrescrever seus drivers personalizados com versões genéricas.',
                'default': False
            },
            {
                'id': 'util_ps_telemetry',
                'name': 'Desativar Telemetria PowerShell',
                'help': 'Remove os relatórios de uso no terminal moderno do Windows.',
                'default': False
            },
            {
                'id': 'util_end_task_rc',
                'name': 'Finalizar Tarefa na Barra de Tarefas',
                'help': 'Adiciona a opção de fechar processos diretamente com o botão direito na barra de tarefas.',
                'default': False
            },
            {
                'id': 'util_start_recommendations',
                'name': 'Remover Recomendações do Iniciar',
                'help': 'Limpa a seção de arquivos recentes e apps sugeridos no Iniciar.',
                'default': False
            },
            {
                'id': 'util_sticky_keys',
                'name': 'Desativar Teclas de Aderência',
                'help': 'Impede o sistema de perguntar sobre as teclas de aderência após apertar Shift várias vezes.',
                'default': False
            },
            {
                'id': 'util_taskbar_center',
                'name': 'Barra de Tarefas: Alinhar à Esquerda',
                'help': 'Restaura a posição clássica dos ícones no desktop do Windows 11.',
                'default': False
            },
            {
                'id': 'util_settings_home',
                'name': 'Remover Home Page de Configurações',
                'help': "Remove a tela 'Início' inútil ao abrir as configurações do Windows.",
                'default': False
            },
            {
                'id': 'util_new_outlook',
                'name': 'Bloquear Novo Outlook',
                'help': 'Impede o Windows de substituir o cliente de e-mail clássico pela versão web-app.',
                'default': False
            },
            {
                'id': 'util_cross_device',
                'name': 'Desativar Exp. Entre Dispositivos',
                'help': 'Desativa a sincronização de tarefas inacabadas com outros PCs ou celulares.',
                'default': False
            },
            {
                'id': 'util_task_view',
                'name': 'Ocultar Visão de Tarefas',
                'help': 'Limpa a barra de tarefas removendo o ícone de áreas de trabalho virtuais.',
                'default': False
            },
            {
                'id': 'util_folder_discovery',
                'name': 'Desligar Descoberta Auto de Pasta',
                'help': 'Impede o Explorer de mudar o tipo de visualização ao abrir pastas com imagens ou música.',
                'default': False
            },
            {
                'id': 'util_bsod_detail',
                'name': 'BSOD com Info Detalhada',
                'help': 'Mostra parâmetros completos e códigos de erro na tela azul da morte.',
                'default': False
            },
            {
                'id': 'util_numlock',
                'name': 'Ativar NumLock ao Iniciar',
                'help': 'Ativa automaticamente o NumLock ao fazer login no Windows.',
                'default': False
            },
            {
                'id': 'util_verbose_logon',
                'name': 'Mensagens de Logon Detalhadas',
                'help': 'Mostra o status de cada serviço durante o logon e logoff.',
                'default': False
            },
            {
                'id': 'util_consumer_features',
                'name': 'Desativar Sugestões Apps da Loja',
                'help': 'Impede a instalação silenciosa de apps promocionais da Microsoft.',
                'default': False
            },
            {
                'id': 'util_wpbt',
                'name': 'Bloquear Injeção Bloatware (WPBT)',
                'help': 'Impede fabricantes de instalarem softwares via BIOS ao iniciar o Windows.',
                'default': False
            },
            {
                'id': 'util_widgets_remove',
                'name': 'Remover Widgets Windows 11',
                'help': 'Desinstala o painel de widgets e notícias da barra de tarefas.',
                'default': False
            },
            {
                'id': 'uwp_xbox',
                'name': 'Remover Apps Xbox',
                'help': 'Deleta todos os apps Xbox (GameBar, TCUI). NÃO USE SE VOCÊ JOGA NO PC GAME PASS.',
                'default': False
            },
            {
                'id': 'uwp_bloatware',
                'name': 'Remover Bloatwares Nativos',
                'help': 'Deleta apps lixo: Zune, BingNews, GetHelp, Solitaire, People...',
                'default': False
            },
            {
                'id': 'uwp_onedrive',
                'name': 'Desinstalar OneDrive',
                'help': 'Desinstala profundamente o Microsoft OneDrive do sistema.',
                'default': False
            },
            {
                'id': 'uwp_edge',
                'name': 'Remover Edge (Avançado)',
                'help': 'Tenta remover o Microsoft Edge com PowerShell. Tenha outro navegador pronto.',
                'default': False
            },
            {
                'id': 'uwp_3dbuilder',
                'name': 'Remover 3D Builder',
                'help': 'Desinstala o app de modelagem 3D da Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_alarms',
                'name': 'Remover Alarmes e Relógio',
                'help': 'Desinstala o app de alarmes e cronômetro.',
                'default': False
            },
            {
                'id': 'uwp_camera',
                'name': 'Remover Câmera',
                'help': 'Desinstala o app de câmera da Loja.',
                'default': False
            },
            {
                'id': 'uwp_communications',
                'name': 'Remover Email e Calendário',
                'help': 'Desinstala os apps integrados de email e calendário.',
                'default': False
            },
            {
                'id': 'uwp_feedback',
                'name': 'Remover Hub de Feedback',
                'help': 'Desinstala o app de feedback da Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_gethelp',
                'name': 'Remover Obter Ajuda',
                'help': 'Desinstala o app de suporte técnico da Microsoft.',
                'default': False
            },
            {
                'id': 'uwp_maps',
                'name': 'Remover Mapas',
                'help': 'Desinstala o app de mapas integrado.',
                'default': False
            },
            {
                'id': 'uwp_mixedreality',
                'name': 'Remover Portal Realidade Mista',
                'help': 'Desinstala o portal de realidade mista.',
                'default': False
            },
            {
                'id': 'uwp_people',
                'name': 'Remover Pessoas (People)',
                'help': 'Desinstala o app de contatos integrado.',
                'default': False
            },
            {
                'id': 'uwp_photos',
                'name': 'Remover Fotos',
                'help': 'Desinstala o app Fotos moderno (substituível pelo visualizador clássico).',
                'default': False
            },
            {
                'id': 'uwp_skype',
                'name': 'Remover Skype',
                'help': 'Desinstala o app do Skype pré-instalado.',
                'default': False
            },
            {
                'id': 'uwp_solitaire',
                'name': 'Remover Solitaire',
                'help': 'Desinstala os jogos de paciência pré-instalados.',
                'default': False
            },
            {
                'id': 'uwp_soundrecorder',
                'name': 'Remover Gravador de Voz',
                'help': 'Desinstala o app de gravação de áudio.',
                'default': False
            },
            {
                'id': 'uwp_stickynotes',
                'name': 'Remover Sticky Notes',
                'help': 'Desinstala o app de notas adesivas.',
                'default': False
            },
            {
                'id': 'uwp_weather',
                'name': 'Remover Clima',
                'help': 'Desinstala o app de clima.',
                'default': False
            },
            {
                'id': 'uwp_yourphone',
                'name': 'Remover Seu Telefone',
                'help': 'Desinstala o app de conexão com o celular.',
                'default': False
            }
        ],
        'cat_pro': [
            {
                'id': 'util_context_compact',
                'name': 'Ativar Menus de Contexto Compactos',
                'help': 'Reduz o preenchimento e espaço entre opções dos menus de clique direito.',
                'default': False
            },
            {
                'id': 'util_legacy_photo',
                'name': 'Restaurar Visualizador de Fotos Clássico (Win7)',
                'help': 'Ativa o visualizador de imagens ultra rápido e leve das versões anteriores.',
                'default': False
            },
            {
                'id': 'util_legacy_calc',
                'name': 'Restaurar Calculadora Clássica Win32',
                'help': 'Substitui a versão UWP lenta pela versão executável tradicional.',
                'default': False
            },
            {
                'id': 'util_god_mode',
                'name': 'Acesso Unificado ao Painel de Controle',
                'help': 'Cria um atalho para todos os ajustes administrativos do sistema em uma única janela.',
                'default': False
            },
            {
                'id': 'util_verbose_boot',
                'name': 'Ativar Histórico de Boot Detalhado',
                'help': 'Exibe os drivers e serviços carregados durante o boot na tela.',
                'default': False
            },
            {
                'id': 'util_desktop_labels',
                'name': 'Remover Setas de Atalho',
                'help': 'Limpa ícones do desktop eliminando a seta de atalho.',
                'default': False
            },
            {
                'id': 'util_explorer_pc',
                'name': "Abrir Explorer em 'Este Computador'",
                'help': 'Configura o explorador para pular a vista de arquivos recentes por padrão.',
                'default': False
            }
        ],
        'cat_help': []
    }
