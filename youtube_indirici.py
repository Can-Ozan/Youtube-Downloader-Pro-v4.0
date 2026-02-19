import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import yt_dlp
import threading
import os
import urllib.request
import io
from PIL import Image, ImageTk 

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader Pro v4.0 - Ultimate")
        self.root.geometry("850x700")
        self.root.minsize(800, 650)
        self.root.resizable(True, True)
        
        # Tema ve Stil
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()
        
        # Değişkenler
        self.download_path = os.path.join(os.path.expanduser("~"), "Desktop", "YouTube_Indirilenler")
        self.var_type = tk.StringVar(value="video")
        self.thumbnail_data = None
        self.is_downloading = False
        
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

        self.create_widgets()

    def configure_styles(self):
        # Renk paleti
        self.bg_color = "#f4f4f9"
        self.accent_color = "#d32f2f" # YouTube Kırmızısı
        
        self.root.configure(bg=self.bg_color)
        
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"))
        self.style.configure("Header.TLabel", font=("Segoe UI", 22, "bold"), foreground=self.accent_color)
        self.style.configure("TLabelframe", background=self.bg_color)
        self.style.configure("TLabelframe.Label", background=self.bg_color, font=("Segoe UI", 10, "bold"), foreground="#444")
        
        # İlerleme çubuğu stili
        self.style.configure("Horizontal.TProgressbar", thickness=20, background="#4caf50")

    def create_widgets(self):
        # --- 1. ÜST BAŞLIK ---
        header_frame = ttk.Frame(self.root, padding="20 20 20 0")
        header_frame.pack(side=tk.TOP, fill=tk.X)
        
        ttk.Label(header_frame, text="YouTube Downloader", style="Header.TLabel").pack(side=tk.LEFT)
        ttk.Label(header_frame, text="Pro v4.0", font=("Segoe UI", 11), foreground="gray").pack(side=tk.LEFT, padx=10, pady=(15,0))

        # --- 2. ALT KISIM (Sabit Kontrol Paneli) ---
        bottom_frame = ttk.LabelFrame(self.root, text="İndirme Durumu", padding="15")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

        # Detaylı Bilgi Satırı (Hız, Boyut, Süre)
        self.info_frame = ttk.Frame(bottom_frame)
        self.info_frame.pack(fill=tk.X, pady=(0, 5))
        
        self.lbl_speed = ttk.Label(self.info_frame, text="Hız: -", font=("Consolas", 9), width=20)
        self.lbl_speed.pack(side=tk.LEFT)
        
        self.lbl_size = ttk.Label(self.info_frame, text="Boyut: -", font=("Consolas", 9), width=20)
        self.lbl_size.pack(side=tk.LEFT)
        
        self.lbl_eta = ttk.Label(self.info_frame, text="Kalan Süre: -", font=("Consolas", 9), width=20)
        self.lbl_eta.pack(side=tk.LEFT)

        # İlerleme Çubuğu
        self.progress_bar = ttk.Progressbar(bottom_frame, orient=tk.HORIZONTAL, length=100, mode='determinate', style="Horizontal.TProgressbar")
        self.progress_bar.pack(fill=tk.X, pady=(5, 10))
        
        # Yüzde Etiketi (Barın üzerinde veya altında)
        self.percent_label = ttk.Label(bottom_frame, text="%0", font=("Segoe UI", 9, "bold"), anchor="center")
        self.percent_label.pack(fill=tk.X)

        # Ana Aksiyon Butonları
        btn_frame = ttk.Frame(bottom_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        self.download_btn = ttk.Button(btn_frame, text="İndirmeyi Başlat", command=self.start_download, state="disabled")
        self.download_btn.pack(side=tk.RIGHT, padx=5, ipadx=20)

        self.open_folder_btn = ttk.Button(btn_frame, text="Klasörü Aç", command=self.open_download_folder, state="disabled")
        self.open_folder_btn.pack(side=tk.RIGHT, padx=5)
        
        self.status_label = ttk.Label(btn_frame, text="Hazır", foreground="gray")
        self.status_label.pack(side=tk.LEFT, padx=5)

        # --- 3. ANA İÇERİK ---
        content_frame = ttk.Frame(self.root, padding="20")
        content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Link Alanı
        link_frame = ttk.LabelFrame(content_frame, text="Video Bağlantısı", padding="15")
        link_frame.pack(fill=tk.X, pady=(0, 15))

        self.url_entry = ttk.Entry(link_frame, font=("Segoe UI", 11))
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.url_entry.bind('<Return>', lambda event: self.start_analysis())
        self.url_entry.bind('<FocusIn>', lambda event: self.clear_placeholder(event))

        ttk.Button(link_frame, text="Yapıştır & Analiz Et", command=self.paste_and_analyze, width=20).pack(side=tk.RIGHT)

        # Orta Bölüm
        mid_frame = ttk.Frame(content_frame)
        mid_frame.pack(fill=tk.BOTH, expand=True)

        # AYARLAR (SOL)
        settings_panel = ttk.Frame(mid_frame)
        settings_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Format
        format_frame = ttk.LabelFrame(settings_panel, text="Biçim Seçenekleri", padding="15")
        format_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Radiobutton(format_frame, text="Video (MP4 - En İyi Kalite)", variable=self.var_type, value="video").pack(anchor=tk.W, pady=5)
        ttk.Radiobutton(format_frame, text="Sadece Ses (M4A/MP3)", variable=self.var_type, value="audio").pack(anchor=tk.W, pady=5)
        
        ttk.Label(format_frame, text="* FFmpeg kurulu değilse en uyumlu sürüm indirilir.", font=("Segoe UI", 8), foreground="gray").pack(anchor=tk.W, pady=(5,0))

        # Konum
        folder_frame = ttk.LabelFrame(settings_panel, text="Kaydetme Yeri", padding="15")
        folder_frame.pack(fill=tk.X)
        
        self.path_label = ttk.Label(folder_frame, text=self.get_short_path(self.download_path), foreground="#1976D2", font=("Segoe UI", 9, "underline"), cursor="hand2")
        self.path_label.pack(fill=tk.X, pady=(0, 10))
        self.path_label.bind("<Button-1>", lambda e: self.browse_folder())
        
        ttk.Button(folder_frame, text="Klasörü Değiştir...", command=self.browse_folder).pack(anchor=tk.W)

        # ÖNİZLEME (SAĞ)
        preview_panel = ttk.LabelFrame(mid_frame, text="Önizleme", padding="10")
        preview_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.img_container = ttk.Label(preview_panel, text="Link bekleniyor...", anchor="center", background="#e0e0e0")
        self.img_container.pack(fill=tk.BOTH, expand=True)

        self.title_label = ttk.Label(preview_panel, text="", font=("Segoe UI", 10, "bold"), wraplength=300, anchor="center")
        self.title_label.pack(fill=tk.X, pady=(10,0))

    def clear_placeholder(self, event):
        # Kullanıcı kolaylığı için metin seçilir
        self.url_entry.selection_range(0, tk.END)

    def get_short_path(self, path):
        if len(path) > 40:
            return "..." + path[-37:]
        return path

    def paste_and_analyze(self):
        try:
            content = self.root.clipboard_get()
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, content)
            self.start_analysis()
        except:
            messagebox.showwarning("Hata", "Pano boş veya okunamadı.")

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_path = folder
            self.path_label.config(text=self.get_short_path(self.download_path))

    def reset_ui_for_new_video(self):
        self.title_label.config(text="")
        self.img_container.config(image="", text="Yükleniyor...")
        self.download_btn.config(state="disabled")
        self.percent_label.config(text="%0")
        self.progress_bar['value'] = 0
        self.lbl_speed.config(text="Hız: -")
        self.lbl_size.config(text="Boyut: -")
        self.lbl_eta.config(text="Kalan Süre: -")

    def start_analysis(self):
        url = self.url_entry.get()
        if not url: return
        
        self.reset_ui_for_new_video()
        self.status_label.config(text="Analiz ediliyor...", foreground="blue")
        
        threading.Thread(target=self.fetch_video_info, args=(url,), daemon=True).start()

    def fetch_video_info(self, url):
        try:
            ydl_opts = {'quiet': True, 'no_warnings': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                title = info.get('title', 'Bilinmeyen Video')
                thumbnail_url = info.get('thumbnail', None)
                
                # Resim İndirme ve İşleme
                img_tk = None
                if thumbnail_url:
                    try:
                        raw_data = urllib.request.urlopen(thumbnail_url).read()
                        im = Image.open(io.BytesIO(raw_data))
                        # En boy oranını koruyarak yeniden boyutlandır
                        base_width = 350
                        w_percent = (base_width / float(im.size[0]))
                        h_size = int((float(im.size[1]) * float(w_percent)))
                        im = im.resize((base_width, h_size), Image.Resampling.LANCZOS)
                        img_tk = ImageTk.PhotoImage(im)
                    except:
                        pass # Resim yüklenemezse sorun değil
                
                self.root.after(0, lambda: self.update_ui_analysis_success(title, img_tk))
        except Exception as e:
            self.root.after(0, lambda: self.update_ui_analysis_fail(str(e)))

    def update_ui_analysis_success(self, title, img_tk):
        self.title_label.config(text=title)
        if img_tk:
            self.thumbnail_data = img_tk # Referansı tutmalıyız yoksa silinir
            self.img_container.config(image=img_tk, text="")
        else:
            self.img_container.config(text="Önizleme yok")
            
        self.download_btn.config(state="normal")
        self.status_label.config(text="İndirmeye hazır", foreground="green")

    def update_ui_analysis_fail(self, error_msg):
        self.title_label.config(text="Video Bulunamadı")
        self.img_container.config(text="Hata oluştu")
        self.status_label.config(text="Hata: Link geçersiz veya bağlantı yok", foreground="red")
        # messagebox.showerror("Hata", f"Detay: {error_msg}") # İsteğe bağlı, çok pop-up çıkmasın diye kapattım

    def start_download(self):
        if self.is_downloading: return
        
        url = self.url_entry.get()
        self.is_downloading = True
        self.download_btn.config(state="disabled")
        self.open_folder_btn.config(state="disabled")
        self.status_label.config(text="İndirme Başlatılıyor...", foreground="blue")
        
        threading.Thread(target=self.download_process, args=(url,), daemon=True).start()

    def download_process(self, url):
        ydl_opts = {
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook],
            'ignoreerrors': True,
            'nocheckcertificate': True,
        }

        if self.var_type.get() == "audio":
            ydl_opts['format'] = 'bestaudio/best'
        else:
            # FFmpeg olmadan birleştirme gerektirmeyen en iyi formatı seç
            ydl_opts['format'] = 'best[ext=mp4]/best'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            self.root.after(0, lambda: self.download_complete(True))
        except Exception as e:
            self.root.after(0, lambda: self.download_complete(False, str(e)))

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            # Verileri güvenli şekilde al
            try:
                total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                downloaded = d.get('downloaded_bytes', 0)
                
                # Yüzde Hesaplama (Matematiksel)
                if total > 0:
                    percent = (downloaded / total) * 100
                else:
                    percent = 0

                # İstatistikler
                speed_str = d.get('_speed_str', 'Hesaplanıyor...')
                eta_str = d.get('_eta_str', '?')
                # Toplam boyutu string'e çevir (Örn: 15.4MiB)
                total_str = self.format_bytes(total) if total > 0 else "Bilinmiyor"

                # UI Güncelleme (Main Thread)
                self.root.after(0, lambda: self.update_progress_ui(percent, speed_str, eta_str, total_str))
            
            except Exception as e:
                print(f"Hook Hatası: {e}")

        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.status_label.config(text="Dosya işleniyor/kaydediliyor...", foreground="orange"))

    def format_bytes(self, size):
        # Byte'ı MB/GB cinsine çeviren yardımcı fonksiyon
        power = 2**10
        n = 0
        power_labels = {0 : '', 1: 'KiB', 2: 'MiB', 3: 'GiB', 4: 'TiB'}
        while size > power:
            size /= power
            n += 1
        return f"{size:.2f} {power_labels.get(n, '')}"

    def update_progress_ui(self, percent, speed, eta, total):
        self.progress_bar['value'] = percent
        self.percent_label.config(text=f"%{percent:.1f}")
        self.lbl_speed.config(text=f"Hız: {speed}")
        self.lbl_eta.config(text=f"Süre: {eta}")
        self.lbl_size.config(text=f"Boyut: {total}")
        self.status_label.config(text="İndiriliyor...", foreground="blue")

    def download_complete(self, success, error_msg=""):
        self.is_downloading = False
        self.download_btn.config(state="normal")
        
        if success:
            self.progress_bar['value'] = 100
            self.percent_label.config(text="%100")
            self.status_label.config(text="✅ İndirme Tamamlandı", foreground="green")
            self.open_folder_btn.config(state="normal")
            self.lbl_eta.config(text="Süre: 00:00")
            messagebox.showinfo("Başarılı", "Video başarıyla indirildi!")
        else:
            self.status_label.config(text="❌ Hata Oluştu", foreground="red")
            messagebox.showerror("Hata", f"İndirme başarısız:\n{error_msg}")

    def open_download_folder(self):
        try:
            os.startfile(self.download_path)
        except:
            messagebox.showinfo("Klasör Yolu", self.download_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()