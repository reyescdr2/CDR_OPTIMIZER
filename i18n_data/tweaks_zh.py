# type: ignore
def get_tweaks_zh():
    return {
        'cat_system': [
            {
                'id': 'svc_diagtrack',
                'name': '禁用遥测',
                'help': '禁用 DiagTrack。释放后台进程。',
                'default': False
            },
            {
                'id': 'svc_sysmain',
                'name': '禁用 SysMain',
                'help': '在 RAM 中预加载应用。如果使用 SSD，请禁用。',
                'default': False
            },
            {
                'id': 'svc_wsearch',
                'name': '禁用 Windows Search',
                'help': '防止持续索引。强烈建议 SSD 用户开启。',
                'default': False
            },
            {
                'id': 'svc_wuauserv_manual',
                'name': '手动 Windows 更新',
                'help': '防止在游戏期间下载更新。',
                'default': False
            },
            {
                'id': 'ai_copilot',
                'name': '阻止 Windows Copilot',
                'help': '在 GPO 级别禁用 Copilot AI。',
                'default': False
            },
            {
                'id': 'ai_recall',
                'name': '禁用 Windows Recall',
                'help': '禁用 Windows Recall (AI) 的持续截屏。',
                'default': False
            },
            {
                'id': 'svc_bcastdvr',
                'name': '禁用 Game DVR',
                'help': '防止后台录制屏幕。提高 FPS。',
                'default': False
            },
            {
                'id': 'svc_wer',
                'name': '禁用 Windows 错误报告',
                'help': '微软的错误收集系统。',
                'default': False
            },
            {
                'id': 'svc_dps',
                'name': '禁用诊断执行',
                'help': '消耗资源以诊断静默故障。',
                'default': False
            },
            {
                'id': 'svc_pcasvc',
                'name': '禁用程序兼容性助手',
                'help': '监视旧版应用，可能导致微卡顿。',
                'default': False
            },
            {
                'id': 'svc_remoteregistry',
                'name': '禁用远程注册表',
                'help': '防止远程用户修改您的注册表。',
                'default': False
            },
            {
                'id': 'svc_tabletinputservice',
                'name': '禁用触摸键盘',
                'help': '如果不使用触摸屏，请禁用。',
                'default': False
            },
            {
                'id': 'svc_wbio_srvc',
                'name': '禁用生物识别',
                'help': '如果不使用指纹或面部识别 (Face ID)，请禁用。',
                'default': False
            },
            {
                'id': 'svc_bits',
                'name': '禁用 BITS',
                'help': '用于 Update/Store 的后台传输。',
                'default': False
            },
            {
                'id': 'svc_defrag_svc',
                'name': '禁用自动碎片整理',
                'help': '禁用自动碎片整理，以便手动控制 SSD trim。',
                'default': False
            }
        ],
        'cat_clean': [
            {
                'id': 'clean_ram',
                'name': '优化 RAM (清理工作集)',
                'help': '强制减少缓存和后台应用，由于立即释放 RAM。',
                'default': False
            },
            {
                'id': 'clean_temp',
                'name': '清理临时文件夹',
                'help': '删除应用程序的临时文件。',
                'default': False
            },
            {
                'id': 'clean_prefetch',
                'name': '清理 Prefetch',
                'help': '删除预取 (prefetch) 文件。',
                'default': False
            },
            {
                'id': 'clean_winupdate',
                'name': '清理 Windows 更新缓存',
                'help': '删除旧更新残留的安装文件。',
                'default': False
            },
            {
                'id': 'clean_recycle',
                'name': '清空回收站',
                'help': '强制清空所有驱动器上的所有回收站。',
                'default': False
            },
            {
                'id': 'clean_dns',
                'name': '清理 DNS 缓存',
                'help': '通过更新网络路线修复缓慢的连接。',
                'default': False
            },
            {
                'id': 'clean_eventlog',
                'name': '清除事件查看器',
                'help': '删除所有 Windows 事件日志。',
                'default': False
            },
            {
                'id': 'clean_thumbcache',
                'name': '清理缩略图缓存',
                'help': '修复损坏的图像/视频图标。',
                'default': False
            },
            {
                'id': 'clean_fontcache',
                'name': '清理字体缓存',
                'help': '如果文本看起来模糊或渲染不正确，此项很有用。',
                'default': False
            },
            {
                'id': 'clean_iconcache',
                'name': '清理图标缓存',
                'help': '删除并重启系统图标缓存。',
                'default': False
            },
            {
                'id': 'clean_crashdumps',
                'name': '删除 BSOD 崩溃转储',
                'help': '删除蓝屏期间产生的大型文件。',
                'default': False
            },
            {
                'id': 'clean_chkdsk',
                'name': '删除 CheckDisk 残余物',
                'help': '删除磁盘修复后留下的 .chk 文件。',
                'default': False
            },
            {
                'id': 'clean_onedrive_temp',
                'name': '清理 OneDrive 缓存',
                'help': '删除 OneDrive 的日志和残留。',
                'default': False
            },
            {
                'id': 'clean_chrome_cache',
                'name': '清理 Chrome 缓存',
                'help': '删除 Google Chrome 缓存（不删除密码）。',
                'default': False
            },
            {
                'id': 'clean_edge_cache',
                'name': '清理 Edge 缓存',
                'help': '删除 Microsoft Edge 缓存。',
                'default': False
            },
            {
                'id': 'clean_firefox_cache',
                'name': '清理 Firefox 缓存',
                'help': '删除 Mozilla Firefox 缓存。',
                'default': False
            },
            {
                'id': 'clean_discord_cache',
                'name': '清理 Discord 缓存',
                'help': 'Discord 随时间会积累大量缓存。',
                'default': False
            },
            {
                'id': 'clean_steam_cache',
                'name': '清理 Steam 缓存',
                'help': 'Steam 浏览器积累的垃圾会导致其变慢。',
                'default': False
            },
            {
                'id': 'clean_epic_cache',
                'name': '清理 Epic Games 缓存',
                'help': '帮助 Epic Games Launcher 更快打开。',
                'default': False
            },
            {
                'id': 'clean_spotify_cache',
                'name': '清理 Spotify 缓存',
                'help': 'Spotify 会暂时存储数 GB 的音乐和封面。',
                'default': False
            },
            {
                'id': 'clean_vcredist',
                'name': '清理 Steam VCRedist',
                'help': '删除 Steam 游戏留下的安装程序。',
                'default': False
            },
            {
                'id': 'clean_usrdoc_temp',
                'name': '清理用户临时文档',
                'help': '删除配置文件文件夹中的临时文件。',
                'default': False
            },
            {
                'id': 'clean_system_logs',
                'name': '删除安装日志',
                'help': '删除 C:\\Windows 中的日志。',
                'default': False
            },
            {
                'id': 'clean_crypt_svc',
                'name': '重置 Crypto 缓存',
                'help': '恢复系统数据库中的签名。',
                'default': False
            },
            {
                'id': 'clean_bits_queue',
                'name': '清理 BITS 队列',
                'help': '删除后台下载任务。',
                'default': False
            }
        ],
        'cat_privacy': [
            {
                'id': 'priv_telemetry_level',
                'name': '遥测级别 0',
                'help': '阻止几乎所有诊断数据的传输。',
                'default': False
            },
            {
                'id': 'priv_etw_disable',
                'name': '深度 ETW 遥测阻止',
                'help': '在内核级别禁用 AutoLogger 会话。',
                'default': False
            },
            {
                'id': 'priv_cortana',
                'name': '禁用 Cortana',
                'help': '释放 RAM 和持续监听进程。',
                'default': False
            },
            {
                'id': 'priv_start_web',
                'name': '禁用开始菜单 Web 搜索',
                'help': '仅限本地搜索。开始菜单超快。',
                'default': False
            },
            {
                'id': 'priv_news',
                'name': '禁用资讯和兴趣',
                'help': '从任务栏移除天气和资讯小部件。',
                'default': False
            },
            {
                'id': 'priv_location',
                'name': '禁用定位',
                'help': '防止 Windows 和应用访问您的位置。',
                'default': False
            },
            {
                'id': 'priv_mic',
                'name': '禁用键入建议',
                'help': '禁用发送您键入模式的预测功能。',
                'default': False
            },
            {
                'id': 'priv_feedback',
                'name': '反馈频率：从不',
                'help': '防止 Windows 不断询问反馈。',
                'default': False
            },
            {
                'id': 'priv_activity',
                'name': '禁用活动历史记录',
                'help': '防止 Windows 保存应用和文件的历史记录。',
                'default': False
            },
            {
                'id': 'priv_sync',
                'name': '禁用设置同步',
                'help': '防止背景和设置上传到云端。',
                'default': False
            },
            {
                'id': 'priv_advertising',
                'name': '禁用广告 ID',
                'help': '防止通过广告 ID 进行个性化广告。',
                'default': False
            },
            {
                'id': 'priv_appdiag',
                'name': '阻止应用诊断',
                'help': '防止应用访问其他应用的诊断信息。',
                'default': False
            },
            {
                'id': 'priv_tailored',
                'name': '禁用个性化体验',
                'help': '防止 MS 使用诊断数据提供个人内容。',
                'default': False
            },
            {
                'id': 'priv_ceip',
                'name': '退出 CEIP',
                'help': '退出微软改进计划。',
                'default': False
            },
            {
                'id': 'priv_handwriting',
                'name': '禁用手写学习',
                'help': '防止收集手写笔数据。',
                'default': False
            },
            {
                'id': 'priv_defender_samples',
                'name': '不发送 Defender 样本',
                'help': '防止 Defender 将文件上传到其服务器。',
                'default': False
            },
            {
                'id': 'priv_onedrive',
                'name': '启动时禁用 OneDrive',
                'help': '防止 OneDrive 随系统启动。',
                'default': False
            },
            {
                'id': 'priv_meetnow',
                'name': '隐藏 "立即开会"',
                'help': '从任务栏移除摄像头图标。',
                'default': False
            },
            {
                'id': 'priv_app_suggestions',
                'name': '禁用应用建议',
                'help': '防止 Windows 在开始菜单中建议应用。',
                'default': False
            },
            {
                'id': 'priv_smartscreen',
                'name': '禁用 SmartScreen',
                'help': '降低恶意软件防护。请注意。',
                'default': False
            }
        ],
        'cat_ui': [
            {
                'id': 'ui_animation',
                'name': '禁用窗口动画',
                'help': '窗口瞬间打开和关闭。',
                'default': False
            },
            {
                'id': 'ui_transparency',
                'name': '禁用透明效果',
                'help': '移除 Mica/Acrylic 效果。释放 GPU。',
                'default': False
            },
            {
                'id': 'ui_shadows',
                'name': '移除阴影',
                'help': '消除窗口和光标的阴影。',
                'default': False
            },
            {
                'id': 'ui_show_ext',
                'name': '显示文件扩展名',
                'help': '显示 .exe .jpg 等等。有利于安全。',
                'default': False
            },
            {
                'id': 'ui_show_hidden',
                'name': '显示隐藏文件',
                'help': '显示 AppData 和隐藏文件夹。',
                'default': False
            },
            {
                'id': 'ui_classic_menu',
                'name': '经典右键菜单 (Win11)',
                'help': 'Win11 中显示完整菜单，无需额外点击。',
                'default': False
            },
            {
                'id': 'ui_darkmode',
                'name': '强制深色模式',
                'help': '对应用和系统应用全局深色模式。',
                'default': False
            },
            {
                'id': 'ui_startup_delay',
                'name': '移除启动延迟',
                'help': '消除 Windows 在加载应用时强加的 10 秒延迟。',
                'default': False
            },
            {
                'id': 'ui_taskbar_search',
                'name': '隐藏搜索栏',
                'help': '移除或最小化搜索栏。',
                'default': False
            },
            {
                'id': 'ui_edge_tabs',
                'name': 'Alt+Tab 中隐藏 Edge 标签页',
                'help': '避免 Edge 标签页弄乱 Alt+Tab 切换。',
                'default': False
            },
            {
                'id': 'ui_lockscreen',
                'name': '禁用锁屏界面',
                'help': '直接进入密码输入界面，无需滑动。',
                'default': False
            },
            {
                'id': 'ui_blur_lock',
                'name': '移除登录界面模糊',
                'help': '移除登录界面的模糊效果。',
                'default': False
            },
            {
                'id': 'ui_actioncenter',
                'name': '禁用通知中心',
                'help': '移除侧边通知面板。',
                'default': False
            },
            {
                'id': 'ui_snap',
                'name': '禁用贴靠助手',
                'help': '拖动窗口时防止显示建议。',
                'default': False
            },
            {
                'id': 'ui_shake',
                'name': '禁用 Aero Shake',
                'help': '防止通过晃动窗口来最小化显示。',
                'default': False
            },
            {
                'id': 'ui_balloon',
                'name': '禁用气泡提示',
                'help': '禁用侵入性的黄色弹出提示。',
                'default': False
            },
            {
                'id': 'ui_taskbar_animations',
                'name': '禁用任务栏动画',
                'help': '图标动作瞬间完成。',
                'default': False
            },
            {
                'id': 'ui_cursor_shadow',
                'name': '禁用光标阴影',
                'help': '移除光标下的细微阴影。',
                'default': False
            }
        ],
        'cat_net': [
            {
                'id': 'net_extreme_tcp',
                'name': '极致 TCP 优化 (BBR)',
                'help': '现代 BBR/CUBIC 算法并禁用中断协调。',
                'default': False
            },
            {
                'id': 'net_autotuning',
                'name': '常规 TCP 自动调优',
                'help': '优化 Windows 处理数据包的方式。改善延迟。',
                'default': False
            },
            {
                'id': 'net_nagles',
                'name': '禁用 Nagle 算法',
                'help': '更快发送数据包。降低 MMO 游戏中的延迟。',
                'default': False
            },
            {
                'id': 'net_rss',
                'name': '启用接收端缩放 (RSS)',
                'help': '将网络处理分布到多个核心。',
                'default': False
            },
            {
                'id': 'net_qos',
                'name': '移除 QoS 带宽限制',
                'help': '释放 Windows 保留的 20% 因特网带宽。',
                'default': False
            },
            {
                'id': 'net_deliveryopt',
                'name': '禁用 P2P 传递优化',
                'help': '防止 Windows 向因特网上传更新。',
                'default': False
            },
            {
                'id': 'net_wifi_power',
                'name': '禁用 WiFi 节能方案',
                'help': '防止笔记本电脑上的临时断连。',
                'default': False
            },
            {
                'id': 'net_ecn',
                'name': '禁用 ECN',
                'help': 'ECN 有时会导致游戏延迟。禁用它可稳定延迟。',
                'default': False
            },
            {
                'id': 'net_heuristics',
                'name': '禁用 TCP 启发式',
                'help': '防止 Windows 限制 TCP 窗口。',
                'default': False
            },
            {
                'id': 'net_lso',
                'name': '禁用 Large Send Offload',
                'help': 'LSO 会导致 Intel/Realtek 网卡出现延迟峰值。',
                'default': False
            },
            {
                'id': 'net_chimney',
                'name': '禁用 TCP Chimney',
                'help': '可能导致现代路由器不稳定。',
                'default': False
            },
            {
                'id': 'net_ipv6',
                'name': '禁用 IPv6',
                'help': '有时会导致本地延迟。请谨慎使用。',
                'default': False
            },
            {
                'id': 'net_dnscache',
                'name': '避免负面 DNS 缓存',
                'help': '防止保存临时的连接失败记录。',
                'default': False
            },
            {
                'id': 'net_smb',
                'name': '禁用 SMBv1',
                'help': '不安全的协议 (WannaCry)。关闭巨大的安全漏洞。',
                'default': False
            },
            {
                'id': 'net_teredo',
                'name': '禁用 Teredo 隧道',
                'help': '会导致开销的 IPv6 过渡技术。',
                'default': False
            },
            {
                'id': 'net_isatap',
                'name': '禁用 ISATAP',
                'help': '另一个具有延迟开销的 IPv6-IPv4 隧道。',
                'default': False
            },
            {
                'id': 'net_netbios',
                'name': '禁用 TCP 上的 NetBIOS',
                'help': '如果您在局域网中共享打印机，请勿使用。',
                'default': False
            },
            {
                'id': 'net_wpad',
                'name': '禁用 WPAD 自动发现',
                'help': '加速 DNS 并阻止一种攻击途径。',
                'default': False
            },
            {
                'id': 'net_tcp_1323',
                'name': '启用 RFC 1323 时间戳',
                'help': '提高大型传输的可靠性。',
                'default': False
            },
            {
                'id': 'net_max_conn',
                'name': '最大连接数 10 (HTTP 1.0)',
                'help': '加速同时加载网页。',
                'default': False
            },
            {
                'id': 'net_max_conn11',
                'name': '最大连接数 10 (HTTP 1.1)',
                'help': '加速 HTTP 1.1 的网页加载。',
                'default': False
            },
            {
                'id': 'net_dns_cloudflare',
                'name': '设置 Cloudflare DNS (1.1.1.1)',
                'help': '配置 Cloudflare 提供的全球最快 DNS。',
                'default': False
            },
            {
                'id': 'net_dns_google',
                'name': '设置 Google DNS (8.8.8.8)',
                'help': '配置 Google DNS，快速且可靠。',
                'default': False
            }
        ],
        'cat_gaming': [
            {
                'id': 'game_mode',
                'name': '启用 Windows 游戏模式',
                'help': '优先保证游戏对 CPU/GPU 的访问。',
                'default': False
            },
            {
                'id': 'game_process_priority',
                'name': '自动提升优先级 (Booster)',
                'help': '为竞技射击类进程强制实时 "高" 优先级。',
                'default': False
            },
            {
                'id': 'game_process_lasso',
                'name': '激活 Game Booster',
                'help': '模拟 Process Lasso。打开游戏时增加 CPU 优先级。',
                'default': False
            },
            {
                'id': 'game_timer_res',
                'name': '计时器精度 0.5ms',
                'help': '通过 BCDEDIT 调整 Windows 以获得高精度时钟频率。',
                'default': False
            },
            {
                'id': 'game_mouse_accel',
                'name': '禁用鼠标加速',
                'help': '真正的 1:1 输入。竞技射击类游戏必选。',
                'default': False
            },
            {
                'id': 'game_ultimate_power',
                'name': '激活 "卓越性能" 方案',
                'help': '解锁隐藏的 Windows 电源方案。',
                'default': False
            },
            {
                'id': 'game_msi_mode',
                'name': '硬件延迟杀手 (MSI)',
                'help': '强制 GPU/网络/USB 使用 MSI 中断。',
                'default': False
            },
            {
                'id': 'game_hags',
                'name': '启用硬件加速 GPU 计划',
                'help': 'DX12 环境下提升 FPS。需要重启。',
                'default': False
            },
            {
                'id': 'game_mmcss',
                'name': '优化 MMCSS',
                'help': '将 NetworkThrottlingIndex 和 GPU 重定向至游戏。',
                'default': False
            },
            {
                'id': 'game_fullscreen_opt',
                'name': '禁用全屏优化',
                'help': '避免伪全屏带来的输入延迟。',
                'default': False
            },
            {
                'id': 'game_edge_bg',
                'name': '关闭后台 Edge 进程',
                'help': '关闭占用 500 MB RAM 的 msedge.exe 进程。',
                'default': False
            },
            {
                'id': 'game_chrome_bg',
                'name': '关闭后台 Chrome 进程',
                'help': '消除后台 Chrome 应用的标志。',
                'default': False
            },
            {
                'id': 'game_steam_hardware',
                'name': '禁用 Steam 硬件加速',
                'help': '防止 Steam 在后台消耗 GPU 资源。',
                'default': False
            },
            {
                'id': 'game_discord_hw',
                'name': '禁用 Discord 硬件加速',
                'help': '如果 GPU 占用为 99%，禁用此项可避免卡顿。',
                'default': False
            },
            {
                'id': 'game_vr',
                'name': '系统响应度 (VR/游戏)',
                'help': '将 SystemResponsiveness 设置为 0。给游戏更多 CPU 周期。',
                'default': False
            },
            {
                'id': 'game_fth',
                'name': '禁用容错堆 (FTH)',
                'help': '防止游戏崩溃时性能下降。',
                'default': False
            },
            {
                'id': 'game_hpet',
                'name': '禁用 HPET',
                'help': '减少旧款 CPU 或第一代 Ryzen 上的巨大输入延迟。',
                'default': False
            },
            {
                'id': 'game_xbox_dvr',
                'name': '删除 Xbox DVR 注册表键',
                'help': '删除隐藏的录制项。提升 DX12 中的最小 FPS。',
                'default': False
            },
            {
                'id': 'game_core_parking',
                'name': '禁用核心停驻',
                'help': '防止 Windows 关闭 CPU 核心。',
                'default': False
            },
            {
                'id': 'game_vbs',
                'name': '禁用 VBS',
                'help': '游戏中会有 10% 的开销。仅在您的目标是 100% 游戏时使用。',
                'default': False
            },
            {
                'id': 'perf_win32_priority',
                'name': 'Win32PrioritySeparation 26',
                'help': '优化活跃窗口（游戏）的 CPU 优先级。',
                'default': False
            },
            {
                'id': 'perf_large_cache',
                'name': '大型系统缓存',
                'help': '通过使用更多 RAM 提高文件性能。',
                'default': False
            },
            {
                'id': 'perf_io_limit',
                'name': '提高 IO 页面锁定限制',
                'help': '加速大型文件传输。',
                'default': False
            },
            {
                'id': 'perf_wait_kill',
                'name': '快速关闭服务 (2秒)',
                'help': '减少杀死服务前的等待时间。',
                'default': False
            },
            {
                'id': 'perf_auto_end',
                'name': '注销时自动关闭卡住的应用',
                'help': '强制在关机时关闭卡住的进程。',
                'default': False
            },
            {
                'id': 'perf_menu_delay',
                'name': '菜单显示延迟设为零',
                'help': '菜单瞬间出现。',
                'default': False
            },
            {
                'id': 'perf_startup_delay',
                'name': '移除总启动延迟',
                'help': '无需人工等待即可启动后台应用。',
                'default': False
            }
        ],
        'cat_power': [
            {
                'id': 'pwr_ultimate',
                'name': '强制卓越性能',
                'help': '最高能级。禁用任何 CPU 节能。',
                'default': False
            },
            {
                'id': 'pwr_min_cpu',
                'name': 'CPU 最小 100%',
                'help': '防止处理器降低频率。',
                'default': False
            },
            {
                'id': 'pwr_throttling',
                'name': '禁用电源节流',
                'help': '防止 Windows 限制 Discord 和后台应用。',
                'default': False
            },
            {
                'id': 'pwr_cpu_boost',
                'name': '始终开启 CPU Turbo Boost',
                'help': '即使在使用电池时也保持 Turbo Boost 开启。',
                'default': False
            },
            {
                'id': 'pwr_pci_link',
                'name': '禁用 PCIe 链路状态电源管理',
                'help': '防止 GPU 进入低功耗状态。',
                'default': False
            },
            {
                'id': 'pwr_hibernation',
                'name': '禁用休眠',
                'help': '释放 C 盘空间并减少 SSD 磨损。',
                'default': False
            },
            {
                'id': 'pwr_disk_timeout',
                'name': '禁用 HDD 超时关闭',
                'help': '防止 HDD 关闭导致卡顿。',
                'default': False
            },
            {
                'id': 'pwr_adaptive_brightness',
                'name': '禁用自适应亮度',
                'help': '防止传感器自动调整亮度。',
                'default': False
            },
            {
                'id': 'pwr_usb_hub_suspend',
                'name': '禁用 USB 集合器选择性暂停',
                'help': '游戏级 USB 暂停补充。更稳定。',
                'default': False
            }
        ],
        'cat_gpu': [
            {
                'id': 'gpu_hags',
                'name': '开启 HAGS (硬件 GPU 计划)',
                'help': '将帧队列从 CPU 转移到 GPU。在 DX12/Vulkan 中提升 FPS。',
                'default': False
            },
            {
                'id': 'gpu_mpo',
                'name': '禁用 MPO',
                'help': 'MPO 会导致黑屏和卡顿。Nvidia 建议禁用。',
                'default': False
            },
            {
                'id': 'gpu_preemption',
                'name': '禁用 GPU 抢占',
                'help': '防止帧中间出现中断。消除微卡顿。',
                'default': False
            },
            {
                'id': 'gpu_reduce_dpc',
                'name': '降低 GPU 的 DPC 延迟',
                'help': '调整 GPU 驱动程序中断以最小化 DPC 延迟。',
                'default': False
            },
            {
                'id': 'gpu_dwm_priority',
                'name': 'DWM 高优先级',
                'help': '增加 dwm.exe 优先级以获得更流畅的渲染。',
                'default': False
            },
            {
                'id': 'gpu_gpu_priority',
                'name': 'GPU 优先级 8 (MMCSS)',
                'help': '调整 GpuPriority 使游戏进程具有更高优先级。',
                'default': False
            },
            {
                'id': 'gpu_perf_registry',
                'name': '优化 GPU MMCSS 注册表',
                'help': '为 GPU 调整 NetworkThrottlingIndex 和 SystemResponsiveness。',
                'default': False
            },
            {
                'id': 'gpu_nvidia_power',
                'name': 'NVIDIA：最高性能',
                'help': '通过注册表在 NVIDIA 面板中强制最高性能。',
                'default': False
            },
            {
                'id': 'gpu_nvidia_telemetry',
                'name': '禁用 NVIDIA 遥测',
                'help': '停止后台的 NVIDIA 遥测任务。',
                'default': False
            },
            {
                'id': 'gpu_amd_power',
                'name': 'AMD：无 GPU 节能',
                'help': '防止 AMD GPU 进入低频状态。',
                'default': False
            },
            {
                'id': 'gpu_amd_telemetry',
                'name': '禁用 AMD 遥测',
                'help': '停止后台的 AMD 遥测服务。',
                'default': False
            },
            {
                'id': 'gpu_pci_express_max',
                'name': 'PCIe GPU 最高模式',
                'help': '专门为 GPU 禁用链路状态电源管理。',
                'default': False
            },
            {
                'id': 'gpu_disable_fullscreen_opt',
                'name': '全局禁用全屏优化',
                'help': '在所有游戏中强制使用真正的全屏。',
                'default': False
            },
            {
                'id': 'gpu_freesync_vsync_off',
                'name': '禁用全局垂直同步',
                'help': '通过注册表在所有应用中默认禁用垂直同步。',
                'default': False
            },
            {
                'id': 'gpu_cache_clean',
                'name': '清理 GPU 着色器缓存',
                'help': '清除积累的着色器缓存。如果进入新区域卡顿，此项很有用。',
                'default': False
            },
            {
                'id': 'gpu_vram_paging',
                'name': '优化 VRAM 分页',
                'help': '将系统 RAM 用作 VRAM 不足的 GPU 的扩展。',
                'default': False
            },
            {
                'id': 'gpu_shader_cache',
                'name': '着色器缓存重定向至高速 SSD',
                'help': '配置着色器缓存以在 NVMe 上快速读取。',
                'default': False
            },
            {
                'id': 'gpu_disable_mpv',
                'name': '禁用后台 DX12/Vulkan 预编译',
                'help': '防止在您玩游戏时进行着色器预编译。',
                'default': False
            },
            {
                'id': 'gpu_gsync_compat',
                'name': 'FreeSync 显示器支持 G-Sync',
                'help': '使 AMD 显示器在使用 Nvidia GPU 时强制兼容 G-Sync。',
                'default': False
            },
            {
                'id': 'gpu_night_light_off',
                'name': '禁用夜间模式',
                'help': '防止 Windows 改变显示器的色彩校准。',
                'default': False
            }
        ],
        'cat_kernel': [
            {
                'id': 'ext_57_processes',
                'name': '系统服务整合 (最小进程数)',
                'help': '重定向 svchost 并禁用非关键服务，将活跃进程总数降至运行所需的最小值。',
                'default': False
            },
            {
                'id': 'kern_registry_size',
                'name': '增加最大注册表大小',
                'help': '防止自定义系统上的注册表限制错误。',
                'default': False
            },
            {
                'id': 'kern_bcdedit_inc',
                'name': 'BCDEDIT 中断频率',
                'help': '通过 BCDEDIT 提高时钟精度。获得 < 1ms 计时器的关键。',
                'default': False
            },
            {
                'id': 'kern_memory_comp',
                'name': '禁用内存压缩 (MMAgent)',
                'help': '防止 CPU 浪费周期压缩 RAM 页面，优先保证延迟。',
                'default': False
            },
            {
                'id': 'kern_system_resp',
                'name': '系统响应度设为 0% (实时)',
                'help': '移除 Windows 后台资源保留，将 100% 奉献给聚焦进程。',
                'default': False
            },
            {
                'id': 'kernel_mitigations',
                'name': '禁用 CPU 缓解措施',
                'help': '禁用 Spectre/Meltdown。提升 5-15% 纯 CPU 性能。会降低安全性。',
                'default': False
            },
            {
                'id': 'kern_large_pages',
                'name': '启用大页面 (虚拟内存)',
                'help': '减少内存高负载应用中的缺页异常 (TLB miss)。',
                'default': False
            },
            {
                'id': 'kern_iot_core',
                'name': '极简 Embedded 配置文件配置',
                'help': '调整系统内部参数，使其表现得像低资源的 Windows IoT 配置文件。',
                'default': False
            },
            {
                'id': 'kern_process_isolation',
                'name': '禁用核心进程隔离',
                'help': '减少内核虚拟化开销，以最大化线程速度。',
                'default': False
            }
        ],
        'cat_extreme': [
            {
                'id': 'ext_super_nuclear',
                'name': '大规模系统服务清理',
                'help': '禁用所有非必要的网络、打印和视觉服务。若无备份则不可逆。',
                'default': False
            },
            {
                'id': 'ext_minimalist',
                'name': '高性能精简 Shell 配置文件',
                'help': '禁用 Windows Shell 的视觉效果，彻底释放 CPU 和 GPU 周期。',
                'default': False
            },
            {
                'id': 'ext_defender_kill',
                'name': '永久禁用 Windows Defender',
                'help': '通过注册表/GPO 移除扫描引擎和原生安全服务。',
                'default': False
            },
            {
                'id': 'ext_uwp_kill_all',
                'name': '彻底移除内置 UWP 应用',
                'help': '为系统所有用户卸载所有预装的 UWP 应用。',
                'default': False
            },
            {
                'id': 'ext_firewall_off',
                'name': '禁用 Windows 防火墙 (堆栈绕过)',
                'help': '禁用原生数据包过滤以最小化网络延迟。',
                'default': False
            },
            {
                'id': 'ext_update_dead',
                'name': '阻止 Windows 更新 (LTSC 策略)',
                'help': '防止操作系统进行任何更新或驱动程序下载尝试。',
                'default': False
            }
        ],
        'cat_util': [
            {
                'id': 'util_dotnet',
                'name': '安装 .NET 运行时',
                'help': '确保与所有版本的应用框架兼容。',
                'default': False
            },
            {
                'id': 'util_vc_redist',
                'name': '安装 C++ 可再发行组件',
                'help': '安装运行游戏和软件所需的所有库。',
                'default': False
            },
            {
                'id': 'util_directx',
                'name': '更新 DirectX 运行时',
                'help': '为旧游戏安装旧版 DirectX 组件。',
                'default': False
            },
            {
                'id': 'util_powershell_7',
                'name': '安装 PowerShell 7',
                'help': '安装现代且更快的 Windows 脚本引擎版本。',
                'default': False
            },
            {
                'id': 'util_driver_updates',
                'name': '排除驱动程序更新',
                'help': '防止 Windows 使用通用版本覆盖您的自定义驱动程序。',
                'default': False
            },
            {
                'id': 'util_ps_telemetry',
                'name': '禁用 PowerShell 遥测',
                'help': '移除现代 Windows 终端中的使用报告。',
                'default': False
            },
            {
                'id': 'util_end_task_rc',
                'name': '任务栏右键 "结束任务"',
                'help': '在任务栏图标右键菜单中增加直接关闭进程的选项。',
                'default': False
            },
            {
                'id': 'util_start_recommendations',
                'name': '移除开始菜单建议',
                'help': '清除开始菜单中的近期文件和建议应用部分。',
                'default': False
            },
            {
                'id': 'util_sticky_keys',
                'name': '禁用粘滞键',
                'help': '防止系统在多次按下 Shift 键后询问粘滞键。',
                'default': False
            },
            {
                'id': 'util_taskbar_center',
                'name': '任务栏：靠左对齐',
                'help': '恢复 Windows 11 桌面上的图标经典位置。',
                'default': False
            },
            {
                'id': 'util_settings_home',
                'name': '移除设置主页',
                'help': '移除打开 Windows 设置时无用的 "主页" 屏幕。',
                'default': False
            },
            {
                'id': 'util_new_outlook',
                'name': '阻止新版 Outlook',
                'help': '防止 Windows 用 Web 应用版取代经典邮件客户端。',
                'default': False
            },
            {
                'id': 'util_cross_device',
                'name': '禁用跨设备体验',
                'help': '禁用与其他 PC 或移动设备同步未完成任务。',
                'default': False
            },
            {
                'id': 'util_task_view',
                'name': '隐藏任务视图',
                'help': '通过移除虚拟桌面图标来清理任务栏。',
                'default': False
            },
            {
                'id': 'util_folder_discovery',
                'name': '关闭文件夹自动发现',
                'help': '防止资源管理在打开包含图片或音乐的文件夹时更改视图类型。',
                'default': False
            },
            {
                'id': 'util_bsod_detail',
                'name': 'BSOD 显示详细信息',
                'help': '在蓝屏界面显示详细参数和错误代码。',
                'default': False
            },
            {
                'id': 'util_numlock',
                'name': '启动时开启 NumLock',
                'help': '登录 Windows 时自动激活 NumLock。',
                'default': False
            },
            {
                'id': 'util_verbose_logon',
                'name': '详细登录消息',
                'help': '在登录和注销期间显示每个服务的状态。',
                'default': False
            },
            {
                'id': 'util_consumer_features',
                'name': '禁用应用商店建议',
                'help': '防止微软静默安装推广应用。',
                'default': False
            },
            {
                'id': 'util_wpbt',
                'name': '阻止 Bloatware 注入 (WPBT)',
                'help': '防止制造商在 Windows 启动时通过 BIOS 安装软件。',
                'default': False
            },
            {
                'id': 'util_widgets_remove',
                'name': '移除 Win11 小组件',
                'help': '卸载任务栏的小组件和资讯面板。',
                'default': False
            },
            {
                'id': 'uwp_xbox',
                'name': '移除 Xbox 应用',
                'help': '删除所有 Xbox 应用 (GameBar, TCUI)。如果您使用 PC Game Pass 玩游戏，请勿使用。',
                'default': False
            },
            {
                'id': 'uwp_bloatware',
                'name': '移除原生自带软件',
                'help': '删除垃圾应用：Zune, BingNews, GetHelp, Solitaire, People...',
                'default': False
            },
            {
                'id': 'uwp_onedrive',
                'name': '卸载 OneDrive',
                'help': '从系统中深度卸载 Microsoft OneDrive。',
                'default': False
            },
            {
                'id': 'uwp_edge',
                'name': '移除 Edge (高级)',
                'help': '尝试用 PowerShell 移除 Microsoft Edge。请预先准备好另一个浏览器。',
                'default': False
            },
            {
                'id': 'uwp_3dbuilder',
                'name': '移除 3D Builder',
                'help': '卸载微软的 3D 建模应用。',
                'default': False
            },
            {
                'id': 'uwp_alarms',
                'name': '移除闹钟和时钟',
                'help': '卸载闹钟和秒表应用。',
                'default': False
            },
            {
                'id': 'uwp_camera',
                'name': '移除相机',
                'help': '从商店中卸载相机应用。',
                'default': False
            },
            {
                'id': 'uwp_communications',
                'name': '移除邮件和日历',
                'help': '卸载内置的邮件和日历应用。',
                'default': False
            },
            {
                'id': 'uwp_feedback',
                'name': '移除反馈中心',
                'help': '卸载微软的反馈应用。',
                'default': False
            },
            {
                'id': 'uwp_gethelp',
                'name': '移除获取帮助',
                'help': '卸载微软的技术支持应用。',
                'default': False
            },
            {
                'id': 'uwp_maps',
                'name': '移除地图',
                'help': '卸载内置的地图应用。',
                'default': False
            },
            {
                'id': 'uwp_mixedreality',
                'name': '移除混合现实门户',
                'help': '卸载混合现实门户。',
                'default': False
            },
            {
                'id': 'uwp_people',
                'name': '移除联系人 (People)',
                'help': '卸载内置的联系人应用。',
                'default': False
            },
            {
                'id': 'uwp_photos',
                'name': '移除照片',
                'help': '卸载现代版照片应用（可用经典查看器替代）。',
                'default': False
            },
            {
                'id': 'uwp_skype',
                'name': '移除 Skype',
                'help': '卸载预装的 Skype 应用。',
                'default': False
            },
            {
                'id': 'uwp_solitaire',
                'name': '移除纸牌游戏',
                'help': '卸载预装的纸牌游戏。',
                'default': False
            },
            {
                'id': 'uwp_soundrecorder',
                'name': '移除录音机',
                'help': '卸载录音应用。',
                'default': False
            },
            {
                'id': 'uwp_stickynotes',
                'name': '移除便笺 (Sticky Notes)',
                'help': '卸载便笺应用。',
                'default': False
            },
            {
                'id': 'uwp_weather',
                'name': '移除天气',
                'help': '卸载天气应用。',
                'default': False
            },
            {
                'id': 'uwp_yourphone',
                'name': '移除手机连接',
                'help': '卸载手机连接应用。',
                'default': False
            }
        ],
        'cat_pro': [
            {
                'id': 'util_context_compact',
                'name': '启用紧凑型右键菜单',
                'help': '减少右键菜单选项之间的填充和间距。',
                'default': False
            },
            {
                'id': 'util_legacy_photo',
                'name': '恢复经典照片查看器 (Win7)',
                'help': '启用旧版本中超快且轻量的图片查看器。',
                'default': False
            },
            {
                'id': 'util_legacy_calc',
                'name': '恢复经典 Win32 计算器',
                'help': '用传统的 exe 版本替换缓慢的 UWP 版本。',
                'default': False
            },
            {
                'id': 'util_god_mode',
                'name': '控制面板统一访问 (神之模式)',
                'help': '在一个窗口中创建所有系统管理设置的快捷方式。',
                'default': False
            },
            {
                'id': 'util_verbose_boot',
                'name': '启用详细启动历史',
                'help': '启动时在屏幕上显示加载的驱动程序和服务。',
                'default': False
            },
            {
                'id': 'util_desktop_labels',
                'name': '移除快捷方式箭头',
                'help': '通过移除快捷方式箭头来清理桌面图标。',
                'default': False
            },
            {
                'id': 'util_explorer_pc',
                'name': "打开资源管理器至 '此电脑'",
                'help': '配置资源管理器，默认跳过最近文件视图。',
                'default': False
            }
        ],
        'cat_help': []
    }
