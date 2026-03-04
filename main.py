# pyre-ignore-all-errors
# type: ignore
import typing
import sys
import winsound
import os
import json
import shutil
import threading
import webbrowser

import customtkinter as ctk  # type: ignore
import psutil  # type: ignore
import ctypes  # type: ignore
import i18n  # type: ignore
import optimizer_core  # type: ignore

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

def get_config_path():
    """Returns the path to the configuration file in LocalAppData, ensures directory exists."""
    appdata = os.environ.get("LOCALAPPDATA", os.environ.get("APPDATA", os.path.expanduser("~")))
    config_dir = os.path.join(appdata, "CDR_Optimizer")
    if not os.path.exists(config_dir):
        try:
            os.makedirs(config_dir, exist_ok=True)
        except Exception:
            # Fallback to current directory if AppData is not writable (rare)
            return "optimizer_config.json"
    return os.path.join(config_dir, "optimizer_config.json")

CONFIG_FILE = get_config_path()

def migrate_config():
    """Migrates configuration from current directory to AppData if it exists there."""
    old_config = "optimizer_config.json"
    new_config = get_config_path()
    
    # Don't migrate if it's the same path (fallback case)
    if os.path.abspath(old_config) == os.path.abspath(new_config):
        return

    if os.path.exists(old_config):
        try:
            with open(old_config, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Save to new location
            with open(new_config, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            
            # Remove old file
            os.remove(old_config)
            print(f"Config migrated to {new_config}")
        except Exception as e:
            print(f"Error migrating config: {e}")

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

try:
    import cv2  # type: ignore
    import PIL.Image
    import PIL.ImageTk  # type: ignore
    import numpy as np  # type: ignore
    HAS_VIDEO = True
except ImportError:
    HAS_VIDEO = False


@typing.no_type_check
class HelpTooltip(ctk.CTkToplevel):
    """Compact floating tooltip for the ? help buttons â€” much smaller than the main dialog."""
    def __init__(self, master_widget, help_text, theme_color="#e600e6"):
        super().__init__()
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(fg_color="#010203")
        self.wm_attributes("-transparentcolor", "#010203")
        # No grab_set() here to allow scrolling while tooltip is shown

        W = 360
        self.border = ctk.CTkFrame(self, fg_color="#0d0d0d", bg_color="#010203", border_width=2,
                                   border_color=theme_color, corner_radius=15)
        self.border.pack(fill="both", expand=True, padx=1, pady=1)

        # Header row
        hdr = ctk.CTkFrame(self.border, fg_color="transparent")
        hdr.pack(fill="x", padx=10, pady=(8, 0))
        ctk.CTkLabel(hdr, text="💡 INFO", font=ctk.CTkFont(size=14, weight="bold"),
                     text_color=theme_color).pack(side="left")
        ctk.CTkButton(hdr, text="✖", width=22, height=22, corner_radius=0,
                      fg_color="transparent", hover_color="#ff4444",
                      text_color="#ffffff", font=ctk.CTkFont(size=11),
                      command=self.close).pack(side="right")

        # Message
        ctk.CTkLabel(self.border, text=help_text,
                     font=ctk.CTkFont(size=12),
                     text_color="#e0e0e0",
                     justify="left",
                     wraplength=W - 40,
                     anchor="w").pack(padx=14, pady=(6, 12), fill="x")

        self.update_idletasks()
        w = W
        h = self.winfo_reqheight()
        # Position near the master widget
        try:
            bx = master_widget.winfo_rootx()
            by = master_widget.winfo_rooty()
            bw = master_widget.winfo_width()
            sx = bx + bw + 5
            sy = by - h // 2
        except Exception:
            sx, sy = 200, 200
        self.geometry(f"{w}x{h}+{sx}+{sy}")
        # Auto-close after 8 seconds
        self.after(8000, self.close)
        self.bind("<Escape>", lambda e: self.close())
        self.bind("<Button-1>", lambda e: self.close())

    def close(self):
        try:
            self.grab_release()
            self.destroy()
        except Exception:
            pass


@typing.no_type_check
class HelpButton(ctk.CTkButton):
    def __init__(self, master, help_text, theme_color="#e600e6", hover_color="#ff33ff", **kwargs):
        super().__init__(master=master, text="?", width=24, height=24, corner_radius=12, fg_color=theme_color,  # type: ignore
                         bg_color="transparent", hover_color=hover_color, font=ctk.CTkFont(size=14, weight="bold"), border_width=2, border_color=theme_color, command=self.show_help, **kwargs)  # type: ignore
        self.help_text = help_text
        self._theme_color = theme_color

    def show_help(self):
        try:
            theme = getattr(sys.modules['__main__'], 'app_instance').current_theme_color  # type: ignore
        except Exception:
            theme = self._theme_color
        tip = HelpTooltip(self, self.help_text, theme_color=theme)
        tip.wait_window()

    def update_text(self, new_help_text):
        self.help_text = new_help_text



@typing.no_type_check
class TweakRow(ctk.CTkFrame):
    def __init__(self, master, tweak_id, tweak_name, help_text, state_controller, 
                 is_enabled_default=False, theme_color="#e600e6", 
                 drag_start_cb=None, drag_move_cb=None, **kwargs):
        super().__init__(master, fg_color="transparent", bg_color="transparent", # type: ignore
                         corner_radius=15, border_width=1, border_color=theme_color, **kwargs)  # type: ignore
        
        # Bind RMB drag to the row itself
        if drag_start_cb: self.bind("<Button-3>", drag_start_cb)
        if drag_move_cb: self.bind("<B3-Motion>", drag_move_cb)
        self.tweak_id = tweak_id
        self.state_controller = state_controller

        self.grid_columnconfigure(0, weight=1)

        self.switch = ctk.CTkSwitch(
            self,
            text=tweak_name,
            onvalue=True,
            offvalue=False,
            progress_color=theme_color,
            button_color="#ffffff",
            button_hover_color="#e6e6e6",
            font=ctk.CTkFont(size=16, weight="bold"),
            switch_width=50,
            switch_height=25,
            command=self.on_toggle,
            text_color="#ffffff",
            fg_color="#333333",
            bg_color="transparent"
        )
        self.switch.grid(row=0, column=0, sticky="w",
                         pady=12, padx=15)  # type: ignore
        
        # Bind RMB drag to switch and its text label for consistency
        if drag_start_cb: self.switch.bind("<Button-3>", drag_start_cb)
        if drag_move_cb: self.switch.bind("<B3-Motion>", drag_move_cb)

        # Load saved state from config instantly rather than querying the system
        saved_state = self.state_controller.get(self.tweak_id, is_enabled_default)

        if saved_state:
            self.switch.select()  # type: ignore
        else:
            self.switch.deselect()  # type: ignore

        self.help_btn = HelpButton(
            self, help_text, theme_color=theme_color, hover_color="#888888")
        self.help_btn.grid(row=0, column=1, sticky="e",
                           padx=15)  # type: ignore

    def update_state(self, real_state):
        if real_state is not None:
            self.state_controller[self.tweak_id] = real_state
            if real_state:
                self.switch.select()  # type: ignore
            else:
                self.switch.deselect()  # type: ignore

    def on_toggle(self):
        # type: ignore
        self.state_controller[self.tweak_id] = self.switch.get()

    def is_selected(self):
        return self.switch.get()  # type: ignore

    def update_text(self, new_name, new_help):
        if hasattr(self, 'switch') and self.switch:
            self.switch.configure(text=new_name)
        if hasattr(self, 'help_btn') and self.help_btn:
            self.help_btn.update_text(new_help)


@typing.no_type_check
class MinecraftMessageBox(ctk.CTkToplevel):
    def __init__(self, title, message, is_yesno=False, theme_color="#55FF55", hover_color="#33DD33"):
        super().__init__()
        self.overrideredirect(True)
        self.geometry("600x450")
        self.configure(fg_color="#010203")
        self.wm_attributes("-transparentcolor", "#010203")
        self.result = False
        self.update_idletasks()
        try:
            x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (600 // 2)
            y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (450 // 2)
            self.geometry(f"+{x}+{y}")
        except:
            pass
        self.attributes("-topmost", True)
        self.grab_set()

        try:
            ctypes.windll.gdi32.AddFontResourceExW(resource_path("minecraft.ttf"), 0x10, 0)  # type: ignore
            cdr_font = ctk.CTkFont(family="Minecraftia", size=20)
            btn_font = ctk.CTkFont(family="Minecraftia", size=14)
            msg_font = ctk.CTkFont(family="Minecraftia", size=14)
        except:
            cdr_font = ctk.CTkFont(family="Impact", size=20)
            btn_font = ctk.CTkFont(family="Impact", size=14)
            msg_font = ctk.CTkFont(size=14, weight="bold")
        # Main border - Square (Restored to 15px)
        self.border_frame = ctk.CTkFrame(self, fg_color="#0d0d0d", bg_color="#010203", border_width=2, border_color=theme_color, corner_radius=15)
        self.border_frame.pack(fill="both", expand=True)

        # Close button "X"
        self.close_btn = ctk.CTkButton(
            self.border_frame, text="✖", width=26, height=26, fg_color="transparent",
            hover_color="#ff4444", text_color="#ffffff", corner_radius=13,
            command=self.do_no
        )
        self.close_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-15, y=15)

        self.title_lbl = ctk.CTkLabel(self.border_frame, text=title.upper(), font=cdr_font, text_color=theme_color)
        self.title_lbl.pack(pady=(20, 10), padx=20)

        self.scroll_frame = ctk.CTkScrollableFrame(self.border_frame, fg_color="#000000", border_width=2, border_color="#333333", corner_radius=0)
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=5)

        self.status_lbl = ctk.CTkLabel(self.scroll_frame, text=message, font=msg_font, text_color="#e0e0e0", justify="center", wraplength=500)
        self.status_lbl.pack(pady=10, padx=10, fill="x", expand=True)

        self.btn_frame = ctk.CTkFrame(self.border_frame, fg_color="transparent")
        self.btn_frame.pack(pady=(5, 15))

        if is_yesno:
            self.btn_yes = ctk.CTkButton(self.btn_frame, text="Sí", width=120, fg_color=theme_color, hover_color=hover_color, corner_radius=8, border_width=2, border_color="#222222", font=btn_font, text_color="#000000", command=self.do_yes)
            self.btn_yes.pack(side="left", padx=10)
            self.btn_no = ctk.CTkButton(self.btn_frame, text="No", width=120, fg_color="#555555", hover_color="#777777", corner_radius=8, border_width=2, border_color="#222222", font=btn_font, text_color="#ffffff", command=self.do_no)
            self.btn_no.pack(side="left", padx=10)
        else:
            self.btn_ok = ctk.CTkButton(self.btn_frame, text="OK", width=120, fg_color=theme_color, hover_color=hover_color, corner_radius=8, border_width=2, border_color="#222222", font=btn_font, text_color="#000000", command=self.do_yes)
            self.btn_ok.pack(padx=10)

    def do_yes(self):
        self.result = True
        self.grab_release()
        self.destroy()

    def do_no(self):
        self.result = False
        self.grab_release()
        self.destroy()

def showinfo(title, message):
    theme = getattr(sys.modules['__main__'], 'app_instance').current_theme_color if hasattr(sys.modules['__main__'], 'app_instance') else "#e600e6"
    dlg = MinecraftMessageBox(title, message, is_yesno=False, theme_color=theme)
    dlg.wait_window()

def askyesno(title, message):
    theme = getattr(sys.modules['__main__'], 'app_instance').current_theme_color if hasattr(sys.modules['__main__'], 'app_instance') else "#e600e6"
    dlg = MinecraftMessageBox(title, message, is_yesno=True, theme_color=theme)
    dlg.wait_window()
    return dlg.result


@typing.no_type_check
class OptimizationProgressDialog(ctk.CTkToplevel):
    _BLOCKS = 16  # total block chars in the bar

    def __init__(self, master, theme_color="#55FF55", on_confirm=None, **kwargs):
        super().__init__(master=master, **kwargs)  # type: ignore
        self.overrideredirect(True)
        self.configure(fg_color="#010203")
        self.wm_attributes("-transparentcolor", "#010203")
        self.on_confirm = on_confirm
        self._theme  = theme_color
        self._pct    = 0
        self._ani    = None

        # â”€â”€ Confirm-phase size â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        W, H = 520, 310
        self.geometry(f"{W}x{H}")
        self.update_idletasks()
        try:
            x = master.winfo_x() + (master.winfo_width()  // 2) - (W // 2)
            y = master.winfo_y() + (master.winfo_height() // 2) - (H // 2)
            self.geometry(f"+{x}+{y}")
        except Exception:
            pass
        self.attributes("-topmost", True)
        self.grab_set()

        # fonts
        try:
            ctypes.windll.gdi32.AddFontResourceExW(resource_path("minecraft.ttf"), 0x10, 0)  # type: ignore
            f_title = ctk.CTkFont(family="Minecraftia", size=17)
            f_body  = ctk.CTkFont(family="Minecraftia", size=12)
            f_btn   = ctk.CTkFont(family="Minecraftia", size=13)
            f_bar   = ctk.CTkFont(family="Minecraftia", size=15)
            f_cdr   = ctk.CTkFont(family="Minecraftia", size=24, weight="bold")
        except Exception:
            f_title = ctk.CTkFont(family="Consolas", size=17, weight="bold")
            f_body  = ctk.CTkFont(family="Consolas", size=12)
            f_btn   = ctk.CTkFont(family="Consolas", size=13, weight="bold")
            f_bar   = ctk.CTkFont(family="Consolas", size=15)
            f_cdr   = ctk.CTkFont(family="Consolas", size=24, weight="bold")
        self._f_bar = f_bar
        self._f_cdr = f_cdr
        self._theme_color = theme_color

        # outer double-border
        outer = ctk.CTkFrame(self, fg_color="#000000", bg_color="#010203",
                             border_width=2, border_color=theme_color, corner_radius=15)
        outer.pack(fill="both", expand=True, padx=2, pady=2)
        self._outer = outer

        inner = ctk.CTkFrame(outer, fg_color="#000000",
                              border_width=1, border_color=theme_color, corner_radius=10)
        inner.pack(fill="both", expand=True, padx=6, pady=6)
        self._inner = inner

        # â”€â”€ Confirm-phase widgets â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        self.title_lbl = ctk.CTkLabel(inner, text=i18n.t("msg_confirm_title").upper(),
                      font=f_title, text_color=theme_color)
        self.title_lbl.pack(pady=(18, 8))

        self.status_lbl = ctk.CTkLabel(inner, text=i18n.t("msg_confirm_body"),
                      font=f_body, text_color="#cccccc",
                      justify="center", wraplength=430)
        self.status_lbl.pack(padx=24, pady=(0, 14))

        btn_row = ctk.CTkFrame(inner, fg_color="transparent")
        btn_row.pack(pady=(0, 18))
        self._btn_row = btn_row

        ctk.CTkButton(btn_row, text="Sí", width=115,
                      fg_color=theme_color, hover_color="#33cc33",
                      corner_radius=8, border_width=2, border_color="#111111",
                      font=f_btn, text_color="#000000",
                      command=self.do_confirm).pack(side="left", padx=8)

        ctk.CTkButton(btn_row, text="No", width=115,
                      fg_color="#444444", hover_color="#666666",
                      corner_radius=8, border_width=2, border_color="#111111",
                      font=f_btn, text_color="#ffffff",
                      command=self.do_cancel).pack(side="left", padx=8)

        # â”€â”€ Loading-phase widgets (hidden until confirmed) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        self.progress_bar = ctk.CTkProgressBar(inner, width=300, height=12, corner_radius=0, 
                                               progress_color=theme_color, fg_color="#333333")
        self._pct_lbl = ctk.CTkLabel(inner, text="0%", font=f_btn, text_color="#ffffff")
        self._cdr_lbl = ctk.CTkLabel(inner, text="CDR", font=f_cdr, text_color=theme_color)

    # â”€â”€ Helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    def set_progress(self, val: int):
        self._pct = val
        self.progress_bar.set(val / 100.0)
        self._pct_lbl.configure(text=f"{self._pct}%")

    def set_complete(self):
        self.progress_bar.set(1.0)
        self._pct_lbl.configure(text="100%  âœ“")

    # â”€â”€ Actions â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    def do_cancel(self):
        if self._ani:
            self.after_cancel(self._ani)
        self.grab_release()
        self.destroy()

    def do_confirm(self):
        # Wipe the buttons row
        if hasattr(self, '_btn_row') and self._btn_row is not None:
            self._btn_row.pack_forget()

        # Resize to loading-only size
        self.geometry("420x280")
        try:
            master = self.master  # type: ignore
            x = (master.winfo_x() + (master.winfo_width()  // 2) - (420 // 2)) if master else 100
            y = (master.winfo_y() + (master.winfo_height() // 2) - (280 // 2)) if master else 100
            self.geometry(f"+{x}+{y}")
        except Exception:
            pass

        self.progress_bar.set(0)
        self._pct_lbl.configure(text="0%")
        
        self.title_lbl.configure(text="APLICANDO OPTIMIZACIONES...")
        self.status_lbl.configure(text="Esto puede tardar unos segundos...")
        
        self.title_lbl.pack(pady=(20, 5))
        self.status_lbl.pack(pady=(0, 10))
        self.progress_bar.pack(pady=(10, 2))
        self._pct_lbl.pack(pady=(0, 4))
        self._cdr_lbl.pack(pady=(6, 20))

        self._pct = 0

        if self.on_confirm:
            self.on_confirm()




@typing.no_type_check
class OptimizerApp(ctk.CTk):
    def __init__(self):
        super(OptimizerApp, self).__init__()

        # Initialize attributes
        self._is_startup = True
        self._is_destroyed = False
        self.config = self.load_config()
        self.all_tweak_rows = {}  # type: ignore
        self.category_btns = []
        self.categories = []
        self.category_original_keys = []
        self.current_theme_color = "#e600e6"
        self.current_hover_color = "#ff33ff"
        self.current_cat_original_key = ""
        self.current_category = ""
        self.video_source = ""
        self.audio_wav = ""
        self.audio_on = False
        self.vid = None
        self.bg_picker_frame = None
        self.drag_x = None
        self.drag_y = None
        self.audio_btn = None
        self.switch_bg_btn = None
        self.bg_win = None
        self.audio_source = ""
        self._transition_state: typing.Optional[str] = None  # None, 'out', 'in'
        self._transition_alpha: float = 0.0   # 0.0 (normal) to 1.0 (black)
        self._pending_background: typing.Optional[str] = None
        self._last_frame: typing.Any = None
        self._is_minimized = False
        saved_lang = self.config.get("lang", "es")
        i18n.set_lang(saved_lang)

        self.title(f"{i18n.t('app_title')} - [ADMINISTRADOR]")
        self.geometry("1152x720")
        self.resizable(False, False)
        # Enable overrideredirect for the "premium" title-bar-less look
        self.overrideredirect(True)

        try:
            icon_path = resource_path("cdrlogo.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except Exception:
            pass

        self.trans_color = "#010203"
        self.configure(fg_color=self.trans_color)  # type: ignore
        self.wm_attributes("-transparentcolor", self.trans_color)

        self.current_theme_color = "#e600e6"
        self.current_hover_color = "#ff33ff"

        # Adaptive Outer Border for the entire window - Aesthetic Rounded Corners
        self.outer_window_border = ctk.CTkFrame(self, fg_color="transparent", bg_color="transparent", border_width=2, border_color=self.current_theme_color, corner_radius=30)
        self.outer_window_border.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Ensure it doesn't block interactions by lowering it or using it as a container? 
        # Actually, if it's over everything, it might block. 
        # Better: place it at the very top but make sure it just draws the border.
        # CTK frames with transparent fg_color but border_width > 0 work well for this.
        self.outer_window_border.lower() 

        self.bg_win = ctk.CTkToplevel(self)
        if self.bg_win is not None:
            self.bg_win.overrideredirect(True)  # type: ignore
            self.bg_win.configure(fg_color="#000000")  # type: ignore

        if self.bg_win is not None:
            self.bg_label = ctk.CTkLabel(
                self.bg_win, text="", fg_color="black")  # type: ignore
            self.bg_label.place(relx=0, rely=0, relwidth=1,
                                relheight=1)  # type: ignore

        if self.bg_win is not None:
            hwnd_main = ctypes.windll.user32.GetParent(  # type: ignore
                self.winfo_id())  # type: ignore
            hwnd_bg = ctypes.windll.user32.GetParent(  # type: ignore
                self.bg_win.winfo_id())  # type: ignore

            ex_style = ctypes.windll.user32.GetWindowLongW(  # type: ignore
                hwnd_bg, -20)  # type: ignore
            # 0x08000000 = WS_EX_NOACTIVATE, 0x20 = WS_EX_TRANSPARENT (pointer-events: none)
            ctypes.windll.user32.SetWindowLongW(  # type: ignore
                hwnd_bg, -20, ex_style | 0x08000000 | 0x20)  # type: ignore

            try:
                ctypes.windll.user32.SetWindowLongPtrW(  # type: ignore
                    hwnd_main, -8, hwnd_bg)  # type: ignore
                ctypes.windll.user32.SetWindowLongPtrW(  # type: ignore
                    hwnd_bg, -8, 0)  # type: ignore
            except AttributeError:
                ctypes.windll.user32.SetWindowLongW(  # type: ignore
                    hwnd_main, -8, hwnd_bg)  # type: ignore
                ctypes.windll.user32.SetWindowLongW(  # type: ignore
                    hwnd_bg, -8, 0)  # type: ignore
            
            # Initial rounding for both windows (30px radius = 60 ellipse)
            w, h = 1152, 720
            self.round_window_corners(hwnd_main, w, h, 60)
            self.round_window_corners(hwnd_bg, w, h, 60)

        def bg_sort_key(filename):
            try:
                return int(filename.split('_')[1].split('.')[0])
            except Exception:
                return 999

        raw_bgs = [
            f for f in os.listdir(resource_path("fondos"))
            if f.endswith(('.mp4', '.mkv', '.avi', '.jpg', '.png'))
        ]
        self.fondos_disponibles = sorted(raw_bgs, key=bg_sort_key)

        saved_video = self.config.get("current_background", "fondo_1.mp4")
        if saved_video in self.fondos_disponibles:
            self.current_fondo_idx = self.fondos_disponibles.index(saved_video)
        else:
            self.current_fondo_idx = 0

        # Apply the background properly (Sync theme colors before creating UI)
        # Deferred: self.set_colors_for_background(saved_video)

        self.bg_label.bind("<ButtonPress-1>",
                           self.bg_start_move)  # type: ignore
        self.bg_label.bind("<B1-Motion>", self.bg_do_move)  # type: ignore
        self.bg_label.bind("<ButtonRelease-1>",
                           self.bg_stop_move)  # type: ignore

        self.bind("<Configure>", self.sync_bg_win)
        self.bind("<Map>", self.on_map)
        self.bind("<Unmap>", self.on_unmap)

        try:
            self.pc_user = os.getlogin()
        except Exception:
            self.pc_user = "GAMER"

        self.is_laptop = optimizer_core.is_laptop()

        # Sidebar with Aesthetic Rounded Corners
        self.sidebar = ctk.CTkFrame(self, width=290, corner_radius=30, fg_color="transparent",
                                    bg_color="transparent", border_width=2, border_color=self.current_theme_color)
        self.sidebar.place(relx=0.03, rely=0.04, relwidth=0.25, relheight=0.92)

        # Bind movement to the sidebar frame so the user can drag the window
        self.sidebar.bind("<ButtonPress-1>", self.bg_start_move)
        self.sidebar.bind("<B1-Motion>", self.bg_do_move)
        self.sidebar.bind("<ButtonRelease-1>", self.bg_stop_move)

        self.sidebar.grid_rowconfigure(14, weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)

        self.top_controls_frame = ctk.CTkFrame(
            self.sidebar, fg_color="transparent", bg_color="transparent")
        self.top_controls_frame.grid(row=0, column=0, padx=15, pady=(
            20, 10), sticky="ew")  # type: ignore

        lang_name = "Español"
        if i18n.CURRENT_LANG == "en":
            lang_name = "English"
        elif i18n.CURRENT_LANG == "pt":
            lang_name = "Português"
        elif i18n.CURRENT_LANG == "fr":
            lang_name = "Français"
        elif i18n.CURRENT_LANG == "de":
            lang_name = "Deutsch"
        elif i18n.CURRENT_LANG == "it":
            lang_name = "Italiano"
        elif i18n.CURRENT_LANG == "zh":
            lang_name = "中文"
        elif i18n.CURRENT_LANG == "ru":
            lang_name = "Ð ÑƒÑÑÐºÐ¸Ð¹"

        self.lang_var = ctk.StringVar(value=lang_name)
        self.lang_wrapper = ctk.CTkFrame(
            self.top_controls_frame, width=32, height=32, fg_color="transparent")
        self.lang_wrapper.pack_propagate(False)
        self.lang_wrapper.pack(side="left", padx=2)
        
        self.lang_btn = ctk.CTkButton(
            self.lang_wrapper, text="🌐", width=32, height=32, corner_radius=8,
            command=self.toggle_lang_picker, fg_color="transparent", bg_color="transparent", 
            hover_color=self.current_theme_color, border_width=2, border_color=self.current_theme_color,
            font=ctk.CTkFont(size=14)
        )
        if self.lang_btn is not None:
            self.lang_btn.pack(expand=True, fill="both")
        
        self.lang_picker_frame = None

        self.audio_on = False
        self.audio_wav = getattr(self, 'audio_source', "")

        self.audio_wrapper = ctk.CTkFrame(
            self.top_controls_frame, width=32, height=32, fg_color="transparent")
        self.audio_wrapper.pack_propagate(False)
        self.audio_wrapper.pack(side="left", padx=2)  # type: ignore
        self.audio_btn = ctk.CTkButton(
            self.audio_wrapper, text="🔊" if self.audio_on else "🔇", width=32, height=32, corner_radius=8,
            command=self.toggle_audio, fg_color="transparent", bg_color="transparent", hover_color=self.current_theme_color, border_width=2, border_color=self.current_theme_color,
            font=ctk.CTkFont(size=14)
        )
        if self.audio_btn is not None:
            self.audio_btn.pack(expand=True, fill="both")  # type: ignore

        self.bg_wrapper = ctk.CTkFrame(
            self.top_controls_frame, width=32, height=32, fg_color="transparent")
        self.bg_wrapper.pack_propagate(False)
        self.bg_wrapper.pack(side="left", padx=2)  # type: ignore
        self.switch_bg_btn = ctk.CTkButton(
            self.bg_wrapper, text="🎨", width=32, height=32, corner_radius=8,
            command=self.toggle_bg_picker, fg_color="transparent", bg_color="transparent", hover_color=self.current_theme_color, border_width=2, border_color=self.current_theme_color,
            font=ctk.CTkFont(size=14)
        )
        if self.switch_bg_btn is not None:
            self.switch_bg_btn.pack(expand=True, fill="both")  # type: ignore

        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text=i18n.t("logo_title"),
            font=ctk.CTkFont(family="Arial Black", size=48, weight="bold"),
            text_color=self.current_theme_color
        )

        self.logo_label.grid(row=1, column=0, padx=25, pady=(
            0, 10), sticky="ew")  # type: ignore

        self.profile_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent", bg_color="transparent",
                                          corner_radius=15, border_width=1, border_color=self.current_theme_color)
        self.profile_frame.grid(row=2, column=0, padx=20,
                                pady=5, sticky="ew")  # type: ignore

        self.user_lbl = ctk.CTkLabel(self.profile_frame, text=f'{i18n.t("user_prefix")} {self.pc_user.upper()}', font=ctk.CTkFont(
            size=14, weight="bold"), text_color="#ffffff")
        self.user_lbl.pack(pady=(12, 10))  # type: ignore

        ram_info = psutil.virtual_memory()
        disk_info = shutil.disk_usage("C:\\")

        self.ram_lbl = ctk.CTkLabel(
            self.profile_frame, text=f'{i18n.t("ram_label")} {ram_info.used / (1024 ** 3):.1f}GB / {ram_info.total / (1024 ** 3):.1f}GB', font=ctk.CTkFont(size=11, weight="bold"))
        self.ram_lbl.pack(pady=(0, 2))  # type: ignore
        self.ram_bar = ctk.CTkProgressBar(
            self.profile_frame, width=180, height=8, progress_color=self.current_theme_color, fg_color="#333333")
        self.ram_bar.pack(pady=(0, 10))  # type: ignore
        self.ram_bar.set(ram_info.percent / 100.0)

        self.disk_lbl = ctk.CTkLabel(
            self.profile_frame, text=f'{i18n.t("disk_label")} {disk_info.used / (1024 ** 3):.0f}GB / {disk_info.total / (1024 ** 3):.0f}GB', font=ctk.CTkFont(size=11, weight="bold"))
        self.disk_lbl.pack(pady=(0, 2))  # type: ignore
        self.disk_bar = ctk.CTkProgressBar(
            self.profile_frame, width=170, height=8, progress_color=self.current_theme_color, fg_color="#333333")
        self.disk_bar.pack(pady=(0, 20))  # type: ignore
        self.disk_bar.set(disk_info.used / disk_info.total)

        self.categories = [
            i18n.t("cat_system"), i18n.t("cat_clean"), i18n.t("cat_privacy"),
            i18n.t("cat_ui"), i18n.t("cat_net"), i18n.t("cat_gaming"),
            i18n.t("cat_power"), i18n.t("cat_gpu"), i18n.t("cat_kernel"),
            i18n.t("cat_extreme"), i18n.t("cat_util"), i18n.t("cat_pro"),
            i18n.t("cat_help")
        ]
        self.category_original_keys = [
            "cat_system", "cat_clean", "cat_privacy",
            "cat_ui", "cat_net", "cat_gaming",
            "cat_power", "cat_gpu", "cat_kernel",
            "cat_extreme", "cat_util", "cat_pro",
            "cat_help"
        ]

        # Scrollable frame for category buttons so they always fit regardless of window height
        self.cat_scroll = ctk.CTkScrollableFrame(
            self.sidebar, fg_color="transparent", bg_color="transparent",
            scrollbar_button_color=self.current_theme_color,
            scrollbar_button_hover_color=self.current_hover_color,
            scrollbar_fg_color=self.trans_color,
            label_text="" 
        )
        # Attempt to make it cleaner by reducing scrollbar width if possible (internal hack)
        try:
            self.cat_scroll._scrollbar.configure(width=16) 
            self.cat_scroll._scrollbar.grid_remove() # Invisible but functional
            # Force yscrollincrement=1 to ensure 'units' scroll per-pixel
            canvas = getattr(self.cat_scroll, '_parent_canvas', getattr(self.cat_scroll, '_canvas', None))
            if canvas:
                canvas.configure(yscrollincrement=1)
        except: pass
        self.cat_scroll.grid(row=3, column=0, rowspan=11,
                             sticky="nsew", padx=5, pady=0)
        self.cat_scroll.grid_columnconfigure(0, weight=1)

        self.category_btns = []

        # Binding for category buttons moved to a method for consistency and to avoid local scope issues

        for i, cat_id in enumerate(self.category_original_keys):
            cat_name = self.categories[i]
            btn = ctk.CTkButton(  # type: ignore
                self.cat_scroll,
                text=cat_name.upper(),
                command=lambda c=cat_id: self.select_category(c),
                fg_color="transparent",
                bg_color="transparent",
                text_color="#ffffff",
                hover_color=self.current_theme_color,
                anchor="center",
                border_color=self.current_theme_color,
                border_width=2,
                font=ctk.CTkFont(size=14, weight="bold"),
                height=32,
                corner_radius=8
            )
            btn.grid(row=i, column=0, padx=8, pady=3,
                     sticky="ew")  # type: ignore
            self.category_btns.append(btn)

        self.bottom_frame = ctk.CTkFrame(
            self.sidebar, fg_color="transparent", bg_color="transparent")
        self.bottom_frame.grid(row=14, column=0, sticky="ew",
                               padx=10, pady=(0, 15))  # type: ignore

        self.driver_btn = ctk.CTkButton(
            self.bottom_frame, text=i18n.t("driver_btn"), fg_color="transparent", hover_color=self.current_theme_color,
            text_color="#8c8c8c", command=self.scan_drivers, font=ctk.CTkFont(size=14, weight="bold"), height=30, corner_radius=8, border_width=2, border_color=self.current_theme_color
        )
        self.driver_btn.pack(fill="x", padx=15, pady=(5, 5))  # type: ignore

        self.optimize_btn = ctk.CTkButton(
            self.bottom_frame, text=i18n.t("apply_btn"), fg_color="transparent", hover_color=self.current_theme_color,
            text_color="#8c8c8c", command=self.apply_optimizations, font=ctk.CTkFont(size=11, weight="bold"), height=30, corner_radius=8, border_width=2, border_color=self.current_theme_color
        )
        self.optimize_btn.pack(fill="x", padx=15, pady=(0, 8))  # type: ignore

        self.status_badge = ctk.CTkLabel(
            self.bottom_frame,
            text=f"{i18n.t('status_label')} {i18n.t('status_ready')}",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=self.current_theme_color, fg_color="transparent", bg_color="transparent", corner_radius=0
        )
        self.status_badge.pack(fill="x", pady=(0, 5))  # type: ignore

        # Main Container with Aesthetic Rounded Corners
        self.main_container = ctk.CTkFrame(self, corner_radius=30, fg_color="transparent",
                                           bg_color="transparent", border_color=self.current_theme_color, border_width=2)
        self.main_container.place(
            relx=0.31, rely=0.04, relwidth=0.66, relheight=0.92)

        # Also bind movement to the main container
        self.main_container.bind("<ButtonPress-1>", self.bg_start_move)
        self.main_container.bind("<B1-Motion>", self.bg_do_move)
        self.main_container.bind("<ButtonRelease-1>", self.bg_stop_move)

        self.main_area = ctk.CTkScrollableFrame(self.main_container, corner_radius=15, fg_color="transparent",
                                                bg_color="transparent", scrollbar_button_color=self.current_theme_color, 
                                                scrollbar_fg_color=self.trans_color, border_width=0)
        try:
            self.main_area._scrollbar.configure(width=16) # Match sidebar width
            # Force yscrollincrement=1 to ensure 'units' scroll per-pixel
            canvas = getattr(self.main_area, '_parent_canvas', getattr(self.main_area, '_canvas', None))
            if canvas:
                canvas.configure(yscrollincrement=1)
        except: pass
        self.main_area.pack(expand=True, fill="both",
                            padx=15, pady=10)  # type: ignore

        # HIDE MAIN SCROLLBAR temporarily - visibility managed by _check_scroll_visibility
        # if hasattr(self.main_area, '_scrollbar'):
        #     self.main_area._scrollbar.grid_remove() # type: ignore

        # Bind Right-Click Drag Scroll to main_area and its internal canvas
        if hasattr(self.main_area, '_parent_canvas'):
            canvas = self.main_area._parent_canvas
            canvas.bind("<Button-3>", self._on_rmb_drag_start)
            canvas.bind("<B3-Motion>", self._on_rmb_drag_move)
        
        # Also bind to the frame itself for safety
        self.main_area.bind("<Button-3>", self._on_rmb_drag_start)
        self.main_area.bind("<B3-Motion>", self._on_rmb_drag_move)

        # GLOBAL SCROLL HANDLER: Catch everything app-wide
        self.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.all_tweak_rows = {}  # type: ignore
        self.tweak_data = i18n.get_tweaks_translated()  # type: ignore
        self.populate_tweaks()

        self.select_category(self.category_original_keys[0])
        self.update_idletasks()
        
        # Initial visibility check
        self.after(500, self._check_scroll_visibility)
        # Bind resize/move to sync video and update scrollbars
        self.bind("<Configure>", self._on_configure)

        # Fire off a background thread to update tweak states from system
        threading.Thread(target=self._async_update_states, daemon=True).start()

        # Now start the video/audio (UI components now exist and will receive updates)
        self.set_colors_for_background(saved_video)
        self.apply_background(saved_video)
        self._is_startup = False
        self.update_video()
        self.update_stats() # Initial stats update and start loop

        # Global Key Binding: Enter to Optimize
        self.bind("<Return>", lambda e: self.apply_optimizations())

        self.close_btn_top = ctk.CTkButton(
            self, text="✖", width=18, height=18, corner_radius=4,
            fg_color="transparent", hover_color=self.current_theme_color,
            text_color="#ffffff", font=ctk.CTkFont(size=11, weight="bold"),
            command=self.destroy,
            border_width=2, border_color=self.current_theme_color
        )
        self.close_btn_top.place(relx=1.0, rely=0.0, anchor="center", x=-20, y=20)

        self.select_category(self.category_original_keys[0])
        self.update_idletasks()

    def set_colors_for_background(self, base_name):
        # Ultra-vibrant "Phosphorescent" theme colors based on background
        if base_name.startswith("fondo_1."):
            m, h = "#ff00ff", "#ff66ff" # Brighter Pink
        elif base_name.startswith("fondo_2."):
            m, h = "#ffcc00", "#ffff00" # Golden/Yellow Glow
        elif base_name.startswith("fondo_3."):
            m, h = "#ff9900", "#ffcc33" # Vivid Orange
        elif base_name.startswith("fondo_4."):
            m, h = "#ffff00", "#f0f0f0" # Pure Neon Yellow
        elif base_name.startswith("fondo_5."):
            m, h = "#00ffff", "#80ffff" # Ice Cyan
        elif base_name.startswith("fondo_6."):
            m, h = "#ff0000", "#ff3333" # Pure Blood Red
        elif base_name.startswith("fondo_7."):
            m, h = "#8c8c8c", "#aaaaaa" # Metallic Gray
        elif base_name.startswith("fondo_8."):
            m, h = "#555555", "#333333" # Grey for readability on white background
        elif base_name.startswith("fondo_9."):
            m, h = "#cc33ff", "#df80ff" # Neon Purple
        elif base_name.startswith("fondo_10."):
            m, h = "#ffcc00", "#ffeb73"
        elif base_name.startswith("fondo_11."):
            m, h = "#39ff14", "#7fff00" # Alien Green
        elif base_name.startswith("fondo_12."):
            m, h = "#ff0000", "#ff3333" # Blood Red (Restored)
        elif base_name.startswith("fondo_13."):
            m, h = "#9900ff", "#cc66ff" # Deep UV Purple
        else:
            m, h = "#ff00ff", "#ff66ff"
        
        self.change_theme(m, h)
        self.sync_bg_win()

    def bg_start_move(self, event):
        self.focus_force()
        self.drag_x = event.x
        self.drag_y = event.y

    def bg_do_move(self, event):
        if hasattr(self, 'drag_x') and self.drag_x is not None:
            deltax = event.x - self.drag_x
            deltay = event.y - self.drag_y
            x = self.winfo_x() + deltax
            y = self.winfo_y() + deltay
            self.geometry(f"+{x}+{y}")

    def bg_stop_move(self, event):
        self.drag_x = None
        self.drag_y = None

    def change_theme(self, main_color, hover_color):
        self.current_theme_color = main_color
        self.current_hover_color = hover_color

        # Fast updates for main UI
        self.sidebar.configure(border_color=main_color)  # type: ignore
        if hasattr(self, 'lang_btn') and self.lang_btn:
            self.lang_btn.configure(hover_color=main_color, border_color=main_color)
        if hasattr(self, 'lang_border_frame') and self.lang_border_frame:
            self.lang_border_frame.configure(border_color=main_color)
        
        # If lang picker is open, update its border and buttons
        if hasattr(self, 'lang_picker_frame') and self.lang_picker_frame and self.lang_picker_frame.winfo_exists():
            self.lang_picker_frame.configure(border_color=main_color)
            for child in self.lang_picker_frame.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(border_color=main_color, hover_color=main_color)

        self.logo_label.configure(text_color=main_color)  # type: ignore
        self.status_badge.configure(text_color=main_color)  # type: ignore
        self.profile_frame.configure(border_color=main_color)  # type: ignore
        self.ram_bar.configure(progress_color=main_color)  # type: ignore
        self.disk_bar.configure(progress_color=main_color)  # type: ignore
        self.optimize_btn.configure(
            hover_color=hover_color, border_color=main_color)  # type: ignore
        self.driver_btn.configure(
            hover_color=hover_color, border_color=main_color)  # type: ignore
        self.main_container.configure(border_color=main_color, border_width=2)  # type: ignore
        self.outer_window_border.configure(border_color=main_color) # Update outer border

        for btn in self.category_btns:
            btn.configure(hover_color=main_color,
                          border_color=main_color)  # type: ignore

        try:
            self.cat_scroll.configure(  # type: ignore
                scrollbar_button_color=main_color,
                scrollbar_button_hover_color=hover_color
            )
        except Exception:
            pass

        try:
            self.main_area.configure(scrollbar_button_color=main_color,
                                     scrollbar_button_hover_color=hover_color)  # type: ignore
        except Exception:
            pass

        if self.audio_btn is not None:
            self.audio_btn.configure(  # type: ignore
                hover_color=main_color, border_color=main_color)  # type: ignore

        if self.switch_bg_btn is not None:
            self.switch_bg_btn.configure(  # type: ignore
                hover_color=main_color, border_color=main_color)  # type: ignore

        if hasattr(self, 'close_btn_top') and self.close_btn_top:
            self.close_btn_top.configure(border_color=main_color, hover_color=main_color)

        # Update ONLY currently visible rows (Optimization)
        current_rows = self.all_tweak_rows.get(self.current_cat_original_key, [])
        for row in current_rows:
            if row is not None:
                row.configure(border_color=main_color)
                if hasattr(row, 'switch') and row.switch:
                    row.switch.configure(progress_color=main_color)
                if hasattr(row, 'help_btn') and row.help_btn:
                    row.help_btn.configure(fg_color=main_color, hover_color=hover_color, border_color=main_color)

        # Re-call select_category to refresh button states and update any extra UI bits in specific cats
        self.select_category(self.current_cat_original_key)

    def on_unmap(self, event=None):
        if event is not None and event.widget is not self:
            return
        self._is_minimized = True
        # Aggressive sync: Reset video frame to 0 immediately on minimize
        v = getattr(self, 'vid', None)
        if v is not None and v.isOpened():
            v.set(cv2.CAP_PROP_POS_FRAMES, 0)

        bg_win = getattr(self, 'bg_win', None)
        if bg_win is not None and bg_win.winfo_exists():  # type: ignore
            bg_win.withdraw()

        if getattr(self, 'audio_on', False):
            winsound_ptr = getattr(winsound, 'PlaySound', None)
            if winsound_ptr:
                winsound_ptr(None, winsound.SND_PURGE)  # type: ignore

    def on_map(self, event=None):
        if event is not None and event.widget is not self:
            return
        self._is_minimized = False
        bg_win = getattr(self, 'bg_win', None)
        if bg_win is not None and bg_win.winfo_exists() and self.state() != "iconic":  # type: ignore
            try:
                bg_win.deiconify()
                self.sync_bg_win()
            except Exception:
                pass

        if getattr(self, 'audio_on', False) and os.path.exists(getattr(self, 'audio_wav', '')):
            # Force video sync on restore: restart both
            v = self.vid
            if v is not None and v.isOpened():
                v.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.play_audio()

    def round_window_corners(self, hwnd, w, h, radius):
        """Apply rounded corners to a window using Windows GDI regions."""
        if not hwnd: return
        try:
            # Create a rounded rectangular region
            # CreateRoundRectRgn(nLeftRect, nTopRect, nRightRect, nBottomRect, nWidthEllipse, nHeightEllipse)
            hrgn = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, w, h, radius, radius)
            # Set the window region
            ctypes.windll.user32.SetWindowRgn(hwnd, hrgn, True)
        except Exception:
            pass

    def sync_bg_win(self, event=None):
        bg_win = getattr(self, 'bg_win', None)
        if not self.winfo_exists() or bg_win is None or not bg_win.winfo_exists() or self.state() == "iconic":
            return

        if event is not None and event.widget is not self:
            return

        try:
            # winfo_rootx/y gives absolute screen coordinates of the client area
            # This is essential when overrideredirect is True for perfect video alignment
            x = self.winfo_rootx()
            y = self.winfo_rooty()
            w = self.winfo_width()
            h = self.winfo_height()

            if w > 1 and h > 1:
                # Try high-precision native sync first
                hwnd_main = ctypes.windll.user32.GetParent(self.winfo_id()) # type: ignore
                # For overrideredirect window, winfo_id() is often the direct HWND
                if bg_win is not None:
                    hwnd_bg_raw = bg_win.winfo_id()
                    hwnd_bg_parent = ctypes.windll.user32.GetParent(hwnd_bg_raw) # type: ignore
                    hwnd_bg = hwnd_bg_parent if hwnd_bg_parent != 0 else hwnd_bg_raw
                    
                    # SWP_NOACTIVATE = 0x0010
                    if hwnd_main and hwnd_bg:
                        ctypes.windll.user32.SetWindowPos(hwnd_bg, hwnd_main, x, y, w, h, 0x0010) # type: ignore
                    
                    # Apply rounding to sync with the menu corners (30px)
                    self.round_window_corners(hwnd_bg, w, h, 60) # 60 ellipse width/height = ~30px radius feel in GDI
                    
                    # Fallback/Safety: Update geometry anyway to stay in sync with Tkinter state
                    bg_win.geometry(f"{w}x{h}+{x}+{y}")
        except Exception:
            pass

        # NOTE: Audio is NOT restarted here intentionally.
        # sync_bg_win fires on every mouse move / resize event.
        # Audio state is managed only by toggle_audio() and on_map().
        if self.audio_btn is not None:
            icon = "🔊" if getattr(self, 'audio_on', False) else "🔇"
            try:
                self.audio_btn.configure(  # type: ignore
                    text=icon)  # type: ignore
            except Exception:
                pass

    def toggle_audio(self):
        self.audio_on = not self.audio_on
        btn = self.audio_btn
        if self.audio_on:
            if btn:
                btn.configure(text="🔊")  # type: ignore
            # Force video sync on unmute: restart both
            v = self.vid
            if v is not None and v.isOpened():
                v.set(cv2.CAP_PROP_POS_FRAMES, 0) # Restart video
            
            if os.path.exists(getattr(self, 'audio_wav', '')):
                self.play_audio() # Restart audio via play_audio helper
        else:
            if btn:
                btn.configure(text="🔇", fg_color="transparent")  # type: ignore
            winsound.PlaySound(None, winsound.SND_PURGE)  # type: ignore

    def destroy(self):
        self._is_destroyed = True
        winsound.PlaySound(None, winsound.SND_PURGE)  # type: ignore
        super().destroy()

    def update_video(self):
        if not HAS_VIDEO:
            return

        # Optimization: Skip processing when minimized
        if getattr(self, '_is_minimized', False):
            self.after(500, self.update_video)
            return

        # Handle Transition Animation
        if self._transition_state == 'out':
            self._transition_alpha += 0.15 # Faster fade
            if self._transition_alpha >= 1.0:
                self._transition_alpha = 1.0
                if self._pending_background:
                    self._perform_background_swap(self._pending_background)
                    self._pending_background = None
                self._transition_state = 'in'
        elif self._transition_state == 'in':
            self._transition_alpha -= 0.15
            if self._transition_alpha <= 0.0:
                self._transition_alpha = 0.0
                self._transition_state = None

        frame = None
        if self.vid is not None and self.vid.isOpened():  # type: ignore
            ret, f = self.vid.read()  # type: ignore
            if not ret:
                # Video reached the end, loop back and restart audio for sync
                self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)  # type: ignore
                ret, f = self.vid.read()  # type: ignore
                if self.audio_on:
                    self.play_audio()
            if ret:
                frame = f
                self._last_frame = f
        else:
            # For static images or if video fails, use the last captured frame
            frame = getattr(self, '_last_frame', None)

        if frame is not None:
            w, h = self.winfo_width(), self.winfo_height()
            if w < 10 or h < 10:
                w, h = 800, 600
            
            # Ensure frame is resized correctly if window moved/resized
            display_frame = cv2.resize(frame, (w, h))

            # High contrast dimming: ensures text and borders pop out
            # Dimmed background (60% brightness) for maximum definition
            v_weight = 0.40 * (1.0 - self._transition_alpha)
            o_weight = 1.0 - v_weight

            overlay = np.zeros_like(display_frame)
            cv2.rectangle(overlay, (0, 0), (w, h), (0, 0, 0), -1) # Pure black overlay for better depth
            display_frame = cv2.addWeighted(display_frame, v_weight, overlay, o_weight, 0)

            cv2image = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGBA)
            full_img = PIL.Image.fromarray(cv2image)
            full_imgtk = ctk.CTkImage(
                light_image=full_img, dark_image=full_img, size=(w, h))
            self.bg_label.configure(image=full_imgtk)  # type: ignore

        self.after(30, self.update_video)

    def update_stats(self):
        if self._is_destroyed:
            return
            
        try:
            ram_info = psutil.virtual_memory()
            disk_info = shutil.disk_usage("C:\\")
            
            if hasattr(self, 'ram_lbl'):
                self.ram_lbl.configure(text=f'{i18n.t("ram_label")} {ram_info.used / (1024 ** 3):.1f}GB / {ram_info.total / (1024 ** 3):.1f}GB')
            if hasattr(self, 'ram_bar'):
                self.ram_bar.set(ram_info.percent / 100.0)
                
            if hasattr(self, 'disk_lbl'):
                self.disk_lbl.configure(text=f'{i18n.t("disk_label")} {disk_info.used / (1024 ** 3):.0f}GB / {disk_info.total / (1024 ** 3):.0f}GB')
            if hasattr(self, 'disk_bar'):
                self.disk_bar.set(disk_info.used / disk_info.total)
        except Exception:
            pass
            
        # Update every 5 seconds (optimized)
        self.after(5000, self.update_stats)

    def get_system_scroll_lines(self) -> int:
        """Fetch the number of lines to scroll from Windows System Parameters."""
        try:
            import ctypes
            lines = ctypes.c_int()
            # SPI_GETWHEELSCROLLLINES = 0x0068
            ctypes.windll.user32.SystemParametersInfoW(0x0068, 0, ctypes.byref(lines), 0) # type: ignore
            return lines.value if lines.value > 0 else 3
        except Exception:
            return 3 # Default Windows value

    def _on_configure(self, event=None):
        """Unified handler for window move/resize: syncs video and checks scroll."""
        if event is not None and event.widget is not self:
            return
        self.sync_bg_win(event)
        self._check_scroll_visibility(event)

    def _check_scroll_visibility(self, event=None):
        """Hides scrollbars if content fits, ensuring no unnecessary visual clutter."""
        cat_scroll = getattr(self, 'cat_scroll', None)
        main_area = getattr(self, 'main_area', None)
        
        # We only apply visibility logic to the sidebar (cat_scroll).
        # The main_area scrollbar is HIDDEN permanently per user request.
        for frame in [cat_scroll]:
            if frame is not None and hasattr(frame, '_scrollbar') and hasattr(frame, '_parent_canvas'):
                try:
                    canvas = getattr(frame, '_parent_canvas', None)
                    if canvas is not None:
                        if hasattr(frame, 'update_idletasks'):
                            frame.update_idletasks() # type: ignore
                        bbox = canvas.bbox("all")
                        if bbox:
                            content_h = bbox[3] - bbox[1]
                            frame_h = canvas.winfo_height()
                            if content_h <= frame_h + 8:
                                frame._scrollbar.grid_remove() # type: ignore
                            else:
                                frame._scrollbar.grid() # type: ignore
                except Exception:
                    pass
        
        # Dynamic visibility for main_area scrollbar
        if main_area is not None and hasattr(main_area, '_scrollbar') and hasattr(main_area, '_parent_canvas'):
            try:
                canvas = getattr(main_area, '_parent_canvas', None)
                if canvas is not None:
                    main_area.update_idletasks()
                    bbox = canvas.bbox("all")
                    if bbox:
                        content_h = bbox[3] - bbox[1]
                        frame_h = canvas.winfo_height()
                        if content_h <= frame_h + 8:
                            main_area._scrollbar.grid_remove()
                        else:
                            main_area._scrollbar.grid()
            except Exception:
                pass
            
        return "break"

    def get_system_scroll_lines(self):
        """Fetches the number of lines to scroll from Windows system settings."""
        try:
            # SPI_GETWHEELSCROLLLINES = 0x0068
            lines = ctypes.c_uint()
            # 0x0068 is SPI_GETWHEELSCROLLLINES
            ctypes.windll.user32.SystemParametersInfoW(0x0068, 0, ctypes.byref(lines), 0)
            return max(1, lines.value) 
        except Exception:
            return 3 # Default to 3 lines if detection fails

    def _on_mousewheel(self, event):
        """Final fail-safe scroll: uses X-coordinates to split Sidebar and Options zones."""
        try:
            # Calculate the mouse's relative X position within the window
            win_x = self.winfo_rootx()
            mouse_x = event.x_root - win_x
            
            # Threshold: Sidebar is roughly the first 350 pixels
            if mouse_x < 350:
                target = getattr(self, 'cat_scroll', None)
                multiplier = 1.0 # Normal sensitivity for sidebar
            else:
                target = getattr(self, 'main_area', None)
                multiplier = 6.0 # Adjusted sensitivity for options (down from 8.0)
            
            if not target:
                return "break"
            
            # Perform scroll on the target's internal canvas
            canvas = getattr(target, '_parent_canvas', getattr(target, '_canvas', None))
            if canvas:
                # Balanced base step (20px per notch)
                base_step = 20
                pixels = -1 * (event.delta / 120.0) * base_step * multiplier
                
                if hasattr(canvas, 'yview_scroll'):
                    canvas.yview_scroll(int(pixels), "units")
                else:
                    canvas.yview("scroll", int(pixels), "units")
        except Exception:
            pass
            
        if hasattr(self, '_check_scroll_visibility'):
            self._check_scroll_visibility()
            
        return "break"

    def _on_rmb_drag_start(self, event):
        """Initialize Right-Click Drag scrolling for the main area."""
        self._drag_last_y = event.y_root
        return "break"

    def _on_rmb_drag_move(self, event):
        """Perform Right-Click Drag scrolling for the main area."""
        if not hasattr(self, '_drag_last_y'):
            self._drag_last_y = event.y_root
            return "break"
            
        delta = self._drag_last_y - event.y_root
        self._drag_last_y = event.y_root
        
        main_area = getattr(self, 'main_area', None)
        if main_area:
            canvas = getattr(main_area, '_parent_canvas', None)
            if canvas:
                # Scroll by pixels
                canvas.yview_scroll(int(delta), "pixels")
        return "break"

    def scan_drivers(self):
        self.status_badge.configure(
            text=f"{i18n.t('status_label')} {i18n.t('status_working')}", text_color="#ffcc00")  # type: ignore
        self.driver_btn.configure(text="...", state="disabled")  # type: ignore
        self.update()
        bad_devices = optimizer_core.check_drivers()
        self.driver_btn.configure(text=i18n.t(
            "driver_btn"), state="normal")  # type: ignore
        self.status_badge.configure(
            text=f"{i18n.t('status_label')} {i18n.t('status_ready')}", text_color="#00ff00")  # type: ignore

        if not bad_devices:
            showinfo("Scanner", i18n.t("driver_ok"))
        else:
            err_msg = i18n.t("driver_err")
            for dev in bad_devices:
                err_msg += f"- {dev.Name} (Err: {dev.ConfigManagerErrorCode})\n"

            do_fix = askyesno(
                "Scanner", err_msg + "\n" + i18n.t("driver_ask_fix"))
            if do_fix:
                self.driver_btn.configure(
                    text="...", state="disabled")  # type: ignore
                self.update()

                def bg_fix():
                    optimizer_core.fix_drivers(bad_devices)
                    self.after(0, self.on_fix_complete)
                threading.Thread(target=bg_fix, daemon=True).start()

    def on_fix_complete(self):
        self.status_badge.configure(
            text=f"{i18n.t('status_label')} {i18n.t('status_ready')}", text_color="#00ff00")  # type: ignore
        self.driver_btn.configure(text=i18n.t(
            "driver_btn"), state="normal")  # type: ignore
        showinfo("Scanner", i18n.t("driver_fix_success"))

    def change_lang(self, choice):
        if choice == "English":
            i18n.set_lang("en")
        elif choice == "Português":
            i18n.set_lang("pt")
        elif choice == "Français":
            i18n.set_lang("fr")
        elif choice == "Deutsch":
            i18n.set_lang("de")
        elif choice == "Italiano":
            i18n.set_lang("it")
        elif choice == "中文":
            i18n.set_lang("zh")
        else:
            i18n.set_lang("es")

        self.config["lang"] = i18n.CURRENT_LANG  # type: ignore
        self.save_config()

        # Close the picker after selection
        if hasattr(self, 'lang_picker_frame') and self.lang_picker_frame:
            self.lang_picker_frame.destroy()
            self.lang_picker_frame = None

        target_main = getattr(self, 'current_theme_color', '#e600e6')
        target_hover = getattr(self, 'current_hover_color', '#ff33ff')

        self.title(i18n.t("app_title"))
        self.logo_label.configure(text=i18n.t("logo_title"))  # type: ignore
        self.user_lbl.configure(
            text=f'{i18n.t("user_prefix")} {self.pc_user.upper()}')  # type: ignore

        ram_info = psutil.virtual_memory()
        total_ram = ram_info.total / (1024**3)
        used_ram = ram_info.used / (1024**3)
        self.ram_lbl.configure(
            text=f"{i18n.t('ram_label')} {used_ram:.1f}GB / {total_ram:.1f}GB")  # type: ignore

        disk_info = shutil.disk_usage("C:\\")
        total_disk = disk_info.total / (1024**3)
        used_disk = disk_info.used / (1024**3)
        self.disk_lbl.configure(
            text=f"{i18n.t('disk_label')} {used_disk:.0f}GB / {total_disk:.0f}GB")  # type: ignore

        self.driver_btn.configure(text=i18n.t("driver_btn"))  # type: ignore
        self.optimize_btn.configure(text=i18n.t("apply_btn"))  # type: ignore
        self.status_badge.configure(
            text=f"{i18n.t('status_label')} {i18n.t('status_ready')}")  # type: ignore

        self.categories = [
            i18n.t("cat_system"), i18n.t("cat_clean"), i18n.t("cat_privacy"),
            i18n.t("cat_ui"), i18n.t("cat_net"), i18n.t("cat_gaming"),
            i18n.t("cat_power"), i18n.t("cat_gpu"), i18n.t("cat_kernel"),
            i18n.t("cat_extreme"), i18n.t("cat_util"), i18n.t("cat_pro"),
            i18n.t("cat_help")
        ]

        for idx, btn in enumerate(self.category_btns):
            cat_id = self.category_original_keys[idx]
            cat_name = self.categories[idx]
            btn.configure(text=cat_name.upper())  # type: ignore

            def update_cmd(cid):
                return lambda: self.select_category(cid)
            btn.configure(command=update_cmd(cat_id))  # type: ignore

        self.tweak_data = i18n.get_tweaks_translated()  # type: ignore

        # OPTIMIZATION: Instead of destroying everything, update in-place
        self.populate_tweaks()

        if self.current_cat_original_key:
            self.select_category(self.current_cat_original_key)
        else:
            self.select_category(self.category_original_keys[0])
        self.change_theme(target_main, target_hover)

    def toggle_lang_picker(self):
        frame = self.lang_picker_frame
        if frame is not None and frame.winfo_exists():  # type: ignore
            frame.destroy()  # type: ignore
            self.lang_picker_frame = None
            return

        new_frame = ctk.CTkFrame(self, fg_color="#0d0d0d", bg_color="transparent", corner_radius=15, border_width=2,
                                 border_color=getattr(self, 'current_theme_color', '#e600e6'))
        self.lang_picker_frame = new_frame
        # Place it near the sidebar top
        new_frame.place(relx=0.08, rely=0.1, anchor="nw")

        title = ctk.CTkLabel(new_frame, text="IDIOMA", font=ctk.CTkFont(
            size=11, weight="bold"), text_color="#ffffff")
        title.pack(pady=(5, 5))  # type: ignore

        langs = ["Español", "English", "Português", "Français", "Deutsch", "Italiano", "中文"]
        for lang in langs:
            btn = ctk.CTkButton(
                new_frame,
                text=lang.upper(),
                border_width=2,
                border_color=getattr(self, 'current_theme_color', '#e600e6'),
                bg_color="transparent",
                fg_color="transparent",
                hover_color=getattr(self, 'current_theme_color', '#e600e6'),
                text_color="#ffffff",
                corner_radius=8,
                command=lambda l=lang: self.change_lang(l)
            )
            btn.pack(pady=3, padx=10)  # type: ignore

    def toggle_bg_picker(self):
        frame = self.bg_picker_frame
        if frame is not None and frame.winfo_exists():  # type: ignore
            frame.destroy()  # type: ignore
            self.bg_picker_frame = None
            return

        new_frame = ctk.CTkFrame(self, fg_color="#0d0d0d", bg_color="transparent", corner_radius=15, border_width=2,
                                 border_color=getattr(self, 'current_theme_color', '#e600e6'))
        self.bg_picker_frame = new_frame
        new_frame.place(relx=0.92, rely=0.93, anchor="se")

        title = ctk.CTkLabel(new_frame, text="FONDOS", font=ctk.CTkFont(
            size=11, weight="bold"), text_color="#ffffff")
        title.pack(pady=(5, 5))  # type: ignore

        for bg in self.fondos_disponibles:
            btn = ctk.CTkButton(
                new_frame,
                text=bg.split('.')[0].upper(),
                border_width=2,
                border_color=getattr(self, 'current_theme_color', '#e600e6'),
                fg_color="transparent",
                hover_color=getattr(self, 'current_theme_color', '#e600e6'),
                text_color="#ffffff",
                corner_radius=8,
                command=lambda b=bg: self.apply_background(b)
            )
            btn.pack(pady=3, padx=10)  # type: ignore

    def apply_background(self, base_name):
        # Force load if it's startup or if it's a different background
        if not self._is_startup and self.config.get("current_background") == base_name:
            # Still close picker if same bg
            picker = self.bg_picker_frame
            if picker is not None and picker.winfo_exists():
                picker.destroy()  # type: ignore
                self.bg_picker_frame = None
            return

        self._pending_background = base_name
        self._transition_state = 'out'

    def _perform_background_swap(self, base_name):
        picker = self.bg_picker_frame
        if picker is not None and picker.winfo_exists():
            picker.destroy()  # type: ignore
            self.bg_picker_frame = None

        self.video_source = resource_path(os.path.join("fondos", base_name))

        import re
        self.audio_source = re.sub(
            r'\.(mp4|mkv|avi)$', '.wav', self.video_source, flags=re.IGNORECASE)
        self.audio_wav = self.audio_source

        self.config["current_background"] = base_name  # type: ignore
        self.save_config()

        # Close the picker after selection
        if hasattr(self, 'lang_picker_frame') and self.lang_picker_frame:
            self.lang_picker_frame.destroy()
            self.lang_picker_frame = None

        # Apply Colors via centralized method for perfect sync
        self.set_colors_for_background(base_name)

        winsound_ptr = getattr(winsound, 'PlaySound', None)
        if winsound_ptr:
            winsound_ptr(None, winsound.SND_PURGE)  # type: ignore

        vid = getattr(self, 'vid', None)
        if vid is not None:
            vid.release()  # type: ignore
            setattr(self, 'vid', None)

        if self.video_source.endswith(('.jpg', '.png')):
            self.vid = None
            try:
                img = PIL.Image.open(self.video_source)
                img = img.resize((self.winfo_width() if self.winfo_width(
                ) > 10 else 800, self.winfo_height() if self.winfo_height() > 10 else 600))

                cv2image = np.array(img.convert('RGB'))
                cv2image = cv2image[:, :, ::-1].copy()
                self._last_frame = cv2image # Store for update_video
                # No need to configure label here, update_video will handle it
            except Exception as e:
                print(f"Error loading image bg: {e}")
        else:
            self.vid = cv2.VideoCapture(self.video_source)
            if self.audio_on:
                self.play_audio()

    def play_audio(self):
        if self.audio_on and os.path.exists(self.audio_wav):
            # We use SND_ASYNC to play in background. 
            # We don't necessarily need SND_LOOP here if we restart it manually in update_video,
            # but having it as a fallback doesn't hurt.
            winsound.PlaySound(self.audio_wav, winsound.SND_ASYNC |  # type: ignore
                               winsound.SND_LOOP)  # type: ignore
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)  # type: ignore

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_config(self):
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def populate_tweaks(self):
        theme = getattr(self, 'current_theme_color', '#e600e6')
        for i, original_cat_id in enumerate(self.category_original_keys):
            current_tweak_data = self.tweak_data
            lookup_key = str(original_cat_id)
            
            if lookup_key not in current_tweak_data:  # type: ignore
                continue
                
            # If rows already exist for this category, update them in-place
            if original_cat_id in self.all_tweak_rows and self.all_tweak_rows[original_cat_id]:
                existing_rows = self.all_tweak_rows[original_cat_id]
                for idx, item in enumerate(current_tweak_data[lookup_key]):  # type: ignore
                    if idx < len(existing_rows):
                        existing_rows[idx].update_text(item["name"], item["help"])
                continue

            # First time load: Create the rows
            self.all_tweak_rows[original_cat_id] = []  # type: ignore
            for item in current_tweak_data[lookup_key]:  # type: ignore
                row = TweakRow(
                    self.main_area,
                    tweak_id=item["id"],
                    tweak_name=item["name"],
                    help_text=item["help"],
                    state_controller=self.config,
                    is_enabled_default=item.get("default", False),
                    theme_color=theme,
                    drag_start_cb=self._on_rmb_drag_start,
                    drag_move_cb=self._on_rmb_drag_move
                )
                self.all_tweak_rows[original_cat_id].append(row)  # type: ignore

    def _async_update_states(self):
        for cat_id, rows in self.all_tweak_rows.items():
            for row in rows:
                if getattr(self, '_is_destroyed', False):
                    return
                try:
                    real_state = optimizer_core.check_state(row.tweak_id)
                    row.after(0, row.update_state, real_state)
                except Exception:
                    pass

    def select_category(self, cat_id):
        # No guard: always refresh to ensure perfect theme/color sync
        self.current_cat_original_key = cat_id
        try:
            idx = self.category_original_keys.index(cat_id)
            category_display_name = self.categories[idx]
        except ValueError:
            category_display_name = cat_id

        self.current_category = category_display_name

        theme = getattr(self, 'current_theme_color', '#e600e6')
        for idx, btn in enumerate(self.category_btns):
            cid = self.category_original_keys[idx]
            if cid == cat_id:
                # Active: filled with theme color, pure white text
                btn.configure(fg_color=theme, bg_color="transparent", text_color="#ffffff",
                              border_width=2, border_color=theme, hover_color=theme)  # type: ignore
            else:
                # Inactive: transparent, white text slightly dimmed, theme border
                btn.configure(fg_color="transparent", bg_color="transparent", text_color="#cccccc",
                              border_width=2, border_color=theme, hover_color=theme)  # type: ignore

        for widget in self.main_area.winfo_children():
            if hasattr(widget, 'grid_forget'):
                widget.grid_forget()

        # OPTIMIZATION: Reuse title label
        if not hasattr(self, 'category_title_lbl'):
            self.category_title_lbl = ctk.CTkLabel(self.main_area, text="", 
                                                   text_color="#ffffff", font=ctk.CTkFont(size=30, weight="bold"))
        
        self.category_title_lbl.configure(text=category_display_name.upper())
        self.category_title_lbl.grid(row=0, column=0, sticky="w", pady=(10, 20), padx=15)
        self.category_title_lbl.bind("<MouseWheel>", self._on_mousewheel)

        if cat_id in self.all_tweak_rows:
            for i, row in enumerate(self.all_tweak_rows[cat_id], start=1):
                if row is not None:
                    # Synchronize theme color for the row before showing it
                    row.configure(border_color=theme)
                    if hasattr(row, 'switch') and row.switch:
                        row.switch.configure(progress_color=theme)
                    if hasattr(row, 'help_btn') and row.help_btn:
                        row.help_btn.configure(fg_color=theme, hover_color=self.current_hover_color, border_color=theme)
                    
                    # Use the class method for scroll consistency
                    
                    row.grid(row=i, column=0, sticky="ew",
                             pady=6, padx=15)  # type: ignore

        try:
            self.main_area._parent_canvas.yview_moveto(0)  # type: ignore
        except Exception:
            pass
            
        # Check if scroll is needed for the new category
        self.after(100, self._check_scroll_visibility)

        if cat_id == "cat_help":
            theme = getattr(self, 'current_theme_color', '#e600e6')
            
            # --- SECTION 1: ENGINE INFO / EXAMPLES ---
            if hasattr(self, 'title_engine'):
                self.title_engine.configure(text=i18n.t("engine_title"), text_color=theme)
            else:
                self.title_engine = ctk.CTkLabel(
                    self.main_area,
                    text=i18n.t("engine_title"),
                    font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=theme
                )
            self.title_engine.grid(row=1, column=0, sticky="nw", padx=25, pady=(10, 5))
            self.title_engine.bind("<MouseWheel>", self._on_mousewheel)

            if hasattr(self, 'lbl_engine'):
                self.lbl_engine.configure(text=i18n.t("engine_info"))
            else:
                self.lbl_engine = ctk.CTkLabel(
                    self.main_area,
                    text=i18n.t("engine_info"),
                    font=ctk.CTkFont(size=13),
                    justify="left",
                    text_color="#cccccc",
                    wraplength=550,
                    anchor="w"
                )
            self.lbl_engine.grid(row=2, column=0, sticky="nw", padx=25, pady=(0, 20))
            self.lbl_engine.bind("<MouseWheel>", self._on_mousewheel)

            # --- SEPARATOR ---
            if not hasattr(self, 'help_sep'):
                self.help_sep = ctk.CTkFrame(self.main_area, height=2, border_width=0)
            self.help_sep.configure(fg_color=theme)
            self.help_sep.grid(row=3, column=0, sticky="ew", padx=25, pady=10)

            # --- SECTION 2: CREDITS ---
            if not hasattr(self, 'credits_lbl_main'):
                self.credits_lbl_main = ctk.CTkLabel(
                    self.main_area, text="", font=ctk.CTkFont(size=14, weight="bold"),
                    justify="left", text_color="#ffffff", wraplength=550, anchor="w"
                )
            self.credits_lbl_main.configure(text=i18n.t("credits_main"))
            self.credits_lbl_main.grid(row=4, column=0, sticky="nw", padx=25, pady=(10, 5))
            self.credits_lbl_main.bind("<MouseWheel>", self._on_mousewheel)

            # SPIDERLILYEDITS
            if not hasattr(self, 'credits_lbl_spider'):
                self.credits_lbl_spider = ctk.CTkLabel(
                    self.main_area, text="", font=ctk.CTkFont(size=13, weight="bold"),
                    justify="left", text_color=theme, wraplength=550, anchor="w"
                )
            self.credits_lbl_spider.configure(text=i18n.t("spider_credits"), text_color=theme)
            self.credits_lbl_spider.grid(row=5, column=0, sticky="nw", padx=25, pady=(5, 5))
            self.credits_lbl_spider.bind("<MouseWheel>", self._on_mousewheel)

            if not hasattr(self, 'spider_btn_frame'):
                self.spider_btn_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
                
                self.spider_tk_btn = ctk.CTkButton(
                    self.spider_btn_frame, text="", width=100, height=30,
                    font=ctk.CTkFont(size=14, weight="bold"),
                    command=lambda: webbrowser.open("https://www.tiktok.com/@spiderlilyedit_s?_r=1&_t=ZT-94G0oPq606f"),
                    fg_color="transparent", text_color="#ffffff",
                    border_width=2, corner_radius=8
                )
                self.spider_tk_btn.pack(side="left", padx=(5, 10))
                self.spider_tk_btn.bind("<MouseWheel>", self._on_mousewheel)

                self.spider_yt_btn = ctk.CTkButton(
                    self.spider_btn_frame, text="", width=100, height=30,
                    font=ctk.CTkFont(size=14, weight="bold"),
                    command=lambda: webbrowser.open("https://youtube.com/@spiderlilyedits?si=SMesb9Z-wjsZXOBk"),
                    fg_color="transparent", text_color="#ffffff",
                    border_width=2, corner_radius=8
                )
                self.spider_yt_btn.pack(side="left")
                self.spider_yt_btn.bind("<MouseWheel>", self._on_mousewheel)

            self.spider_tk_btn.configure(text=i18n.t("btn_spider_tiktok"), hover_color=theme, border_color=theme)
            self.spider_yt_btn.configure(text=i18n.t("btn_spider_youtube"), hover_color=theme, border_color=theme)
            self.spider_btn_frame.grid(row=6, column=0, sticky="nw", padx=20, pady=(0, 10))
            self.spider_btn_frame.bind("<MouseWheel>", self._on_mousewheel)

            # CDR BY REYES
            if not hasattr(self, 'credits_lbl_reyes'):
                self.credits_lbl_reyes = ctk.CTkLabel(
                    self.main_area, text="", font=ctk.CTkFont(size=13, weight="bold"),
                    justify="left", text_color=theme, wraplength=550, anchor="w"
                )
            self.credits_lbl_reyes.configure(text=i18n.t("reyes_credits"), text_color=theme)
            self.credits_lbl_reyes.grid(row=7, column=0, sticky="nw", padx=25, pady=(10, 5))
            self.credits_lbl_reyes.bind("<MouseWheel>", self._on_mousewheel)

            if not hasattr(self, 'reyes_btn_frame'):
                self.reyes_btn_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
                
                self.reyes_tk_btn = ctk.CTkButton(
                    self.reyes_btn_frame, text="", width=100, height=30,
                    font=ctk.CTkFont(size=14, weight="bold"),
                    command=lambda: webbrowser.open("https://www.tiktok.com/@c.d.r_1?_r=1&_t=ZT-94OP0Ujm77l"),
                    fg_color="transparent", text_color="#ffffff",
                    border_width=2, corner_radius=8
                )
                self.reyes_tk_btn.pack(side="left", padx=(5, 10))
                self.reyes_tk_btn.bind("<MouseWheel>", self._on_mousewheel)

                self.reyes_ig_btn = ctk.CTkButton(
                    self.reyes_btn_frame, text="", width=100, height=30,
                    font=ctk.CTkFont(size=14, weight="bold"),
                    command=lambda: webbrowser.open("https://www.instagram.com/_reyes_cdr?igsh=NTc4MTIwNjQ2YQ%3D%3D&utm_source=qr"),
                    fg_color="transparent", text_color="#ffffff",
                    border_width=2, corner_radius=8
                )
                self.reyes_ig_btn.pack(side="left")
                self.reyes_ig_btn.bind("<MouseWheel>", self._on_mousewheel)

            self.reyes_tk_btn.configure(text=i18n.t("btn_reyes_tiktok"), hover_color=theme, border_color=theme)
            self.reyes_ig_btn.configure(text=i18n.t("btn_reyes_ig"), hover_color=theme, border_color=theme)
            self.reyes_btn_frame.grid(row=8, column=0, sticky="nw", padx=20, pady=(0, 30))
            self.reyes_btn_frame.bind("<MouseWheel>", self._on_mousewheel)

            self.main_area.grid_rowconfigure(9, weight=1)
            self.main_area.grid_columnconfigure(0, weight=1)

    def apply_optimizations(self):
        
        def start_bg_tweak():
            self.save_config()
            self.status_badge.configure(
                text=f"{i18n.t('status_label')} {i18n.t('status_working')}", text_color=self.current_theme_color)  # type: ignore
            self.optimize_btn.configure(
                text="...", state="disabled")  # type: ignore
            self.driver_btn.configure(state="disabled") # type: ignore
            self.update()

            def bg_optimize():
                def prog_update(p):
                    if self.progress_dialog:
                        self.after(0, lambda: self.progress_dialog.set_progress(p)) # type: ignore
                
                optimizer_core.execute_tweaks(self.config, progress_callback=prog_update)
                self.after(0, self.on_optimize_complete)

            threading.Thread(target=bg_optimize, daemon=True).start()

        # Spawn Custom Progress Dialog in Confirm Mode
        self.progress_dialog = OptimizationProgressDialog(self, theme_color=self.current_theme_color, on_confirm=start_bg_tweak)
        self.eval(f'tk::PlaceWindow {str(self.progress_dialog)} center') # Attempt OS centering backup

    def on_optimize_complete(self):
        self.status_badge.configure(
            text=f"{i18n.t('status_label')} Completado, Reiniciando...", text_color=self.current_theme_color)  # type: ignore
        
        if hasattr(self, 'progress_dialog') and self.progress_dialog is not None:
            self.progress_dialog.title_lbl.configure(text="Â¡OPTIMIZACIÃ“N COMPLETADA!", text_color="#00ff00") # type: ignore
            self.progress_dialog.status_lbl.configure(text="Reiniciando el sistema en 3 segundos...", text_color="#ffffff") # type: ignore
            self.progress_dialog.progress_bar.stop() # type: ignore
            self.progress_dialog.progress_bar.set(1.0) # type: ignore
            self.progress_dialog.progress_bar.configure(progress_color="#00ff00") # type: ignore
            
        # Give user 3 seconds to read the message before triggering hard system reboot
        def do_reboot():
            os.system("shutdown /r /t 0")
        
        self.after(3000, do_reboot)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()  # type: ignore
    except:
        return False


def require_admin():
    """Returns True if already admin. If not, re-launches as admin and returns False."""
    if ctypes.windll.shell32.IsUserAnAdmin():  # type: ignore
        return True
    try:
        if getattr(sys, 'frozen', False):
            # Compiled .exe - re-run itself with runas
            exe = sys.executable
            params = " ".join(f'"{a}"' for a in sys.argv[1:])  # type: ignore
        else:
            # Python script - run python with the script path
            exe = sys.executable
            script = os.path.abspath(__file__)
            params = f'"{script}"'
            if len(sys.argv) > 1:
                # type: ignore
                params += " " + " ".join(f'"{a}"' for a in sys.argv[1:])

        ret = ctypes.windll.shell32.ShellExecuteW(  # type: ignore
            None, "runas", exe, params, None, 1)  # type: ignore
        if ret > 32:
            return False  # Successfully launched elevated copy, exit this one
        else:
            # Elevation failed (user cancelled UAC or UAC disabled)
            ctypes.windll.user32.MessageBoxW(  # type: ignore
                0,
                "CDR Optimizer necesita permisos de Administrador para funcionar.\n\nEjecuta el archivo como Administrador.",
                "CDR OPTIMIZER - Se requiere Administrador",
                0x10  # MB_ICONERROR
            )
            return False
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(  # type: ignore
            0, f"Error al solicitar permisos: {e}", "CDR ERROR", 0x10)  # type: ignore
        return False


if __name__ == "__main__":
    if not require_admin():
        sys.exit(0)
    try:
        migrate_config()
        app_instance = OptimizerApp()
        app_instance.mainloop()
        app_instance.save_config()
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(  # type: ignore
            0, f"Error Critico: {e}", "CDR ERROR", 0x10)  # type: ignore
